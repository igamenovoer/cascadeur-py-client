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