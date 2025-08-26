# General Tasks Description

## Task 1: create a pipe-based json-rpc server

we are going to develop a named pipe based json-rpc server, such that:
- it never touches socket api
- it works on both windows and linux
- it processes requests and responses using a system pipe
  - pipe name is fixed as `\\.\pipe\my-test-pipe` on windows
- it accepts json-rpc 2.0 conformant requests, use responses using json-rpc 2.0 conformant responses
- it has a `echo` method, which takes a single string parameter, and returns the same string
- the source code should be written to `src\cascadeur_client\server`

reference approach: `context\hints\about-jsonrpc-without-networking.md`

# Task 2: create a utility to inspect cascadeur state

- READ FIRST: Cascadeur python env notes: `context\instructions\cascadeur-env.md`

create a utility script that outputs the python interpreter info, such that:
- look for an env variable named `CASCADEUR_PYTHON_OUTPUT_DIR`, if it exists, write the output file to that directory, otherwise write to system temp directory
- the output file name is `cascadeur_python_info.json`

# Task 3: testing outgoing communication from cascadeur

- READ FIRST: Cascadeur python env notes: `context\instructions\cascadeur-env.md`
- json rpc server: `src\cascadeur_client\server\jsonrpc_pipe_server.py`
- json rpc client: `src\cascadeur_client\client\jsonrpc_pipe_client.py`

create a one-off script, that behaves as follows:
- just like the client, it connects to the json-rpc server using the named pipe `\\.\pipe\my-test-pipe` on windows
- and sends an `echo` request with a string parameter, e.g. "hello from test script"
- it gets back the response, and prints it to console
- then finished

create the script in `src\cascadeur_client\inspection/try_pipe_client.py`

# Task 4: implement a synchronous jsonrpc pipe server

- multi-threaded json rpc server (`mt-pipe-server`): `src\cascadeur_client\server\jsonrpc_pipe_server.py`

now implement as synchronous jsonrpc pipe server, such that:
- the core behavior is just like `mt-pipe-server`, but it is single-threaded, received messages are processed in the one by one in main thread
- once called the start(), it blocks the caller thread, and it will NOT create threads for clients, just a single thread, receives and processes messages one by one
- incoming messages are queued (implicitly by system), we do not need to implement an explicit queue

the implemented server should be in `src\cascadeur_client\server\jsonrpc_pipe_server_sync.py`