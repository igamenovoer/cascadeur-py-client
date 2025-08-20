"""Fuller-featured JSON-RPC server intended to back an external MCP server.

Design goals:
 - Stable handle registry for scene objects (abstract example, replace with real Cascadeur API usage).
 - Methods grouped: ping, exec, eval, list_tools, describe_tool, call_tool, release_handle, list_handles.
 - Tool interface mirrors MCP concepts so an external FastMCP server can translate MCP -> these JSON-RPC calls.
 - Batch support (JSON-RPC array per line).
 - Simple version/capability handshake.

SECURITY: No auth, no sandbox.
NOTE: Replace stub scene API with actual Cascadeur csc.* calls.
"""
from __future__ import annotations
import json
import socket
import sys
import io
import threading
import traceback
import time
from typing import Any, Dict, Callable

HOST = "127.0.0.1"
PORT = 31002
PROTOCOL_VERSION = "1.0"

# Execution context for exec/eval
EXEC_GLOBALS: Dict[str, Any] = {"__name__": "__cascadeur_exec__"}
EXEC_LOCALS = EXEC_GLOBALS

# Handle registry (simple example)
_next_handle = 1
_handles: Dict[int, Any] = {}
_handle_rev: Dict[int, float] = {}  # last access timestamp

HANDLE_TTL = 60 * 60  # 1 hour idle expiry (not enforced continuously, just on access)

# Tool registry (toy examples) -------------------------------------------------
class Tool:
    def __init__(self, name: str, description: str, func: Callable[[Dict[str, Any]], Any]):
        self.name = name
        self.description = description
        self.func = func

TOOLS: Dict[str, Tool] = {}

def tool(name: str, description: str):
    def decorator(fn):
        TOOLS[name] = Tool(name, description, fn)
        return fn
    return decorator


@tool("list_nodes", "List example scene node names.")
def _tool_list_nodes(params: Dict[str, Any]):
    # Replace with actual Cascadeur API: e.g., [n.name for n in csc.scene.nodes]
    return [f"Node{i}" for i in range(3)]


@tool("make_handle", "Create a handle for a pseudo scene object (demo).")
def _tool_make_handle(params: Dict[str, Any]):
    global _next_handle
    name = params.get("name", f"Obj{_next_handle}")
    obj = {"name": name, "created": time.time()}
    h = _next_handle
    _next_handle += 1
    _handles[h] = obj
    _handle_rev[h] = time.time()
    return {"handle": h, "name": name}


@tool("get_handle", "Fetch stored object info by handle.")
def _tool_get_handle(params: Dict[str, Any]):
    h = params.get("handle")
    if not isinstance(h, int) or h not in _handles:
        raise ValueError("Unknown handle")
    _handle_rev[h] = time.time()
    return _handles[h]


# JSON-RPC Framework -----------------------------------------------------------

def _run_code(code: str, eval_mode: bool):
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


def _result(id_, value):
    return {"jsonrpc": "2.0", "id": id_, "result": value}


def _error(id_, code, message, data=None):
    err = {"code": code, "message": message}
    if data is not None:
        err["data"] = data
    return {"jsonrpc": "2.0", "id": id_, "error": err}


def _prune_handles():
    now = time.time()
    stale = [h for h, ts in _handle_rev.items() if now - ts > HANDLE_TTL]
    for h in stale:
        _handles.pop(h, None)
        _handle_rev.pop(h, None)


def _call_tool(name: str, params: Dict[str, Any]):
    if name not in TOOLS:
        raise ValueError("Unknown tool")
    return TOOLS[name].func(params or {})


def _handle(req: Dict[str, Any]):
    if req.get("jsonrpc") != "2.0":
        return _error(req.get("id"), -32600, "Invalid Request")
    mid = req.get("id")
    method = req.get("method")
    params = req.get("params") or {}

    try:
        if method == "ping":
            return _result(mid, {"pong": True, "version": PROTOCOL_VERSION})
        if method in ("exec", "eval"):
            code = params.get("code")
            if not isinstance(code, str):
                return _error(mid, -32602, "code param required")
            res, stdout, stderr, err = _run_code(code, method == "eval")
            if err:
                return _error(mid, -32000, err["message"], err)
            return _result(mid, {"stdout": stdout, "stderr": stderr, "result": repr(res)})
        if method == "list_tools":
            return _result(mid, [
                {"name": t.name, "description": t.description} for t in TOOLS.values()
            ])
        if method == "describe_tool":
            name = params.get("name")
            if name not in TOOLS:
                return _error(mid, -32602, "Unknown tool")
            t = TOOLS[name]
            return _result(mid, {"name": t.name, "description": t.description, "params_schema": {"type": "object"}})
        if method == "call_tool":
            name = params.get("name")
            if not isinstance(name, str):
                return _error(mid, -32602, "name param required")
            tool_params = params.get("params") or {}
            out = _call_tool(name, tool_params)
            return _result(mid, out)
        if method == "release_handle":
            h = params.get("handle")
            if isinstance(h, int) and h in _handles:
                _handles.pop(h, None)
                _handle_rev.pop(h, None)
                return _result(mid, {"released": h})
            return _error(mid, -32602, "Unknown handle")
        if method == "list_handles":
            _prune_handles()
            return _result(mid, sorted(_handles.keys()))
        return _error(mid, -32601, "Method not found")
    except Exception as e:  # noqa: BLE001
        return _error(mid, -32001, "Internal error", {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()})


def _client(sock: socket.socket):
    buf = b""
    with sock:
        while True:
            data = sock.recv(8192)
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
                    resp = _error(None, -32700, f"Parse error: {e}")
                else:
                    if isinstance(payload, list):
                        resp = [_handle(r) for r in payload if isinstance(r, dict)]
                    else:
                        resp = _handle(payload) if isinstance(payload, dict) else _error(None, -32600, "Invalid Request")
                sock.sendall((json.dumps(resp) + "\n").encode("utf-8"))


def serve():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[mcp_ready_server] listening on {HOST}:{PORT}")
    while True:
        c, _ = s.accept()
        threading.Thread(target=_client, args=(c,), daemon=True).start()


if __name__ == "__main__":
    serve()
