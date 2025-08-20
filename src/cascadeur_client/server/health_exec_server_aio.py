"""Async (aiohttp) JSON-RPC 2.0 server for Cascadeur.

Goals:
  - Non-blocking (can run inside an existing interactive shell without freezing UI)
  - Two methods: health, exec_b64 (same semantics as sync variant)
  - Execution requests funneled through a single async queue for ordering
  - Optional execution in a background thread executor (if code is CPU-bound)

Usage Patterns:
  1. Existing asyncio loop (e.g. external tool already running a loop):
        import asyncio
        from cascadeur_client.server import health_exec_server_aio as aio_srv
        handle = await aio_srv.start_async()
        # ... later
        await handle.stop()

  2. No running loop (pure Cascadeur shell): start a dedicated loop thread:
        from cascadeur_client.server import health_exec_server_aio as aio_srv
        handle = aio_srv.start_in_thread()
        # handle.stop() when done

  3. Curl test (after server started on 127.0.0.1:31005):
        curl -s -X POST http://127.0.0.1:31005/ -H "Content-Type: application/json" \
             -d '{"jsonrpc":"2.0","id":1,"method":"health"}'

Notes:
  - If Cascadeur APIs must run only on main thread, keep use_executor=False.
  - If code execution is heavy and can be off-thread, set use_executor=True.

Paste-Safe Behavior:
  This module is designed so you can copy-paste it into an interactive Cascadeur
  Python shell without immediately blocking. Auto-start is disabled by default.
  To start after pasting:
      handle = start_in_thread()            # threaded loop
  or if an event loop already exists:
      handle = await start_async()
  To enable legacy CLI auto-start when run as a script, set AUTO_START = True
  near the top (or export env var before running and read it yourself).
"""
from __future__ import annotations

import asyncio
import base64
import io
import json
import platform
import sys
import traceback
from dataclasses import dataclass
from typing import Any, Dict, Optional
import threading

from aiohttp import web

HOST = "127.0.0.1"
PORT = 31005

# Set to True ONLY if you explicitly want script execution (python file.py) to
# auto-start the blocking serve() loop. Left False to stay paste-safe.
AUTO_START = False

# --------------------------- Helpers --------------------------- #

def _interp_info() -> Dict[str, Any]:
    return {
        "python_version": sys.version,
        "implementation": platform.python_implementation(),
        "executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "sys_prefix": sys.prefix,
        "base_prefix": getattr(sys, "base_prefix", sys.prefix),
        "in_virtual_env": sys.prefix != getattr(sys, "base_prefix", sys.prefix),
        "sys_path_sample": sys.path[:10],
    }


def _jsonrpc_error(id_, code: int, message: str, data: Any = None):
    err = {"code": code, "message": message}
    if data is not None:
        err["data"] = data
    return {"jsonrpc": "2.0", "id": id_, "error": err}


def _jsonrpc_result(id_, result: Any):
    return {"jsonrpc": "2.0", "id": id_, "result": result}


def _exec_code_sync(source: str):  # isolated synchronous exec capturing stdout
    import builtins as _b  # local import keeps function picklable if needed
    stdout_buf = io.StringIO()
    old_out = sys.stdout
    sys.stdout = stdout_buf
    err = None
    try:
        exec(compile(source, "<exec_b64>", "exec"), {"__name__": "__exec__", "__builtins__": _b.__dict__})  # noqa: S102
    except Exception as e:  # noqa: BLE001
        err = {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()}
    finally:
        sys.stdout = old_out
    stdout_text = stdout_buf.getvalue()
    lines = [ln for ln in stdout_text.strip().splitlines() if ln.strip()]
    message = lines[-1] if lines else ""
    return stdout_text, message, err

# --------------------------- Core Objects --------------------------- #

@dataclass
class _ExecRequest:
    id: Any
    code_b64: str
    future: asyncio.Future


@dataclass
class AsyncServerHandle:
    app: web.Application
    runner: web.AppRunner
    site: web.TCPSite
    queue: "asyncio.Queue[_ExecRequest]"
    worker: asyncio.Task
    use_executor: bool

    async def stop(self):
        if not self.worker.done():
            self.worker.cancel()
            try:
                await self.worker
            except asyncio.CancelledError:  # noqa: PERF203
                pass
        await self.runner.cleanup()

# --------------------------- Worker --------------------------- #

async def _worker(queue: "asyncio.Queue[_ExecRequest]", use_executor: bool):
    loop = asyncio.get_running_loop()
    while True:
        req = await queue.get()
        try:
            try:
                raw = base64.b64decode(req.code_b64.encode("utf-8"), validate=True)
            except Exception as e:  # noqa: BLE001
                req.future.set_result(_jsonrpc_error(req.id, -32602, "Invalid base64", {"error": str(e)}))
                continue
            source = raw.decode("utf-8", errors="replace")
            if use_executor:
                stdout_text, message, err = await loop.run_in_executor(None, _exec_code_sync, source)
            else:
                stdout_text, message, err = _exec_code_sync(source)
            if err:
                req.future.set_result(_jsonrpc_error(req.id, -32000, err["message"], {"stdout": stdout_text, **err}))
            else:
                req.future.set_result(_jsonrpc_result(req.id, {"stdout": stdout_text, "message": message}))
        except Exception as e:  # noqa: BLE001
            req.future.set_result(_jsonrpc_error(req.id, -32001, "Internal error", {"type": type(e).__name__, "message": str(e)}))
        finally:
            queue.task_done()

# --------------------------- HTTP Handler --------------------------- #

async def _handle_request(request: web.Request):
    print("[health_exec_server_aio] POST / received")
    data = await request.read()
    try:
        payload = json.loads(data.decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        return web.json_response(_jsonrpc_error(None, -32700, f"Parse error: {e}"))

    queue: asyncio.Queue = request.app["exec_queue"]

    async def process_one(obj: Dict[str, Any]):
        if not isinstance(obj, dict) or obj.get("jsonrpc") != "2.0":
            return _jsonrpc_error(obj.get("id") if isinstance(obj, dict) else None, -32600, "Invalid Request")
        mid = obj.get("id")
        method = obj.get("method")
        params = obj.get("params") or {}
        if method == "health":
            return _jsonrpc_result(mid, _interp_info())
        if method == "exec_b64":
            code_b64 = params.get("code_b64")
            if not isinstance(code_b64, str):
                return _jsonrpc_error(mid, -32602, "code_b64 param required")
            fut: asyncio.Future = asyncio.get_running_loop().create_future()
            await queue.put(_ExecRequest(mid, code_b64, fut))
            return await fut
        return _jsonrpc_error(mid, -32601, "Method not found")

    if isinstance(payload, list):
        results = [await process_one(p) for p in payload]
        return web.json_response(results)
    else:
        result = await process_one(payload)
        return web.json_response(result)

# --------------------------- Start / Stop APIs --------------------------- #

async def start_async(host: str = HOST, port: int = PORT, *, use_executor: bool = False) -> AsyncServerHandle:
    app = web.Application()
    queue: asyncio.Queue[_ExecRequest] = asyncio.Queue()
    app["exec_queue"] = queue
    async def _handle_health(request: web.Request):  # simple GET for quick curl without JSON-RPC
        return web.json_response({"status": "ok", "info": _interp_info()})

    app.add_routes([
        web.post("/", _handle_request),
        web.get("/health", _handle_health),
    ])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=host, port=port)
    await site.start()
    worker_task = asyncio.create_task(_worker(queue, use_executor), name="hes_exec_worker")
    print(f"[health_exec_server_aio] listening on http://{host}:{port}/ (use_executor={use_executor})")
    return AsyncServerHandle(app, runner, site, queue, worker_task, use_executor)

# Threaded loop variant for environments without an existing event loop

@dataclass
class ThreadServerHandle:
    thread: 'threading.Thread'
    loop: asyncio.AbstractEventLoop
    inner: Optional[AsyncServerHandle]
    _ready: asyncio.Event

    def stop(self):  # synchronous convenience
        if self.loop.is_closed():
            return
        fut = asyncio.run_coroutine_threadsafe(self._stop_inner(), self.loop)
        fut.result(timeout=5)
        self.loop.call_soon_threadsafe(self.loop.stop)

    async def _stop_inner(self):  # pragma: no cover - simple
        if self.inner:
            await self.inner.stop()

try:
    from threading import Thread
except ImportError:  # pragma: no cover
    Thread = None  # type: ignore


def start_in_thread(host: str = HOST, port: int = PORT, *, use_executor: bool = False) -> ThreadServerHandle:
    if Thread is None:  # pragma: no cover
        raise RuntimeError("Threading not available")
    loop = asyncio.new_event_loop()
    ready_flag = asyncio.Event()
    handle = ThreadServerHandle(thread=None, loop=loop, inner=None, _ready=ready_flag)  # type: ignore[arg-type]

    def runner():  # thread target
        asyncio.set_event_loop(loop)
        async def bootstrap():
            inner = await start_async(host=host, port=port, use_executor=use_executor)
            handle.inner = inner
            ready_flag.set()
        loop.create_task(bootstrap())
        loop.run_forever()
        # cleanup
        try:
            loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            loop.close()

    t = Thread(target=runner, name="hes_aio_loop", daemon=True)
    handle.thread = t  # type: ignore[assignment]
    t.start()
    # Wait until listening (poll event)
    while not ready_flag.is_set():
        if not t.is_alive():
            raise RuntimeError("Server thread terminated prematurely")
        # small sleep
        import time as _time
        _time.sleep(0.01)
    return handle

# --------------------------- CLI (blocking) --------------------------- #

def serve(host: str = HOST, port: int = PORT, *, use_executor: bool = False):  # blocking
    asyncio.run(_serve_main(host, port, use_executor=use_executor))


async def _serve_main(host: str, port: int, *, use_executor: bool):
    handle = await start_async(host=host, port=port, use_executor=use_executor)
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:  # pragma: no cover
        print("\n[health_exec_server_aio] stopping")
    finally:
        await handle.stop()


# Optional CLI entry point (disabled unless AUTO_START toggled)
if __name__ == "__main__" and AUTO_START:  # pragma: no cover
    serve()