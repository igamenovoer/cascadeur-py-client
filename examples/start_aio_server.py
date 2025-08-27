"""Helper script to start the aiohttp health_exec_server_aio reliably.

Usage (PowerShell):
  pixi run python examples/start_aio_server.py
Then in another terminal:
  curl -v http://127.0.0.1:31333/health
  curl -v -X POST http://127.0.0.1:31333/ -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":1,"method":"health"}'
Stop with Ctrl+C.
"""
from __future__ import annotations

import asyncio
from cascadeur_py_client.server import health_exec_server_aio as aio

PORT = 31333

async def main():
    handle = await aio.start_async(port=PORT)
    print(f"Server started on http://127.0.0.1:{PORT}/  (Ctrl+C to stop)")
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        await handle.stop()

if __name__ == "__main__":
    asyncio.run(main())
