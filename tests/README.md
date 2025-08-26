# Test Directory Structure

## Overview

The test suite is organized into two main categories:

### `/auto` - Automated Tests
- Contains all pytest-based automated tests
- Runs in CI/CD pipelines
- Includes unit tests, integration tests, and regression tests
- Coverage reports generated from these tests

### `/manual` - Manual Testing Scripts  
- Contains CLI scripts for manual testing and debugging
- Interactive tools for inspecting specific functionality
- Performance benchmarking scripts
- Debugging utilities

## Running Tests

### Automated Tests
```bash
# Run all automated tests
pixi run -e dev pytest tests/auto/

# Run specific test file
pixi run -e dev pytest tests/auto/test_jsonrpc_pipe.py

# Run with coverage
pixi run -e dev pytest tests/auto/ --cov=cascadeur_client --cov-report=term-missing
```

### Manual Tests
```bash
# Example: Test IPC server manually
pixi run -e dev python tests/manual/test_ipc_server.py --port 5555 --verbose

# Example: Benchmark IPC performance
pixi run -e dev python tests/manual/benchmark_ipc.py --messages 10000
```

## Test Organization Guidelines

### Auto Tests (`/auto`)
- Follow pytest naming conventions: `test_*.py`
- Use fixtures for common setup/teardown
- Include proper type hints
- Must be deterministic and reproducible
- Should complete within reasonable time (<30s per test file)

### Manual Tests (`/manual`)
- Use descriptive script names
- Include CLI argument parsing with argparse
- Provide --help documentation
- Can be interactive or long-running
- Include verbose output options for debugging