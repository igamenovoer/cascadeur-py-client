"""
Utilities for managing pipe addresses across platforms.

This module provides helper functions to handle pipe naming conventions
and environment variable configuration for JSON-RPC pipe servers and clients.

Environment Variables:
    CASCADEUR_PYTHON_RPC_PIPE_NAME:
        Sets the default pipe name for JSON-RPC communication.
        If not set, defaults to "cas-pipe".

        The value can be:
        - A simple name (e.g., "my-pipe") - OS-specific prefix will be added
        - A full path (e.g., "\\\\.\\pipe\\my-pipe" on Windows) - used as-is

        Examples:
            Windows:
                set CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
                # Results in: \\\\.\\pipe\\my-custom-pipe

                set CASCADEUR_PYTHON_RPC_PIPE_NAME=\\\\.\\pipe\\special-pipe
                # Results in: \\\\.\\pipe\\special-pipe (unchanged)

            Linux/macOS:
                export CASCADEUR_PYTHON_RPC_PIPE_NAME=my-custom-pipe
                # Results in: /tmp/my-custom-pipe.sock

                export CASCADEUR_PYTHON_RPC_PIPE_NAME=/var/run/my-pipe.sock
                # Results in: /var/run/my-pipe.sock (unchanged)
"""

import os
from typing import Optional


def get_default_pipe_address(custom_name: Optional[str] = None) -> str:
    """
    Get the default pipe address with proper OS-specific formatting.

    Priority order:
    1. If custom_name is provided, use it
    2. Check CASCADEUR_PYTHON_RPC_PIPE_NAME environment variable
    3. Fall back to "cas-pipe" as default

    The function automatically adds OS-specific prefixes if not already present:
    - Windows: \\.\pipe\<name>
    - Unix/Linux/macOS: /tmp/<name>.sock

    Args:
        custom_name: Optional custom pipe name to use instead of defaults

    Returns:
        The full pipe address with proper OS-specific formatting
    """
    # Determine the pipe name
    if custom_name:
        pipe_name = custom_name
    else:
        # Check environment variable first
        pipe_name = os.environ.get("CASCADEUR_PYTHON_RPC_PIPE_NAME", "cas-pipe")

    # Add OS-specific prefix if not already present
    if os.name == "nt":  # Windows
        # Check if it already has Windows pipe prefix
        if pipe_name.startswith(r"\\.\pipe\\"):
            return pipe_name
        elif pipe_name.startswith("\\\\"):
            # Might be a different format, return as-is
            return pipe_name
        else:
            # Add Windows named pipe prefix
            return rf"\\.\pipe\{pipe_name}"
    else:  # Unix/Linux/macOS
        # Check if it already looks like a full path
        if pipe_name.startswith("/"):
            # Already has a path, return as-is
            return pipe_name
        else:
            # Add Unix socket path and extension
            if not pipe_name.endswith(".sock"):
                pipe_name = f"{pipe_name}.sock"
            return f"/tmp/{pipe_name}"
