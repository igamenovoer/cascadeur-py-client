"""
Minimal paste-safe JSON-RPC like server for Cascadeur embedded Python.

Drop this entire file (or just the code region below) into a plain Python
interpreter inside Cascadeur. It uses ONLY the standard library.

Provided methods (JSON-RPC 2.0 over raw TCP, line-delimited JSON objects):
  health    -> returns interpreter / platform info
  exec_b64  -> executes base64-encoded Python source

Transport:
  - Raw TCP (NOT HTTP) on 127.0.0.1:<port>
  - Each request must be one JSON object terminated by a single '\n'.
  - Each response is one line JSON.

Example request lines (don't forget the final newline):
  {"jsonrpc":"2.0","id":1,"method":"health"}\n
  {"jsonrpc":"2.0","id":2,"method":"exec_b64","params":{"code":"<base64>"}}\n
Security: NO authentication. Run only on localhost and trusted machines.

Typical usage inside Cascadeur interactive console:
  # Paste the code (definitions) first.
  handle = start(port=31015)   # Start server (non-blocking)
  # ... leave running while external tooling connects ...
  handle.stop()                # Stop when finished

External test (PowerShell):
  $req = '{"jsonrpc":"2.0","id":1,"method":"health"}' + "`n"
  [System.Net.Sockets.TcpClient]$c = New-Object System.Net.Sockets.TcpClient
  $c.Connect('127.0.0.1',31015)
  $stream = $c.GetStream()
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($req)
  $stream.Write($bytes,0,$bytes.Length)
  $buf = New-Object byte[] 4096
  $n = $stream.Read($buf,0,$buf.Length)
  [Text.Encoding]::UTF8.GetString($buf,0,$n)

Author: Minimal version tailored for environments where importing project
modules is not possible.
"""
from __future__ import annotations

import base64
import io
import json
import os
import platform
import socket
import threading
import time
import traceback
import sys
from typing import Optional

# --------------------------- Core RPC Logic ---------------------------------

_START_TIME = time.time()


def _json(obj) -> str:
    return json.dumps(obj, separators=(",", ":"))


def _health_payload():
    return {
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "pid": os.getpid(),
        "uptime_sec": round(time.time() - _START_TIME, 3),
    }


def _exec_b64(code_b64: str):
    """Decode base64, execute code, capture stdout and a 'result'.

    Strategy: we try to eval the last non-empty line as an expression; if that
    fails, we just exec the whole block. This mimics REPL convenience.
    """
    try:
        source = base64.b64decode(code_b64).decode("utf-8", errors="replace")
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(f"base64 decode failed: {e}") from e

    # Normalize newlines
    source = source.replace('\r\n', '\n').replace('\r', '\n')

    # Split lines and attempt expression on last non-empty
    lines = [ln for ln in source.split('\n')]
    non_empty = [ln for ln in lines if ln.strip()]

    buf = io.StringIO()
    stdout_before = sys.stdout
    sys.stdout = buf
    result_value = None
    error = None
    try:
        if non_empty:
            *body, last = non_empty
            tentative_expr = last
            # Construct body code (original ordering preserved but filter out empties we moved)
            # Insert a blank line to keep line numbers natural for tracebacks when we later eval
            # (Previously stored in an unused variable.)
            if body:
                body.append("")
            try:
                compiled_expr = compile(tentative_expr, '<exec_b64_expr>', 'eval')
            except SyntaxError:
                # Not an expression: exec full source
                exec(  # noqa: S102
                    source,  # use original full block to preserve semantics
                    globals(),
                    globals(),
                )
            else:
                # Exec body first (if any meaningful non-empty lines except last)
                if body:
                    body_block = '\n'.join(body)
                    exec(  # noqa: S102
                        body_block,
                        globals(),
                        globals(),
                    )
                result_value = eval(compiled_expr, globals(), globals())  # noqa: S307
        else:
            # Empty source: no-op
            result_value = None
    except Exception:  # noqa: BLE001
        error = traceback.format_exc()
    finally:
        sys.stdout = stdout_before

    stdout_text = buf.getvalue()
    return {
        "stdout": stdout_text,
        "result_repr": repr(result_value),
        "error": error,
    }


def _process(message: str):
    try:
        payload = json.loads(message)
    except json.JSONDecodeError as e:
        return _json({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32700, "message": f"Parse error: {e}"},
        })

    if not isinstance(payload, dict):
        return _json({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32600, "message": "Invalid Request (not object)"},
        })

    method = payload.get("method")
    rpc_id = payload.get("id")

    try:
        if method == "health":
            result = _health_payload()
            return _json({"jsonrpc": "2.0", "id": rpc_id, "result": result})
        if method == "exec_b64":
            params = payload.get("params") or {}
            code_b64 = params.get("code")
            if not isinstance(code_b64, str):
                raise ValueError("params.code must be base64 string")
            exec_res = _exec_b64(code_b64)
            return _json({"jsonrpc": "2.0", "id": rpc_id, "result": exec_res})
        raise ValueError(f"Unknown method: {method}")
    except Exception as e:  # noqa: BLE001
        return _json({
            "jsonrpc": "2.0",
            "id": rpc_id,
            "error": {"code": -32000, "message": f"Server error: {e}"},
        })


# --------------------------- Networking -------------------------------------

class _ServerHandle:
    def __init__(self, thread: threading.Thread, stop_evt: threading.Event, sock: socket.socket, port: int):
        self._thread = thread
        self._stop_evt = stop_evt
        self._sock = sock
        self.port = port

    def stop(self, timeout: Optional[float] = 2.0):
        self._stop_evt.set()
        try:
            # Dummy connect to unblock accept if needed
            with socket.create_connection(("127.0.0.1", self.port), timeout=0.2):
                pass
        except Exception:
            pass
        try:
            self._sock.close()
        except Exception:
            pass
        self._thread.join(timeout=timeout)


def start(port: int = 31015, host: str = "127.0.0.1") -> _ServerHandle:
    """Start the JSON-RPC loop in a background thread and return handle."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(8)
    stop_evt = threading.Event()

    def _loop():
        print(f"[paste_min_server] listening on {host}:{port}")
        while not stop_evt.is_set():
            try:
                try:
                    conn, addr = sock.accept()
                except OSError:
                    break  # socket likely closed
                conn.settimeout(5.0)
                with conn:
                    buffer = b""
                    while not stop_evt.is_set():
                        chunk = b""
                        try:
                            chunk = conn.recv(4096)
                        except socket.timeout:
                            break
                        if not chunk:
                            break
                        buffer += chunk
                        while b"\n" in buffer:
                            line, buffer = buffer.split(b"\n", 1)
                            if not line.strip():
                                continue
                            response_line = _process(line.decode("utf-8", errors="replace")) + "\n"
                            try:
                                conn.sendall(response_line.encode("utf-8"))
                            except OSError:
                                break
            except Exception as e:  # noqa: BLE001
                print(f"[paste_min_server] loop error: {e}")
                continue
        print("[paste_min_server] stopped")

    thread = threading.Thread(target=_loop, name="paste_min_server", daemon=True)
    thread.start()
    return _ServerHandle(thread, stop_evt, sock, port)


# --------------------------- If run directly --------------------------------
# if __name__ == "__main__":
#     h = start()
#     print("Server running; press Ctrl+C to stop...")
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         h.stop()
#         print("Server stopped.")
h=start()
