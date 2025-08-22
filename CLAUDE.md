# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Development Commands

### Installation
```bash
# Install package in development mode with all dependencies
pip install -e ".[dev]"

# Or using pixi (project uses pixi for environment management)
pixi install
```

### Code Quality
```bash
# Format code
black src tests examples

# Sort imports
isort src tests examples

# Lint code
flake8 src tests examples

# Type checking
mypy src
```

### Testing
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=cascadeur_client --cov-report=term-missing

# Run specific test file
pytest tests/test_client.py
```

### Documentation Building
```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build HTML documentation
cd docs && make html
```

## Architecture Overview

This is a Python client library for interfacing with Cascadeur animation software. The project consists of:

### Core Client Architecture
- **CascadeurClient** (`src/cascadeur_client/client.py`): Main entry point that manages connections to Cascadeur and provides high-level scene operations
- **Scene** (`src/cascadeur_client/scene.py`): Represents a Cascadeur scene with methods for manipulating joints, frames, and animation data
- **Animation/Rig** modules: Provide specialized functionality for animation curves and character rigs

### Server Components
The `src/cascadeur_client/server/` directory contains multiple JSON-RPC server implementations designed to run inside Cascadeur's Python environment:
- **health_exec_server_aio.py**: Async (aiohttp) server with non-blocking execution
- **health_exec_server_threaded.py**: Thread-based server for concurrent handling
- **health_exec_server.py**: Basic synchronous implementation
- All servers expose `health` and `exec_b64` methods for remote code execution in Cascadeur

### Key Design Patterns
- Client-Server architecture where the Python client communicates with a server running inside Cascadeur
- Base64 encoding for code transmission to avoid JSON escaping issues
- Multiple server implementations (async, threaded, sync) for different deployment scenarios
- Placeholder implementations currently exist as the actual Cascadeur API integration is in development

## Package Structure
- Python 3.7+ compatible with type hints
- Uses setuptools for packaging with pyproject.toml configuration
- Optional pixi environment management for Windows development
- Follows standard Python package layout with src/ directory

## Context Directory
The `context/` directory contains comprehensive project documentation, development history, and AI collaboration materials. Key areas include:
- `design/` - Architecture specifications and technical designs
- `hints/` - How-to guides and troubleshooting tips
- `plans/` - Development roadmaps and implementation strategies
- `summaries/` - Project analysis and knowledge consolidation
- `tasks/` - Current and planned work items organized by type

See `context/README.md` for detailed information about the project's knowledge base.