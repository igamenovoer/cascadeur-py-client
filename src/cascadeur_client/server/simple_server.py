"""Minimal JSON-RPC server for running inside Cascadeur.

Line-delimited JSON-RPC 2.0 over TCP (127.0.0.1:31000).
Exposes methods:
 - ping -> "pong"
 - exec(code:str) -> executes code, returns stdout/stderr and None result
 - eval(code:str) -> evaluates expression, returns stdout/stderr/result
State persists across calls via shared globals.
SECURITY: Intentionally no auth or sandboxing.
"""
from __future__ import annotations
import socket
import threading
import json
import sys
import io
import traceback
from typing import Any, Dict

HOST = "127.0.0.1"
PORT = 31000

EXEC_GLOBALS: Dict[str, Any] = {"__name__": "__cascadeur_exec__"}
EXEC_LOCALS = EXEC_GLOBALS  # share


def _run(code: str, eval_mode: bool):
    out_buf, err_buf = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out_buf, err_buf
    result = None
    error = None
    try:
        if eval_mode:
            result = eval(code, EXEC_GLOBALS, EXEC_LOCALS)  # noqa: S307 - deliberate
        else:
            exec(compile(code, "<remote>", "exec"), EXEC_GLOBALS, EXEC_LOCALS)  # noqa: S102
    except Exception as e:  # noqa: BLE001
        error = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc(),
        }
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return result, out_buf.getvalue(), err_buf.getvalue(), error


def _handle(req: Any):
    if not isinstance(req, dict) or req.get("jsonrpc") != "2.0":
        return {"jsonrpc": "2.0", "id": req.get("id") if isinstance(req, dict) else None, "error": {"code": -32600, "message": "Invalid Request"}}
    mid = req.get("id")
    method = req.get("method")
    params = req.get("params") or {}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": "pong"}
    if method in ("exec", "eval"):
        code = params.get("code") if isinstance(params, dict) else None
        if not isinstance(code, str):
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "code param required"}}
        res, stdout, stderr, err = _run(code, method == "eval")
        if err:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32000, "message": err["message"], "data": err}}
        return {"jsonrpc": "2.0", "id": mid, "result": {"stdout": stdout, "stderr": stderr, "result": repr(res)}}
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "Method not found"}}


def _client(sock: socket.socket):
    buf = b""
    with sock:
        while True:
            data = sock.recv(4096)
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
                    resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": f"Parse error: {e}"}}
                else:
                    if isinstance(payload, list):
                        resp = [_handle(r) for r in payload]
                    else:
                        resp = _handle(payload)
                sock.sendall((json.dumps(resp) + "\n").encode("utf-8"))


def serve():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[simple_server] listening on {HOST}:{PORT}")
    while True:
        c, _ = s.accept()
        threading.Thread(target=_client, args=(c,), daemon=True).start()


if __name__ == "__main__":  # Allow manual run
    serve()
