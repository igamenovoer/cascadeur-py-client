"""Spawn the health_exec_server in a background subprocess, run RPC tests, then terminate.

Usage (PowerShell):
  pixi run python examples/test_health_exec_server_spawn.py

This avoids manually starting the server in a blocking terminal.
"""
from __future__ import annotations

import base64
import json
import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict

HOST = "127.0.0.1"
PORT = 31003
ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = ROOT / "src" / "cascadeur_client" / "server" / "health_exec_server.py"


def wait_for_port(host: str, port: int, timeout: float = 5.0) -> bool:
    end = time.time() + timeout
    while time.time() < end:
        with socket.socket() as s:
            s.settimeout(0.25)
            try:
                s.connect((host, port))
                return True
            except OSError:
                time.sleep(0.1)
    return False


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
    print(f"Spawning server: {SERVER_PATH}")
    # Use current interpreter; environment already prepared by pixi
    proc = subprocess.Popen([sys.executable, str(SERVER_PATH)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    try:
        if not wait_for_port(HOST, PORT, 5.0):
            print("Server did not start within timeout. Output so far:")
            if proc.stdout:
                try:
                    print(proc.stdout.read())
                except Exception:  # noqa: BLE001
                    pass
            raise SystemExit(1)
        print("Server is up. Running tests...")

        health = rpc("health", _id=1)
        print("health keys:", sorted(list(health.get("result", {}).keys())))

        code = "print('hello world')\nprint('FINAL-LINE')\n"
        exec_ok = rpc("exec_b64", {"code_b64": base64.b64encode(code.encode()).decode()}, _id=2)
        print("exec_b64 success:", exec_ok)

        bad = rpc("exec_b64", {"code_b64": "!!!!"}, _id=3)
        print("exec_b64 bad base64:", bad)

        err_code = "print('before error')\n1/0\n"
        exec_err = rpc("exec_b64", {"code_b64": base64.b64encode(err_code.encode()).decode()}, _id=4)
        print("exec_b64 runtime error:", exec_err)

    finally:
        print("Terminating server...")
        if os.name == "nt":
            proc.terminate()
            try:
                proc.wait(timeout=2)
            except Exception:  # noqa: BLE001
                proc.kill()
        else:
            proc.send_signal(signal.SIGTERM)
            try:
                proc.wait(timeout=2)
            except Exception:  # noqa: BLE001
                proc.kill()
        if proc.stdout:
            leftover = proc.stdout.read()
            if leftover:
                print("--- server output ---\n" + leftover)


if __name__ == "__main__":
    main()
