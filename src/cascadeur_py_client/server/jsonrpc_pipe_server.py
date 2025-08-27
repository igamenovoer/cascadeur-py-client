"""
JSON-RPC 2.0 Server using Named Pipes (Multi-threaded)

This module implements a JSON-RPC 2.0 server that communicates through
named pipes (Windows) or Unix domain sockets (Linux/macOS) without any
network/socket APIs. This version handles multiple clients concurrently
using threads.

Environment Variables:
    CASCADEUR_PYTHON_RPC_PIPE_NAME:
        Sets the default pipe name for the JSON-RPC server to listen on.
        If not set, defaults to "cas-pipe".

        Usage:
            # Windows
            set CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
            python server.py  # Listens on \\\\.\\pipe\\my-custom-pipe

            # Linux/macOS
            export CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
            python server.py  # Listens on /tmp/my-custom-pipe.sock

        Note: You can override this by passing an explicit address to the server constructor.

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
import time
import itertools
from dataclasses import dataclass, field
from queue import Queue, Empty
from typing import Optional, Any, Union
from multiprocessing.connection import Listener, Client
from jsonrpcserver import method, dispatch

try:
    # Try to import the modern API (version 5.x)
    from jsonrpcserver import Success, Error
except ImportError:
    # Fallback for older versions that use result module
    from jsonrpcserver.result import Success, Error

# Use centralized logging from caslogger
from cascadeur_py_client.caslogger import get_logger

# Import pipe utilities
from cascadeur_py_client.server.pipe_utils import get_default_pipe_address

logger = get_logger("jsonrpc_pipe_server")

# Configure default pipe address based on environment and platform
PIPE_ADDRESS = get_default_pipe_address()

# Global server instance for quit command and cleanup
_server_instance: Optional["JSONRPCPipeServer"] = None
_active_servers: weakref.WeakSet[Any] = weakref.WeakSet()

# Sequence counter for request ordering
_seq_counter = itertools.count()


@dataclass(order=True)
class RPCRequest:
    """Represents an RPC request in the work queue."""
    seq: int = field(compare=True)  # Sequence number for ordering
    raw: str = field(compare=False)  # Raw JSON-RPC request string
    conn: Any = field(compare=False)  # Connection object
    id: Optional[Union[str, int]] = field(compare=False, default=None)  # Request ID
    timestamp: float = field(compare=False, default_factory=time.time)


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
        except Exception:
            pass
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
        except Exception:
            pass


# Register cleanup on exit
atexit.register(cleanup_all_pipes)


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
    This allows the server to be restarted by calling main() again.

    Returns:
        Success message indicating server released
    """
    global _server_instance
    if _server_instance:
        logger.info(
            "Release command received, breaking main loop but keeping pipe open..."
        )
        _server_instance._release_requested = True

        # Schedule disconnect in a separate thread to allow response to be sent
        def delayed_release() -> None:
            import time

            time.sleep(0.5)  # Give time for response to be sent
            _server_instance._disconnect_all_clients()

            # On Windows, send a dummy connection to unblock accept()
            if os.name == "nt" and not _server_instance._shutdown_in_progress:
                _server_instance._shutdown_in_progress = True
                try:
                    dummy = Client(_server_instance.address)
                    dummy.close()
                except Exception:
                    pass

        release_thread = threading.Thread(target=delayed_release)
        release_thread.daemon = True
        release_thread.start()

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

        # Schedule shutdown in a separate thread to allow response to be sent
        def delayed_shutdown() -> None:
            import time

            time.sleep(0.5)  # Give time for response to be sent
            _server_instance._disconnect_all_clients()

            # Close the listener to unblock accept()
            if _server_instance.listener:
                try:
                    _server_instance.listener.close()
                except Exception:
                    pass

            # On Windows, send a dummy connection to unblock accept()
            if os.name == "nt" and not _server_instance._shutdown_in_progress:
                _server_instance._shutdown_in_progress = True
                try:
                    dummy = Client(_server_instance.address)
                    dummy.close()
                except Exception:
                    pass

        shutdown_thread = threading.Thread(target=delayed_shutdown)
        shutdown_thread.daemon = True
        shutdown_thread.start()

        return Success("Server shutdown initiated")
    else:
        return Error(code=-32603, message="No server instance found")


@method
def quit() -> Any:
    """
    Shutdown the server gracefully (alias for shutdown).
    This is an alternative to Ctrl+C for environments where signal handling doesn't work.

    Returns:
        Success message indicating shutdown initiated
    """
    # quit is now an alias for shutdown
    return shutdown()


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


# Message framing helpers
def send_message(conn: Any, message_string: str) -> None:
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


def recv_message(conn: Any) -> str:
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

    message: str = actual_data.decode("utf-8")
    logger.debug(f"Received message: {message}")
    return message


class JSONRPCPipeServer:
    """
    JSON-RPC 2.0 server that uses named pipes for communication.
    All RPC method executions happen strictly on the main thread.
    """

    def __init__(self, address: Optional[str] = None):
        """
        Initialize the JSON-RPC pipe server.

        Args:
            address: The pipe address. If None, uses environment variable or default.
        """
        global _server_instance
        self.address = address if address else get_default_pipe_address()
        self.running = False
        self.listener: Optional[Listener] = None
        self._shutdown_requested = False
        self._release_requested = False
        self._client_threads: list[threading.Thread] = []
        self._client_connections: list[Any] = []  # Track active connections
        self._shutdown_in_progress = False
        
        # Work queue for serializing RPC requests on main thread
        # Bounded queue to apply backpressure under load
        self._work_queue: Queue[RPCRequest] = Queue(maxsize=1024)
        
        # Set global instance for quit command
        _server_instance = self
        # Register for cleanup
        _active_servers.add(self)

    def __del__(self) -> None:
        """Cleanup on garbage collection."""
        self._cleanup()

    def _cleanup(self, close_listener: bool = True) -> None:
        """Perform cleanup of pipes and resources.

        Args:
            close_listener: If True, close the listener. If False, keep it open.
        """
        try:
            # Close listener if requested and still open
            if close_listener and self.listener:
                try:
                    self.listener.close()
                    logger.debug("Listener closed successfully")
                except Exception:
                    pass
                self.listener = None

            # Clean up the pipe/socket if listener was closed
            if close_listener:
                cleanup_pipe(self.address)

        except Exception as e:
            logger.debug(f"Cleanup error (non-critical): {e}")

    def _disconnect_all_clients(self) -> None:
        """Disconnect all active client connections."""
        for conn in self._client_connections:
            try:
                conn.close()
            except Exception:
                pass
        self._client_connections.clear()

        # Wait briefly for threads to finish
        for thread in self._client_threads:
            try:
                thread.join(timeout=0.1)
            except Exception:
                pass

    def _handle_client_reader(self, conn: Any) -> None:
        """
        Reader thread for a client connection. Only reads and enqueues messages.
        Does NOT execute RPC methods - that happens on the main thread.

        Args:
            conn: The connection object from multiprocessing.connection
        """
        # Track this connection
        self._client_connections.append(conn)
        try:
            while not self._shutdown_requested and not self._release_requested:
                try:
                    # Receive JSON-RPC request
                    request_string = recv_message(conn)
                    
                    # Parse request ID if possible (for debugging/logging)
                    request_id = None
                    try:
                        parsed = json.loads(request_string)
                        request_id = parsed.get('id')
                    except Exception:
                        pass
                    
                    # Enqueue the request for main thread processing
                    # Block if queue is full (backpressure)
                    request = RPCRequest(
                        seq=next(_seq_counter),
                        raw=request_string,
                        conn=conn,
                        id=request_id
                    )
                    
                    self._work_queue.put(request, block=True, timeout=30)
                    logger.debug(f"Enqueued request #{request.seq} (id={request_id})")

                except EOFError:
                    # Client disconnected normally
                    logger.debug("Client closed connection")
                    break
                except Exception as e:
                    if self._shutdown_requested or self._release_requested:
                        break
                    logger.error(f"Error reading from client: {e}")
                    # Send error response directly for read errors
                    error_response = json.dumps(
                        {
                            "jsonrpc": "2.0",
                            "error": {
                                "code": -32603,
                                "message": f"Read error: {str(e)}",
                            },
                            "id": None,
                        }
                    )
                    try:
                        send_message(conn, error_response)
                    except Exception:
                        pass
                    break
        finally:
            conn.close()
            # Remove from active connections
            try:
                self._client_connections.remove(conn)
            except Exception:
                pass
            logger.info("Client reader thread exited")

    def _accept_loop(self) -> None:
        """
        Accept loop that runs in a separate thread.
        Accepts new connections and starts reader threads for them.
        """
        logger.info("Accept thread started")
        
        if not self.listener:
            logger.error("No listener available for accept loop")
            return
        
        while not self._shutdown_requested and not self._release_requested:
            try:
                # Accept connection (this blocks)
                conn = self.listener.accept()

                if self._shutdown_requested or self._release_requested:
                    conn.close()
                    break

                logger.info("Client connected")

                # Start a reader thread for this client
                # Reader only enqueues messages, doesn't execute them
                client_thread = threading.Thread(
                    target=self._handle_client_reader, args=(conn,)
                )
                client_thread.daemon = True
                client_thread.start()
                self._client_threads.append(client_thread)

                # Clean up finished threads
                self._client_threads = [
                    t for t in self._client_threads if t.is_alive()
                ]

            except OSError as e:
                if self._shutdown_requested or self._release_requested:
                    break
                logger.error(f"Error accepting connection: {e}")
            except Exception as e:
                if self._shutdown_requested or self._release_requested:
                    break
                logger.error(f"Error in accept loop: {e}")
        
        logger.info("Accept thread stopped")

    def _dispatch_loop(self) -> None:
        """
        Main thread dispatcher loop. Processes queued requests sequentially.
        All RPC method executions happen here on the main thread.
        """
        logger.info("Main thread dispatcher started")
        
        while not self._shutdown_requested and not self._release_requested:
            try:
                # Get next request from queue (with timeout to check shutdown)
                request = self._work_queue.get(timeout=0.25)
                
                logger.debug(f"Processing request #{request.seq} (id={request.id})")
                
                # Process the request with jsonrpcserver
                # This executes the RPC method on the main thread
                response_string = dispatch(request.raw)
                
                # Send response if not a notification
                if response_string:
                    try:
                        send_message(request.conn, response_string)
                        logger.info(f"Processed request #{request.seq} and sent response")
                    except Exception as e:
                        logger.error(f"Error sending response for request #{request.seq}: {e}")
                else:
                    logger.info(f"Processed notification #{request.seq} (no response)")
                    
            except Empty:
                # Queue is empty, continue checking for shutdown
                continue
            except Exception as e:
                logger.error(f"Error in dispatch loop: {e}")
                # Don't exit the loop on errors, continue processing
                continue
        
        # Drain remaining requests on shutdown (optional)
        if self._shutdown_requested:
            logger.info("Draining work queue on shutdown...")
            while True:
                try:
                    request = self._work_queue.get_nowait()
                    # Send error response for unprocessed requests
                    error_response = json.dumps({
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32000,
                            "message": "Server shutting down"
                        },
                        "id": request.id
                    })
                    try:
                        send_message(request.conn, error_response)
                    except Exception:
                        pass
                except Empty:
                    break
        
        logger.info("Main thread dispatcher stopped")

    def start(self, reuse_listener: bool = False) -> None:
        """
        Start the JSON-RPC server and listen for connections.

        Args:
            reuse_listener: If True and a listener exists, reuse it instead of creating new one.
        """
        # Reset flags for new run
        self._shutdown_requested = False
        self._release_requested = False
        self._shutdown_in_progress = False

        # Clean up any existing pipe/socket before starting (unless reusing)
        if not reuse_listener or not self.listener:
            cleanup_pipe(self.address)

        # Check if we can setup signal handlers
        can_use_signals = is_main_thread()

        if can_use_signals:

            def signal_handler(signum: Any, frame: Any) -> None:
                """Handle Ctrl+C gracefully."""
                logger.info(f"Received signal {signum}, shutting down...")
                self._shutdown_requested = True

                # Close listener to unblock accept() on all platforms
                try:
                    if self.listener:
                        self.listener.close()
                except Exception:
                    pass

                # On Windows, also attempt a dummy connection to ensure accept() is unblocked
                if os.name == "nt":
                    # Use an instance-level guard to avoid repeated attempts
                    if not self._shutdown_in_progress:
                        self._shutdown_in_progress = True
                        try:
                            dummy = Client(self.address)
                            dummy.close()
                        except Exception:
                            pass

            try:
                # Setup signal handlers
                signal.signal(signal.SIGINT, signal_handler)
                signal.signal(signal.SIGTERM, signal_handler)
                logger.info("Signal handlers registered (Ctrl+C to stop)")
            except Exception as e:
                # If signal setup fails, continue without it
                logger.warning(f"Could not setup signal handlers: {e}")
                logger.info("Send 'shutdown' to stop server, 'release' to pause it")
                can_use_signals = False
        else:
            logger.info("Running in non-main thread/interpreter (e.g., Jupyter)")
            logger.info("Send 'shutdown' to stop server, 'release' to pause it")

        try:
            if reuse_listener and self.listener:
                logger.info(f"Reusing existing listener on {self.address}")
            else:
                self.listener = Listener(self.address)
                logger.info(f"Created new listener on {self.address}")

            self.running = True
            logger.info(f"JSON-RPC server listening on {self.address}")
            logger.info("All RPC methods will execute on the main thread")

            # Start accept thread to handle incoming connections
            accept_thread = threading.Thread(target=self._accept_loop)
            accept_thread.daemon = True
            accept_thread.start()
            
            # Run the main dispatcher loop on the main thread
            # This ensures all RPC methods execute on the main thread
            self._dispatch_loop()
            
            # Wait for accept thread to finish
            accept_thread.join(timeout=2.0)

        except Exception as e:
            logger.error(f"Failed to start server: {e}")
            self._cleanup()
            raise
        finally:
            self.running = False
            # Only close listener if shutdown was requested
            close_listener = self._shutdown_requested
            self._cleanup(close_listener=close_listener)

            if self._release_requested:
                logger.info("Server released from main loop (listener kept open)")
            else:
                logger.info("Server shutdown complete")

    def stop(self) -> None:
        """
        Stop the JSON-RPC server.
        """
        self._shutdown_requested = True
        self.running = False
        logger.info("Server stopping...")

        # Clear the work queue by adding a sentinel or draining
        try:
            # Try to drain the queue quickly
            while True:
                self._work_queue.get_nowait()
        except Empty:
            pass

        # Close the listener to unblock accept()
        if self.listener:
            try:
                self.listener.close()
            except Exception:
                pass

        # On Windows, send a dummy connection to unblock accept() if needed
        if os.name == "nt" and not self._shutdown_in_progress:
            self._shutdown_in_progress = True
            try:
                dummy = Client(self.address)
                dummy.close()
            except Exception:
                pass

        # Ensure cleanup
        self._cleanup()


def main() -> None:
    """
    Main entry point for running the JSON-RPC pipe server.
    """
    global _server_instance

    # Check if we can reuse an existing server that was released
    reuse_listener = False
    if _server_instance and _server_instance.listener:
        server = _server_instance
        logger.info("Reusing existing server instance after release")
        reuse_listener = True
    else:
        server = JSONRPCPipeServer()

    try:
        logger.info("Starting JSON-RPC Pipe Server...")
        logger.info(f"Platform: {os.name}")
        logger.info(f"Pipe address: {server.address}")

        # Check if we're in main thread
        if is_main_thread():
            logger.info("Press Ctrl+C to stop the server (or use 'quit' RPC method)")
        else:
            logger.info("Send 'shutdown' to stop server, 'release' to pause it")

        server.start(reuse_listener=reuse_listener)
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        server.stop()
    except Exception as e:
        logger.error(f"Server error: {e}")
        if "signal only works in main thread" in str(e):
            logger.info(
                "TIP: Server can still be started - it will use the 'quit' command instead of Ctrl+C"
            )
        # Ensure cleanup on error
        server._cleanup()
        sys.exit(1)
    finally:
        # Final cleanup attempt
        if server:
            server._cleanup()


if __name__ == "__main__":
    main()

# Uncomment below to auto-start server when imported (e.g., in Jupyter notebooks)
# th = threading.Thread(target=main)
# th.start()
