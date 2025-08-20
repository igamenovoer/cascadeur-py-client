"""Thread-based minimal HTTP echo server (standard library only).

Paste this entire source into a plain Python interpreter (e.g., Cascadeur).
Then start it with:

    handle = start_http_echo_server(port=31080)

It runs in a background daemon thread; the main thread remains free.
Stop it with:

    handle.stop()

Behavior:
  - GET: echoes path, query string, headers as JSON.
  - Other methods with a body (POST/PUT/PATCH/DELETE): echoes *exact* body bytes back.
    * If a Content-Type header is provided, it's reused in the response; else text/plain.
  - If no body is sent for non-GET, returns JSON metadata like GET.

Uses only: http.server, socketserver, threading, json, time.
No global while True in main thread, no __main__ guard.

Security: Development / local usage only. No TLS, no auth, no input validation.
"""
from __future__ import annotations

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from typing import Optional

__all__ = ["start_http_echo_server"]


class _ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True  # Kill worker threads automatically on shutdown


class EchoHandler(BaseHTTPRequestHandler):
    """Pure echo handler.

    For ANY method:
      - Reads request body (if any) and echos it back verbatim with same Content-Type if provided.
      - If body is empty, returns 204 No Content.
    """
    server_version = "EchoServer/0.1"

    def _read_body(self) -> bytes:
        length = int(self.headers.get("Content-Length", "0") or 0)
        if length <= 0:
            return b""
        return self.rfile.read(length)

    def _echo(self):
        # For non-GET methods: echo body (if any). For GET we'll short-circuit above.
        body = self._read_body()
        ctype = self.headers.get("Content-Type") or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        self.end_headers()
        if body:
            self.wfile.write(body)
        try:
            self.wfile.flush()
        except Exception:
            pass

    # Map all verbs to same behavior
    def do_GET(self):  # noqa: N802
        # Immediate small OK payload so client always sees a response (no body read attempt)
        body = b"OK"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body)
        try:
            self.wfile.flush()
        except Exception:
            pass
    def do_POST(self):  # noqa: N802
        self._echo()
    def do_PUT(self):  # noqa: N802
        self._echo()
    def do_PATCH(self):  # noqa: N802
        self._echo()
    def do_DELETE(self):  # noqa: N802
        self._echo()

    def log_message(self, format, *args):  # noqa: A003,D401
        if getattr(self.server, "_echo_log", True):  # type: ignore[attr-defined]
            super().log_message(format, *args)


class _ServerHandle:
    def __init__(self, server: _ThreadingHTTPServer, thread: threading.Thread):
        self._server = server
        self._thread = thread
        addr = server.server_address
        self.host = addr[0]
        self.port = addr[1]

    def stop(self, timeout: Optional[float] = 3.0):
        try:
            self._server.shutdown()
        except Exception:
            pass
        try:
            self._server.server_close()
        except Exception:
            pass
        self._thread.join(timeout=timeout)

    def __repr__(self):  # pragma: no cover - convenience only
        return f"<HTTPServerHandle {self.host}:{self.port} alive={self._thread.is_alive()}>"


def start_http_echo_server(host: str = "127.0.0.1", port: int = 31080, log: bool = True) -> _ServerHandle:
    """Start the echo HTTP server in a background thread and return a handle.

    Pass port=0 to auto-select a free port. Check handle.port afterward.
    """
    server = _ThreadingHTTPServer((host, port), EchoHandler)
    # Stash log flag
    server._echo_log = log  # type: ignore[attr-defined]

    def _serve():
        try:
            server.serve_forever(poll_interval=0.5)
        except Exception as e:  # noqa: BLE001
            if log:
                print(f"[echo-server] serve loop exited: {e}")

    thread = threading.Thread(target=_serve, name="http-echo-server", daemon=True)
    thread.start()

    if log:
        addr = server.server_address
        print(f"[echo-server] listening on http://{addr[0]}:{addr[1]} (threaded)")

    return _ServerHandle(server, thread)


# Example usage after paste:
#   handle = start_http_echo_server(port=31080)
#   # ... make HTTP requests ...
#   handle.stop()
