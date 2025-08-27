"""
Synchronous JSON-RPC 2.0 Server using Named Pipes

This module implements a single-threaded, synchronous JSON-RPC 2.0 server that
processes requests one by one in the main thread without creating any additional threads.

Environment Variables:
    CASCADEUR_PYTHON_RPC_PIPE_NAME:
        Sets the default pipe name for the JSON-RPC server to listen on.
        If not set, defaults to "cas-pipe".

        Usage:
            # Windows
            set CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
            python server_sync.py  # Listens on \\\\.\\pipe\\my-custom-pipe

            # Linux/macOS
            export CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
            python server_sync.py  # Listens on /tmp/my-custom-pipe.sock

        Note: You can override this by passing an explicit address to the server constructor.

        This synchronous version is ideal for:
        - Embedded Python environments (like Cascadeur)
        - Simple request/response patterns
        - Situations where thread safety is a concern

Commands:
    echo: Echo back the received message
    release: Break main loop but keep pipe open (allows server restart)
    shutdown: Completely shut down server and close pipe
    quit: Alias for shutdown (backward compatibility)
"""

import os
import sys
import json
import struct
import signal
import threading
import atexit
import weakref
import uuid
import time
from typing import Optional, Any
from multiprocessing.connection import Listener, Client, Connection
from jsonrpcserver import method, dispatch

try:
    # Try to import the modern API (version 5.x)
    from jsonrpcserver import Success, Error
except ImportError:
    # Fallback for older versions that use result module
    from jsonrpcserver.result import Success, Error

# Use centralized logging from caslogger
from cascadeur_py_client.caslogger import get_logger, LogContext

# Import pipe utilities
from cascadeur_py_client.server.pipe_utils import get_default_pipe_address

logger = get_logger("jsonrpc_pipe_server_sync")

# Configure default pipe address based on environment and platform
PIPE_ADDRESS = get_default_pipe_address()

# Global server instance for quit/release/shutdown commands and cleanup
_server_instance: Optional["SyncJSONRPCPipeServer"] = None
_active_servers: weakref.WeakSet[Any] = weakref.WeakSet()


def cleanup_pipe(address: str) -> None:
    """
    Clean up named pipe or Unix socket.

    Args:
        address: The pipe/socket address to clean up
    """
    if os.name == "nt":
        # Windows named pipes are cleaned up when all handles are closed
        # But we'll ensure any lingering connections are closed
        try:
            # Try to connect and immediately disconnect to clear any stuck state
            dummy = Client(address)
            dummy.close()
            logger.debug(f"Cleared Windows pipe state for: {address}")
        except Exception as e:
            logger.debug(f"Could not clear pipe state for {address}: {e}")
    else:
        # Unix domain sockets need explicit file removal
        if os.path.exists(address):
            try:
                os.unlink(address)
                logger.debug(f"Removed Unix socket: {address}")
            except Exception as e:
                logger.debug(f"Could not remove socket {address}: {e}")


def cleanup_all_pipes() -> None:
    """Clean up all registered server pipes on exit."""
    for server in list(_active_servers):
        try:
            if hasattr(server, "address"):
                cleanup_pipe(server.address)
                logger.debug(f"Cleaned up pipe: {server.address}")
        except Exception as e:
            logger.debug(f"Error during pipe cleanup: {e}")


# Register cleanup on exit
atexit.register(cleanup_all_pipes)


# Helper functions
def is_main_thread() -> bool:
    """
    Check if we're running in the main thread of the main interpreter.

    Returns:
        True if in main thread and signal handlers can be registered
    """
    try:
        # Try to check if we're in the main thread
        return threading.current_thread() is threading.main_thread()
    except AttributeError:
        # Python < 3.4 doesn't have main_thread()
        return threading.current_thread().name == "MainThread"


# Define JSON-RPC methods
@method
def echo(*args: Any, **kwargs: Any) -> Any:
    """
    Echo method that returns the same string it receives.
    Handles both positional and keyword arguments.

    Args:
        message: String to echo back (can be positional or keyword)

    Returns:
        The same string that was received wrapped in Success
    """
    # Handle positional arguments
    if args and len(args) > 0:
        message = args[0]
    # Handle keyword arguments
    elif "message" in kwargs:
        message = kwargs["message"]
    else:
        return Error(code=-32602, message="Missing required parameter 'message'")

    if not isinstance(message, str):
        return Error(code=-32602, message="Parameter must be a string")

    # Return Success result with the message
    return Success(message)


@method
def release() -> Any:
    """
    Release the server from the main loop but keep the pipe open.
    The server can be restarted by calling main() again.

    Returns:
        Success message indicating server released
    """
    global _server_instance
    if _server_instance:
        logger.info(
            "Release command received, breaking main loop but keeping pipe open..."
        )
        _server_instance._release_requested = True
        return Success("Server released from main loop")
    else:
        return Error(code=-32603, message="No server instance found")


@method
def shutdown() -> Any:
    """
    Shutdown the server completely, closing the pipe.

    Returns:
        Success message indicating shutdown initiated
    """
    global _server_instance
    if _server_instance:
        logger.info("Shutdown command received, initiating full shutdown...")
        _server_instance._shutdown_requested = True
        return Success("Server shutdown initiated")
    else:
        return Error(code=-32603, message="No server instance found")


@method
def quit() -> Any:
    """
    Alias for shutdown command (for backward compatibility).

    Returns:
        Success message indicating shutdown initiated
    """
    return shutdown()


# Message framing helpers
def send_message(conn: Connection, message_string: str) -> None:
    """
    Send a JSON-RPC message with a length prefix for proper framing.

    Args:
        conn: The connection object from multiprocessing.connection
        message_string: The JSON-RPC message string to send
    """
    if message_string:
        data = message_string.encode("utf-8")
        # Send message with 4-byte length prefix (big-endian)
        length_prefix = struct.pack("!I", len(data))
        conn.send_bytes(length_prefix + data)
        logger.debug(f"Sent message: {message_string}")


def recv_message(conn: Connection) -> str:
    """
    Receive a JSON-RPC message with length prefix.

    Args:
        conn: The connection object from multiprocessing.connection

    Returns:
        The received JSON-RPC message string

    Raises:
        EOFError: If the connection is closed or message is incomplete
    """
    # Receive the complete message
    blob = conn.recv_bytes()

    if len(blob) < 4:
        raise EOFError("Message too short to contain length prefix")

    # Extract length from first 4 bytes (big-endian)
    expected_length = struct.unpack("!I", blob[:4])[0]
    actual_data = blob[4:]

    if len(actual_data) != expected_length:
        logger.warning(
            f"Length mismatch: expected {expected_length}, got {len(actual_data)}"
        )

    message = actual_data.decode("utf-8")
    logger.debug(f"Received message: {message}")
    return message


class SyncJSONRPCPipeServer:
    """
    Synchronous JSON-RPC 2.0 server that uses named pipes for communication.
    Processes all requests in a single thread without creating any additional threads.
    """

    def __init__(self, address: Optional[str] = None):
        """
        Initialize the synchronous JSON-RPC pipe server.

        Args:
            address: The pipe address. If None, uses environment variable or default.
        """
        global _server_instance
        self.address = address if address else get_default_pipe_address()
        self.running = False
        self.listener: Optional[Listener] = None
        self._shutdown_requested = False
        self._release_requested = False

        # Set global instance for quit/release/shutdown commands
        _server_instance = self
        # Register for cleanup
        _active_servers.add(self)

        logger.info(f"Initialized synchronous server with address: {self.address}")

    def __del__(self) -> None:
        """Cleanup on garbage collection."""
        self._cleanup()

    def _cleanup(self, close_listener: bool = True) -> None:
        """Perform cleanup of pipes and resources.

        Args:
            close_listener: If True, close the listener. If False, keep it open.
        """
        try:
            # Close listener if requested
            if close_listener and self.listener:
                try:
                    self.listener.close()
                    logger.debug("Listener closed successfully")
                except Exception as e:
                    logger.debug(f"Error closing listener: {e}")
                self.listener = None

            # Clean up the pipe/socket only if listener is closed
            if close_listener:
                cleanup_pipe(self.address)

        except Exception as e:
            logger.debug(f"Cleanup error (non-critical): {e}")

    def _handle_client_sync(self, conn: Connection) -> None:
        """
        Handle a client connection synchronously in the main thread.

        Args:
            conn: The connection object from multiprocessing.connection
        """
        # Generate unique connection ID for tracking
        connection_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        request_count = 0

        with LogContext(logger, {"conn_id": connection_id}):
            logger.info(
                f"Client connected - handling synchronously (connection_id={connection_id})"
            )

            try:
                while not self._shutdown_requested and not self._release_requested:
                    try:
                        # Receive JSON-RPC request
                        logger.debug(
                            f"Waiting for request from connection {connection_id}"
                        )
                        request_string = recv_message(conn)
                        request_count += 1

                        # Try to extract request ID for logging
                        request_id = None
                        try:
                            request_data = json.loads(request_string)
                            request_id = request_data.get("id", "notification")
                            method = request_data.get("method", "unknown")
                            logger.debug(
                                f"Processing request #{request_count}: method={method}, id={request_id}"
                            )
                        except Exception:
                            logger.debug(
                                f"Processing request #{request_count} (could not parse for logging)"
                            )

                        # Process the request with jsonrpcserver
                        response_string = dispatch(request_string)

                        # Send response (skip for notifications)
                        if response_string:
                            send_message(conn, response_string)
                            logger.info(
                                f"Processed request #{request_count} and sent response (method={method if 'method' in locals() else 'unknown'})"
                            )
                        else:
                            logger.info(
                                f"Processed notification #{request_count} (no response required)"
                            )

                        # Check if this was a quit/shutdown/release command
                        if self._shutdown_requested or self._release_requested:
                            logger.info(
                                f"{'Shutdown' if self._shutdown_requested else 'Release'} requested during request processing (connection {connection_id})"
                            )
                            break

                    except EOFError:
                        # Client disconnected normally
                        logger.debug(
                            f"Client {connection_id} closed connection normally"
                        )
                        break
                    except Exception as e:
                        if self._shutdown_requested or self._release_requested:
                            logger.debug(
                                f"Error during {'shutdown' if self._shutdown_requested else 'release'} for connection {connection_id}: {e}"
                            )
                            break
                        logger.error(
                            f"Error handling client request from {connection_id}: {e}",
                            exc_info=True,
                        )
                        # Send error response
                        error_response = json.dumps(
                            {
                                "jsonrpc": "2.0",
                                "error": {
                                    "code": -32603,
                                    "message": f"Internal error: {str(e)}",
                                },
                                "id": None,
                            }
                        )
                        try:
                            send_message(conn, error_response)
                            logger.debug(f"Sent error response to {connection_id}")
                        except Exception as send_error:
                            logger.error(
                                f"Failed to send error response to {connection_id}: {send_error}"
                            )
                        break
            finally:
                conn.close()
                duration = time.time() - start_time
                logger.info(
                    f"Client {connection_id} disconnected after {duration:.2f}s and {request_count} requests"
                )

    def start(self, reuse_listener: bool = False) -> None:
        """
        Start the synchronous JSON-RPC server and listen for connections.
        This method blocks the calling thread and processes clients one by one.

        Args:
            reuse_listener: If True and a listener exists, reuse it instead of creating new one.
        """
        # Reset release flag at start
        self._release_requested = False

        # Only clean up if we're not reusing an existing listener
        if not reuse_listener or not self.listener:
            # Clean up any existing pipe/socket before starting
            cleanup_pipe(self.address)

        # Check if we can setup signal handlers
        can_use_signals = is_main_thread()

        if can_use_signals:
            # Setup signal handlers for graceful shutdown
            def signal_handler(signum: int, frame: Any) -> None:
                """Handle Ctrl+C gracefully."""
                logger.info(f"Received signal {signum}, shutting down...")
                self._shutdown_requested = True

                # Close listener to unblock accept()
                if self.listener:
                    try:
                        self.listener.close()
                        logger.debug("Listener closed by signal handler")
                    except Exception as e:
                        logger.debug(f"Error closing listener in signal handler: {e}")

                # On Windows, send dummy connection to unblock accept()
                if os.name == "nt":
                    try:
                        dummy = Client(self.address)
                        dummy.close()
                        logger.debug("Sent dummy connection to unblock accept()")
                    except Exception as e:
                        logger.debug(f"Could not send dummy connection: {e}")

            try:
                # Setup signal handlers
                signal.signal(signal.SIGINT, signal_handler)
                signal.signal(signal.SIGTERM, signal_handler)
                logger.info("Signal handlers registered (Ctrl+C to stop)")
            except Exception as e:
                # If signal setup fails, continue without it
                logger.warning(f"Could not setup signal handlers: {e}")
                logger.info("Use the 'quit' JSON-RPC method to stop the server")
                can_use_signals = False
        else:
            logger.info("Running in non-main thread/interpreter (e.g., Jupyter)")
            logger.info("Use the 'quit' JSON-RPC method to stop the server")

        try:
            # Create listener only if needed
            if not self.listener:
                self.listener = Listener(self.address)
                logger.info(f"Created new listener on {self.address}")
            else:
                logger.info(f"Reusing existing listener on {self.address}")

            self.running = True
            logger.info(f"Synchronous JSON-RPC server listening on {self.address}")
            logger.info("Processing clients one at a time in main thread")

            while not self._shutdown_requested and not self._release_requested:
                try:
                    # Accept connection (this blocks)
                    logger.debug(
                        f"Server ready, waiting for client connection on {self.address}..."
                    )
                    conn = self.listener.accept()

                    if self._shutdown_requested or self._release_requested:
                        conn.close()
                        logger.debug(
                            f"Connection closed due to {'shutdown' if self._shutdown_requested else 'release'} request"
                        )
                        break

                    # Handle client synchronously in main thread
                    # This blocks until client disconnects
                    logger.debug("New client connection accepted, starting handler")
                    self._handle_client_sync(conn)

                except OSError as e:
                    if self._shutdown_requested or self._release_requested:
                        break
                    logger.error(f"Error accepting connection: {e}")
                except Exception as e:
                    if self._shutdown_requested or self._release_requested:
                        break
                    logger.error(f"Error in accept loop: {e}")

        except Exception as e:
            logger.error(f"Failed to start server: {e}")
            self._cleanup(close_listener=True)
            raise
        finally:
            self.running = False
            # Only close listener on shutdown, not on release
            if self._shutdown_requested:
                self._cleanup(close_listener=True)
                logger.info("Server shutdown complete")
            else:
                # Release mode - keep listener open
                logger.info("Server released from main loop (listener kept open)")

    def stop(self, full_shutdown: bool = True) -> None:
        """
        Stop the synchronous JSON-RPC server.

        Args:
            full_shutdown: If True, close everything. If False, just release from loop.
        """
        if full_shutdown:
            self._shutdown_requested = True
            logger.info("Server stopping (full shutdown)...")
        else:
            self._release_requested = True
            logger.info("Server releasing from loop...")
        self.running = False

        # Close the listener to unblock accept()
        if self.listener:
            try:
                self.listener.close()
                logger.debug("Listener closed in stop()")
            except Exception as e:
                logger.debug(f"Error closing listener in stop(): {e}")

        # On Windows, send a dummy connection to unblock accept()
        if os.name == "nt":
            try:
                dummy = Client(self.address)
                dummy.close()
                logger.debug("Sent dummy connection in stop()")
            except Exception as e:
                logger.debug(f"Could not send dummy connection in stop(): {e}")

        # Ensure cleanup (full cleanup only on shutdown)
        if full_shutdown:
            self._cleanup(close_listener=True)
        else:
            logger.debug("Release mode - keeping listener open")


def main() -> None:
    """
    Main entry point for running the synchronous JSON-RPC pipe server.
    Supports restarting after release command.
    """
    global _server_instance

    # Check if we have an existing server instance (from release)
    if _server_instance and _server_instance.listener:
        server = _server_instance
        logger.info("Reusing existing server instance after release")
        reuse_listener = True
    else:
        server = SyncJSONRPCPipeServer()
        reuse_listener = False

    try:
        logger.info("=" * 60)
        logger.info("Starting Synchronous JSON-RPC Pipe Server")
        logger.info(f"Platform: {os.name}")
        logger.info(f"Pipe address: {server.address}")
        logger.info("Mode: Single-threaded, synchronous processing")
        logger.info("=" * 60)

        # Check if we're in main thread
        if is_main_thread():
            logger.info(
                "Press Ctrl+C to stop (or use 'shutdown'/'release' RPC methods)"
            )
        else:
            logger.info("Send 'shutdown' to stop server, 'release' to pause it")

        # This blocks until shutdown or release
        server.start(reuse_listener=reuse_listener)

        # Check if it was a release (not shutdown)
        if server._release_requested and not server._shutdown_requested:
            logger.info("Server released - can be restarted by calling main() again")
            return  # Exit cleanly without cleanup

    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        server.stop(full_shutdown=True)
    except Exception as e:
        logger.error(f"Server error: {e}")
        server._cleanup()
        sys.exit(1)
    finally:
        # Final cleanup attempt (only on shutdown)
        if server and server._shutdown_requested:
            server._cleanup(close_listener=True)


if __name__ == "__main__":
    main()

# To start the server in a separate thread (e.g., for jupyter notebooks)
# import threading
# th = threading.Thread(target=main)
# th.start()
