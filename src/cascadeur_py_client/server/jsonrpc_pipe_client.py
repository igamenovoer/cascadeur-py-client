"""
JSON-RPC 2.0 Client using Named Pipes

This module implements a JSON-RPC 2.0 client that communicates through
named pipes (Windows) or Unix domain sockets (Linux/macOS) without any
network/socket APIs.
"""

import os
import sys
import json
import struct
from typing import Optional, Any, Dict
from multiprocessing.connection import Client

# Import jsonrpcclient components
try:
    from jsonrpcclient import request_json, notification_json, parse_json, Ok, Error as RPCError
except ImportError:
    # Fallback if specific functions are not available
    from jsonrpcclient import request, notification, parse_json, Ok
    
    def request_json(method, params=None):
        return json.dumps(request(method, params))
    
    def notification_json(method, params=None):
        return json.dumps(notification(method, params))

# Use centralized logging from caslogger
from cascadeur_py_client.caslogger import get_logger

logger = get_logger("jsonrpc_pipe_client")

# Configure pipe address based on platform
if os.name == 'nt':  # Windows
    PIPE_ADDRESS = r'\\.\pipe\my-test-pipe'
else:  # Unix/Linux
    PIPE_ADDRESS = '/tmp/my-test-pipe.sock'


# Message framing helpers
def send_message(conn, message_string: str) -> None:
    """
    Send a JSON-RPC message with a length prefix for proper framing.
    
    Args:
        conn: The connection object from multiprocessing.connection
        message_string: The JSON-RPC message string to send
    """
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


class JSONRPCPipeClient:
    """
    JSON-RPC 2.0 client that uses named pipes for communication.
    """
    
    def __init__(self, address: Optional[str] = None):
        """
        Initialize the JSON-RPC pipe client.
        
        Args:
            address: The pipe address. If None, uses platform default.
        """
        self.address = address or PIPE_ADDRESS
        
    def call(self, method: str, params: Any = None, timeout: float = 10.0) -> Any:
        """
        Make a JSON-RPC call and return the result.
        
        Args:
            method: The RPC method name to call
            params: Parameters for the method (list or dict)
            timeout: Connection timeout in seconds
            
        Returns:
            The result from the RPC call
            
        Raises:
            Exception: If there's an RPC error or connection issue
        """
        try:
            # Connect to the server
            with Client(self.address, authkey=None) as conn:
                # Create request using jsonrpcclient
                request_string = request_json(method, params)
                logger.info(f"Calling method '{method}' with params: {params}")
                
                # Send request
                send_message(conn, request_string)
                
                # Receive and parse response
                response_string = recv_message(conn)
                parsed = parse_json(response_string)
                
                if isinstance(parsed, Ok):
                    logger.info(f"Method '{method}' returned: {parsed.result}")
                    return parsed.result
                else:
                    # Handle RPC error
                    error_msg = f"RPC Error: {parsed.message} (code: {parsed.code})"
                    if hasattr(parsed, 'data') and parsed.data:
                        error_msg += f" - {parsed.data}"
                    logger.error(error_msg)
                    raise Exception(error_msg)
                    
        except FileNotFoundError:
            error_msg = f"Cannot connect to server at {self.address}. Is the server running?"
            logger.error(error_msg)
            raise ConnectionError(error_msg)
        except Exception as e:
            logger.error(f"Error calling method '{method}': {e}")
            raise
            
    def notify(self, method: str, params: Any = None) -> None:
        """
        Send a notification (no response expected).
        
        Args:
            method: The RPC method name to call
            params: Parameters for the method (list or dict)
        """
        try:
            # Connect to the server
            with Client(self.address, authkey=None) as conn:
                # Create notification using jsonrpcclient
                notification_string = notification_json(method, params)
                logger.info(f"Sending notification '{method}' with params: {params}")
                
                # Send notification
                send_message(conn, notification_string)
                logger.info(f"Notification '{method}' sent successfully")
                
        except FileNotFoundError:
            error_msg = f"Cannot connect to server at {self.address}. Is the server running?"
            logger.error(error_msg)
            raise ConnectionError(error_msg)
        except Exception as e:
            logger.error(f"Error sending notification '{method}': {e}")
            raise
            
    def batch_call(self, requests: list) -> list:
        """
        Make multiple JSON-RPC calls in a single batch.
        
        Args:
            requests: List of tuples (method, params) to call
            
        Returns:
            List of results from the RPC calls
            
        Raises:
            Exception: If there's an RPC error or connection issue
        """
        try:
            with Client(self.address, authkey=None) as conn:
                # Create batch request
                batch_requests = []
                for i, (method, params) in enumerate(requests):
                    req = {
                        "jsonrpc": "2.0",
                        "method": method,
                        "params": params,
                        "id": i + 1
                    }
                    batch_requests.append(req)
                
                batch_string = json.dumps(batch_requests)
                logger.info(f"Sending batch request with {len(requests)} calls")
                
                # Send batch request
                send_message(conn, batch_string)
                
                # Receive and parse batch response
                response_string = recv_message(conn)
                responses = json.loads(response_string)
                
                # Extract results
                results = []
                for response in responses:
                    if "result" in response:
                        results.append(response["result"])
                    elif "error" in response:
                        error = response["error"]
                        error_msg = f"RPC Error: {error['message']} (code: {error['code']})"
                        results.append(Exception(error_msg))
                    else:
                        results.append(None)
                
                logger.info(f"Batch request completed with {len(results)} results")
                return results
                
        except Exception as e:
            logger.error(f"Error in batch call: {e}")
            raise


def test_client():
    """
    Test function to demonstrate client usage.
    """
    client = JSONRPCPipeClient()
    
    print("\n=== JSON-RPC Pipe Client Test ===")
    print(f"Connecting to: {client.address}")
    print()
    
    try:
        # Test echo method
        test_message = "Hello from JSON-RPC client!"
        print(f"Testing echo method with message: '{test_message}'")
        result = client.call("echo", [test_message])
        print(f"Echo result: '{result}'")
        print()
        
        # Test with different parameter format (as dict)
        print("Testing echo with dict params...")
        result = client.call("echo", {"message": "Testing with dict params"})
        print(f"Echo result: '{result}'")
        print()
        
        # Test invalid method
        print("Testing invalid method (should raise error)...")
        try:
            result = client.call("invalid_method")
            print(f"Result: {result}")
        except Exception as e:
            print(f"Expected error: {e}")
        print()
        
        # Test notification
        print("Sending notification (no response expected)...")
        client.notify("log", ["This is a notification"])
        print("Notification sent successfully")
        print()
        
        # Test batch call
        print("Testing batch call...")
        batch_requests = [
            ("echo", ["First"]),
            ("echo", ["Second"]),
            ("echo", ["Third"])
        ]
        results = client.batch_call(batch_requests)
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"  Request {i+1}: Error - {result}")
            else:
                print(f"  Request {i+1}: Result - '{result}'")
        
    except ConnectionError as e:
        print(f"Connection error: {e}")
        print("Make sure the server is running first!")
    except Exception as e:
        print(f"Error: {e}")


def interactive_client():
    """
    Interactive client for testing the JSON-RPC server.
    """
    client = JSONRPCPipeClient()
    
    print("\n=== JSON-RPC Pipe Client (Interactive Mode) ===")
    print(f"Connected to: {client.address}")
    print("Type 'quit' to exit, 'help' for commands")
    print()
    
    while True:
        try:
            command = input(">> ").strip()
            
            if command.lower() == 'quit':
                print("Goodbye!")
                break
            elif command.lower() == 'help':
                print("Commands:")
                print("  echo <message>  - Echo a message")
                print("  notify <message> - Send a notification")
                print("  quit            - Exit the client")
                print("  help            - Show this help")
            elif command.startswith('echo '):
                message = command[5:]
                result = client.call("echo", [message])
                print(f"Server response: {result}")
            elif command.startswith('notify '):
                message = command[7:]
                client.notify("log", [message])
                print("Notification sent")
            else:
                print("Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    """
    Main entry point for the JSON-RPC pipe client.
    """
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_client()
    else:
        test_client()


if __name__ == "__main__":
    main()