"""Test script for health_exec_server (TCP JSON-RPC on 127.0.0.1:31003).

Run the server separately (PowerShell example):
  Start-Process -FilePath pixi -ArgumentList 'run','python','src/cascadeur_client/server/health_exec_server.py' -WindowStyle Hidden
Or (synchronous / foreground):
  pixi run python src/cascadeur_client/server/health_exec_server.py
"""
from __future__ import annotations

import base64
import json
import socket
from typing import Any, Dict

HOST = "127.0.0.1"
PORT = 31003


def rpc(method: str, params: Dict[str, Any] | None = None, *, _id: int = 1):
    s = socket.socket()
    s.connect((HOST, PORT))
    try:
        req: Dict[str, Any] = {"jsonrpc": "2.0", "id": _id, "method": method}
        if params is not None:
            req["params"] = params
        s.sendall((json.dumps(req) + "\n").encode())
        data = b""
        while b"\n" not in data:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
        line = data.split(b"\n", 1)[0]
        return json.loads(line.decode())
    finally:
        s.close()


def main():
    print("Request: health")
    health = rpc("health", _id=1)
    print("Response (keys):", sorted(list(health.get("result", {}).keys())))

    code = "print('hello world')\nprint('FINAL-LINE')\n"
    code_b64 = base64.b64encode(code.encode()).decode()
    print("\nRequest: exec_b64 (success)")
    exec_ok = rpc("exec_b64", {"code_b64": code_b64}, _id=2)
    print("Response:", exec_ok)

    print("\nRequest: exec_b64 (bad base64)")
    bad = rpc("exec_b64", {"code_b64": "!!!!"}, _id=3)
    print("Response:", bad)

    print("\nRequest: exec_b64 (runtime error)")
    bad_code = "print('before error')\n1/0\n"
    bad_code_b64 = base64.b64encode(bad_code.encode()).decode()
    err = rpc("exec_b64", {"code_b64": bad_code_b64}, _id=4)
    print("Response:", err)


if __name__ == "__main__":
    main()
