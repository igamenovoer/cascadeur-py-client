"""Paste-safe background HTTP pusher (standard library only).

Purpose:
  Run this INSIDE the Cascadeur embedded Python interpreter to periodically
  send random text payloads (POST) to an external HTTP echo server you run
  outside (e.g. the thread_http_echo_server on port 31080).

Usage inside Cascadeur:

    # Paste this whole file (or at least everything below the docstring)
    handle = start_http_pusher("http://127.0.0.1:31080/", interval=1.0)
    # ... observe external server stdout / logs ...
    handle.stop()

Features:
  - Pure stdlib (urllib, threading, time, secrets)
  - Background daemon thread; main thread remains free
  - stop() method for graceful shutdown (sends a final marker)
  - Prints concise status lines with success / error

Adjustable:
  - interval seconds between pushes
  - max_errors before auto-stop (default unlimited unless set)

Security: Designed for local dev only (no TLS, no auth, no retries/backoff sophistication).
"""
from __future__ import annotations

import secrets
import threading
import time
import urllib.error
import urllib.request
from typing import Optional

__all__ = ["start_http_pusher", "HttpPusherHandle"]


class HttpPusherHandle:
    """Handle for controlling the background pusher thread."""

    def __init__(self, thread: threading.Thread, stop_evt: threading.Event):
        self._thread = thread
        self._stop_evt = stop_evt

    def stop(self, timeout: Optional[float] = 3.0):
        """Signal the thread to stop and wait up to timeout seconds."""
        self._stop_evt.set()
        self._thread.join(timeout=timeout)

    @property
    def alive(self) -> bool:
        return self._thread.is_alive()

    def __repr__(self):  # pragma: no cover
        return f"<HttpPusherHandle alive={self.alive}>"


def start_http_pusher(
    url: str,
    interval: float = 1.0,
    content_type: str = "text/plain; charset=utf-8",
    max_errors: Optional[int] = None,
    print_errors: bool = True,
) -> HttpPusherHandle:
    """Start background thread sending random text to given echo URL.

    Args:
      url: Target echo endpoint (e.g. "http://127.0.0.1:31080/")
      interval: Seconds between sends
      content_type: MIME type header to send
      max_errors: If set, stop after this many consecutive errors
      print_errors: Whether to print exception summaries
    """
    stop_evt = threading.Event()

    def _loop():
        print(f"[http-pusher] starting -> {url}")
        consecutive_errors = 0
        count = 0
        opener = urllib.request.build_opener()
        while not stop_evt.is_set():
            token = secrets.token_hex(8)  # 16 hex chars
            payload = f"msg#{count}:{token}".encode("utf-8")
            req = urllib.request.Request(url=url, data=payload, method="POST")
            req.add_header("Content-Type", content_type)
            req.add_header("Content-Length", str(len(payload)))
            try:
                with opener.open(req, timeout=5) as resp:
                    # Read small body (echo) but guard length
                    body = resp.read(200)
                    print(
                        f"[http-pusher] sent {len(payload)}B -> status={resp.status} echo={body!r}")
                consecutive_errors = 0
            except urllib.error.HTTPError as e:  # noqa: BLE001
                consecutive_errors += 1
                if print_errors:
                    print(f"[http-pusher] HTTPError status={e.code} msg={e.reason}")
            except Exception as e:  # noqa: BLE001
                consecutive_errors += 1
                if print_errors:
                    print(f"[http-pusher] error: {e}")
            count += 1
            if max_errors is not None and consecutive_errors >= max_errors:
                print(f"[http-pusher] stopping after {consecutive_errors} consecutive errors")
                break
            # Wait interval in small slices so we can react quickly to stop
            end_time = time.time() + interval
            while not stop_evt.is_set() and time.time() < end_time:
                time.sleep(min(0.1, max(0.0, end_time - time.time())))
        # Final marker
        print("[http-pusher] exited")

    thread = threading.Thread(target=_loop, name="http-pusher", daemon=True)
    thread.start()
    return HttpPusherHandle(thread, stop_evt)


# Quick inline demo usage (comment out if undesired):
handle = start_http_pusher("http://127.0.0.1:31111/")
# time.sleep(5)
# handle.stop()
