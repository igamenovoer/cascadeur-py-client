"""Minimal script: write exactly 10 unique UUID .txt files (one per second) then exit.

Behavior:
- Creates (or reuses) directory 'uuid_files' in current working directory.
- Each file is named '<uuid>.txt' and contains the UUID string plus a trailing newline.
- Uses exclusive create ('x') so we never overwrite an existing file; on the ultra-rare collision it retries.
- Sleeps 1 second between files to mirror earlier periodic writer behavior.
- Pure stdlib, paste-safe. No functions/classes required.
"""
from __future__ import annotations

import os
import time
import uuid
import threading

OUTPUT_DIR = "d:/"
COUNT = 10        # number of files to write
INTERVAL = 1.0    # seconds between writes

def _write_uuid_files(count: int = COUNT, interval: float = INTERVAL, output_dir: str = OUTPUT_DIR) -> None:
    os.makedirs(output_dir, exist_ok=True)
    written = 0
    while written < count:
        u = uuid.uuid4().hex
        path = os.path.join(output_dir, f"{u}.txt")
        try:
            with open(path, "x", encoding="utf-8") as f:
                f.write(u + "\n")
            written += 1
            print(f"[uuid-writer] wrote {written}/{count}: {path}")
        except FileExistsError:
            # Extremely unlikely; retry with a new UUID immediately (no sleep)
            continue
        if written < count:
            time.sleep(interval)
    print(f"[uuid-writer] done: {count} files in '{output_dir}'")


def start_uuid_writer(count: int = COUNT, interval: float = INTERVAL, output_dir: str = OUTPUT_DIR, background: bool = False) -> threading.Thread:
    """Start the UUID writer in a thread.

    Parameters:
        count: number of files to create
        interval: seconds between file creations
        output_dir: directory to place files
        background: if True, return immediately (daemon thread); if False, join before returning
    Returns:
        The Thread object (already started).
    """
    t = threading.Thread(target=_write_uuid_files, args=(count, interval, output_dir), name="uuid-writer", daemon=background)
    t.start()
    if not background:
        t.join()
    return t


h = start_uuid_writer()
time.sleep(10)  # Let it run for a while; in real usage, you might not need this