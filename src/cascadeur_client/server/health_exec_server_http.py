"""HTTP JSON-RPC 2.0 wrapper exposing the same two methods as health_exec_server:

Methods:
  health
  exec_b64

Endpoint: POST http://127.0.0.1:31004/
Body: JSON-RPC 2.0 request object (or batch list)

Designed so you can use curl easily.
"""
from __future__ import annotations

import base64
import io
import json
import platform
import sys
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict

HOST = "127.0.0.1"
PORT = 31004


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


class Handler(BaseHTTPRequestHandler):
    server_version = "HealthExecHTTP/0.1"

    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b""
        try:
            payload = json.loads(raw.decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            resp = _jsonrpc_error(None, -32700, f"Parse error: {e}")
        else:
            if isinstance(payload, list):
                resp = [_handle(r) for r in payload if isinstance(r, dict)]
            else:
                resp = _handle(payload) if isinstance(payload, dict) else _jsonrpc_error(None, -32600, "Invalid Request")
        data = json.dumps(resp).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args):  # type: ignore[override]  # silence std log
        return


def serve():
    httpd = HTTPServer((HOST, PORT), Handler)
    print(f"[health_exec_server_http] listening on http://{HOST}:{PORT}/")
    httpd.serve_forever()


if __name__ == "__main__":
    serve()
