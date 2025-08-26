"""
JSON-RPC 2.0 Server using Named Pipes

This module implements a JSON-RPC 2.0 server that communicates through
named pipes (Windows) or Unix domain sockets (Linux/macOS) without any
network/socket APIs.
"""

import os
import sys
import json
import struct
import signal
import threading
import logging
from typing import Optional, Any
from multiprocessing.connection import Listener, Client
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
    # Clean up any existing socket file
    if os.path.exists(PIPE_ADDRESS):
        os.unlink(PIPE_ADDRESS)


# Define JSON-RPC methods
@method
def echo(*args, **kwargs):
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


# Message framing helpers
def send_message(conn, message_string: str) -> None:
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


def recv_message(conn) -> str:
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


class JSONRPCPipeServer:
    """
    JSON-RPC 2.0 server that uses named pipes for communication.
    """
    
    def __init__(self, address: Optional[str] = None):
        """
        Initialize the JSON-RPC pipe server.
        
        Args:
            address: The pipe address. If None, uses platform default.
        """
        self.address = address or PIPE_ADDRESS
        self.running = False
        self.listener: Optional[Listener] = None
        self._shutdown_requested = False
        self._client_threads = []
        
    def _handle_client(self, conn) -> None:
        """
        Handle a single client connection.
        
        Args:
            conn: The connection object from multiprocessing.connection
        """
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
                        logger.info(f"Processed request and sent response")
                    else:
                        logger.info("Processed notification (no response)")
                        
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
        Start the JSON-RPC server and listen for connections.
        """
        # Clean up Unix socket if it exists before starting
        if os.name != 'nt' and os.path.exists(self.address):
            try:
                os.unlink(self.address)
            except:
                pass
        
        def signal_handler(signum, frame):
            """Handle Ctrl+C gracefully."""
            logger.info(f"Received signal {signum}, shutting down...")
            self._shutdown_requested = True
            # On Windows, create a dummy connection to unblock accept()
            if os.name == 'nt' and self.listener and not self._shutdown_requested:
                try:
                    # Prevent recursive shutdown attempts
                    if not hasattr(signal_handler, '_shutdown_in_progress'):
                        signal_handler._shutdown_in_progress = True
                        dummy = Client(self.address)
                        dummy.close()
                except:
                    pass
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        try:
            self.listener = Listener(self.address)
            self.running = True
            logger.info(f"JSON-RPC server listening on {self.address}")
            
            while not self._shutdown_requested:
                try:
                    # Accept connection (this blocks)
                    conn = self.listener.accept()
                    
                    if self._shutdown_requested:
                        conn.close()
                        break
                    
                    logger.info(f"Client connected")
                    
                    # Handle client in a separate thread
                    client_thread = threading.Thread(
                        target=self._handle_client,
                        args=(conn,)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    self._client_threads.append(client_thread)
                    
                    # Clean up finished threads
                    self._client_threads = [t for t in self._client_threads if t.is_alive()]
                    
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
            raise
        finally:
            self.running = False
            if self.listener:
                try:
                    self.listener.close()
                except:
                    pass
                self.listener = None
            # Clean up Unix socket if necessary
            if os.name != 'nt' and os.path.exists(self.address):
                try:
                    os.unlink(self.address)
                except:
                    pass
            logger.info("Server shutdown complete")
    
    def stop(self) -> None:
        """
        Stop the JSON-RPC server.
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


def main():
    """
    Main entry point for running the JSON-RPC pipe server.
    """
    server = JSONRPCPipeServer()
    
    try:
        logger.info("Starting JSON-RPC Pipe Server...")
        logger.info(f"Platform: {os.name}")
        logger.info(f"Pipe address: {server.address}")
        logger.info("Press Ctrl+C to stop the server")
        server.start()
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        server.stop()
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()