"""Run the threaded HTTP echo server as a standalone process.

Usage:
  pixi run python examples/run_http_echo_server.py --port 31111

Options:
  --host  (default 127.0.0.1)
  --port  (default 31111; use 0 for auto free port)
  --quiet suppress per-request log lines (only startup + errors)

Behavior:
  - Starts server in a background thread (same implementation as thread_http_echo_server)
  - Main thread sleeps until Ctrl+C.
  - Echo semantics: GET returns 'OK'; other methods echo request body (empty body -> 200 with empty body).

Exit with Ctrl+C (SIGINT) for graceful shutdown.
"""
from __future__ import annotations

import argparse
import time
import importlib.util
import os
import sys

# Allow running the script directly without package-style import.
_HERE = os.path.dirname(os.path.abspath(__file__))
_SERVER_PATH = os.path.join(_HERE, "thread_http_echo_server.py")
if not os.path.exists(_SERVER_PATH):
  print(f"[runner] cannot locate thread_http_echo_server.py at {_SERVER_PATH}", file=sys.stderr)
  raise SystemExit(2)

_spec = importlib.util.spec_from_file_location("_echo_server_mod", _SERVER_PATH)
if _spec is None or _spec.loader is None:  # pragma: no cover
  print("[runner] failed to load server module spec", file=sys.stderr)
  raise SystemExit(2)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)  # type: ignore[assignment]
start_http_echo_server = getattr(_mod, "start_http_echo_server")


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Threaded HTTP echo server runner")
    p.add_argument("--host", default="127.0.0.1", help="Bind host (default 127.0.0.1)")
    p.add_argument("--port", type=int, default=31111, help="Bind port (default 31111, 0 = auto)")
    p.add_argument("--quiet", action="store_true", help="Suppress request log output")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    handle = start_http_echo_server(host=args.host, port=args.port, log=not args.quiet)
    print(f"[runner] echo server running on http://{handle.host}:{handle.port} (Ctrl+C to stop)")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\n[runner] stopping...")
        handle.stop()
        print("[runner] stopped")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
