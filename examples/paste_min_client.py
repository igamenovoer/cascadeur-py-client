"""Minimal client for the paste_min_server raw TCP JSON-RPC service.

Features:
  - health            : query server health
  - exec (inline code): execute inline Python source (auto base64 encoded)
  - exec-file         : execute contents of a .py file

Protocol: line-delimited JSON-RPC 2.0 over plain TCP (NOT HTTP)
Each request is one JSON object + '\n'. Response is one JSON line.

Usage examples:
  # Health
  python examples/paste_min_client.py --port 31015 health

  # Execute a snippet (last expression captured in result_repr)
  python examples/paste_min_client.py --port 31015 exec "print('hi'); 2+2"

  # Execute a file
  python examples/paste_min_client.py --port 31015 exec-file myscript.py

  # Demo mode (starts an in-process server, runs a sample health + exec, then stops)
  python examples/paste_min_client.py --demo

Security: NO auth. Use only on localhost / trusted environment.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import socket
import sys
from typing import Any, Dict


def send_rpc(host: str, port: int, method: str, params: Dict[str, Any] | None = None, rpc_id: int = 1, timeout: float = 5.0) -> dict:
    """Send a single JSON-RPC request and return decoded JSON response dict.

    Raises RuntimeError on malformed or transport errors.
    """
    req = {"jsonrpc": "2.0", "id": rpc_id, "method": method}
    if params:
        req["params"] = params
    line = json.dumps(req, separators=(",", ":")) + "\n"

    with socket.create_connection((host, port), timeout=timeout) as s:
        s.sendall(line.encode("utf-8"))
        # Read until newline
        data = b""
        resp_line = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
            if b"\n" in data:
                resp_line, _rest = data.split(b"\n", 1)
                break
        else:  # pragma: no cover (loop never falls through because of break or return)
            raise RuntimeError("No newline-terminated response received")

    try:
        return json.loads(resp_line.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as e:  # noqa: BLE001
        raise RuntimeError(f"Invalid JSON response: {resp_line!r}: {e}") from e


def cmd_health(args):  # noqa: D401
    resp = send_rpc(args.host, args.port, "health")
    print(json.dumps(resp, indent=2))


def _make_exec_params(source: str) -> dict:
    code_b64 = base64.b64encode(source.encode("utf-8")).decode("ascii")
    return {"code": code_b64}


def cmd_exec(args):
    params = _make_exec_params(args.code)
    resp = send_rpc(args.host, args.port, "exec_b64", params=params)
    print(json.dumps(resp, indent=2))


def cmd_exec_file(args):
    path = args.path
    if not os.path.isfile(path):
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(2)
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    params = _make_exec_params(src)
    resp = send_rpc(args.host, args.port, "exec_b64", params=params)
    print(json.dumps(resp, indent=2))


def cmd_demo(_args):
    try:
        from examples import paste_min_server  # Local import only for demo
    except Exception as e:  # noqa: BLE001
        print(f"Could not import paste_min_server for demo: {e}", file=sys.stderr)
        sys.exit(1)

    handle = paste_min_server.start(port=32199)
    try:
        print("[demo] started temporary server on 127.0.0.1:32199")
        resp_h = send_rpc("127.0.0.1", 32199, "health")
        print("[demo] health ->")
        print(json.dumps(resp_h, indent=2))
        code = "print('demo run'); 40+2"  # last expression becomes result_repr
        resp_e = send_rpc("127.0.0.1", 32199, "exec_b64", _make_exec_params(code))
        print("[demo] exec ->")
        print(json.dumps(resp_e, indent=2))
    finally:
        handle.stop()
        print("[demo] server stopped")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Client for paste_min_server raw JSON-RPC")
    p.add_argument("--host", default="127.0.0.1", help="Server host (default 127.0.0.1)")
    p.add_argument("--port", type=int, default=31015, help="Server port (default 31015)")

    sub = p.add_subparsers(dest="command")

    hp = sub.add_parser("health", help="Call health method")
    hp.set_defaults(func=cmd_health)

    ex = sub.add_parser("exec", help="Execute inline code snippet")
    ex.add_argument("code", help="Inline Python code; last expression captured")
    ex.set_defaults(func=cmd_exec)

    exf = sub.add_parser("exec-file", help="Execute code from a .py file")
    exf.add_argument("path", help="Path to Python source file")
    exf.set_defaults(func=cmd_exec_file)

    dm = sub.add_parser("demo", help="Run self-contained demo (no external server)")
    dm.set_defaults(func=cmd_demo)

    return p


def main(argv=None):  # noqa: D401
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    try:
        args.func(args)
    except Exception as e:  # noqa: BLE001
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
