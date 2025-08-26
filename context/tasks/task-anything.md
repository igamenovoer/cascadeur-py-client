# General Tasks Description

## Task 1: create a pipe-based json-rpc server

we are going to develop a named pipe based json-rpc server, such that:
- it never touches socket api
- it works on both windows and linux
- it processes requests and responses using a system pipe
  - pipe name is fixed as `\\.\pipe\my-test-pipe` on windows
- it accepts json-rpc 2.0 conformant requests, use responses using json-rpc 2.0 conformant responses
- the source code should be written to `src\cascadeur_client\server`

reference approach: `context\hints\about-jsonrpc-without-networking.md`