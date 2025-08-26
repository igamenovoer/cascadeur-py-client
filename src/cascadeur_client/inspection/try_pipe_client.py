"""
Minimal JSON-RPC pipe client for Cascadeur.
Self-contained, no external dependencies.
"""

import json
import struct
import os
import tempfile
import logging
from pathlib import Path
from multiprocessing.connection import Client
from datetime import datetime
from typing import Any, Optional

# Configure logging
def setup_logging() -> logging.Logger:
    """Setup logging to both console and file."""
    # Determine output directory
    output_dir = os.environ.get('CASCADEUR_PYTHON_OUTPUT_DIR')
    if output_dir:
        log_dir = Path(output_dir)
    else:
        log_dir = Path(tempfile.gettempdir())
    
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create log filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    log_file = log_dir / f"log-{timestamp}.txt"
    
    # Configure logger
    logger = logging.getLogger('pipe_client')
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Format
    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s', 
                                  datefmt='%H:%M:%S')
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console)
    logger.addHandler(file_handler)
    
    logger.info(f"Logging to: {log_file}")
    return logger

# Config
PIPE_ADDRESS = r'\\.\pipe\my-test-pipe'
log = setup_logging()

def send_msg(conn: Any, msg: str) -> None:
    """Send with 4-byte length prefix."""
    data = msg.encode('utf-8')
    conn.send_bytes(struct.pack('!I', len(data)) + data)

def recv_msg(conn: Any) -> str:
    """Receive with length prefix."""
    raw: bytes = conn.recv_bytes()
    if len(raw) < 4:
        raise ValueError("Message too short")
    length = struct.unpack('!I', raw[:4])[0]
    message: str = raw[4:4+length].decode('utf-8')
    return message

def rpc_call(method: str, params: Optional[dict] = None, pipe_address: Optional[str] = None) -> Optional[Any]:
    """Make a JSON-RPC call."""
    address = pipe_address or PIPE_ADDRESS
    request = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    
    try:
        with Client(address, authkey=None) as conn:
            # Send request
            send_msg(conn, json.dumps(request))
            log.debug(f"Sent: {method} with {params}")
            
            # Get response
            response = json.loads(recv_msg(conn))
            
            if "error" in response:
                error = response["error"]
                log.error(f"RPC Error: {error.get('message')} (code: {error.get('code')})")
                return None
            
            result = response.get("result")
            log.debug(f"Result: {result}")
            return result
            
    except FileNotFoundError:
        log.error(f"Server not found at {address}")
        return None
    except Exception as e:
        log.error(f"Failed: {e}")
        return None

# === Main execution ===
log.info("=" * 40)
log.info("MINIMAL PIPE CLIENT TEST")
log.info("=" * 40)

# Simple echo test
message = "Hello from minimal client"
log.info(f"Testing echo: '{message}'")

result = rpc_call("echo", {"message": message})

if result == message:
    log.info("SUCCESS: Echo worked correctly")
else:
    log.error(f"FAILED: Got '{result}' expected '{message}'")