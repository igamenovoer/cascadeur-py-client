<execution>
  <constraint>
    ## Technical Constraints
    
    ### Python Version Requirements
    - Minimum Python 3.11 for full typing features
    - Use `from __future__ import annotations` for forward references
    - Leverage PEP 604 union types (X | Y instead of Union[X, Y])
    
    ### Platform Constraints
    - Windows: Named pipes require specific path format (\\.\pipe\)
    - Linux/Mac: Unix domain sockets have path length limits
    - Cross-platform: Pickle protocol differences between Python versions
    - Memory: Shared memory size limits vary by OS
    
    ### Serialization Limits
    - Pickle: Security risks with untrusted data
    - JSON: No datetime, bytes, or custom object support
    - MessagePack: Better performance but external dependency
    - Protobuf: Requires schema definition overhead
  </constraint>
  
  <rule>
    ## Mandatory Development Rules
    
    ### Type Safety Rules
    - Every function MUST have complete type hints
    - Use mypy strict mode (disallow_untyped_defs = true)
    - Runtime validation at process boundaries is required
    - No Any types without explicit justification
    
    ### IPC Safety Rules
    - Always implement message framing (never raw send/recv)
    - Set explicit timeouts on all blocking operations
    - Clean up IPC resources in finally blocks or context managers
    - Validate message size before allocation
    
    ### Process Management Rules
    - Always join() or terminate() child processes
    - Use process pools for repeated work
    - Implement graceful shutdown handlers
    - Monitor process health with heartbeats
  </rule>
  
  <guideline>
    ## Best Practice Guidelines
    
    ### Code Organization
    ```
    project/
    ├── protocols/      # Type Protocol definitions
    ├── messages/       # Message type definitions
    ├── workers/        # Process worker implementations
    ├── ipc/           # IPC utilities and abstractions
    └── monitors/      # Health check and monitoring
    ```
    
    ### Naming Conventions
    - Suffix process classes with `Process` or `Worker`
    - Prefix IPC protocols with `IPC` (e.g., `IPCClient`)
    - Use `_msg` suffix for message types
    - Use `_handler` suffix for message handlers
    
    ### Documentation Standards
    - Document IPC protocol with sequence diagrams
    - Include message format examples
    - Specify timeout and retry behavior
    - Note platform-specific considerations
  </guideline>
  
  <process>
    ## Standard Development Workflow
    
    ### Step 1: Define Message Types
    ```python
    from typing import TypedDict, Literal
    from datetime import datetime
    
    class RequestMsg(TypedDict):
        id: str
        method: Literal['echo', 'process', 'shutdown']
        params: dict[str, Any]
        timestamp: datetime
    
    class ResponseMsg(TypedDict):
        id: str
        result: Any
        error: str | None
        timestamp: datetime
    ```
    
    ### Step 2: Create Protocol Interface
    ```python
    from typing import Protocol, Generic, TypeVar
    
    T = TypeVar('T', covariant=True)
    R = TypeVar('R', contravariant=True)
    
    class IPCChannel(Protocol[T, R]):
        def send(self, message: T) -> None: ...
        def recv(self, timeout: float | None = None) -> R: ...
        def close(self) -> None: ...
    ```
    
    ### Step 3: Implement IPC Layer
    ```python
    import struct
    from multiprocessing.connection import Connection
    
    class FramedConnection:
        def __init__(self, conn: Connection) -> None:
            self.conn = conn
        
        def send_bytes(self, data: bytes) -> None:
            # Send 4-byte length prefix + data
            self.conn.send_bytes(struct.pack('!I', len(data)) + data)
        
        def recv_bytes(self) -> bytes:
            # Read length prefix then exact bytes
            header = self.conn.recv_bytes(4)
            length = struct.unpack('!I', header)[0]
            return self.conn.recv_bytes(length)
    ```
    
    ### Step 4: Build Worker Processes
    ```python
    from multiprocessing import Process
    from typing import Callable
    
    class TypedWorker(Process):
        def __init__(
            self, 
            handler: Callable[[RequestMsg], ResponseMsg],
            connection: FramedConnection
        ) -> None:
            super().__init__()
            self.handler = handler
            self.connection = connection
        
        def run(self) -> None:
            try:
                while True:
                    msg = self.receive_message()
                    if msg['method'] == 'shutdown':
                        break
                    response = self.handler(msg)
                    self.send_message(response)
            finally:
                self.connection.close()
    ```
    
    ### Step 5: Add Monitoring
    ```python
    import logging
    from contextlib import contextmanager
    from typing import Iterator
    
    @contextmanager
    def monitored_worker(name: str) -> Iterator[TypedWorker]:
        worker = TypedWorker(...)
        logging.info(f"Starting worker {name}")
        worker.start()
        try:
            yield worker
        finally:
            worker.terminate()
            worker.join(timeout=5.0)
            if worker.is_alive():
                worker.kill()
            logging.info(f"Worker {name} stopped")
    ```
  </process>
  
  <criteria>
    ## Quality Criteria
    
    ### Type Safety Metrics
    - ✅ 100% type coverage (mypy reports no untyped)
    - ✅ No use of Any without comment justification
    - ✅ Protocol types for all IPC interfaces
    - ✅ Runtime validation at boundaries
    
    ### Reliability Metrics
    - ✅ Zero zombie processes after shutdown
    - ✅ All IPC resources properly cleaned
    - ✅ Graceful handling of process crashes
    - ✅ Message delivery guarantees documented
    
    ### Performance Metrics
    - ✅ IPC latency < 1ms for local messages
    - ✅ Process startup time < 100ms
    - ✅ Memory usage stable under load
    - ✅ CPU utilization scales linearly
    
    ### Code Quality
    - ✅ All functions have docstrings
    - ✅ Complex IPC flows have sequence diagrams
    - ✅ Integration tests cover happy and error paths
    - ✅ Platform-specific code clearly marked
  </criteria>
</execution>