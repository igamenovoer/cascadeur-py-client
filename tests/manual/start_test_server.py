#!/usr/bin/env python
"""
Start a JSON-RPC test server with a random or specified pipe name.

Usage:
    python start_test_server.py                    # Random pipe name
    python start_test_server.py --pipe custom-name # Specific pipe name
"""

import os
import sys
import uuid
import argparse
from pathlib import Path

# Add src to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

from cascadeur_py_client.server.jsonrpc_pipe_server import JSONRPCPipeServer


def generate_unique_pipe_name() -> str:
    """Generate a unique pipe name using UUID."""
    unique_id = str(uuid.uuid4())[:8]
    return f"test-pipe-{unique_id}"


def format_pipe_address(pipe_name: str) -> str:
    """Convert pipe name to OS-specific full address."""
    if os.name == 'nt':  # Windows
        return rf'\\.\pipe\{pipe_name}'
    else:  # Unix/Linux/macOS
        return f'/tmp/{pipe_name}.sock'


def main():
    """Start the test server."""
    parser = argparse.ArgumentParser(
        description="Start a JSON-RPC test server",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--pipe",
        type=str,
        help="Pipe name (if not provided, generates a random one)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Get or generate pipe name
    if args.pipe:
        pipe_name = args.pipe
        print(f"Using specified pipe name: {pipe_name}")
    else:
        pipe_name = generate_unique_pipe_name()
        print(f"Generated random pipe name: {pipe_name}")
    
    # Get full address
    pipe_address = format_pipe_address(pipe_name)
    
    # Print connection info
    print("\n" + "=" * 60)
    print("JSON-RPC Test Server")
    print("=" * 60)
    print(f"Pipe name:    {pipe_name}")
    print(f"Full address: {pipe_address}")
    print("=" * 60)
    print("\nTo connect with client:")
    print(f"  python tests/manual/run_ipc_client.py --pipe {pipe_name} -i")
    print("\nTo shutdown server:")
    print(f"  python tests/manual/run_ipc_client.py --pipe {pipe_name} --shutdown")
    print("\nOr in interactive mode, use the 'shutdown' command")
    print("=" * 60)
    print()
    
    # Configure logging if verbose
    if args.verbose:
        import logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    # Start server
    server = JSONRPCPipeServer(pipe_address)
    
    try:
        print("Starting server... (Press Ctrl+C or use 'quit' RPC method to stop)")
        server.start()
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except Exception as e:
        print(f"\nServer error: {e}")
        sys.exit(1)
    
    print("\nServer shutdown complete")


if __name__ == "__main__":
    main()