"""Client test script for health_exec_server_threaded (raw TCP JSON-RPC).

Usage:
  pixi run python examples/test_threaded_server.py
  pixi run python examples/test_threaded_server.py --port 31015 --code "print('hello')\nprint('DONE')\n"
  pixi run python examples/test_threaded_server.py --raw '{"jsonrpc":"2.0","id":99,"method":"health"}'

Ensure the server is running in Cascadeur first, e.g. inside Cascadeur Python:
    from cascadeur_client.server import health_exec_server_threaded as hst
    srv = hst.start_server(port=31015)
"""
from __future__ import annotations

import argparse
import base64
import json
import socket
import sys
from typing import Any, Dict, Optional

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 31015


def send_request(host: str, port: int, obj: Dict[str, Any]) -> Any:
    line = json.dumps(obj) + "\n"
    data = line.encode("utf-8")
    with socket.create_connection((host, port), timeout=3) as s:
        s.sendall(data)
        buf = b""
        while b"\n" not in buf:
            chunk = s.recv(4096)
            if not chunk:
                break
            buf += chunk
    if not buf:
        raise RuntimeError("No response received")
    first_line = buf.split(b"\n", 1)[0].decode("utf-8", errors="replace")
    try:
        return json.loads(first_line)
    except json.JSONDecodeError as e:  # noqa: BLE001
        raise RuntimeError(f"Invalid JSON in response: {first_line!r}") from e


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Test client for threaded JSON-RPC server")
    p.add_argument("--host", default=DEFAULT_HOST, help="Server host (default 127.0.0.1)")
    p.add_argument("--port", type=int, default=DEFAULT_PORT, help="Server port (default 31015)")
    p.add_argument("--code", help="Python source to execute (base64 encoded automatically)")
    p.add_argument("--raw", help="Raw JSON-RPC object to send (overrides --code / default tests)")
    args = p.parse_args(argv)

    host = args.host
    port = args.port

    if args.raw:
        try:
            obj = json.loads(args.raw)
        except json.JSONDecodeError as e:  # noqa: BLE001
            print(f"--raw invalid JSON: {e}", file=sys.stderr)
            return 1
        print("Sending raw ->", obj)
        resp = send_request(host, port, obj)
        print("Response:", json.dumps(resp, indent=2))
        return 0

    # Default: health then optional exec
    print("Sending health request...")
    health_resp = send_request(host, port, {"jsonrpc": "2.0", "id": 1, "method": "health"})
    print("Health response keys:", sorted(list(health_resp.get("result", {}).keys())))

    if args.code:
        print("Sending exec_b64 request...")
        code_b64 = base64.b64encode(args.code.encode("utf-8")).decode("ascii")
        exec_resp = send_request(
            host,
            port,
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "exec_b64",
                "params": {"code_b64": code_b64},
            },
        )
        print("Exec response:", json.dumps(exec_resp, indent=2))
    else:
        print("No --code provided; exec_b64 test skipped.")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
