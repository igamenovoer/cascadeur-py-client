# General Tasks Description

## Task 1: create a pipe-based json-rpc server

we are going to develop a named pipe based json-rpc server, such that:
- it never touches socket api
- it works on both windows and linux
- it processes requests and responses using a system pipe
  - pipe name is given in env variable `NOSOCK_SERVER_PIPE_NAME`
- it accepts json-rpc 2.0 conformant requests

- reference approach: `context\hints\about-single-machine-server-client-ipc.md`