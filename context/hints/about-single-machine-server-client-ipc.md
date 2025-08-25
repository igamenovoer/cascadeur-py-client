# About Single-Machine Server/Client IPC in Python

This hint explains practical approaches to implement a request/response style *server ↔ client* interaction **on a single machine** (no external networking) using Python. It focuses on OS‑local IPC (Inter‑Process Communication) without requiring you to build a low‑level protocol from scratch.

## When to Use Which Mechanism
| Mechanism | Platform | Framing / Message Boundary | Duplex | Pros | Cons | Best For |
|----------|----------|----------------------------|--------|------|------|---------|
| `multiprocessing.connection` (Listener/Client) | Win / Unix | Built‑in (pickle or bytes) | Yes | Stdlib, simple, supports named pipes (Win) & Unix domain sockets | Uses pickle by default (security), blocking by default | General request/response, quick start |
| Windows Named Pipes (`\\.\pipe\…`) via `pywin32` | Windows | Manual | Yes | Fine control, async/overlapped IO | More boilerplate | High concurrency, custom perf tuning |
| Unix Domain Sockets (UDS) | Unix | Stream (need framing) or SOCK_DGRAM | Yes | Fast, filesystem namespace, permissions | Not on Windows (except WSL / recent py3.12 AF_UNIX on Win) | Cross‑process RPC on Unix |
| POSIX Message Queues (`posix_ipc.MessageQueue`) | Unix | Message framed | Half / Full (use 2 queues or IDs) | Kernel message boundaries, priorities | Not on Windows | High rate small messages |
| Shared Memory + Events/Semaphores | Win / Unix | You design | Yes | Lowest latency, zero copy | Highest complexity | Large blobs, ultra‑low latency |
| Memory‑Mapped Files (`mmap`) | Win / Unix | You design | Yes | Share big data efficiently | Need signaling mechanism | Shared large arrays/images |
| File Drop (request_*.json / resp_*.json) | Win / Unix | File boundary | Half (needs two dirs) | Trivial tools, auditable | Latency, cleanup, race handling | Rarely—last resort / constrained env |
| ZeroMQ (`pyzmq` ipc://) | Unix (ipc), Win (tcp loopback) | Message framed | Yes | Rich patterns (REQ/REP, PUB/SUB) | Adds dep, may use TCP on Win | Complex topologies |
| gRPC over Unix Socket | Unix | Streaming (HTTP/2 frames) | Yes | Strong schema (Proto), tooling | Heavy for simple cases, not Win named pipe | Formal APIs |

## Recommended Starting Point (Cross‑Platform)
Use `multiprocessing.connection.Listener` + `Client`:
- Windows: gives you **Named Pipes** if the address looks like `r"\\.\\pipe\\name"`.
- Unix: gives you **Unix Domain Sockets** if the address is a filesystem path.
- Already implements object send/receive (pickled) or `send_bytes/recv_bytes` for custom serialization.

### Minimal Persistent Server (safe serialization variant)
```python
# server.py
import os, json, struct
from multiprocessing.connection import Listener

if os.name == 'nt':
    ADDRESS = r'\\.\\pipe\\demo_pipe'
else:
    ADDRESS = '/tmp/demo_socket'
    if os.path.exists(ADDRESS):
        os.unlink(ADDRESS)

def send_json(conn, obj):
    data = json.dumps(obj, separators=(',', ':')).encode()
    conn.send_bytes(struct.pack('!I', len(data)) + data)  # length prefix

def recv_json(conn):
    blob = conn.recv_bytes()
    size = struct.unpack('!I', blob[:4])[0]
    return json.loads(blob[4:4+size].decode())

def handle(req):
    cmd = req.get('cmd')
    if cmd == 'echo':
        return {'ok': True, 'echo': req.get('data')}
    return {'ok': False, 'error': 'unknown_command'}

with Listener(ADDRESS) as listener:
    while True:
        conn = listener.accept()
        try:
            while True:
                try:
                    req = recv_json(conn)
                except EOFError:
                    break
                resp = handle(req)
                resp['id'] = req.get('id')
                send_json(conn, resp)
        finally:
            conn.close()
```

### Client
```python
# client.py
import os, uuid, json, struct
from multiprocessing.connection import Client

if os.name == 'nt':
    ADDRESS = r'\\.\\pipe\\demo_pipe'
else:
    ADDRESS = '/tmp/demo_socket'

def send_json(conn, obj):
    data = json.dumps(obj).encode(); conn.send_bytes(len(data).to_bytes(4,'big') + data)

def recv_json(conn):
    blob = conn.recv_bytes(); n = int.from_bytes(blob[:4],'big'); return json.loads(blob[4:4+n])

with Client(ADDRESS) as conn:
    rid = uuid.uuid4().hex
    send_json(conn, {'id': rid, 'cmd': 'echo', 'data': 'hello'})
    resp = recv_json(conn)
    assert resp['id'] == rid
    print(resp)
```

## Key Design Considerations
### 1. Framing
- Pipes / stream sockets require explicit framing (length prefix, delimiter, or structured protocol).
- Avoid ad‑hoc `read until EOF` for request/response loops.

### 2. Serialization
- Pickle is convenient but unsafe with untrusted clients (RCE risk). Prefer JSON / MsgPack / CBOR.
- Large binary payloads: Share via shared memory, send only a descriptor (name + size).

### 3. Concurrency & Scaling
Patterns:
- Per‑connection thread: Simple, scales modestly.
- Event loop (async wrappers around named pipes on Windows require `overlapped` style via `pywin32` or Proactor in `asyncio` for pipes on Win  (>=3.8)).
- Worker pool: Accept, enqueue jobs, reply later with correlation IDs.

### 4. Correlation IDs
Needed if you pipeline multiple outstanding requests on one channel or have asynchronous responses.
```python
req = {'id': uuid.uuid4().hex, 'cmd': 'op'}
# Map id -> Future/Callback on the client
```

### 5. Timeouts
Use `multiprocessing.connection.wait([conn], timeout=secs)` before `recv()` to avoid indefinite hangs. Implement retry/backoff.

### 6. Backpressure
Bound internal queues (e.g., `queue.Queue(maxsize=...)`) and return `busy` or apply flow control. Don’t buffer unbounded data.

### 7. Security
- Limit filesystem permissions (Unix `chmod 600` on UDS path; Windows set pipe ACLs if sensitive).
- Use `authkey` in `Listener(..., authkey=b'shared-secret')` if you trust all local processes but want accidental connection prevention.
- Validate inputs strictly (types, expected keys, max sizes).

### 8. Cleanup
- Unix: unlink the socket path before binding; also on shutdown (`atexit` handler or signal handler).
- Remove temp shared memory segments explicitly (`SharedMemory.unlink`).

### 9. Performance Tips
| Need | Adjustment |
|------|-----------|
| Lower latency | Persistent connections, avoid reconnect cost |
| Large objects | Shared memory (`multiprocessing.shared_memory`) + small control message |
| High message rate | Preallocate threads or use async + batching |
| Serialization overhead | Switch to MsgPack (`msgpack`), or struct for fixed binary |

### 10. Shared Memory Pattern (Control + Data)
```python
from multiprocessing import shared_memory, Event
import struct
# Layout: [4 bytes length][payload bytes]
shm = shared_memory.SharedMemory(create=True, size=4096, name='demo_seg')
req_ready = Event(); resp_ready = Event()
# Writer (client): write payload -> set req_ready; wait resp_ready
```
Add sequence numbers to avoid missed events (ABA problem) if reusing events rapidly.

### 11. File Drop Pattern (Fallback)
```text
requests/req_<uuid>.json
responses/resp_<uuid>.json
```
- Client writes temp file then atomic rename into `requests/`.
- Server `watchdog` observer or periodic scan picks up, processes, writes response to `responses/`.
- Client polls for its response filename.
Mitigate cleanup via TTL sweeper.

## Choosing Libraries
| Goal | Library / Module | Notes |
|------|------------------|-------|
| Simple RPC (local) | `multiprocessing.connection` | Fastest to implement |
| Advanced patterns | `pyzmq` (REQ/REP, ROUTER/DEALER) | `ipc://path` on Unix; Windows likely TCP (check policy) |
| Schema & streaming | gRPC over UDS | `grpcio` + `unix://` target string |
| Low-level Win control | `pywin32` | Overlapped I/O & security descriptors |
| POSIX queues | `posix_ipc` | Use two queues or tagged IDs |

## Example: JSON-RPC 2.0 over Named Pipe (Windows) / UDS (Unix)

This example shows how to run JSON-RPC 2.0 over a local OS IPC transport using `multiprocessing.connection`:
- Windows: Named pipe at `r"\\.\pipe\csc_jsonrpc_demo"`
- Unix: Unix Domain Socket `/tmp/csc_jsonrpc_demo.sock`

It uses explicit length-prefix framing as recommended in the Framing section, and JSON for safe serialization.

Prerequisites
- pip install json-rpc
- Python 3.8+

Server (JSON-RPC over Named Pipe/UDS)
```python
# np_jsonrpc_server.py
import os
import json
import struct
from multiprocessing.connection import Listener, wait
from jsonrpc import JSONRPCResponseManager, dispatcher

# 1) Transport address: Named pipe on Windows; UDS on Unix
if os.name == "nt":
    ADDRESS = r"\\.\pipe\csc_jsonrpc_demo"
else:
    ADDRESS = "/tmp/csc_jsonrpc_demo.sock"

# 2) Helpers: explicit framing (length-prefix) on top of send_bytes/recv_bytes
def write_frame(conn, payload: bytes) -> None:
    conn.send_bytes(struct.pack("!I", len(payload)) + payload)

def read_frame(conn, max_size: int = 10 * 1024 * 1024) -> bytes:
    blob = conn.recv_bytes()
    if len(blob) &lt; 4:
        raise EOFError("short frame")
    size = struct.unpack("!I", blob[:4])[0]
    if size &gt; max_size:
        raise ValueError(f"frame too large: {size} &gt; {max_size}")
    return blob[4:4 + size]

# 3) Register JSON-RPC methods
def ping() -&gt; str:
    return "pong"

def add(a: int, b: int) -&gt; int:
    return a + b

dispatcher["ping"] = ping
dispatcher["add"] = add

def handle_jsonrpc(request_text: str) -&gt; str:
    # JSONRPCResponseManager handles single and batch requests per JSON-RPC 2.0
    response = JSONRPCResponseManager.handle(request_text, dispatcher)
    # For notifications (no id) response may be None; send empty object to keep transport simple
    return (response.json if response is not None else "{}")

def main() -&gt; None:
    # On Unix, cleanup stale socket path
    if os.name != "nt" and os.path.exists(ADDRESS):
        try:
            os.unlink(ADDRESS)
        except OSError:
            pass

    # Optional: authkey=b"shared-secret" to prevent accidental connects
    with Listener(ADDRESS) as listener:
        print(f"JSON-RPC pipe server listening at {ADDRESS}")
        while True:
            conn = listener.accept()
            try:
                # Keep-alive connection: handle multiple requests on one connection
                while True:
                    # Optional idle timeout
                    ready = wait([conn], timeout=60.0)
                    if not ready:
                        break
                    try:
                        payload = read_frame(conn)
                    except EOFError:
                        break
                    except Exception as e:
                        print(f"Receive error: {e}")
                        break

                    try:
                        request_text = payload.decode("utf-8")
                        response_text = handle_jsonrpc(request_text)
                        write_frame(conn, response_text.encode("utf-8"))
                    except Exception:
                        # JSON-RPC error envelope (generic internal error)
                        error_resp = {
                            "jsonrpc": "2.0",
                            "error": {"code": -32603, "message": "Internal error"},
                            "id": None,
                        }
                        try:
                            write_frame(conn, json.dumps(error_resp).encode("utf-8"))
                        except Exception:
                            pass
                        break
            finally:
                conn.close()

if __name__ == "__main__":
    main()
```

Client (JSON-RPC over Named Pipe/UDS)
```python
# np_jsonrpc_client.py
import os
import json
import struct
import uuid
from multiprocessing.connection import Client

if os.name == "nt":
    ADDRESS = r"\\.\pipe\csc_jsonrpc_demo"
else:
    ADDRESS = "/tmp/csc_jsonrpc_demo.sock"

def write_frame(conn, payload: bytes) -> None:
    conn.send_bytes(struct.pack("!I", len(payload)) + payload)

def read_frame(conn, max_size: int = 10 * 1024 * 1024) -> bytes:
    blob = conn.recv_bytes()
    if len(blob) &lt; 4:
        raise EOFError("short frame")
    size = struct.unpack("!I", blob[:4])[0]
    if size &gt; max_size:
        raise ValueError(f"frame too large: {size} &gt; {max_size}")
    return blob[4:4 + size]

def jsonrpc_call(method: str, params):
    rid = uuid.uuid4().hex
    req = {"jsonrpc": "2.0", "method": method, "params": params, "id": rid}
    with Client(ADDRESS) as conn:
        write_frame(conn, json.dumps(req, separators=(",", ":")).encode("utf-8"))
        resp_text = read_frame(conn).decode("utf-8")
        resp = json.loads(resp_text or "{}")
        if "error" in resp and resp["error"] is not None:
            raise RuntimeError(f"JSON-RPC error: {resp['error']}")
        if resp.get("id") != rid:
            raise RuntimeError(f"mismatched id: expected {rid}, got {resp.get('id')}")
        return resp.get("result")

if __name__ == "__main__":
    print("ping -&gt;", jsonrpc_call("ping", []))
    print("add(2, 3) -&gt;", jsonrpc_call("add", [2, 3]))
```

How to run
1) Install: `pip install json-rpc`
2) Start server: `python np_jsonrpc_server.py`
3) In another terminal: `python np_jsonrpc_client.py`
   - Expected:
     - `ping -&gt; pong`
     - `add(2, 3) -&gt; 5`

Notes
- Framing: 4-byte big-endian length prefix on each message.
- Timeouts: `wait(..., timeout=60.0)` to prevent hanging reads.
- Notifications (no id): This sample returns an empty `{}` frame; you can omit sending any frame to match spec strictly.
- Security: Consider `authkey` and Windows pipe ACLs; validate max sizes and fields.
- Scaling: Start with per-connection thread; move to overlapped I/O (`pywin32`) if needed for high concurrency.

Source: https://pypi.org/project/json-rpc/
## Example: ZeroMQ Local REQ/REP (Unix)
```python
import zmq
ctx = zmq.Context.instance()
# Server
rep = ctx.socket(zmq.REP); rep.bind('ipc:///tmp/demo_zmq')
msg = rep.recv_json(); rep.send_json({'ok': True, 'echo': msg})
# Client
req = ctx.socket(zmq.REQ); req.connect('ipc:///tmp/demo_zmq')
req.send_json({'hello': 'world'}); print(req.recv_json())
```
Source: https://zeromq.org/get-started/

## Example: POSIX Message Queue (Unix)
```python
import posix_ipc, json
mq = posix_ipc.MessageQueue('/demo', flags=posix_ipc.O_CREX)
mq.send(json.dumps({'cmd': 'ping'}))
msg, _prio = mq.receive()
```
Source: https://pypi.org/project/posix_ipc/

## Testing Checklist
- [ ] Multiple sequential requests on single connection
- [ ] Concurrent clients (thread explosion?)
- [ ] Large payload path (switch to shared memory?)
- [ ] Timeout & reconnection logic
- [ ] Graceful shutdown command
- [ ] Socket/pipe path collisions on restart
- [ ] Security: attempt invalid / oversize message

## Troubleshooting
| Symptom | Cause | Fix |
|---------|-------|-----|
| `FileExistsError` on Unix | Stale socket path | Unlink before binding |
| Client hangs on `recv()` | Server crashed / no response | Add timeout + retry or health check |
| `EOFError` on `recv()` | Peer closed connection | Reconnect and resend idempotent request |
| High CPU with shared memory | Busy spin loop | Use Events/Semaphores instead of polling |
| Message corruption | Missing framing | Implement length prefix |

## References
- Python `multiprocessing.connection`: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.connection
- Python Shared Memory: https://docs.python.org/3/library/multiprocessing.shared_memory.html
- ZeroMQ Guide: https://zguide.zeromq.org/
- posix_ipc PyPI: https://pypi.org/project/posix_ipc/
- gRPC Python: https://grpc.io/docs/languages/python/
- Windows Named Pipes (MS Docs overview): https://learn.microsoft.com/windows/win32/ipc/named-pipes

## Summary
For most single-machine server/client patterns, start with `multiprocessing.connection` (simple, portable, framed). Escalate only if you hit clear limitations (performance, advanced topologies, schema). Keep framing explicit, serialization safe, and plan for timeouts and cleanup.
