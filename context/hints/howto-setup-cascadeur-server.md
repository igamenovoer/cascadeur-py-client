# How to Setup Cascadeur Server

## HEADER
- **Purpose**: Guide for setting up the JSON-RPC server inside Cascadeur
- **Status**: Active
- **Date**: 2025-01-22
- **Dependencies**: Cascadeur installation, Python environment
- **Target**: Developers and AI assistants

## Quick Start

### Option 1: Using Async Server (Recommended)
```python
# In Cascadeur's Python console
from cascadeur_py_client.server import health_exec_server_aio as aio_srv

# If no event loop is running (typical in Cascadeur)
handle = aio_srv.start_in_thread()

# Server now running on http://127.0.0.1:31005
# To stop later:
# handle.stop()
```

### Option 2: Using Threaded Server
```python
# In Cascadeur's Python console
from cascadeur_py_client.server import health_exec_server_threaded as threaded_srv

server = threaded_srv.HealthExecServer(port=31005)
server.start()

# To stop:
# server.stop()
```

## Testing the Server

### Health Check
```bash
curl -s -X POST http://127.0.0.1:31005/ \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"health"}'
```

Expected response:
```json
{"jsonrpc": "2.0", "id": 1, "result": {"status": "healthy", "version": "1.0.0"}}
```

### Execute Code
```python
import base64
import json
import requests

code = "import sys; print(sys.version)"
encoded = base64.b64encode(code.encode()).decode()

response = requests.post(
    "http://127.0.0.1:31005/",
    json={
        "jsonrpc": "2.0",
        "id": 2,
        "method": "exec_b64",
        "params": {"code_b64": encoded}
    }
)

result = response.json()
print(result["result"]["output"])
```

## Server Selection Guide

### Use Async Server When:
- Running in an environment with existing event loop
- Need non-blocking operation
- Want to handle multiple concurrent requests
- UI responsiveness is important

### Use Threaded Server When:
- Need true parallel execution
- CPU-bound operations are common
- Simpler mental model preferred
- Don't have asyncio experience

### Use Sync Server When:
- Debugging or development
- Simplest possible implementation needed
- Single request at a time is acceptable
- Learning the system

## Common Issues

### Port Already in Use
```python
# Change port number
handle = aio_srv.start_in_thread(port=31006)
```

### Server Not Accessible
- Check firewall settings
- Ensure binding to correct interface (127.0.0.1 for local only)
- Verify Cascadeur's Python has network permissions

### Code Execution Fails
- Check for import errors in executed code
- Ensure Cascadeur API is available in the execution context
- Look for Python version compatibility issues

## Best Practices
1. Always use base64 encoding for code transmission
2. Include error handling in executed code
3. Start server early in Cascadeur session
4. Use health checks to verify server status
5. Implement timeout for long-running operations

## Security Considerations
- Server binds to localhost only by default
- No authentication implemented (add if needed)
- Be cautious with code execution capabilities
- Consider adding request validation
- Log all executed code for audit trail