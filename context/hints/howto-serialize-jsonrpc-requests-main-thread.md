# How to Serialize JSON-RPC Requests on the Main Thread

This guide explains how to adapt the existing `jsonrpc_pipe_server` so that **all JSON-RPC method executions occur strictly on the main thread**, while still allowing multiple clients to connect concurrently. The goal is to prevent user RPC handlers from running in per-client worker threads (e.g., for thread-unsafe engine APIs) and instead funnel every call through a single, ordered execution path.

## When You Need This
Use this pattern if:
- Underlying logic (e.g., Cascadeur host API, GUI bindings, embedded interpreter state) is **not thread-safe**.
- Side effects (filesystem mutations, engine state changes) must be **strictly ordered**.
- You want simpler reasoning / deterministic replay of client interactions.

## High-Level Design
Replace the current "thread-per-client executes handler" model with a **producer–consumer** pattern:

1. Lightweight I/O layer (can be per-connection threads OR a selector-based multiplexer) reads framed JSON-RPC requests and enqueues them.
2. A **single main-thread dispatcher loop** pulls requests from a `queue.Queue` (FIFO) and executes `jsonrpcserver.dispatch` (or manual method resolution) synchronously.
3. Responses are handed back to the originating connection via a response channel (direct connection handle, or a per-request future/promise).
4. Notifications (no `id`) are processed the same but produce no response write.
5. Shutdown gracefully drains or aborts the queue before closing connections.

## Two Implementation Options (Both Standard Library Only)

### Option A: Queue + Minimal Reader Threads (Simplest Migration)
Keep most of current structure:
- Each accepted connection has a reader thread whose ONLY job is:
  - `recv_message(conn)` (already exists)
  - Wrap into an `RPCRequest` object: `{id, raw_json, conn, timestamp, order}`
  - Push onto `work_queue` (a bounded `queue.Queue` to apply backpressure)
- Main thread runs a loop: `req = work_queue.get(); response = dispatch(req.raw_json); send_message(req.conn, response)`
- Reader thread never calls `dispatch`.
- On client disconnect / EOF: reader thread exits and (optionally) enqueues a sentinel to inform cleanup.

Pros: minimal change, easy to reason about.
Cons: still uses reader threads (but they are now harmless and small).

### Option B: Single-Threaded Multiplexing with `selectors`
Eliminate per-client threads entirely:
- Use `selectors.DefaultSelector()` to register each new connection for `EVENT_READ`.
- Main loop: `events = selector.select(timeout)`; for each ready conn, read any complete framed message(s), enqueue into `work_queue`.
- Immediately (same loop) drain / process the queue in arrival order.

Pros: no extra threads; easier debugging; natural fairness.
Cons: Slightly more refactor; need to handle partial frames carefully if moving away from `recv_bytes()` convenience.

## Data Structure Sketch
```python
from dataclasses import dataclass, field
from queue import Queue, Empty
import time, itertools

_seq = itertools.count()

@dataclass(order=True)
class RPCRequest:
    seq: int = field(compare=True)
    raw: str = field(compare=False)
    conn: any = field(compare=False)
    id: object = field(compare=False, default=None)  # parsed later if desired
    ts: float = field(compare=False, default_factory=time.time)

work_queue: Queue[RPCRequest] = Queue(maxsize=1024)  # tune size for backpressure
```

Enqueue in reader layer:
```python
def reader_loop(conn):
    try:
        while not shutting_down:
            raw = recv_message(conn)
            # (Optional) quick parse id for prioritization
            # parsed = json.loads(raw); rpc_id = parsed.get('id')
            work_queue.put(RPCRequest(next(_seq), raw, conn), block=True)
    except EOFError:
        pass
    finally:
        conn.close()
```

Main-thread dispatcher:
```python
def dispatch_loop():
    while running:
        try:
            req = work_queue.get(timeout=0.25)
        except Empty:
            continue
        response = dispatch(req.raw)  # jsonrpcserver.dispatch
        if response:  # not a notification
            send_message(req.conn, response)
```

## Ensuring Main-Thread Execution
If other parts of your program (GUI loop, engine tick) already own the main thread, integrate the dispatcher:

### Integration Patterns
1. Periodic Pump: Call `pump_rpc_once()` inside the host application's main loop.
2. Timer Callback: Schedule recurring callback pulling limited number of items per tick.
3. Dedicated Loop: If server owns process, just spin `dispatch_loop()` in main.

Example pump function:
```python
def pump_rpc_once(limit=32):
    processed = 0
    while processed < limit:
        try:
            req = work_queue.get_nowait()
        except Empty:
            break
        response = dispatch(req.raw)
        if response:
            send_message(req.conn, response)
        processed += 1
```

Then integrate with (pseudo):
```python
while app_running:
    engine.update()
    pump_rpc_once()
```

## Backpressure & Flow Control
- Use `Queue(maxsize=N)` to avoid unbounded memory growth under burst load.
- Reader threads block on `put()` once queue is full, naturally slowing clients.
- Optionally parse requests early and reject / drop if queue is saturated (send server busy error `-32000`).

## Error Handling & Shutdown
Add flags:
```python
shutting_down = False

def initiate_shutdown():
    global shutting_down
    shutting_down = True
    # Close listener so no new connections
    # Drain queue (optional) or discard remaining
```
During shutdown:
- Stop accepting new connections.
- Either finish processing queued requests or immediately close all conns.
- Send a final error for unprocessed requests if you need explicit notification.

## Ordering Guarantees
All requests are processed in strict queue order (arrival-based). If you need **per-client** ordering but allow **interleaving** across clients, this is already satisfied. If you need strict per-client fairness (avoid one chatty client starving others), implement a round-robin scheduler: maintain per-connection sub-queues and a deque of active connections.

Round-robin sketch:
```python
from collections import deque

per_conn = {}
active = deque()

def enqueue(conn, raw):
    q = per_conn.setdefault(conn, deque())
    q.append(raw)
    if len(q) == 1:
        active.append(conn)

def pump():
    if not active: return
    conn = active.popleft()
    raw = per_conn[conn].popleft()
    if per_conn[conn]:
        active.append(conn)
    response = dispatch(raw)
    if response:
        send_message(conn, response)
```

## Do We Need a Third-Party Library?
Not necessarily.

| Concern | Standard Lib? | Third-Party Option | Comment |
|---------|---------------|--------------------|---------|
| Single-thread multiplexing | `selectors`, `queue` | `anyio`, `trio`, `curio` | Stdlib is enough. |
| Async integration | `asyncio` | `trio`, `anyio` | If migrating to full async, consider `anyio` for portability. |
| JSON-RPC layer | `jsonrpcserver` (already) | `aiohttp-json-rpc`, `json-rpc` | Existing lib sufficient. |

You only need an external library if you: (a) want structured cancellation/timeouts across tasks (`anyio`), (b) require advanced concurrency patterns (nurseries, cancellation scopes), or (c) are already rewriting around `asyncio`.

## Migration Steps Summary (Option A)
1. Add `work_queue`, `RPCRequest` dataclass.
2. Change `_handle_client` to a read-and-enqueue loop (no dispatch inside).
3. Add `dispatch_loop()` (or integrate pumping into existing main loop).
4. Ensure shutdown sets a flag, closes listener, and lets reader threads exit.
5. Remove response sending from worker threads; only main thread sends.
6. (Optional) Add backpressure + fairness logic.

## Testing Strategy
1. Multi-client concurrency test: ensure ordering by injecting sequence numbers and asserting serialized execution.
2. Stress test: thousands of rapid requests; assert queue bounds respected (no memory explosion).
3. Shutdown mid-load: ensure no deadlocks and resources freed (pipes cleaned up).
4. Notification (no `id`) behavior unaffected (no responses emitted).
5. Error injection: raise exception in a handler; confirm it doesn't kill dispatcher loop.

## Example Conceptual Diff (Illustrative, Not Applied)
```diff
- def _handle_client(self, conn):
-     while ...:
-         request_string = recv_message(conn)
-         response_string = dispatch(request_string)
-         if response_string:
-             send_message(conn, response_string)
+ def _handle_client(self, conn):  # now only producer
+     while ...:
+         raw = recv_message(conn)
+         work_queue.put(RPCRequest(next(_seq), raw, conn))

+ def dispatch_loop(self):  # consumer on main thread
+     while not self._shutdown_requested:
+         req = work_queue.get()
+         response = dispatch(req.raw)
+         if response:
+             send_message(req.conn, response)
```

## Performance Considerations
For typical RPC workloads dominated by CPU-bound handlers, serialization will not increase total throughput (handlers were never parallel-safe anyway). If handlers are I/O-bound and safe to parallelize, this design reduces concurrency—but that is intentional for safety. If you later need selective concurrency, you can:
- Tag certain methods as parallel-safe and dispatch them to a worker pool (`concurrent.futures.ThreadPoolExecutor`) while keeping unsafe ones serialized.
- Implement a registry: `SAFE_METHODS = {"echo"}` and branch in dispatcher.

## Links / References
- Python Queue: https://docs.python.org/3/library/queue.html
- Python selectors: https://docs.python.org/3/library/selectors.html
- jsonrpcserver docs: https://www.jsonrpcserver.com/
- anyio (optional abstraction): https://anyio.readthedocs.io/
- Trio (structured concurrency): https://trio.readthedocs.io/

## Recommendation
Start with **Option A (Queue + Reader Threads)** for the smallest, low-risk change. Only move to a `selectors`-based single-thread loop if you later want to eliminate reader threads or need tighter control over fairness.

---
Feel free to adapt snippets above; they intentionally omit unrelated code for clarity.
