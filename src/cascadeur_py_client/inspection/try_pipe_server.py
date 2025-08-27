from cascadeur_py_client.server.jsonrpc_pipe_server import main as start_server
import cascadeur_py_client.caslogger as caslogger

clog = caslogger.logger

if __name__ == "__main__":
    clog.info("Starting server...")
    start_server()
    clog.info("Server stopped.")