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
black src tests scripts examples

# Sort imports
isort src tests scripts examples

# Lint with flake8
flake8 src tests scripts examples

# Type checking
mypy src

# Or using ruff (faster alternative)
ruff check src tests scripts
ruff format src tests scripts
```

### Testing
```bash
# Run all automated tests
pytest tests/auto/

# Run with coverage report
pytest tests/auto/ --cov=cascadeur_client --cov-report=term-missing

# Run specific test file
pytest tests/auto/test_jsonrpc_pipe.py

# Run a single test
pytest tests/auto/test_jsonrpc_pipe.py::TestJSONRPCPipe::test_simple_echo
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

#### Server Components (`src/cascadeur_client/server/`)
- **jsonrpc_pipe_server.py**: Main server running inside Cascadeur, handles RPC requests
- **jsonrpc_pipe_server_simple.py**: Simplified server for testing and debugging
- **jsonrpc_pipe_client.py**: Client library for connecting to the server

#### Communication Protocol
- Uses Windows named pipes (`\\.\pipe\cascadeur_jsonrpc`)
- JSON-RPC 2.0 protocol with base64 encoding for code transmission
- Supports synchronous and asynchronous execution models
- Health check endpoint for connection verification

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