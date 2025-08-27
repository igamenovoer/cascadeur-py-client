# Cascadeur Python Client

Remote Python execution bridge for [Cascadeur](https://cascadeur.com/) animation software.

## Overview

This library enables external Python environments to execute code within Cascadeur's embedded Python interpreter through a JSON-RPC bridge over named pipes. This solves the challenge that Cascadeur's Python environment lacks console access, making it difficult to run interactive scripts or integrate with development tools.

## Features

- **Remote Code Execution**: Execute Python code in Cascadeur from external environments
- **High-level Client API**: Simple `CascadeurRemoteClient` for easy interaction
- **JSON-RPC Server**: Robust server implementation with concurrent client support
- **Error Handling**: Comprehensive error reporting with tracebacks
- **Binary Data Support**: Handle both JSON and binary data via base64 encoding
- **Cross-platform**: Works on Windows (named pipes) and Unix (domain sockets)

## Installation

```bash
pip install cascadeur-py-client
```

## Quick Start

### 1. Start the Server in Cascadeur

In Cascadeur's Python environment (via a startup script or the Python console if available):

```python
from cascadeur_py_client.server.jsonrpc_pipe_server import JSONRPCPipeServer
server = JSONRPCPipeServer()  # Uses default pipe name
server.start()
```

### 2. Connect from External Python

```python
from cascadeur_py_client.client import CascadeurRemoteClient

# Create client
client = CascadeurRemoteClient.from_pipe()  # Auto-detects pipe

# Test connection
response = client.send_echo("Hello Cascadeur!")
print(response)  # "Hello Cascadeur!"

# Execute Python code in Cascadeur
result = client.send_python("""
import csc
joints = csc.get_scene().get_joints()
result = len(joints)
""")

if result.success:
    print(f"Number of joints: {result.data}")
else:
    print(f"Error: {result.error.message}")

# Execute with arguments
code = "result = a + b"
result = client.send_python(code, {"a": 10, "b": 20})
print(f"Result: {result.data}")  # 30
```

## API Details

### CascadeurRemoteClient

The high-level client provides a clean interface for remote execution:

```python
from cascadeur_py_client.client import CascadeurRemoteClient

client = CascadeurRemoteClient.from_pipe()  # or specify pipe name
result = client.send_python("result = 2 + 2")
print(result.data)  # 4

# Control commands
client.send_release()  # Unfreeze Cascadeur GUI
client.send_shutdown()  # Terminate server
```

### Low-level JSON-RPC Client

For direct JSON-RPC communication:

```python
from cascadeur_py_client.server.jsonrpc_pipe_client import JSONRPCPipeClient

client = JSONRPCPipeClient()
response = client.call("exec_code", {
    "code": "result = 42",
    "encoding": None  # or "base64" for binary code
})
```

### Security Warning

⚠️ **The server executes arbitrary Python code. Only use in trusted environments.**

## Configuration

### Named Pipes

- **Windows**: `\\.\pipe\<pipe_name>` (default: `\\.\pipe\cas-pipe`)
- **Unix/Linux/macOS**: `/tmp/<pipe_name>.sock` (default: `/tmp/cas-pipe.sock`)

Set custom pipe name via environment variable:
```bash
export CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
```

## Requirements

- Python 3.7+ (3.11 recommended for Cascadeur compatibility)
- Cascadeur 2022.1+ (with Python API support)
- Windows: pywin32 (for named pipe support)
- Unix/Linux/macOS: Standard library only

## Testing

```bash
# Start a test server (if not in Cascadeur)
python src/cascadeur_py_client/server/jsonrpc_pipe_server.py

# Test with high-level client
python -c "from cascadeur_py_client.client import CascadeurRemoteClient; 
client = CascadeurRemoteClient.from_pipe(); 
print(client.send_echo('test'))"

# Interactive testing
python src/cascadeur_py_client/server/jsonrpc_pipe_client.py --interactive
```

## Documentation

Full documentation is available at [Read the Docs](https://cascadeur-py-client.readthedocs.io/) (coming soon).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cascadeur](https://cascadeur.com/) by Nekki - The amazing physics-based animation software
- The Cascadeur development team for providing the Python API

## Related Links

- [Cascadeur Official Website](https://cascadeur.com/)
- [Cascadeur Python API Documentation](https://cascadeur.com/help/category/215)
- [Cascadeur Community](https://cascadeur.com/community)

## Disclaimer

This is an unofficial client library. It is not affiliated with or endorsed by Nekki or the Cascadeur development team.