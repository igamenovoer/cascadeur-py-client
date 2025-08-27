# Manual Testing for exec_code JSON-RPC Method

This guide describes how to test the `exec_code` JSON-RPC method for executing arbitrary Python code on the server.

## Prerequisites

1. Start a JSON-RPC pipe server that supports the `exec_code` method:
   ```bash
   pixi run -e dev python src/cascadeur_py_client/server/jsonrpc_pipe_server.py
   ```
   This will start a server on the default pipe (`cas-pipe`).

2. Or start with a custom pipe name:
   ```bash
   pixi run -e dev python tests/manual/run_ipc_server.py --pipe my-test-pipe
   ```

## Testing Code Execution

### Command Line Mode

Execute single line Python code:
```bash
pixi run -e dev python tests/manual/run_ipc_client.py --pipe cas-pipe --exec "result = 2 + 3"
```

Execute Python code from a file:
```bash
pixi run -e dev python tests/manual/run_ipc_client.py --pipe cas-pipe --exec-file my_script.py
```

### Interactive Mode

Start the client in interactive mode:
```bash
pixi run -e dev python tests/manual/run_ipc_client.py --pipe cas-pipe --interactive
```

Available exec commands in interactive mode:
- `exec <code>` - Execute single line Python code
- `execm` - Execute multiline Python code (enter END to finish)
- `execf <file>` - Execute Python code from a file

## Examples

### Single Line Execution
```
>>> exec result = sum(range(1, 11))

[SUCCESS] Code executed successfully
Result type: text/plain
----------------------------------------
Result: 55
```

### Multiline Code
```
>>> execm
Enter Python code (type 'END' on a new line to finish):
... def factorial(n):
...     if n <= 1:
...         return 1
...     return n * factorial(n - 1)
... 
... result = factorial(5)
... END

[SUCCESS] Code executed successfully
Result type: text/plain
----------------------------------------
Result: 120
```

### Error Handling
```
>>> exec result = 1 / 0

[ERROR] Execution failed (type 1):
ZeroDivisionError: division by zero
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

### Working with Different Data Types

**Lists and Dicts (JSON-serializable):**
```
>>> exec result = {'name': 'test', 'values': [1, 2, 3]}

[SUCCESS] Code executed successfully
Result type: application/json
----------------------------------------
{
  "name": "test",
  "values": [1, 2, 3]
}
```

**Binary Data:**
```
>>> exec result = b'binary data'

[SUCCESS] Code executed successfully
Result type: application/octet-stream
Encoding: base64
----------------------------------------
<bytes: 11 bytes>
Content: binary data
```

## Advanced Usage

### Using External Arguments

The `exec_code` method supports passing external arguments via `kw_binary_args`. This requires manual JSON-RPC construction:

```bash
# Use the raw command in interactive mode
>>> raw {"method": "exec_code", "params": {"code": "result = x + y", "kw_binary_args": "<base64-encoded-pickle>"}}
```

### Testing with Different Encodings

The code parameter can be base64-encoded:
```python
import base64
code_b64 = base64.b64encode("result = 42".encode()).decode()
# Then use: {"code": code_b64, "encoding": "base64"}
```

## Security Considerations

**WARNING:** The `exec_code` method executes arbitrary Python code on the server. Only use this in controlled environments and never expose it to untrusted users.

## Troubleshooting

1. **Connection Error**: Make sure the server is running with the same pipe name
2. **No exec_code method**: Ensure you're running a server that has the exec_code implementation
3. **Import errors in code**: The executed code runs in an isolated environment with limited imports