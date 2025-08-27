#!/usr/bin/env python
"""
Run the JSON-RPC IPC client for manual testing.

This script provides an interactive client to test the JSON-RPC pipe server
with various commands and options.
"""

import os
import sys
import json
import time
import argparse
import logging
import base64
import pickle
from pathlib import Path
from typing import Optional, Any, List, Dict

# Add src to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

from cascadeur_py_client.server.jsonrpc_pipe_client import JSONRPCPipeClient  # noqa: E402


def format_pipe_address(pipe_name: str) -> str:
    """
    Convert a simple pipe name to OS-specific full pipe address.
    
    Args:
        pipe_name: Simple pipe name like "my-test-pipe"
        
    Returns:
        OS-specific pipe address
    """
    if os.name == 'nt':  # Windows
        return rf'\\.\pipe\{pipe_name}'
    else:  # Unix/Linux/macOS
        return f'/tmp/{pipe_name}.sock'


def print_result(result: Any, format_json: bool = False) -> None:
    """Print the result in a formatted way."""
    if format_json and (isinstance(result, dict) or isinstance(result, list)):
        print(json.dumps(result, indent=2))
    else:
        print(f"Result: {result}")


def decode_exec_result(result: Dict[str, Any]) -> Any:
    """
    Decode the result from exec_code response.
    
    Args:
        result: The result dict from exec_code
        
    Returns:
        The decoded data
    """
    if not isinstance(result, dict):
        return result
    
    # Check for error
    error = result.get("error", {})
    error_type = error.get("type", 0)
    if error_type != 0:
        error_msg = error.get("message", "Unknown error")
        error_traceback = error.get("traceback", "")
        print(f"[ERROR] Execution failed (type {error_type}):")
        print(error_msg)
        if error_traceback:
            print("Traceback:")
            print(error_traceback)
        return None
    
    # Get the data
    data = result.get("data")
    encoding = result.get("encoding")
    
    # Decode if necessary
    if encoding == "base64" and data is not None:
        try:
            decoded_bytes = base64.b64decode(data)
            
            # Try to unpickle (for binary/pickle data)
            try:
                return pickle.loads(decoded_bytes)
            except Exception:
                # Return as raw bytes if unpickle fails
                return decoded_bytes
        except Exception as e:
            print(f"[WARNING] Failed to decode base64 data: {e}")
            return data
    
    return data


def print_exec_result(result: Dict[str, Any]) -> None:
    """
    Print the result from exec_code in a user-friendly way.
    
    Args:
        result: The result dict from exec_code
    """
    if not isinstance(result, dict):
        print(f"Result: {result}")
        return
    
    # Check for error
    error = result.get("error", {})
    error_type = error.get("type", 0)
    if error_type != 0:
        error_msg = error.get("message", "Unknown error")
        error_traceback = error.get("traceback", "")
        print(f"\n[ERROR] Execution failed (type {error_type}):")
        print(error_msg)
        if error_traceback:
            print("\nTraceback:")
            print(error_traceback)
        return
    
    # Get metadata
    encoding = result.get("encoding")
    
    # Decode and print the data
    decoded_data = decode_exec_result(result)
    
    if decoded_data is not None:
        print("\n[SUCCESS] Code executed successfully")
        if encoding == "base64":
            print("Data type: Binary/Pickled (base64 encoded)")
        else:
            print("Data type: JSON-compatible")
        print("-" * 40)
        
        if isinstance(decoded_data, bytes):
            print(f"<bytes: {len(decoded_data)} bytes>")
            # Try to decode as string for display
            try:
                text = decoded_data.decode('utf-8')
                if len(text) <= 100:
                    print(f"Content: {text}")
                else:
                    print(f"Content (first 100 chars): {text[:100]}...")
            except UnicodeDecodeError:
                print(f"Content (hex, first 50 bytes): {decoded_data[:50].hex()}")
        elif isinstance(decoded_data, (dict, list)):
            print(json.dumps(decoded_data, indent=2))
        else:
            print(f"Result: {decoded_data}")


def get_multiline_code() -> str:
    """
    Get multiline Python code from user input.
    
    Returns:
        The complete code as a string
    """
    print("Enter Python code (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input("... ")
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def interactive_mode(client: JSONRPCPipeClient) -> None:
    """Run the client in interactive mode."""
    print("\n" + "=" * 60)
    print("Interactive JSON-RPC Client with Code Execution")
    print("=" * 60)
    print("Commands:")
    print("  exec <code>       - Execute single line Python code")
    print("  execm             - Execute multiline Python code")
    print("  execf <file>      - Execute Python code from file")
    print("  echo <message>    - Send echo request")
    print("  notify <message>  - Send notification (no response)")
    print("  raw <json>        - Send raw JSON-RPC request")
    print("  batch             - Enter batch mode")
    print("  release           - Release server (keeps pipe open)")
    print("  shutdown          - Shutdown server completely")
    print("  help              - Show this help")
    print("  quit              - Exit the client (local only)")
    print("=" * 60)
    print()
    
    while True:
        try:
            command = input(">>> ").strip()
            
            if not command:
                continue
            
            if command.lower() == 'quit':
                print("Goodbye!")
                break
            
            elif command.lower() == 'help':
                print("\nAvailable commands:")
                print("  exec <code>       - Execute single line Python code")
                print("  execm             - Execute multiline Python code")
                print("  execf <file>      - Execute Python code from file")
                print("  echo <message>    - Test echo method")
                print("  notify <message>  - Send notification")
                print("  raw <json>        - Send raw JSON-RPC")
                print("  batch             - Batch request mode")
                print("  release           - Release server (keeps pipe open)")
                print("  shutdown          - Shutdown server completely")
                print("  quit              - Exit client (local only)")
                print()
            
            elif command.startswith('exec '):
                # Execute single line Python code
                code = command[5:]
                try:
                    result = client.call("exec_code", {"code": code})
                    print_exec_result(result)
                except Exception as e:
                    print(f"Error: {e}")
            
            elif command.lower() == 'execm':
                # Execute multiline Python code
                code = get_multiline_code()
                if code:
                    try:
                        result = client.call("exec_code", {"code": code})
                        print_exec_result(result)
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("No code entered.")
            
            elif command.startswith('execf '):
                # Execute Python code from file
                filename = command[6:].strip()
                try:
                    with open(filename, 'r') as f:
                        code = f.read()
                    print(f"Executing code from {filename}...")
                    result = client.call("exec_code", {"code": code})
                    print_exec_result(result)
                except FileNotFoundError:
                    print(f"File not found: {filename}")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif command.lower() == 'release':
                print("Sending release command to server...")
                try:
                    result = client.release()
                    print(f"Server response: {result}")
                    print("Server released from main loop (pipe still open)")
                    print("You can restart the server by calling main() again")
                except Exception as e:
                    print(f"Error sending release command: {e}")
                    print("The server may not support the release command.")
            
            elif command.lower() == 'shutdown':
                print("Sending shutdown command to server...")
                try:
                    result = client.shutdown()
                    print(f"Server response: {result}")
                    print("Server is shutting down. Client will exit in 2 seconds...")
                    time.sleep(2)
                    print("Goodbye!")
                    break
                except Exception as e:
                    print(f"Error sending shutdown command: {e}")
                    print("The server may not support the shutdown command or may already be stopped.")
            
            elif command.startswith('echo '):
                message = command[5:]
                try:
                    result = client.call("echo", {"message": message})
                    print(f"Server echoed: {result}")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif command.startswith('notify '):
                message = command[7:]
                try:
                    client.notify("log", [message])
                    print("Notification sent")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif command.startswith('raw '):
                json_str = command[4:]
                try:
                    request = json.loads(json_str)
                    method = request.get('method', 'unknown')
                    params = request.get('params', None)
                    result = client.call(method, params)
                    print_result(result, format_json=True)
                except json.JSONDecodeError as e:
                    print(f"Invalid JSON: {e}")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif command == 'batch':
                print("\nBatch mode - enter requests (empty line to execute):")
                requests: List[tuple[str, Optional[Any]]] = []
                while True:
                    req = input("  method params> ").strip()
                    if not req:
                        break
                    parts = req.split(maxsplit=1)
                    if len(parts) == 1:
                        requests.append((parts[0], None))
                    else:
                        try:
                            params = json.loads(parts[1])
                            requests.append((parts[0], params))
                        except json.JSONDecodeError:
                            requests.append((parts[0], [parts[1]]))
                
                if requests:
                    try:
                        results = client.batch_call(requests)
                        print("\nBatch results:")
                        for i, result in enumerate(results):
                            print(f"  [{i+1}] {result}")
                    except Exception as e:
                        print(f"Batch error: {e}")
            
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands")
        
        except KeyboardInterrupt:
            print("\n\nInterrupted. Type 'quit' to exit.")
        except Exception as e:
            print(f"Unexpected error: {e}")


def main() -> None:
    """Main entry point for the IPC client."""
    parser = argparse.ArgumentParser(
        description="JSON-RPC IPC client for testing",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--pipe",
        type=str,
        required=True,
        help="Pipe name (e.g., 'my-test-pipe')"
    )
    
    parser.add_argument(
        "--method",
        type=str,
        help="Method to call (for non-interactive mode)"
    )
    
    parser.add_argument(
        "--params",
        type=str,
        help="Parameters as JSON string"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    parser.add_argument(
        "--format-json",
        action="store_true",
        help="Format JSON output with indentation"
    )
    
    parser.add_argument(
        "--release",
        action="store_true",
        help="Send release command to pause server (keeps pipe open)"
    )
    
    parser.add_argument(
        "--shutdown",
        action="store_true",
        help="Send shutdown command to stop server completely"
    )
    
    parser.add_argument(
        "--exec",
        type=str,
        help="Execute Python code directly"
    )
    
    parser.add_argument(
        "--exec-file",
        type=str,
        help="Execute Python code from a file"
    )
    
    args = parser.parse_args()
    
    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Format pipe address
    pipe_address = format_pipe_address(args.pipe)
    
    print("\n" + "=" * 60)
    print("JSON-RPC IPC Client")
    print("=" * 60)
    print(f"Pipe name:    {args.pipe}")
    print(f"Full address: {pipe_address}")
    print("=" * 60)
    
    # Create client
    client = JSONRPCPipeClient(pipe_address)
    
    try:
        if args.exec:
            # Execute Python code directly
            print(f"\nExecuting Python code: {args.exec[:50]}{'...' if len(args.exec) > 50 else ''}")
            try:
                result = client.call("exec_code", {"code": args.exec})
                print_exec_result(result)
            except Exception as e:
                print(f"Error: {e}")
                sys.exit(1)
        elif args.exec_file:
            # Execute Python code from file
            print(f"\nExecuting Python code from file: {args.exec_file}")
            try:
                with open(args.exec_file, 'r') as f:
                    code = f.read()
                result = client.call("exec_code", {"code": code})
                print_exec_result(result)
            except FileNotFoundError:
                print(f"File not found: {args.exec_file}")
                sys.exit(1)
            except Exception as e:
                print(f"Error: {e}")
                sys.exit(1)
        elif args.release:
            # Release mode - send release command to server
            print("\nSending release command to server...")
            try:
                result = client.release()
                print(f"Server response: {result}")
                print("Server released from main loop successfully.")
                print("The pipe remains open and server can be restarted.")
            except Exception as e:
                print(f"Error: {e}")
                print("The server may not support the release command.")
                sys.exit(1)
        elif args.shutdown:
            # Shutdown mode - send shutdown command to server
            print("\nSending shutdown command to server...")
            try:
                result = client.shutdown()
                print(f"Server response: {result}")
                print("Server is shutting down successfully.")
            except Exception as e:
                print(f"Error: {e}")
                print("The server may not support the shutdown command or may already be stopped.")
                sys.exit(1)
        elif args.interactive:
            interactive_mode(client)
        elif args.method:
            # Single call mode
            params = None
            if args.params:
                try:
                    params = json.loads(args.params)
                except json.JSONDecodeError:
                    # Treat as single string parameter
                    params = [args.params]
            
            print(f"\nCalling method: {args.method}")
            if params:
                print(f"With params: {params}")
            
            result = client.call(args.method, params)
            print("\nResponse:")
            print_result(result, args.format_json)
        else:
            # Default to interactive if no method specified
            interactive_mode(client)
    
    except ConnectionError as e:
        print(f"\nConnection error: {e}")
        print("Make sure the server is running with the same pipe name.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nClient interrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()