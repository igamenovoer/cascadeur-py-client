# Task 1: Implement Cascadeur Remote Client

## References
- the `jsonrpc-client`: `src\cascadeur_py_client\server\jsonrpc_pipe_client.py`
- the `jsonrpc-server`: `src\cascadeur_py_client\server\jsonrpc_pipe_server.py`

## Task 1.1

create a `CascadeurRemoteClient` class in `src\cascadeur_py_client`, name the file `client.py`, and implement the following features:
- `from_pipe(pipe_name:str | None) -> CascadeurRemoteClient`: A static method that creates a `CascadeurRemoteClient` instance using the specified pipe name, when None is provided, use the default pipe name (`jsonrpc-client` will handle it).
- `send_python(code:str, args:dict | None) -> CallResult`: Executes the provided Python code with the given arguments and returns the result.
- `send_release()`: send the `release` command to the server to let it break out the main loop, so as to unfreeze the Cascadeur application GUI.
- `send_shutdown()`: send the `shutdown` command to the server to let it terminate.
- `send_echo(message:str) -> str`: Sends an echo message to the server and returns the echoed response, if error then raise an exception.

Implementation details:
- Use `jsonrpc-client` as a member of `CascadeurRemoteClient`, delegate the JSON-RPC communication to it.
- `jsonrpc-client` creates connections on demand, so no need to manage connection state in `CascadeurRemoteClient`.
- provide access to the underlying `jsonrpc-client` instance via a property named `rpc_client`.
- `jsonrpc-client` should be created in the constructor of `CascadeurRemoteClient`, and closed in a `close()` method of `CascadeurRemoteClient`.