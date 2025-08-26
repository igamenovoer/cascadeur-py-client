#!/usr/bin/env python
"""
Run the JSON-RPC IPC server with a custom pipe name.

This script starts the JSON-RPC pipe server with OS-specific pipe naming
handled automatically. User provides simple pipe names without OS prefixes.
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional

# Add src to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

from cascadeur_client.server.jsonrpc_pipe_server import JSONRPCPipeServer


def format_pipe_address(pipe_name: str) -> str:
    """
    Convert a simple pipe name to OS-specific full pipe address.
    
    Args:
        pipe_name: Simple pipe name like "my-test-pipe"
        
    Returns:
        OS-specific pipe address:
        - Windows: \\.\pipe\<pipe_name>
        - Unix: /tmp/<pipe_name>.sock
    """
    if os.name == 'nt':  # Windows
        return rf'\\.\pipe\{pipe_name}'
    else:  # Unix/Linux/macOS
        return f'/tmp/{pipe_name}.sock'


def cleanup_unix_socket(address: str) -> None:
    """Clean up existing Unix socket file if it exists."""
    if os.name != 'nt' and os.path.exists(address):
        try:
            os.unlink(address)
            print(f"Cleaned up existing socket: {address}")
        except Exception as e:
            print(f"Warning: Failed to clean up socket: {e}")


def main() -> None:
    """Main entry point for running the IPC server."""
    parser = argparse.ArgumentParser(
        description="Run JSON-RPC IPC server with custom pipe name",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--pipe",
        type=str,
        required=True,
        help="Pipe name (e.g., 'my-test-pipe'). OS-specific formatting is handled automatically."
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose debug logging"
    )
    
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress info messages, only show warnings and errors"
    )
    
    args = parser.parse_args()
    
    # Configure logging
    if args.quiet:
        log_level = logging.WARNING
    elif args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    # Format pipe address
    pipe_address = format_pipe_address(args.pipe)
    
    # Clean up Unix socket if it exists
    cleanup_unix_socket(pipe_address)
    
    # Display server information
    print("\n" + "=" * 60)
    print("JSON-RPC IPC Server Configuration")
    print("=" * 60)
    print(f"Platform:        {sys.platform}")
    print(f"OS Type:         {'Windows' if os.name == 'nt' else 'Unix-like'}")
    print(f"Python Version:  {sys.version.split()[0]}")
    print(f"Simple Name:     {args.pipe}")
    print(f"Full Address:    {pipe_address}")
    print(f"Log Level:       {logging.getLevelName(log_level)}")
    print("=" * 60)
    
    # Create and start server
    server = JSONRPCPipeServer(pipe_address)
    
    print(f"\nStarting server on: {pipe_address}")
    print("Press Ctrl+C to stop the server\n")
    print("-" * 60)
    
    try:
        server.start()
    except KeyboardInterrupt:
        print("\n\nServer interrupted by user")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)
    finally:
        print("\nServer stopped")
        # Final cleanup for Unix sockets
        cleanup_unix_socket(pipe_address)


if __name__ == "__main__":
    main()