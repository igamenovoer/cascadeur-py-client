# Cascadeur Python Client

A pythonic client API and IPC bridge to interface with [Cascadeur](https://cascadeur.com/) animation software.

## Overview

Cascadeur is a physics-based animation software that allows animators to create realistic character animations. This Python client library provides:

1. **High-level Python API**: A pythonic interface to interact with Cascadeur's native Python API
2. **JSON-RPC IPC Bridge**: Remote code execution capability for external tools to communicate with Cascadeur's embedded Python environment

The IPC bridge is particularly important because Cascadeur uses an embedded Python interpreter that lacks console access, making it challenging to run interactive scripts or integrate with external development tools.

## Features

- **High-level API**: Simplified, pythonic interface over Cascadeur's native Python API
- **JSON-RPC Server**: Execute Python code remotely in Cascadeur's environment via named pipes
- **Remote Code Execution**: Run scripts, automation, and tools from external Python environments
- **Scene Management**: Easy scene creation, loading, and manipulation
- **Animation Tools**: Programmatic access to Cascadeur's animation tools
- **Rig Management**: Create and modify character rigs
- **Asset Management**: Handle mesh data and assets
- **Node Editor Integration**: Work with Cascadeur's node-based update system

## Installation

```bash
pip install cascadeur-py-client
```

## Quick Start

### Using the Python API

```python
import cascadeur_py_client as csc

# Connect to Cascadeur
client = csc.CascadeurClient()

# Load a scene
scene = client.load_scene("path/to/scene.casc")

# Get all joints in the scene
joints = scene.get_joints()

# Move a joint
joint = joints[0]
joint.move_to(x=10, y=20, z=30)

# Save the scene
scene.save("path/to/modified_scene.casc")
```

### Using the JSON-RPC IPC Bridge

The IPC bridge allows external tools to execute Python code within Cascadeur's embedded environment:

```python
# In Cascadeur's Python environment, start the server:
from cascadeur_py_client.server.jsonrpc_pipe_server import JSONRPCPipeServer
server = JSONRPCPipeServer(pipe_name="cas-pipe")
server.start()
```

```python
# From external Python environment, connect and execute code:
from cascadeur_py_client.server.jsonrpc_pipe_client import JSONRPCPipeClient

# Connect to the server
client = JSONRPCPipeClient(r"\\.\pipe\cas-pipe")  # Windows
# client = JSONRPCPipeClient("/tmp/cas-pipe.sock")  # Linux/macOS

# Execute code in Cascadeur's environment
response = client.call("exec_code", {
    "code": """
import csc
scene = csc.get_scene()
result = len(scene.get_joints())
"""
})

print(f"Number of joints: {response['data']}")
```

## JSON-RPC Server Details

### Remote Code Execution

The `exec_code` method enables remote Python code execution within Cascadeur's embedded environment. This is essential for:

- **Development and Debugging**: Test and debug scripts without restarting Cascadeur
- **External Tool Integration**: IDEs and development tools can execute code directly
- **Automation Pipelines**: CI/CD systems can run automated tests and validations
- **Interactive Scripting**: REPL-like experience for exploratory programming

#### Security Warning

⚠️ **The `exec_code` method executes arbitrary Python code. Only use in trusted environments and never expose the named pipe to untrusted sources.**

#### Advanced Usage

```python
# Execute code with external arguments
import base64
import pickle

# Prepare keyword arguments
kw_args = {"frame_number": 42, "joint_name": "spine_01"}
kw_args_binary = base64.b64encode(pickle.dumps(kw_args)).decode()

response = client.call("exec_code", {
    "code": "result = process_frame(frame_number, joint_name)",
    "kw_binary_args": kw_args_binary
})

# Handle different response types
if response["error"]["type"] != 0:
    print(f"Error: {response['error']['message']}")
    print(f"Traceback: {response['error']['traceback']}")
elif response["encoding"] == "base64":
    # Binary or pickled data
    import base64, pickle
    data = pickle.loads(base64.b64decode(response["data"]))
else:
    # JSON-compatible data
    data = response["data"]
```

### Named Pipe Configuration

The server uses named pipes for IPC:
- **Windows**: `\\.\pipe\<pipe_name>`
- **Unix/Linux/macOS**: `/tmp/<pipe_name>.sock`

Pipe names can be configured via the `CASCADEUR_PYTHON_RPC_PIPE_NAME` environment variable.

## Requirements

- Python 3.7+ (3.11 recommended for Cascadeur compatibility)
- Cascadeur 2022.1+ (with Python API support)
- Windows: pywin32 (for named pipe support)
- Unix/Linux/macOS: Standard library only

## Testing

### Manual Testing of JSON-RPC Server

```bash
# Start the test server
python src/cascadeur_py_client/server/jsonrpc_pipe_server.py

# In another terminal, run the interactive client
python tests/manual/run_ipc_client.py --pipe cas-pipe --interactive

# Execute code directly
python tests/manual/run_ipc_client.py --pipe cas-pipe --exec "result = 2 + 2"

# Execute from file
python tests/manual/run_ipc_client.py --pipe cas-pipe --exec-file script.py
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