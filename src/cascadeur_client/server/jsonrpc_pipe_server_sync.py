"""
Synchronous JSON-RPC 2.0 Server using Named Pipes

This module implements a single-threaded, synchronous JSON-RPC 2.0 server that 
processes requests one by one in the main thread without creating any additional threads.
"""

import os
import sys
import json
import struct
import signal
import logging
import atexit
import weakref
from typing import Optional, Any, Dict
from multiprocessing.connection import Listener, Client, Connection
from jsonrpcserver import method, dispatch
try:
    # Try to import the modern API (version 5.x)
    from jsonrpcserver import Success, Error
except ImportError:
    # Fallback for older versions that use result module
    from jsonrpcserver.result import Success, Error

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure pipe address based on platform
if os.name == 'nt':  # Windows
    PIPE_ADDRESS = r'\\.\pipe\my-test-pipe'
else:  # Unix/Linux
    PIPE_ADDRESS = '/tmp/my-test-pipe.sock'

# Global server instance for quit command and cleanup
_server_instance: Optional['SyncJSONRPCPipeServer'] = None
_active_servers: weakref.WeakSet = weakref.WeakSet()


def cleanup_pipe(address: str) -> None:
    """
    Clean up named pipe or Unix socket.
    
    Args:
        address: The pipe/socket address to clean up
    """
    if os.name == 'nt':
        # Windows named pipes are cleaned up when all handles are closed
        # But we'll ensure any lingering connections are closed
        try:
            # Try to connect and immediately disconnect to clear any stuck state
            dummy = Client(address)
            dummy.close()
        except:
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
            if hasattr(server, 'address'):
                cleanup_pipe(server.address)
                logger.debug(f"Cleaned up pipe: {server.address}")
        except:
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
    elif 'message' in kwargs:
        message = kwargs['message']
    else:
        return Error("Missing required parameter 'message'", code=-32602)
    
    if not isinstance(message, str):
        return Error("Parameter must be a string", code=-32602)
    
    # Return Success result with the message
    return Success(message)


@method  
def quit() -> Any:
    """
    Shutdown the server gracefully.
    
    Returns:
        Success message indicating shutdown initiated
    """
    global _server_instance
    if _server_instance:
        logger.info("Quit command received, initiating shutdown...")
        _server_instance._shutdown_requested = True
        return Success("Server shutdown initiated")
    else:
        return Error("No server instance found", code=-32603)


# Message framing helpers
def send_message(conn: Connection, message_string: str) -> None:
    """
    Send a JSON-RPC message with a length prefix for proper framing.
    
    Args:
        conn: The connection object from multiprocessing.connection
        message_string: The JSON-RPC message string to send
    """
    if message_string:
        data = message_string.encode('utf-8')
        # Send message with 4-byte length prefix (big-endian)
        length_prefix = struct.pack('!I', len(data))
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
    expected_length = struct.unpack('!I', blob[:4])[0]
    actual_data = blob[4:]
    
    if len(actual_data) != expected_length:
        logger.warning(f"Length mismatch: expected {expected_length}, got {len(actual_data)}")
    
    message = actual_data.decode('utf-8')
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
            address: The pipe address. If None, uses platform default.
        """
        global _server_instance
        self.address = address or PIPE_ADDRESS
        self.running = False
        self.listener: Optional[Listener] = None
        self._shutdown_requested = False
        
        # Set global instance for quit command
        _server_instance = self
        # Register for cleanup
        _active_servers.add(self)
        
        logger.info(f"Initialized synchronous server with address: {self.address}")
        
    def __del__(self) -> None:
        """Cleanup on garbage collection."""
        self._cleanup()
    
    def _cleanup(self) -> None:
        """Perform cleanup of pipes and resources."""
        try:
            # Close listener if still open
            if self.listener:
                try:
                    self.listener.close()
                except:
                    pass
                self.listener = None
            
            # Clean up the pipe/socket
            cleanup_pipe(self.address)
            
        except Exception as e:
            logger.debug(f"Cleanup error (non-critical): {e}")
    
    def _handle_client_sync(self, conn: Connection) -> None:
        """
        Handle a client connection synchronously in the main thread.
        
        Args:
            conn: The connection object from multiprocessing.connection
        """
        logger.info("Client connected - handling synchronously")
        
        try:
            while not self._shutdown_requested:
                try:
                    # Receive JSON-RPC request
                    request_string = recv_message(conn)
                    
                    # Process the request with jsonrpcserver
                    response_string = dispatch(request_string)
                    
                    # Send response (skip for notifications)
                    if response_string:
                        send_message(conn, response_string)
                        logger.info("Processed request and sent response")
                    else:
                        logger.info("Processed notification (no response)")
                    
                    # Check if this was a quit command
                    if self._shutdown_requested:
                        logger.info("Shutdown requested during request processing")
                        break
                        
                except EOFError:
                    # Client disconnected normally
                    logger.debug("Client closed connection")
                    break
                except Exception as e:
                    if self._shutdown_requested:
                        break
                    logger.error(f"Error handling client request: {e}")
                    # Send error response
                    error_response = json.dumps({
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32603,
                            "message": f"Internal error: {str(e)}"
                        },
                        "id": None
                    })
                    try:
                        send_message(conn, error_response)
                    except:
                        pass
                    break
        finally:
            conn.close()
            logger.info("Client disconnected")
    
    def start(self) -> None:
        """
        Start the synchronous JSON-RPC server and listen for connections.
        This method blocks the calling thread and processes clients one by one.
        """
        # Clean up any existing pipe/socket before starting
        cleanup_pipe(self.address)
        
        # Setup signal handlers for graceful shutdown
        def signal_handler(signum: int, frame: Any) -> None:
            """Handle Ctrl+C gracefully."""
            logger.info(f"Received signal {signum}, shutting down...")
            self._shutdown_requested = True
            
            # Close listener to unblock accept()
            if self.listener:
                try:
                    self.listener.close()
                except:
                    pass
            
            # On Windows, send dummy connection to unblock accept()
            if os.name == 'nt':
                try:
                    dummy = Client(self.address)
                    dummy.close()
                except:
                    pass
        
        try:
            # Setup signal handlers if possible
            signal.signal(signal.SIGINT, signal_handler)
            signal.signal(signal.SIGTERM, signal_handler)
            logger.info("Signal handlers registered (Ctrl+C to stop)")
        except Exception as e:
            logger.warning(f"Could not setup signal handlers: {e}")
            logger.info("Use the 'quit' JSON-RPC method to stop the server")
        
        try:
            self.listener = Listener(self.address)
            self.running = True
            logger.info(f"Synchronous JSON-RPC server listening on {self.address}")
            logger.info("Processing clients one at a time in main thread")
            
            while not self._shutdown_requested:
                try:
                    # Accept connection (this blocks)
                    logger.debug("Waiting for client connection...")
                    conn = self.listener.accept()
                    
                    if self._shutdown_requested:
                        conn.close()
                        break
                    
                    # Handle client synchronously in main thread
                    # This blocks until client disconnects
                    self._handle_client_sync(conn)
                    
                except OSError as e:
                    if self._shutdown_requested:
                        break
                    logger.error(f"Error accepting connection: {e}")
                except Exception as e:
                    if self._shutdown_requested:
                        break
                    logger.error(f"Error in accept loop: {e}")
                    
        except Exception as e:
            logger.error(f"Failed to start server: {e}")
            self._cleanup()
            raise
        finally:
            self.running = False
            self._cleanup()
            logger.info("Server shutdown complete")
    
    def stop(self) -> None:
        """
        Stop the synchronous JSON-RPC server.
        """
        self._shutdown_requested = True
        self.running = False
        logger.info("Server stopping...")
        
        # Close the listener to unblock accept()
        if self.listener:
            try:
                self.listener.close()
            except:
                pass
        
        # On Windows, send a dummy connection to unblock accept()
        if os.name == 'nt':
            try:
                dummy = Client(self.address)
                dummy.close()
            except:
                pass
        
        # Ensure cleanup
        self._cleanup()


def main() -> None:
    """
    Main entry point for running the synchronous JSON-RPC pipe server.
    """
    server = SyncJSONRPCPipeServer()
    
    try:
        logger.info("=" * 60)
        logger.info("Starting Synchronous JSON-RPC Pipe Server")
        logger.info(f"Platform: {os.name}")
        logger.info(f"Pipe address: {server.address}")
        logger.info("Mode: Single-threaded, synchronous processing")
        logger.info("=" * 60)
        logger.info("Press Ctrl+C to stop (or use 'quit' RPC method)")
        
        # This blocks until shutdown
        server.start()
        
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        server.stop()
    except Exception as e:
        logger.error(f"Server error: {e}")
        server._cleanup()
        sys.exit(1)
    finally:
        # Final cleanup attempt
        if server:
            server._cleanup()


if __name__ == "__main__":
    main()