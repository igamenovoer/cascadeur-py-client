"""Paste-safe threaded JSON-RPC server (no asyncio) for Cascadeur.

Features:
  - Methods: health, exec_b64
  - Start with start_server(); returns handle.stop() for shutdown
  - Line-delimited JSON-RPC 2.0 over TCP (default 127.0.0.1:31015)
  - No auto-start on import / paste

Usage inside Cascadeur interpreter (copy/paste this whole file or import it):

    from cascadeur_client.server import health_exec_server_threaded as hst
    srv = hst.start_server()              # non-blocking (threaded)
    # ... use it ...
    srv.stop()

JSON-RPC Examples (client side):
    {"jsonrpc":"2.0","id":1,"method":"health"}\n
    {"jsonrpc":"2.0","id":2,"method":"exec_b64","params":{"code_b64":"..."}}\n
Note: exec_b64 decodes base64 to UTF-8 source, executes with isolated globals, captures stdout.
The "message" field in result is last non-empty printed line (if any).
"""
from __future__ import annotations

import base64
import io
import json
import platform
import socket
import sys
import threading
import traceback
from dataclasses import dataclass
from typing import Any, Dict, Optional

HOST = "127.0.0.1"
PORT = 31015
BACKLOG = 8

# ---------------- Core helpers ---------------- #

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


def _exec_source(source: str):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    err: Optional[Dict[str, Any]] = None
    try:
        exec(compile(source, "<exec_b64>", "exec"), {})  # noqa: S102
    except Exception as e:  # noqa: BLE001
        err = {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()}
    finally:
        sys.stdout = old
    out = buf.getvalue()
    lines = [line for line in out.strip().splitlines() if line.strip()]
    last = lines[-1] if lines else ""
    return out, last, err


def _handle_one(req: Dict[str, Any]):
    if req.get("jsonrpc") != "2.0":
        return _jsonrpc_error(req.get("id"), -32600, "Invalid Request")
    mid = req.get("id")
    method = req.get("method")
    params = req.get("params") or {}
    if method == "health":
        return _jsonrpc_result(mid, _interp_info())
    if method == "exec_b64":
        b64 = params.get("code_b64")
        if not isinstance(b64, str):
            return _jsonrpc_error(mid, -32602, "code_b64 param required")
        try:
            raw = base64.b64decode(b64.encode("utf-8"), validate=True)
        except Exception as e:  # noqa: BLE001
            return _jsonrpc_error(mid, -32602, "Invalid base64", {"error": str(e)})
        src = raw.decode("utf-8", errors="replace")
        stdout, message, err = _exec_source(src)
        if err:
            return _jsonrpc_error(mid, -32000, err["message"], {"stdout": stdout, **err})
        return _jsonrpc_result(mid, {"stdout": stdout, "message": message})
    return _jsonrpc_error(mid, -32601, "Method not found")


def _process_payload(payload):
    if isinstance(payload, list):
        return [_handle_one(p) for p in payload if isinstance(p, dict)]
    if isinstance(payload, dict):
        return _handle_one(payload)
    return _jsonrpc_error(None, -32600, "Invalid Request")

# ---------------- Server threading ---------------- #

@dataclass
class ServerHandle:
    thread: threading.Thread
    stop_event: threading.Event
    sock: socket.socket
    host: str
    port: int

    def stop(self):
        if self.stop_event.is_set():
            return
        self.stop_event.set()
        try:
            with socket.socket() as s:
                s.settimeout(0.2)
                try:
                    s.connect((self.host, self.port))
                    s.sendall(b"\n")
                except Exception:  # noqa: BLE001
                    pass
        except Exception:  # noqa: BLE001
            pass
        self.thread.join(timeout=2)
        try:
            self.sock.close()
        except Exception:  # noqa: BLE001
            pass


def start_server(host: str = HOST, port: int = PORT, *, verbose: bool = True) -> ServerHandle:
    srv_sock = socket.socket()
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((host, port))
    srv_sock.listen(BACKLOG)
    if verbose:
        print(f"[threaded_jsonrpc] listening on {host}:{port}")
    stop_event = threading.Event()

    def client_thread(conn: socket.socket):
        buf = b""
        with conn:
            while not stop_event.is_set():
                try:
                    data = conn.recv(4096)
                    if not data:
                        break
                    buf += data
                    while b"\n" in buf:
                        line, buf = buf.split(b"\n", 1)
                        if not line.strip():
                            continue
                        try:
                            payload = json.loads(line.decode("utf-8"))
                        except Exception as e:  # noqa: BLE001
                            resp = _jsonrpc_error(None, -32700, f"Parse error: {e}")
                        else:
                            resp = _process_payload(payload)
                        try:
                            conn.sendall((json.dumps(resp) + "\n").encode("utf-8"))
                        except Exception:  # noqa: BLE001
                            break
                except Exception:  # noqa: BLE001
                    break

    def accept_loop():
        while not stop_event.is_set():
            try:
                conn, _ = srv_sock.accept()
            except OSError:
                break
            threading.Thread(target=client_thread, args=(conn,), daemon=True).start()
        if verbose:
            print("[threaded_jsonrpc] stopped")

    t = threading.Thread(target=accept_loop, name="threaded_jsonrpc", daemon=True)
    t.start()
    return ServerHandle(t, stop_event, srv_sock, host, port)

# No auto-start; paste-safe.

if __name__ == "__main__":  # Optional manual run
    start_server()
    try:
        while True:
            threading.Event().wait(3600)
    except KeyboardInterrupt:
        print("\nStopping...")