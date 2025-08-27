"""
JSON-RPC 2.0 Server using Named Pipes (Asyncio)

This module implements a JSON-RPC 2.0 server that communicates through
named pipes (Windows) or Unix domain sockets (Linux/macOS) using asyncio
for asynchronous I/O. Each client connection is handled as an async task.

Environment Variables:
    CASCADEUR_PYTHON_RPC_PIPE_NAME:
        Sets the default pipe name for the JSON-RPC server to listen on.
        If not set, defaults to "cas-pipe".

        Usage:
            # Windows
            set CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
            python server.py  # Listens on \\.\pipe\my-custom-pipe

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
import asyncio
import atexit
import weakref
import concurrent.futures
from typing import Optional, Any, Set
from jsonrpcserver import method, dispatch

from multiprocessing.connection import Listener, Client

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

logger = get_logger("jsonrpc_pipe_server_asyncio")

# Configure default pipe address based on environment and platform
PIPE_ADDRESS = get_default_pipe_address()

# Global server instance for quit command and cleanup
_server_instance: Optional["JSONRPCPipeServerAsync"] = None
_active_servers: weakref.WeakSet[Any] = weakref.WeakSet()


def cleanup_pipe(address: str) -> None:
    """
    Clean up named pipe or Unix socket.

    Args:
        address: The pipe/socket address to clean up
    """
    if os.name != "nt":
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


# Define JSON-RPC methods (these remain synchronous as they're quick operations)
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

        # Schedule disconnection of all clients
        async def delayed_release() -> None:
            await asyncio.sleep(0.5)  # Give time for response to be sent
            await _server_instance._disconnect_all_clients()

        # Create the task but don't await it
        asyncio.create_task(delayed_release())

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

        # Schedule shutdown
        async def delayed_shutdown() -> None:
            await asyncio.sleep(0.5)  # Give time for response to be sent
            await _server_instance._disconnect_all_clients()
            
            # Close the server/listener
            if _server_instance.server:
                _server_instance.server.close()
                await _server_instance.server.wait_closed()
            
            # For Windows, close the listener and send dummy connection to unblock accept
            if os.name == "nt" and hasattr(_server_instance, '_listener'):
                try:
                    # Send a dummy connection to unblock accept()
                    dummy = Client(_server_instance.address)
                    dummy.close()
                except Exception:
                    pass
                try:
                    _server_instance._listener.close()
                except Exception:
                    pass

        # Create the task but don't await it
        asyncio.create_task(delayed_shutdown())

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


# Async message framing helpers
async def send_message_async(writer: asyncio.StreamWriter, message_string: str) -> None:
    """
    Send a JSON-RPC message with a length prefix for proper framing.

    Args:
        writer: The asyncio StreamWriter
        message_string: The JSON-RPC message string to send
    """
    if message_string:
        data = message_string.encode("utf-8")
        # Send message with 4-byte length prefix (big-endian)
        length_prefix = struct.pack("!I", len(data))
        writer.write(length_prefix + data)
        await writer.drain()
        logger.debug(f"Sent message: {message_string}")


async def recv_message_async(reader: asyncio.StreamReader) -> str:
    """
    Receive a JSON-RPC message with length prefix.

    Args:
        reader: The asyncio StreamReader

    Returns:
        The received JSON-RPC message string

    Raises:
        EOFError: If the connection is closed or message is incomplete
    """
    # Read the 4-byte length prefix
    length_data = await reader.readexactly(4)
    if not length_data:
        raise EOFError("Connection closed")

    # Extract length from first 4 bytes (big-endian)
    expected_length = struct.unpack("!I", length_data)[0]
    
    # Read the actual message data
    message_data = await reader.readexactly(expected_length)
    if not message_data:
        raise EOFError("Connection closed during message read")

    message: str = message_data.decode("utf-8")
    logger.debug(f"Received message: {message}")
    return message


class JSONRPCPipeServerAsync:
    """
    Async JSON-RPC 2.0 server that uses named pipes for communication.
    """

    def __init__(self, address: Optional[str] = None):
        """
        Initialize the async JSON-RPC pipe server.

        Args:
            address: The pipe address. If None, uses environment variable or default.
        """
        global _server_instance
        self.address = address if address else get_default_pipe_address()
        self.running = False
        self.server: Optional[asyncio.Server] = None
        self._shutdown_requested = False
        self._release_requested = False
        self._client_tasks: Set[asyncio.Task[None]] = set()
        self._client_writers: list[asyncio.StreamWriter] = []
        # Set global instance for quit command
        _server_instance = self
        # Register for cleanup
        _active_servers.add(self)

    def __del__(self) -> None:
        """Cleanup on garbage collection."""
        self._cleanup_sync()

    def _cleanup_sync(self) -> None:
        """Synchronous cleanup for use in __del__ and other sync contexts."""
        try:
            # Clean up the pipe/socket
            cleanup_pipe(self.address)
        except Exception as e:
            logger.debug(f"Cleanup error (non-critical): {e}")

    async def _cleanup(self, close_server: bool = True) -> None:
        """
        Perform async cleanup of server and resources.

        Args:
            close_server: If True, close the server. If False, keep it open.
        """
        try:
            # Close server if requested
            if close_server and self.server:
                self.server.close()
                await self.server.wait_closed()
                self.server = None
                logger.debug("Server closed successfully")
            
            # Close Windows listener if requested
            if close_server and hasattr(self, '_listener'):
                try:
                    self._listener.close()
                except Exception:
                    pass
            
            # Shutdown executor
            if hasattr(self, '_executor'):
                try:
                    self._executor.shutdown(wait=False)
                except Exception:
                    pass

            # Clean up the pipe/socket if server was closed
            if close_server:
                cleanup_pipe(self.address)

        except Exception as e:
            logger.debug(f"Cleanup error (non-critical): {e}")

    async def _disconnect_all_clients(self) -> None:
        """Disconnect all active client connections."""
        # Close all StreamWriters (Unix sockets)
        for writer in self._client_writers:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        self._client_writers.clear()
        
        # Close all pipe connections (Windows)
        pipe_connections = getattr(self, '_pipe_connections', [])
        for conn in pipe_connections:
            try:
                conn.close()
            except Exception:
                pass
        if hasattr(self, '_pipe_connections'):
            self._pipe_connections.clear()

        # Cancel all client tasks
        for task in self._client_tasks:
            task.cancel()
        
        # Wait for all tasks to complete
        if self._client_tasks:
            await asyncio.gather(*self._client_tasks, return_exceptions=True)
        self._client_tasks.clear()
        
        # Cancel and wait for pipe server task if it exists (Windows)
        if hasattr(self, '_pipe_server_task'):
            self._pipe_server_task.cancel()
            try:
                await self._pipe_server_task
            except asyncio.CancelledError:
                pass

    async def _handle_client(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        """
        Handle a single client connection.

        Args:
            reader: The asyncio StreamReader
            writer: The asyncio StreamWriter
        """
        # Track this writer
        self._client_writers.append(writer)
        
        client_addr = writer.get_extra_info('peername', 'unknown')
        logger.info(f"Client connected from {client_addr}")
        
        try:
            while not self._shutdown_requested and not self._release_requested:
                try:
                    # Receive JSON-RPC request
                    request_string = await recv_message_async(reader)

                    # Process the request with jsonrpcserver (this is sync but fast)
                    response_string = dispatch(request_string)

                    # Send response (skip for notifications)
                    if response_string:
                        await send_message_async(writer, response_string)
                        logger.info("Processed request and sent response")
                    else:
                        logger.info("Processed notification (no response)")

                except asyncio.IncompleteReadError:
                    # Client disconnected
                    logger.debug("Client closed connection")
                    break
                except EOFError:
                    # Client disconnected normally
                    logger.debug("Client closed connection")
                    break
                except Exception as e:
                    if self._shutdown_requested or self._release_requested:
                        break
                    logger.error(f"Error handling client request: {e}")
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
                        await send_message_async(writer, error_response)
                    except Exception:
                        pass
                    break
        finally:
            # Clean up
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
            
            # Remove from active writers
            try:
                self._client_writers.remove(writer)
            except Exception:
                pass
            
            logger.info(f"Client {client_addr} disconnected")

    async def _create_server(self) -> None:
        """Create the appropriate server based on platform."""
        if os.name == "nt":
            # Windows named pipes
            await self._create_windows_pipe_server()
        else:
            # Unix domain sockets
            await self._create_unix_socket_server()

    async def _create_windows_pipe_server(self) -> None:
        """Create a Windows named pipe server using a hybrid approach."""
        # Create a listener for the named pipe (authkey=None to match client)
        self._listener = Listener(self.address, authkey=None)
        logger.info(f"Windows pipe listener created on {self.address}")
        
        # We'll use a thread executor to handle blocking pipe operations
        # Need at least 2 threads - one for accept loop, one for handling other operations
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        executor = self._executor
        
        async def pipe_server() -> None:
            """Accept pipe connections using thread executor."""
            loop = asyncio.get_running_loop()
            logger.debug("Windows pipe server task started")
            
            while not self._shutdown_requested and not self._release_requested:
                try:
                    logger.debug("Waiting for pipe connection...")
                    
                    # Accept connection in executor (blocking operation)
                    conn = await loop.run_in_executor(executor, self._listener.accept)
                    logger.info("Pipe connection accepted from client")
                    
                    if self._shutdown_requested or self._release_requested:
                        conn.close()
                        break
                    
                    logger.debug("Creating handler task for connection")
                    # Handle the connection in an async task
                    task = asyncio.create_task(self._handle_windows_pipe_client(conn))
                    self._client_tasks.add(task)
                    task.add_done_callback(self._client_tasks.discard)
                    logger.debug("Handler task created successfully")
                    
                except asyncio.CancelledError:
                    logger.debug("Pipe server task cancelled")
                    break
                except Exception as e:
                    if self._shutdown_requested or self._release_requested:
                        break
                    logger.error(f"Error accepting pipe connection: {e}", exc_info=True)
                    await asyncio.sleep(1)  # Prevent tight loop on error
            
            # Clean up
            executor.shutdown(wait=False)
            if hasattr(self, '_listener'):
                self._listener.close()
        
        # Start the pipe server task
        self._pipe_server_task = asyncio.create_task(pipe_server())
    
    async def _handle_windows_pipe_client(self, conn: Any) -> None:
        """
        Handle a Windows pipe client connection using async wrappers.
        
        Args:
            conn: The connection from multiprocessing.connection.Listener
        """
        client_addr = f"pipe:{self.address}"
        logger.info(f"Client connected from {client_addr}")
        
        # Track this connection for cleanup
        if not hasattr(self, '_pipe_connections'):
            self._pipe_connections = []
        self._pipe_connections.append(conn)
        
        loop = asyncio.get_running_loop()
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        
        try:
            while not self._shutdown_requested and not self._release_requested:
                try:
                    # Receive message in executor (blocking operation)
                    def recv_msg() -> str:
                        """Blocking receive with framing."""
                        # Receive the complete message
                        blob: bytes = conn.recv_bytes()
                        if len(blob) < 4:
                            raise EOFError("Message too short")
                        
                        # Extract length and data
                        expected_length = struct.unpack("!I", blob[:4])[0]
                        actual_data = blob[4:]
                        
                        if len(actual_data) != expected_length:
                            logger.warning(
                                f"Length mismatch: expected {expected_length}, got {len(actual_data)}"
                            )
                        
                        decoded: str = actual_data.decode("utf-8")
                        return decoded
                    
                    request_string = await loop.run_in_executor(executor, recv_msg)
                    logger.debug(f"Received message: {request_string}")
                    
                    # Process the request with jsonrpcserver (this is sync but fast)
                    response_string = dispatch(request_string)
                    
                    # Send response if not a notification
                    if response_string:
                        def send_msg() -> None:
                            """Blocking send with framing."""
                            data = response_string.encode("utf-8")
                            length_prefix = struct.pack("!I", len(data))
                            conn.send_bytes(length_prefix + data)
                        
                        await loop.run_in_executor(executor, send_msg)
                        logger.info("Processed request and sent response")
                    else:
                        logger.info("Processed notification (no response)")
                        
                except EOFError:
                    # Client disconnected normally
                    logger.debug("Client closed connection")
                    break
                except Exception as e:
                    if self._shutdown_requested or self._release_requested:
                        break
                    logger.error(f"Error handling client request: {e}")
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
                        def send_error() -> None:
                            data = error_response.encode("utf-8")
                            length_prefix = struct.pack("!I", len(data))
                            conn.send_bytes(length_prefix + data)
                        await loop.run_in_executor(executor, send_error)
                    except Exception:
                        pass
                    break
        finally:
            # Clean up
            executor.shutdown(wait=False)
            try:
                conn.close()
            except Exception:
                pass
            
            # Remove from tracked connections
            try:
                self._pipe_connections.remove(conn)
            except Exception:
                pass
            
            logger.info(f"Client {client_addr} disconnected")

    async def _create_unix_socket_server(self) -> None:
        """Create a Unix domain socket server."""
        # Clean up any existing socket
        cleanup_pipe(self.address)
        
        # Create the server - Unix domain sockets are only available on Unix-like systems
        if os.name != "nt" and hasattr(asyncio, 'start_unix_server'):
            # Use getattr to avoid attribute errors on Windows
            start_unix_server = getattr(asyncio, 'start_unix_server')
            self.server = await start_unix_server(
                self._handle_client_wrapper,
                path=self.address,
            )
            logger.info(f"Unix socket server created on {self.address}")
        else:
            # This should not be called on Windows
            raise RuntimeError("Unix domain sockets not supported on this platform")

    async def _handle_client_wrapper(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        """
        Wrapper to handle client connections as tasks.
        
        Args:
            reader: The asyncio StreamReader
            writer: The asyncio StreamWriter
        """
        # Create a task for this client
        task = asyncio.create_task(self._handle_client(reader, writer))
        self._client_tasks.add(task)
        task.add_done_callback(self._client_tasks.discard)

    async def start(self, reuse_server: bool = False) -> None:
        """
        Start the async JSON-RPC server and listen for connections.

        Args:
            reuse_server: If True and a server exists, reuse it instead of creating new one.
        """
        # Reset flags for new run
        self._shutdown_requested = False
        self._release_requested = False

        # Clean up any existing pipe/socket before starting (unless reusing)
        if not reuse_server or not self.server:
            cleanup_pipe(self.address)

        try:
            if reuse_server and self.server:
                logger.info(f"Reusing existing server on {self.address}")
            else:
                await self._create_server()
                logger.info(f"Created new server on {self.address}")

            self.running = True
            logger.info(f"Async JSON-RPC server listening on {self.address}")

            # Different handling for Unix vs Windows
            if os.name == "nt":
                # For Windows pipes, wait for the pipe server task
                if hasattr(self, '_pipe_server_task'):
                    # Wait until shutdown or release is requested
                    while not self._shutdown_requested and not self._release_requested:
                        await asyncio.sleep(0.5)
                        
                        # Check if pipe server task has failed
                        if self._pipe_server_task.done():
                            try:
                                await self._pipe_server_task
                            except Exception as e:
                                logger.error(f"Pipe server task failed: {e}")
                                break
                        
                        # Clean up completed tasks
                        completed_tasks = [t for t in self._client_tasks if t.done()]
                        for task in completed_tasks:
                            try:
                                await task
                            except Exception:
                                pass
            else:
                # For Unix sockets, start serving
                if self.server:
                    async with self.server:
                        await self.server.start_serving()
                        
                        # Wait until shutdown or release is requested
                        while not self._shutdown_requested and not self._release_requested:
                            await asyncio.sleep(0.5)
                            
                            # Clean up completed tasks
                            completed_tasks = [t for t in self._client_tasks if t.done()]
                            for task in completed_tasks:
                                try:
                                    await task
                                except Exception:
                                    pass

        except Exception as e:
            logger.error(f"Failed to start server: {e}")
            await self._cleanup()
            raise
        finally:
            self.running = False
            # Only close server if shutdown was requested
            close_server = self._shutdown_requested
            await self._cleanup(close_server=close_server)

            if self._release_requested:
                logger.info("Server released from main loop (server kept open)")
            else:
                logger.info("Server shutdown complete")

    async def stop(self) -> None:
        """Stop the async JSON-RPC server."""
        self._shutdown_requested = True
        self.running = False
        logger.info("Server stopping...")

        # Close the server
        if self.server:
            self.server.close()
            await self.server.wait_closed()

        # Ensure cleanup
        await self._cleanup()


def setup_signal_handlers(server: JSONRPCPipeServerAsync) -> None:
    """
    Setup signal handlers for graceful shutdown.
    
    Args:
        server: The server instance to control
    """
    def signal_handler(signum: Any, frame: Any) -> None:
        """Handle Ctrl+C gracefully."""
        logger.info(f"Received signal {signum}, shutting down...")
        server._shutdown_requested = True
        
        # Close the server
        if server.server:
            server.server.close()

    try:
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        logger.info("Signal handlers registered (Ctrl+C to stop)")
    except Exception as e:
        logger.warning(f"Could not setup signal handlers: {e}")
        logger.info("Send 'shutdown' to stop server, 'release' to pause it")


async def async_main() -> None:
    """
    Async main entry point for running the JSON-RPC pipe server.
    """
    global _server_instance

    # Check if we can reuse an existing server that was released
    reuse_server = False
    if _server_instance and _server_instance.server:
        server = _server_instance
        logger.info("Reusing existing server instance after release")
        reuse_server = True
    else:
        server = JSONRPCPipeServerAsync()

    # Setup signal handlers
    setup_signal_handlers(server)

    try:
        logger.info("Starting Async JSON-RPC Pipe Server...")
        logger.info(f"Platform: {os.name}")
        logger.info(f"Pipe address: {server.address}")
        logger.info("Send 'shutdown' to stop server, 'release' to pause it")

        await server.start(reuse_server=reuse_server)
    except Exception as e:
        logger.error(f"Server error: {e}")
        await server._cleanup()
        sys.exit(1)


def main() -> None:
    """
    Main entry point for running the async JSON-RPC pipe server.
    """
    try:
        # Run the async main
        asyncio.run(async_main())
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()