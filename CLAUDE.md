# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Development Commands

### Environment Setup
```bash
# Using pixi (recommended - handles both conda and PyPI dependencies)
pixi install
pixi shell  # Activate default environment

# Or traditional pip install
pip install -e ".[dev]"
```

### Code Quality
```bash
# Format code with black
pixi run -e dev black src tests scripts examples

# Sort imports
pixi run -e dev isort src tests scripts examples

# Lint with ruff (recommended - faster and comprehensive)
pixi run -e dev ruff check src tests scripts
pixi run -e dev ruff format src tests scripts

# Type checking with mypy strict mode
pixi run -e dev mypy src --strict

# Check server code specifically
pixi run -e dev mypy src/cascadeur_py_client/server/ --strict
pixi run -e dev ruff check src/cascadeur_py_client/server/
```

### Testing
```bash
# Run all automated tests
pixi run -e dev pytest tests/auto/

# Run with coverage report
pixi run -e dev pytest tests/auto/ --cov=cascadeur_py_client --cov-report=term-missing

# Run specific test file
pixi run -e dev pytest tests/auto/test_jsonrpc_pipe.py

# Run a single test
pixi run -e dev pytest tests/auto/test_jsonrpc_pipe.py::TestJSONRPCPipe::test_simple_echo

# Manual testing of JSON-RPC servers
pixi run -e dev python tests/manual/run_ipc_server.py  # Start server
pixi run -e dev python tests/manual/run_ipc_client.py  # Test client
```

### Cascadeur Package Management
```bash
# Activate the cas-installer environment (Python 3.11 for binary compatibility)
pixi shell -e cas-installer

# Install packages into Cascadeur
python scripts/pip_for_cascadeur.py install <package_name>
python scripts/pip_for_cascadeur.py install -r requirements-cascadeur.txt

# List installed packages
python scripts/pip_for_cascadeur.py list
python scripts/pip_for_cascadeur.py list --format=freeze

# Uninstall packages
python scripts/pip_for_cascadeur.py uninstall <package_name>
```

## Architecture Overview

### Cascadeur's Embedded Python Environment
Cascadeur uses an embedded Python 3.11 interpreter with these characteristics:
- **No standalone python.exe**: Python runs through cascadeur.exe
- **Isolated runtime**: Ignores environment variables, no user site packages
- **No console I/O**: stdin/stdout/stderr are null
- **Custom module**: `csc` module provides Cascadeur's internal API
- **Site-packages locations**: 
  - `%LOCALAPPDATA%\Cascadeur\Lib\site-packages`
  - `%LOCALAPPDATA%\Cascadeur\python\Lib\site-packages`

### IPC Architecture
The project implements a JSON-RPC over named pipes communication system:

#### Server Components (`src/cascadeur_py_client/server/`)
- **jsonrpc_pipe_server.py**: Threaded server with concurrent client handling
- **jsonrpc_pipe_server_sync.py**: Single-threaded synchronous server
- **jsonrpc_pipe_client.py**: Client library for connecting to servers
- **pipe_utils.py**: Centralized pipe configuration and environment handling

#### Communication Protocol
- Uses named pipes (Windows: `\\.\pipe\name`, Unix: `/tmp/name.sock`)
- JSON-RPC 2.0 protocol with message length prefixing
- Configurable pipe names via `CASCADEUR_PYTHON_RPC_PIPE_NAME` environment variable
- Default pipe name: `cas-pipe` (with OS-specific prefixes)
- Supports `release` (break loop, keep pipe) and `shutdown` (full termination) commands

### Package Management System
Due to Cascadeur's embedded Python limitations:
- External Python 3.11 environment (`cas-installer`) manages packages
- `scripts/pip_for_cascadeur.py`: Pip-like interface for package management
- Uses `--target` flag to install directly into Cascadeur's site-packages
- Binary wheel compatibility requires exact Python 3.11 match

### Testing Infrastructure
- **tests/auto/**: Automated pytest tests for CI/CD
- **tests/manual/**: Interactive testing tools (only created when explicitly needed)
- JSON-RPC pipe tests verify IPC functionality
- Coverage reporting integrated with pytest

## Key Design Decisions

### Why Named Pipes?
- Native Windows IPC mechanism with good performance
- No firewall issues unlike TCP sockets
- Built-in security through Windows access controls
- Simple to implement with Python's win32 libraries

### Why External Package Management?
- Cascadeur's Python lacks pip and console access
- External Python can download and install packages normally
- Binary compatibility ensured by matching Python versions (3.11)
- Allows full pip functionality (requirements files, upgrades, etc.)

### Why JSON-RPC?
- Standard protocol with good library support
- Clean separation between transport and application logic
- Supports batching and async operations
- Easy to debug and extend

## Project Dependencies

### Core Runtime
- Python 3.11+ (must match Cascadeur's version for binary compatibility)
- jsonrpc, aiohttp, requests: RPC and HTTP communication
- pydantic: Data validation and serialization
- loguru: Structured logging

### Development
- pytest: Testing framework
- black, isort, ruff: Code formatting and linting
- mypy: Static type checking
- pixi: Cross-platform package management (conda + PyPI)

## Important Reminders

### Code Style and Type Safety
- **Always write strongly typed Python code** - Use type hints for all function parameters and return values
- **Validate with mypy strict mode** - Run `pixi run -e dev mypy <file> --strict` after making changes
- **Use absolute imports** - Prefer `from cascadeur_py_client.server import ...` over relative imports
- **Handle exceptions properly** - Never use bare `except:`, always specify exception types

### Testing JSON-RPC Servers
```bash
# Start a server (choose one)
pixi run -e dev python src/cascadeur_py_client/server/jsonrpc_pipe_server.py       # Threaded version
pixi run -e dev python src/cascadeur_py_client/server/jsonrpc_pipe_server_sync.py  # Sync version

# Test with client
pixi run -e dev python src/cascadeur_py_client/server/jsonrpc_pipe_client.py --interactive

# Use custom pipe name via environment
set CASCADEUR_PYTHON_RPC_PIPE_NAME=my-pipe  # Windows
export CASCADEUR_PYTHON_RPC_PIPE_NAME=my-pipe  # Linux/macOS
```

### Temporary Files
- Place all temporary scripts and test files in the `tmp/` directory
- Never commit files from `tmp/` directory - it's gitignored
- Use `tmp/` for experimental code before integrating into main source