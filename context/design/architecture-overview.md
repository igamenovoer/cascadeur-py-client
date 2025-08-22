# Cascadeur Python Client Architecture Overview

## HEADER
- **Purpose**: Document the high-level architecture of the Cascadeur Python Client
- **Status**: Active
- **Date**: 2025-01-22
- **Dependencies**: Cascadeur API, JSON-RPC 2.0 protocol
- **Target**: AI assistants and developers

## Architecture Components

### Client Layer
The main entry point for users, providing a pythonic interface:
- **CascadeurClient** (`src/cascadeur_client/client.py`) - Main client class managing connections
- **Scene** (`src/cascadeur_client/scene.py`) - Scene manipulation and management
- **Animation** (`src/cascadeur_client/animation.py`) - Animation curve and keyframe handling
- **Rig** (`src/cascadeur_client/rig.py`) - Character rig management

### Server Layer
Multiple server implementations running inside Cascadeur's Python environment:

#### Server Variants
1. **Async Server** (`health_exec_server_aio.py`)
   - Non-blocking aiohttp implementation
   - Suitable for concurrent request handling
   - Can run in existing event loops

2. **Threaded Server** (`health_exec_server_threaded.py`)
   - Thread-based concurrent handling
   - Good for CPU-bound operations

3. **Sync Server** (`health_exec_server.py`)
   - Simple synchronous implementation
   - Baseline reference implementation

### Communication Protocol
- **JSON-RPC 2.0** over HTTP
- **Base64 encoding** for code transmission (avoids JSON escaping issues)
- **Two core methods**:
  - `health` - Server status check
  - `exec_b64` - Execute base64-encoded Python code

### Data Flow
```
User Code → CascadeurClient → JSON-RPC Request → Server in Cascadeur
                                                           ↓
                                                    Execute in Cascadeur
                                                           ↓
User Code ← Parse Response ← JSON-RPC Response ← Return Results
```

## Design Decisions

### Why Multiple Server Implementations?
- Different deployment scenarios require different approaches
- Async for UI responsiveness
- Threaded for parallel processing
- Sync for simplicity and debugging

### Why Base64 Encoding?
- Eliminates JSON string escaping issues
- Preserves code formatting exactly
- Simplifies multiline code transmission
- Reduces parsing errors

### Why JSON-RPC?
- Industry standard protocol
- Built-in error handling
- Request/response correlation via ID
- Language agnostic

## Integration Points
- Cascadeur's internal Python API (`csc.app`)
- MCP (Model Context Protocol) readiness
- External tool integration capabilities

## Current State
- Core client structure implemented
- Multiple server variants created
- Placeholder Cascadeur API integration (actual API pending)
- Basic test coverage established