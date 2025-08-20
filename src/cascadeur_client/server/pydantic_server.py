"""JSON-RPC server variant using pydantic for request validation.

Features:
 - Methods: ping, exec, eval
 - Batch support
 - Persistent state

Intended for embedding in Cascadeur. SECURITY: No auth.
"""
from __future__ import annotations

import json
import socket
import sys
import io
import threading
import traceback
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ValidationError

HOST = "127.0.0.1"
PORT = 31001  # different port to allow running alongside simple_server

EXEC_GLOBALS: Dict[str, Any] = {"__name__": "__cascadeur_exec__"}
EXEC_LOCALS = EXEC_GLOBALS


class JsonRpcRequest(BaseModel):
    jsonrpc: str
    method: str
    id: Optional[Union[int, str]] = None
    params: Optional[Any] = None

    def validate_version(self) -> None:
        if self.jsonrpc != "2.0":  # noqa: PLR2004
            raise ValueError("jsonrpc must be '2.0'")


class CodeParams(BaseModel):
    code: str


def _run(code: str, eval_mode: bool):
    out_buf, err_buf = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out_buf, err_buf
    result = None
    error = None
    try:
        if eval_mode:
            result = eval(code, EXEC_GLOBALS, EXEC_LOCALS)  # noqa: S307
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


def _handle_single(raw: Dict[str, Any]):
    try:
        req = JsonRpcRequest(**raw)
        req.validate_version()
    except (ValidationError, ValueError) as e:  # noqa: BLE001
        return {"jsonrpc": "2.0", "id": raw.get("id"), "error": {"code": -32600, "message": "Invalid Request", "data": str(e)}}

    params = req.params or {}
    if req.method == "ping":
        return {"jsonrpc": "2.0", "id": req.id, "result": "pong"}
    if req.method in ("exec", "eval"):
        try:
            cp = CodeParams(**params)
        except ValidationError as ve:  # noqa: BLE001
            return {"jsonrpc": "2.0", "id": req.id, "error": {"code": -32602, "message": "Invalid params", "data": ve.errors()}}
        res, stdout, stderr, err = _run(cp.code, req.method == "eval")
        if err:
            return {"jsonrpc": "2.0", "id": req.id, "error": {"code": -32000, "message": err["message"], "data": err}}
        return {"jsonrpc": "2.0", "id": req.id, "result": {"stdout": stdout, "stderr": stderr, "result": repr(res)}}
    return {"jsonrpc": "2.0", "id": req.id, "error": {"code": -32601, "message": "Method not found"}}


def _client(sock: socket.socket):
    buf = b""
    with sock:
        while True:
            chunk = sock.recv(8192)
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
                    resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": f"Parse error: {e}"}}
                else:
                    if isinstance(payload, list):
                        resp = [_handle_single(r) for r in payload if isinstance(r, dict)]
                    else:
                        resp = _handle_single(payload) if isinstance(payload, dict) else {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid Request"}}
                sock.sendall((json.dumps(resp) + "\n").encode("utf-8"))


def serve():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[pydantic_server] listening on {HOST}:{PORT}")
    while True:
        c, _ = s.accept()
        threading.Thread(target=_client, args=(c,), daemon=True).start()


if __name__ == "__main__":
    serve()
