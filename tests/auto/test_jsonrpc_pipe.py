"""
Test suite for JSON-RPC pipe server and client.

This module tests the JSON-RPC server and client implementation
using named pipes for inter-process communication.
"""

import os
import sys
import time
import subprocess
import pytest
from pathlib import Path
from typing import Optional, Any, List, Tuple, Dict
from multiprocessing import Process

# Add src directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from cascadeur_client.server.jsonrpc_pipe_client import JSONRPCPipeClient
from cascadeur_client.server.jsonrpc_pipe_server import JSONRPCPipeServer


class TestJSONRPCPipe:
    """Test class for JSON-RPC pipe communication."""
    
    server_process: Optional[subprocess.Popen] = None
    server_proc: Optional[Process] = None
    client: Optional[JSONRPCPipeClient] = None
    
    @classmethod
    def setup_class(cls) -> None:
        """Setup test class - starts the server process."""
        # Path to server script
        server_script: Path = project_root / "src" / "cascadeur_client" / "server" / "jsonrpc_pipe_server.py"
        
        # Start server in subprocess using pixi
        cmd: List[str] = ["pixi", "run", "-e", "dev", "python", str(server_script)]
        
        try:
            cls.server_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Give server time to start
            time.sleep(2)
            
            # Check if process is still running
            if cls.server_process.poll() is not None:
                stdout, stderr = cls.server_process.communicate()
                raise RuntimeError(f"Server failed to start. STDOUT: {stdout}, STDERR: {stderr}")
                
            # Initialize client
            cls.client = JSONRPCPipeClient()
            
        except Exception as e:
            pytest.fail(f"Failed to start server: {e}")
    
    @classmethod
    def teardown_class(cls) -> None:
        """Teardown test class - stops the server process."""
        if cls.server_process:
            cls.server_process.terminate()
            time.sleep(1)
            if cls.server_process.poll() is None:
                cls.server_process.kill()
    
    def test_simple_echo(self) -> None:
        """Test simple echo functionality."""
        assert self.client is not None, "Client not initialized"
        
        message: str = "Hello, JSON-RPC!"
        result: str = self.client.call("echo", [message])
        assert result == message, f"Expected '{message}', got '{result}'"
    
    def test_echo_with_dict_params(self) -> None:
        """Test echo with dictionary parameters."""
        assert self.client is not None, "Client not initialized"
        
        message: str = "Testing dict params"
        result: str = self.client.call("echo", {"message": message})
        assert result == message, f"Expected '{message}', got '{result}'"
    
    def test_empty_string_echo(self) -> None:
        """Test echo with empty string."""
        assert self.client is not None, "Client not initialized"
        
        message: str = ""
        result: str = self.client.call("echo", [message])
        assert result == message, "Expected empty string"
    
    def test_special_characters(self) -> None:
        """Test echo with special characters."""
        assert self.client is not None, "Client not initialized"
        
        message: str = "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?"
        result: str = self.client.call("echo", [message])
        assert result == message, f"Special characters not handled correctly"
    
    def test_unicode_characters(self) -> None:
        """Test echo with unicode characters."""
        assert self.client is not None, "Client not initialized"
        
        message: str = "Unicode: 你好世界 مرحبا بالعالم こんにちは"
        result: str = self.client.call("echo", [message])
        assert result == message, "Unicode characters not handled correctly"
    
    def test_long_message(self) -> None:
        """Test echo with a long message."""
        assert self.client is not None, "Client not initialized"
        
        message: str = "A" * 10000  # 10KB message
        result: str = self.client.call("echo", [message])
        assert result == message, "Long message not handled correctly"
        assert len(result) == 10000, f"Expected length 10000, got {len(result)}"
    
    def test_invalid_method(self) -> None:
        """Test calling an invalid method."""
        assert self.client is not None, "Client not initialized"
        
        with pytest.raises(Exception) as exc_info:
            self.client.call("invalid_method")
        
        assert "Method not found" in str(exc_info.value), "Expected 'Method not found' error"
        assert "-32601" in str(exc_info.value), "Expected JSON-RPC error code -32601"
    
    def test_missing_parameter(self) -> None:
        """Test calling echo without required parameter."""
        assert self.client is not None, "Client not initialized"
        
        with pytest.raises(Exception) as exc_info:
            self.client.call("echo", [])
        
        assert "Missing required parameter" in str(exc_info.value) or "Invalid params" in str(exc_info.value), \
            "Expected parameter error"
    
    def test_wrong_parameter_type(self) -> None:
        """Test calling echo with wrong parameter type."""
        assert self.client is not None, "Client not initialized"
        
        with pytest.raises(Exception) as exc_info:
            self.client.call("echo", [123])  # Number instead of string
        
        assert "Parameter must be a string" in str(exc_info.value), "Expected type error"
    
    def test_notification(self) -> None:
        """Test sending a notification (no response expected)."""
        assert self.client is not None, "Client not initialized"
        
        # Should not raise any exception
        self.client.notify("log", ["This is a test notification"])
        
        # Give it a moment to process
        time.sleep(0.1)
        
        # Test notification with no method (should still work)
        self.client.notify("nonexistent", ["Another notification"])
    
    def test_batch_request(self) -> None:
        """Test batch request functionality."""
        assert self.client is not None, "Client not initialized"
        
        requests: List[Tuple[str, List[str]]] = [
            ("echo", ["First"]),
            ("echo", ["Second"]),
            ("echo", ["Third"])
        ]
        
        results: List[Any] = self.client.batch_call(requests)
        
        assert len(results) == 3, f"Expected 3 results, got {len(results)}"
        
        expected: List[str] = ["First", "Second", "Third"]
        for i, (exp, res) in enumerate(zip(expected, results)):
            if isinstance(res, Exception):
                pytest.fail(f"Request {i+1} raised exception: {res}")
            assert res == exp, f"Request {i+1}: expected '{exp}', got '{res}'"
    
    def test_mixed_batch_request(self) -> None:
        """Test batch request with valid and invalid methods."""
        assert self.client is not None, "Client not initialized"
        
        requests: List[Tuple[str, Optional[List[str]]]] = [
            ("echo", ["Valid"]),
            ("invalid_method", None),
            ("echo", ["Another valid"])
        ]
        
        results: List[Any] = self.client.batch_call(requests)
        
        assert len(results) == 3, f"Expected 3 results, got {len(results)}"
        assert results[0] == "Valid", f"First result should be 'Valid', got {results[0]}"
        assert isinstance(results[1], Exception), "Second result should be an exception"
        assert results[2] == "Another valid", f"Third result should be 'Another valid', got {results[2]}"
    
    def test_concurrent_requests(self) -> None:
        """Test multiple concurrent client connections."""
        assert self.client is not None, "Client not initialized"
        
        # Create multiple clients
        client1: JSONRPCPipeClient = JSONRPCPipeClient()
        client2: JSONRPCPipeClient = JSONRPCPipeClient()
        
        # Make concurrent requests
        result1: str = client1.call("echo", ["Client 1"])
        result2: str = client2.call("echo", ["Client 2"])
        
        assert result1 == "Client 1", f"Client 1: expected 'Client 1', got '{result1}'"
        assert result2 == "Client 2", f"Client 2: expected 'Client 2', got '{result2}'"
    
    def test_rapid_successive_calls(self) -> None:
        """Test rapid successive calls to ensure connection stability."""
        assert self.client is not None, "Client not initialized"
        
        for i in range(50):
            message: str = f"Message {i}"
            result: str = self.client.call("echo", [message])
            assert result == message, f"Call {i}: expected '{message}', got '{result}'"
    
    def test_json_special_characters(self) -> None:
        """Test JSON special characters in messages."""
        assert self.client is not None, "Client not initialized"
        
        # Test various JSON special characters
        test_cases: List[str] = [
            '{"test": "value"}',
            '"quoted string"',
            'string with "quotes" inside',
            'backslash \\ test',
            'newline \n and tab \t test',
            '{"nested": {"json": "structure"}}',
        ]
        
        for message in test_cases:
            result: str = self.client.call("echo", [message])
            assert result == message, f"Failed for message: {message}"


class TestJSONRPCPipeServerDirect:
    """Test the server class directly without subprocess."""
    
    def test_server_initialization(self) -> None:
        """Test server initialization."""
        server: JSONRPCPipeServer = JSONRPCPipeServer()
        assert server.address is not None, "Server address not set"
        assert not server.running, "Server should not be running initially"
        
        # Check platform-specific address
        if os.name == 'nt':
            assert server.address == r'\\.\pipe\my-test-pipe', f"Wrong Windows pipe address: {server.address}"
        else:
            assert server.address == '/tmp/my-test-pipe.sock', f"Wrong Unix socket address: {server.address}"
    
    def test_server_with_custom_address(self) -> None:
        """Test server with custom address."""
        custom_address: str = r'\\.\pipe\custom-test-pipe' if os.name == 'nt' else '/tmp/custom.sock'
        server: JSONRPCPipeServer = JSONRPCPipeServer(custom_address)
        assert server.address == custom_address, f"Custom address not set correctly: {server.address}"
    
    def test_client_initialization(self) -> None:
        """Test client initialization."""
        client: JSONRPCPipeClient = JSONRPCPipeClient()
        assert client.address is not None, "Client address not set"
        
        # Check platform-specific address
        if os.name == 'nt':
            assert client.address == r'\\.\pipe\my-test-pipe', f"Wrong Windows pipe address: {client.address}"
        else:
            assert client.address == '/tmp/my-test-pipe.sock', f"Wrong Unix socket address: {client.address}"
    
    def test_client_with_custom_address(self) -> None:
        """Test client with custom address."""
        custom_address: str = r'\\.\pipe\custom-test-pipe' if os.name == 'nt' else '/tmp/custom.sock'
        client: JSONRPCPipeClient = JSONRPCPipeClient(custom_address)
        assert client.address == custom_address, f"Custom address not set correctly: {client.address}"


@pytest.fixture
def isolated_server_client() -> Tuple[JSONRPCPipeServer, JSONRPCPipeClient]:
    """
    Fixture to create an isolated server and client pair for testing.
    
    Returns:
        Tuple of (server, client) instances
    """
    # Use a unique address for isolation
    unique_address: str = (
        rf'\\.\pipe\test-pipe-{os.getpid()}' 
        if os.name == 'nt' 
        else f'/tmp/test-pipe-{os.getpid()}.sock'
    )
    
    server: JSONRPCPipeServer = JSONRPCPipeServer(unique_address)
    client: JSONRPCPipeClient = JSONRPCPipeClient(unique_address)
    
    return server, client


def test_connection_error_when_server_not_running(isolated_server_client: Tuple[JSONRPCPipeServer, JSONRPCPipeClient]) -> None:
    """Test that client raises appropriate error when server is not running."""
    server, client = isolated_server_client
    
    with pytest.raises(ConnectionError) as exc_info:
        client.call("echo", ["test"])
    
    assert "Cannot connect to server" in str(exc_info.value), "Expected connection error message"
    assert "Is the server running?" in str(exc_info.value), "Expected helpful error message"