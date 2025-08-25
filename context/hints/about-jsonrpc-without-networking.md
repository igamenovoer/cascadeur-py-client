# About Using jsonrpcclient and jsonrpcserver Without Networking APIs

This hint explains how to use the `jsonrpcclient` and `jsonrpcserver` libraries for JSON-RPC 2.0 communication over local IPC mechanisms (named pipes, Unix domain sockets) without any HTTP or network APIs. Both libraries are transport-agnostic and work perfectly with OS-level IPC.

## Library Overview

### jsonrpcclient
- Purpose: Creates JSON-RPC 2.0 request objects and parses responses
- Transport: Completely transport-agnostic (no networking code)
- Core API:
  - Builders: `request()`, `notification()`; some versions also provide `request_json()`, `notification_json()` (otherwise `json.dumps(request(...))`)
  - Parser: `parse()` and `parse_json()`
  - Parsed types: `Ok` (success with `.result`) and `Error` (error with `.code`, `.message`, optional `.data`)

### jsonrpcserver
- Purpose: Dispatches JSON-RPC requests to methods and generates responses
- Transport: Transport-agnostic with optional basic HTTP server for development
- Core API:
  - Method reg: `@method`
  - Dispatcher: `dispatch()`
  - Responses: You can simply `return` Python values (recommended), or explicitly use `Success(...)` / `Error(...)`

## Key Advantages for IPC Use Cases

1. **No networking dependencies** - Pure protocol handling
2. **Transport flexibility** - Works with any message transport
3. **Clean separation** - Business logic separate from transport
4. **Easy testing** - Test with simple strings

## Basic Usage Pattern

### Server Side (Message Processing)
```python
from jsonrpcserver import method, dispatch, Success, Error

# Define your RPC methods
@method
def add(a, b):
    # You can return plain values; jsonrpcserver will wrap them into Success
    return a + b

@method
def get_version():
    return "1.0.0"

@method
def divide(a, b):
    if b == 0:
        # Invalid params is -32602 per spec; custom server errors use -32000..-32099
        return Error("Division by zero", code=-32602)
    return a / b

# Process incoming JSON-RPC messages (transport-agnostic)
def handle_message(request_string):
    """Process a JSON-RPC request string and return the response JSON string or None (notification)"""
    response_json = dispatch(request_string)
    return response_json  # JSON string or None for notifications

# Handle batch requests automatically
batch_request = '''[
    {"jsonrpc": "2.0", "method": "add", "params": [1, 2], "id": 1},
    {"jsonrpc": "2.0", "method": "get_version", "id": 2}
]'''
batch_response = dispatch(batch_request)
```

### Client Side (Message Creation)
```python
from jsonrpcclient import request, notification, parse_json, Ok
import json
import uuid

# Create JSON-RPC requests (dict form)
def create_request(method, params=None):
    """Create a JSON-RPC request as a Python dict"""
    return request(method, params)

# Create JSON string version (works even if request_json is not available)
def create_request_json(method, params=None):
    """Create a JSON-RPC request as JSON string"""
    try:
        from jsonrpcclient import request_json
        return request_json(method, params)
    except ImportError:
        return json.dumps(request(method, params))

# Create notifications (no response expected)
def create_notification(method, params=None):
    """Create a JSON-RPC notification as a Python dict"""
    return notification(method, params)

# Parse responses
def parse_response(response_string):
    """Parse JSON-RPC response JSON string and extract result or raise"""
    parsed = parse_json(response_string)
    if isinstance(parsed, Ok):
        return parsed.result
    else:
        # parsed is an Error object
        raise Exception(f"RPC Error: {parsed.message} (code: {parsed.code})")
```

## Integration with Named Pipes (Windows/Unix)

### Complete Server Example
```python
# jsonrpc_pipe_server.py
import os
import json
import struct
from multiprocessing.connection import Listener
from jsonrpcserver import method, dispatch, Success, Error

# Configure transport address
if os.name == 'nt':
    ADDRESS = r'\\.\pipe\jsonrpc_demo'
else:
    ADDRESS = '/tmp/jsonrpc_demo.sock'
    if os.path.exists(ADDRESS):
        os.unlink(ADDRESS)

# Define RPC methods
@method
def ping():
    return "pong"

@method
def add(a, b):
    return a + b

@method
def echo(message):
    return f"Echo: {message}"

# Framing helpers for reliable message boundaries
def send_message(conn, message_string):
    """Send JSON-RPC message with length prefix"""
    data = message_string.encode('utf-8')
    conn.send_bytes(struct.pack('!I', len(data)) + data)

def recv_message(conn):
    """Receive JSON-RPC message with length prefix"""
    blob = conn.recv_bytes()
    if len(blob) < 4:
        raise EOFError("Short frame")
    size = struct.unpack('!I', blob[:4])[0]
    return blob[4:4+size].decode('utf-8')

# Server main loop
def run_server():
    with Listener(ADDRESS) as listener:
        print(f"JSON-RPC server listening on {ADDRESS}")
        while True:
            conn = listener.accept()
            try:
                while True:
                    try:
                        # Receive JSON-RPC request
                        request_string = recv_message(conn)
                        print(f"Received: {request_string}")
                        
                        # Process with jsonrpcserver
                        response_string = dispatch(request_string)
                        
                        # Send response (skip for notifications)
                        if response_string:
                            send_message(conn, response_string)
                            print(f"Sent: {response_string}")
                            
                    except EOFError:
                        break
            finally:
                conn.close()

if __name__ == "__main__":
    run_server()
```

### Complete Client Example
```python
# jsonrpc_pipe_client.py
import os
import json
import struct
from multiprocessing.connection import Client
from jsonrpcclient import request_json, notification_json, parse_json

# Same address as server
if os.name == 'nt':
    ADDRESS = r'\\.\pipe\jsonrpc_demo'
else:
    ADDRESS = '/tmp/jsonrpc_demo.sock'

# Framing helpers (same as server)
def send_message(conn, message_string):
    data = message_string.encode('utf-8')
    conn.send_bytes(struct.pack('!I', len(data)) + data)

def recv_message(conn):
    blob = conn.recv_bytes()
    size = struct.unpack('!I', blob[:4])[0]
    return blob[4:4+size].decode('utf-8')

# High-level RPC client
class JSONRPCClient:
    def __init__(self, address):
        self.address = address
    
    def call(self, method, params=None):
        """Make a JSON-RPC call and return the result"""
        with Client(self.address) as conn:
            # Create request using jsonrpcclient
            try:
                from jsonrpcclient import request_json
                request_string = request_json(method, params)
            except ImportError:
                from jsonrpcclient import request
                import json as _json
                request_string = _json.dumps(request(method, params))
            
            # Send request
            send_message(conn, request_string)
            
            # Receive and parse response
            response_string = recv_message(conn)
            parsed = parse_json(response_string)
            
            if isinstance(parsed, Ok):
                return parsed.result
            else:
                raise Exception(f"RPC Error: {parsed.message} (code: {parsed.code})")
    
    def notify(self, method, params=None):
        """Send a notification (no response expected)"""
        with Client(self.address) as conn:
            # Create notification using jsonrpcclient
            try:
                from jsonrpcclient import notification_json
                notification_string = notification_json(method, params)
            except ImportError:
                from jsonrpcclient import notification
                import json as _json
                notification_string = _json.dumps(notification(method, params))
            send_message(conn, notification_string)

# Usage example
if __name__ == "__main__":
    client = JSONRPCClient(ADDRESS)
    
    try:
        # Make RPC calls
        result = client.call("ping")
        print(f"ping() -> {result}")
        
        result = client.call("add", [5, 3])
        print(f"add(5, 3) -> {result}")
        
        result = client.call("echo", ["Hello World"])
        print(f"echo('Hello World') -> {result}")
        
        # Send notification
        client.notify("log", ["Client connected"])
        
    except Exception as e:
        print(f"Error: {e}")
```

## Alternative Transport: Shared Memory + Events

For ultra-low latency scenarios, you can use shared memory with events.

Caution:
- `multiprocessing.Event()` objects are not named; they must be created in a parent process and shared (e.g., via `multiprocessing.Manager().Event()` or by passing the event objects to child processes). Creating separate `Event()` instances in different processes will not synchronize.
- The sketch below focuses on message flow; ensure you wire up shared Events via a Manager or inherit them properly.

```python
# Server using shared memory
from multiprocessing import shared_memory, Manager
from jsonrpcserver import dispatch

def shared_memory_server(req_ready, resp_ready):
    # Create shared memory segments
    req_shm = shared_memory.SharedMemory(create=True, size=4096, name='jsonrpc_req')
    resp_shm = shared_memory.SharedMemory(create=True, size=4096, name='jsonrpc_resp')
    try:
        while True:
            req_ready.wait()  # Wait for request signal
            req_ready.clear()
            # Read request
            req_len = int.from_bytes(req_shm.buf[:4], 'little')
            request_string = req_shm.buf[4:4+req_len].decode('utf-8')
            # Process
            response_string = dispatch(request_string)
            if response_string:
                resp_data = response_string.encode('utf-8')
                resp_shm.buf[:4] = len(resp_data).to_bytes(4, 'little')
                resp_shm.buf[4:4+len(resp_data)] = resp_data
                resp_ready.set()  # Signal response ready
    finally:
        req_shm.unlink()
        resp_shm.unlink()

# Client using shared memory (assumes req_ready/resp_ready are shared, e.g., via Manager)
def shared_memory_call(req_ready, resp_ready, method, params=None):
    from multiprocessing import shared_memory
    from jsonrpcclient import request, parse_json
    import json
    req_shm = shared_memory.SharedMemory(name='jsonrpc_req')
    resp_shm = shared_memory.SharedMemory(name='jsonrpc_resp')

    request_string = json.dumps(request(method, params))
    req_data = request_string.encode('utf-8')
    req_shm.buf[:4] = len(req_data).to_bytes(4, 'little')
    req_shm.buf[4:4+len(req_data)] = req_data

    resp_ready.clear()
    req_ready.set()
    resp_ready.wait()

    resp_len = int.from_bytes(resp_shm.buf[:4], 'little')
    response_string = resp_shm.buf[4:4+resp_len].decode('utf-8')
    parsed = parse_json(response_string)
    from jsonrpcclient import Ok
    return parsed.result if isinstance(parsed, Ok) else None
```

## File-Based Transport (Simple Fallback)

For simple scenarios or debugging:

```python
# File-based JSON-RPC
import os
import json
import time
import uuid
from jsonrpcclient import request_json, parse_json
from jsonrpcserver import dispatch

# Server: Monitor request directory
def file_server():
    req_dir = "requests"
    resp_dir = "responses"
    os.makedirs(req_dir, exist_ok=True)
    os.makedirs(resp_dir, exist_ok=True)
    
    processed = set()
    while True:
        for filename in os.listdir(req_dir):
            if filename in processed:
                continue
                
            req_path = os.path.join(req_dir, filename)
            try:
                with open(req_path, 'r') as f:
                    request_string = f.read()
                
                # Process with jsonrpcserver
                response_string = dispatch(request_string)
                
                if response_string:
                    # Write response
                    resp_path = os.path.join(resp_dir, filename)
                    with open(resp_path, 'w') as f:
                        f.write(response_string)
                
                processed.add(filename)
                os.remove(req_path)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        
        time.sleep(0.1)

# Client: Write request, read response
def file_call(method, params=None):
    req_id = str(uuid.uuid4())
    req_path = f"requests/{req_id}.json"
    resp_path = f"responses/{req_id}.json"
    
    # Create and write request
    request_string = request_json(method, params)
    with open(req_path, 'w') as f:
        f.write(request_string)
    
    # Wait for response
    timeout = 30
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(resp_path):
            with open(resp_path, 'r') as f:
                response_string = f.read()
            os.remove(resp_path)
            
            parsed = parse_json(response_string)
            return parsed.result if parsed.ok else None
        time.sleep(0.1)
    
    raise TimeoutError("No response received")
```

## Error Handling Best Practices

```python
from jsonrpcserver import method, Success, Error
from jsonrpcclient import parse_json

# Server-side error handling
@method
def safe_divide(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return Error("Invalid parameters", code=-32602)
        
        if b == 0:
            return Error("Division by zero", code=-32000)  # Custom error code
        
        return Success(a / b)
        
    except Exception as e:
        return Error(f"Internal error: {str(e)}", code=-32603)

# Client-side error handling
def robust_call(client, method, params=None, retries=3):
    for attempt in range(retries):
        try:
            result = client.call(method, params)
            return result
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(0.5 * (2 ** attempt))  # Exponential backoff
```

## Performance Considerations

1. **Connection Reuse**: Keep connections open for multiple requests
2. **Batch Requests**: Use JSON-RPC batch for multiple operations
3. **Async Processing**: Use async versions for concurrent handling
4. **Shared Memory**: For large data or ultra-low latency
5. **Message Framing**: Always use explicit framing for reliable delivery

## Security Notes

1. **Input Validation**: Always validate RPC method parameters
2. **Method Registration**: Only expose intended methods via `@method`
3. **Access Control**: Use IPC permissions (file permissions, pipe ACLs)
4. **Safe Serialization**: jsonrpcclient/server use JSON (safer than pickle)

## References

- jsonrpcclient: https://github.com/explodinglabs/jsonrpcclient
- jsonrpcserver: https://github.com/explodinglabs/jsonrpcserver
- jsonrpcclient docs: https://jsonrpcclient.readthedocs.io/
- jsonrpcserver docs: https://jsonrpcserver.readthedocs.io/
- JSON-RPC 2.0 Spec: https://www.jsonrpc.org/specification
- Python multiprocessing.connection: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.connection
- Windows Named Pipes: https://learn.microsoft.com/windows/win32/ipc/named-pipes
- Unix Domain Sockets: https://man7.org/linux/man-pages/man7/unix.7.html

## Summary

The jsonrpcclient and jsonrpcserver libraries provide clean, transport-agnostic JSON-RPC 2.0 handling that works perfectly with OS-level IPC mechanisms. Their design separates protocol concerns from transport, making them ideal for named pipes, Unix domain sockets, shared memory, or any custom message transport you need.
