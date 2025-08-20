"""Minimal JSON-RPC 2.0 server for Cascadeur with only two methods:

Methods:
  health      -> returns Python interpreter/environment info
  exec_b64    -> accepts base64-encoded Python source, executes it, captures stdout
                 Assumption: the executed code prints a final string; the last
                 non-empty stdout line is returned as "message" along with full stdout.

Protocol: line-delimited JSON-RPC over TCP 127.0.0.1:31003
Security: NONE (intentionally minimal). Do not expose beyond localhost.

Non-blocking usage inside Cascadeur GUI:

    from cascadeur_client.server import health_exec_server as hes
    server = hes.start_background()  # returns a handle; does NOT block GUI
    # ... later when shutting down:
    server.stop()

Blocking CLI usage (for manual testing):

    python -m cascadeur_client.server.health_exec_server
"""
from __future__ import annotations

import base64
import io
import json
import platform
import socket
import sys
import threading
import time
from dataclasses import dataclass
import select
import traceback
from typing import Any, Dict

HOST = "127.0.0.1"
PORT = 31003

_DEFAULT_ACCEPT_TIMEOUT = 0.5  # seconds


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


def _handle(req: Dict[str, Any]):
    if req.get("jsonrpc") != "2.0":
        return _jsonrpc_error(req.get("id"), -32600, "Invalid Request")
    mid = req.get("id")
    method = req.get("method")
    params = req.get("params") or {}

    try:
        if method == "health":
            return _jsonrpc_result(mid, _interp_info())
        if method == "exec_b64":
            code_b64 = params.get("code_b64")
            if not isinstance(code_b64, str):
                return _jsonrpc_error(mid, -32602, "code_b64 param required")
            try:
                raw = base64.b64decode(code_b64.encode("utf-8"), validate=True)
            except Exception as e:  # noqa: BLE001
                return _jsonrpc_error(mid, -32602, "Invalid base64", {"error": str(e)})
            source = raw.decode("utf-8", errors="replace")
            stdout_buf = io.StringIO()
            old_out = sys.stdout
            sys.stdout = stdout_buf
            exec_error = None
            try:
                exec(compile(source, "<exec_b64>", "exec"), {})  # noqa: S102
            except Exception as e:  # noqa: BLE001
                exec_error = {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()}
            finally:
                sys.stdout = old_out
            stdout_text = stdout_buf.getvalue()
            lines = [ln for ln in stdout_text.strip().splitlines() if ln.strip()]
            message = lines[-1] if lines else ""
            if exec_error:
                return _jsonrpc_error(mid, -32000, exec_error["message"], {"stdout": stdout_text, **exec_error})
            return _jsonrpc_result(mid, {"stdout": stdout_text, "message": message})
        return _jsonrpc_error(mid, -32601, "Method not found")
    except Exception as e:  # noqa: BLE001
        return _jsonrpc_error(mid, -32001, "Internal error", {"type": type(e).__name__, "message": str(e)})


def _client(sock: socket.socket):
    buf = b""
    with sock:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                if not line.strip():
                    continue
                try:
                    payload = json.loads(line.decode("utf-8"))
                except Exception as e:  # noqa: BLE001
                    resp = _jsonrpc_error(None, -32700, f"Parse error: {e}")
                else:
                    if isinstance(payload, list):
                        resp = [_handle(r) for r in payload if isinstance(r, dict)]
                    else:
                        resp = _handle(payload) if isinstance(payload, dict) else _jsonrpc_error(None, -32600, "Invalid Request")
                sock.sendall((json.dumps(resp) + "\n").encode("utf-8"))


@dataclass
class _ServerHandle:
    host: str
    port: int
    thread: threading.Thread
    stop_event: threading.Event
    socket: socket.socket

    def stop(self, timeout: float | None = 2.0):  # graceful shutdown
        if self.stop_event.is_set():
            return
        self.stop_event.set()
        try:
            # Dummy connect to unblock accept quickly
            with socket.socket() as _s:
                _s.settimeout(0.2)
                try:
                    _s.connect((self.host, self.port))
                except Exception:  # noqa: BLE001
                    pass
        except Exception:  # noqa: BLE001
            pass
        self.thread.join(timeout=timeout)
        try:
            self.socket.close()
        except Exception:  # noqa: BLE001
            pass


def start_background(host: str = HOST, port: int = PORT) -> _ServerHandle:
    """Start server in a background thread (non-blocking) and return a handle.

    If the port is already in use, raises OSError.
    """
    srv_sock = socket.socket()
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((host, port))
    srv_sock.listen(5)
    srv_sock.settimeout(_DEFAULT_ACCEPT_TIMEOUT)
    stop_event = threading.Event()

    def _loop():
        print(f"[health_exec_server] listening (background) on {host}:{port}")
        while not stop_event.is_set():
            try:
                try:
                    client, _ = srv_sock.accept()
                except socket.timeout:
                    continue
                except OSError:
                    break
                threading.Thread(target=_client, args=(client,), daemon=True).start()
            except Exception:  # noqa: BLE001
                # brief pause to avoid tight error loops
                time.sleep(0.05)
        # exiting
        try:
            srv_sock.close()
        except Exception:  # noqa: BLE001
            pass

    t = threading.Thread(target=_loop, name="health_exec_server", daemon=True)
    t.start()
    return _ServerHandle(host, port, t, stop_event, srv_sock)


# -------- Threadless polling variant (call poll() regularly from GUI main loop) -------- #

@dataclass
class PollServer:
    host: str
    port: int
    sock: socket.socket
    clients: set
    closed: bool = False

    def poll(self, max_accept: int = 4, max_recv: int = 32):  # non-blocking progression
        if self.closed:
            return
        # Accept new clients (non-blocking)
        for _ in range(max_accept):
            try:
                client, _ = self.sock.accept()
                client.setblocking(False)
                self.clients.add(client)
            except BlockingIOError:
                break
            except Exception:
                break
        if not self.clients:
            return
        rlist, _, _ = select.select(list(self.clients), [], [], 0)
        for c in rlist:
            try:
                data = c.recv(4096)
                if not data:
                    self.clients.discard(c)
                    c.close()
                    continue
                buff = getattr(c, "_hes_buf", b"") + data
                while b"\n" in buff:
                    line, buff = buff.split(b"\n", 1)
                    if line.strip():
                        try:
                            payload = json.loads(line.decode("utf-8"))
                        except Exception as e:  # noqa: BLE001
                            resp = _jsonrpc_error(None, -32700, f"Parse error: {e}")
                        else:
                            if isinstance(payload, list):
                                resp = [_handle(r) for r in payload if isinstance(r, dict)]
                            else:
                                resp = _handle(payload) if isinstance(payload, dict) else _jsonrpc_error(None, -32600, "Invalid Request")
                        c.sendall((json.dumps(resp) + "\n").encode("utf-8"))
                setattr(c, "_hes_buf", buff)
            except Exception:
                try:
                    self.clients.discard(c)
                    c.close()
                except Exception:
                    pass

    def close(self):
        if self.closed:
            return
        self.closed = True
        try:
            for c in list(self.clients):
                try:
                    c.close()
                except Exception:  # noqa: BLE001
                    pass
            self.clients.clear()
        finally:
            try:
                self.sock.close()
            except Exception:  # noqa: BLE001
                pass


def start_polling(host: str = HOST, port: int = PORT) -> PollServer:
    """Create a non-threaded server; user must call poll() periodically.

    Example inside GUI main loop:
        srv = health_exec_server.start_polling()
        # each frame:
        srv.poll()
    """
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(32)
    s.setblocking(False)
    print(f"[health_exec_server] polling mode on {host}:{port}")
    return PollServer(host, port, s, set())


def serve(host: str = HOST, port: int = PORT):  # blocking variant
    handle = start_background(host=host, port=port)
    try:
        while handle.thread.is_alive():
            handle.thread.join(timeout=1.0)
    except KeyboardInterrupt:  # pragma: no cover
        print("\n[health_exec_server] KeyboardInterrupt -> stopping")
        handle.stop()


if __name__ == "__main__":
    serve()
