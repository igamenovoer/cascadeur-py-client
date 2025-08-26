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
from pathlib import Path
from typing import Optional, Any, List

# Add src to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

from cascadeur_client.server.jsonrpc_pipe_client import JSONRPCPipeClient


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


def interactive_mode(client: JSONRPCPipeClient) -> None:
    """Run the client in interactive mode."""
    print("\n" + "=" * 60)
    print("Interactive JSON-RPC Client")
    print("=" * 60)
    print("Commands:")
    print("  echo <message>    - Send echo request")
    print("  notify <message>  - Send notification (no response)")
    print("  raw <json>        - Send raw JSON-RPC request")
    print("  batch             - Enter batch mode")
    print("  shutdown          - Send quit command to server")
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
                print("  echo <message>    - Test echo method")
                print("  notify <message>  - Send notification")
                print("  raw <json>        - Send raw JSON-RPC")
                print("  batch             - Batch request mode")
                print("  shutdown          - Send quit command to server")
                print("  quit              - Exit client (local only)")
                print()
            
            elif command.lower() == 'shutdown':
                print("Sending shutdown command to server...")
                try:
                    result = client.call("quit", {})
                    print(f"Server response: {result}")
                    print("Server is shutting down. Client will exit in 2 seconds...")
                    time.sleep(2)
                    print("Goodbye!")
                    break
                except Exception as e:
                    print(f"Error sending shutdown command: {e}")
                    print("The server may not support the quit command or may already be stopped.")
            
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
                        except:
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
        "--shutdown",
        action="store_true",
        help="Send quit command to shutdown the server"
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
        if args.shutdown:
            # Shutdown mode - send quit command to server
            print("\nSending shutdown command to server...")
            try:
                result = client.call("quit", {})
                print(f"Server response: {result}")
                print("Server is shutting down successfully.")
            except Exception as e:
                print(f"Error: {e}")
                print("The server may not support the quit command or may already be stopped.")
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