"""
Cascadeur Remote Client

This module provides a high-level client for communicating with Cascadeur's
embedded Python interpreter through JSON-RPC over named pipes.
"""

from __future__ import annotations

import logging
from typing import Any, Optional

import attrs

from cascadeur_py_client.server.jsonrpc_pipe_client import JSONRPCPipeClient

# Set up logging
logger = logging.getLogger(__name__)


@attrs.define
class ErrorInfo:
    """Error information from remote execution."""
    
    message: str = attrs.field(default="")
    traceback: str = attrs.field(default="")
    type: int = attrs.field(default=0)  # 0 = no error, 1 = error
    
    @property
    def has_error(self) -> bool:
        """Check if there's an error."""
        return self.type != 0 or bool(self.message)


@attrs.define
class CallResult:
    """Result from executing Python code in Cascadeur."""
    
    data: Any = attrs.field(default=None)
    encoding: Optional[str] = attrs.field(default=None)  # None for JSON, "base64" for binary
    error: ErrorInfo = attrs.field(factory=ErrorInfo)
    
    @classmethod
    def from_dict(cls, response: dict[str, Any]) -> CallResult:
        """Create CallResult from server response dictionary."""
        error_dict = response.get("error", {})
        error = ErrorInfo(
            message=error_dict.get("message", ""),
            traceback=error_dict.get("traceback", ""),
            type=error_dict.get("type", 0)
        )
        
        return cls(
            data=response.get("data"),
            encoding=response.get("encoding"),
            error=error
        )
    
    @property
    def success(self) -> bool:
        """Check if the call was successful."""
        return not self.error.has_error


class CascadeurRemoteClient:
    """High-level client for communicating with Cascadeur's embedded Python."""
    
    def __init__(self, pipe_name: Optional[str] = None):
        """
        Initialize the Cascadeur Remote Client.
        
        Args:
            pipe_name: The pipe name to connect to. If None, uses default.
        """
        self._rpc_client = JSONRPCPipeClient(address=pipe_name)
        logger.info(f"CascadeurRemoteClient initialized with pipe: {self._rpc_client.address}")
    
    @staticmethod
    def from_pipe(pipe_name: Optional[str] = None) -> CascadeurRemoteClient:
        """
        Create a CascadeurRemoteClient instance using the specified pipe name.
        
        Args:
            pipe_name: The pipe name to connect to. If None, uses default.
            
        Returns:
            A new CascadeurRemoteClient instance.
        """
        return CascadeurRemoteClient(pipe_name=pipe_name)
    
    def send_python(self, code: str, args: Optional[dict[str, Any]] = None) -> CallResult:
        """
        Execute Python code in Cascadeur with optional arguments.
        
        Args:
            code: The Python code to execute
            args: Optional dictionary of arguments to pass to the code execution
            
        Returns:
            CallResult containing the execution result and any error information
        """
        params: dict[str, Any] = {
            "code": code,
            "encoding": None  # Use UTF-8 encoding
        }
        
        # Add kw_binary_args if args provided
        if args is not None:
            # Note: The server expects kw_binary_args to be base64 encoded pickle data
            # For now, we'll pass args directly if the server supports it
            # Otherwise, we'd need to pickle and base64 encode the args
            import base64
            import pickle
            
            args_bytes = pickle.dumps(args)
            args_b64 = base64.b64encode(args_bytes).decode("utf-8")
            params["kw_binary_args"] = args_b64
        
        try:
            logger.debug(f"Executing Python code: {code[:100]}...")
            result = self._rpc_client.call("exec_code", params)
            
            # Convert response to CallResult
            if isinstance(result, dict):
                return CallResult.from_dict(result)
            else:
                # Unexpected response format
                error = ErrorInfo(
                    message=f"Unexpected response format: {type(result)}",
                    type=1
                )
                return CallResult(data=result, error=error)
                
        except Exception as e:
            logger.error(f"Error executing Python code: {e}")
            error = ErrorInfo(
                message=str(e),
                type=1
            )
            return CallResult(error=error)
    
    def send_release(self) -> None:
        """
        Send the release command to break out of the server's main loop.
        This unfreezes the Cascadeur application GUI.
        """
        try:
            logger.info("Sending release command")
            self._rpc_client.release()
        except Exception as e:
            logger.error(f"Error sending release command: {e}")
            raise
    
    def send_shutdown(self) -> None:
        """
        Send the shutdown command to terminate the server.
        """
        try:
            logger.info("Sending shutdown command")
            self._rpc_client.shutdown()
        except Exception as e:
            logger.error(f"Error sending shutdown command: {e}")
            raise
    
    def send_echo(self, message: str) -> str:
        """
        Send an echo message to the server.
        
        Args:
            message: The message to echo
            
        Returns:
            The echoed message from the server
            
        Raises:
            Exception: If there's an error with the echo request
        """
        try:
            logger.debug(f"Sending echo: {message}")
            result = self._rpc_client.call("echo", [message])
            
            if isinstance(result, str):
                return result
            else:
                raise Exception(f"Unexpected echo response type: {type(result)}")
                
        except Exception as e:
            logger.error(f"Error sending echo: {e}")
            raise
    
    @property
    def rpc_client(self) -> JSONRPCPipeClient:
        """
        Get the underlying JSON-RPC client instance.
        
        Returns:
            The JSONRPCPipeClient instance
        """
        return self._rpc_client
    
    def close(self) -> None:
        """
        Close the client connection.
        
        Note: The JSONRPCPipeClient creates connections on demand,
        so this is mainly for cleanup and logging purposes.
        """
        logger.info("Closing CascadeurRemoteClient")
        # JSONRPCPipeClient doesn't maintain persistent connections
        # But we can set it to None to indicate closed state
        self._rpc_client = None  # type: ignore[assignment]


def main() -> None:
    """Example usage of CascadeurRemoteClient."""
    # Create client using the static method
    client = CascadeurRemoteClient.from_pipe()
    
    try:
        # Test echo
        echo_result = client.send_echo("Hello, Cascadeur!")
        print(f"Echo result: {echo_result}")
        
        # Execute some Python code
        code = """
import sys
result = {
    'python_version': sys.version,
    'platform': sys.platform
}
"""
        exec_result = client.send_python(code)
        
        if exec_result.success:
            print(f"Execution result: {exec_result.data}")
        else:
            print(f"Execution failed: {exec_result.error.message}")
            if exec_result.error.traceback:
                print(f"Traceback: {exec_result.error.traceback}")
        
        # Execute with arguments
        code_with_args = """
result = a + b
"""
        args = {"a": 10, "b": 20}
        exec_result = client.send_python(code_with_args, args)
        
        if exec_result.success:
            print(f"Result with args: {exec_result.data}")
        else:
            print(f"Execution failed: {exec_result.error.message}")
        
    finally:
        # Clean up
        client.close()


if __name__ == "__main__":
    main()