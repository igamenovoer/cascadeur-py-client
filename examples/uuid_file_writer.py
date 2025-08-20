"""Ultra-simple background UUID file writer (no CLI args).

Every 1 second creates a file:  D:\\<uuid>.txt  with the UUID inside.

Run:
    pixi run python examples/uuid_file_writer.py

Stop:
    Ctrl+C

Import usage (optional):
    from examples.uuid_file_writer import start_uuid_writer
    h = start_uuid_writer()  # defaults to D:\\, interval 1s
    h.stop()
"""
from __future__ import annotations
import os
import threading
import time
import uuid
from typing import Optional

__all__ = ["start_uuid_writer", "UUIDWriterHandle"]


class UUIDWriterHandle:
    def __init__(self, thread: threading.Thread, stop_evt: threading.Event, directory: str):
        self._thread = thread
        self._stop_evt = stop_evt
        self.directory = directory

    def stop(self, timeout: Optional[float] = 5.0):
        self._stop_evt.set()
        self._thread.join(timeout=timeout)

    @property
    def alive(self) -> bool:
        return self._thread.is_alive()

    def __repr__(self):  # pragma: no cover
        return f"<UUIDWriterHandle dir={self.directory!r} alive={self.alive}>"


def start_uuid_writer(directory: str = r"D:\\", interval: float = 1.0, print_each: bool = True) -> UUIDWriterHandle:
    """Start the UUID writer in a daemon thread.

    Args:
      directory: Target directory (must exist and be writable)
      interval: Seconds between file creations (>= 0)
      print_each: Whether to print each written file path
    """
    directory = os.path.abspath(directory)
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    stop_evt = threading.Event()

    def _loop():
        print(f"[uuid-writer] started directory={directory} interval={interval}s")
        while not stop_evt.is_set():
            u = str(uuid.uuid4())
            path = os.path.join(directory, f"{u}.txt")
            try:
                # 'x' ensures we don't overwrite if improbable collision
                with open(path, "x", encoding="utf-8") as f:
                    f.write(u + "\n")
                if print_each:
                    print(f"[uuid-writer] wrote {path}")
            except FileExistsError:
                if print_each:
                    print(f"[uuid-writer] collision (rare) skipped {path}")
            except Exception as e:  # noqa: BLE001
                print(f"[uuid-writer] error: {e}")
            # Sleep with responsiveness to stop
            end_t = time.time() + interval
            while not stop_evt.is_set() and time.time() < end_t:
                time.sleep(min(0.2, max(0, end_t - time.time())))
        print("[uuid-writer] stopped")

    thread = threading.Thread(target=_loop, name="uuid-writer", daemon=True)
    thread.start()
    return UUIDWriterHandle(thread, stop_evt, directory)

# Auto-start only when executed as a script.
if __name__ == "__main__":
    handle = start_uuid_writer()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\n[uuid-writer] Ctrl+C; stopping...")
        handle.stop()
