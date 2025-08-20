# Contributing to Cascadeur Python Client

Thank you for your interest in contributing to the Cascadeur Python Client! This document provides guidelines and information for contributors.

## Development Setup

1. Fork the repository
2. Clone your fork:
   `ash
   git clone https://github.com/yourusername/cascadeur-py-client.git
   cd cascadeur-py-client
   `

3. Create a virtual environment:
   `ash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   `

4. Install the package in development mode:
   `ash
   pip install -e ".[dev]"
   `

## Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

Run all checks:
`ash
black src tests examples
isort src tests examples
flake8 src tests examples
mypy src
`

## Testing

Run tests with pytest:
`ash
pytest
`

For coverage report:
`ash
pytest --cov=cascadeur_client --cov-report=html
`

## Documentation

Documentation is built with Sphinx. To build docs locally:
`ash
cd docs
make html
`

## Submitting Changes

1. Create a new branch for your feature:
   `ash
   git checkout -b feature/your-feature-name
   `

2. Make your changes and commit:
   `ash
   git add .
   git commit -m "Add your descriptive commit message"
   `

3. Push to your fork:
   `ash
   git push origin feature/your-feature-name
   `

4. Create a Pull Request

## Pull Request Guidelines

- Include a clear description of the changes
- Add tests for new functionality
- Update documentation if needed
- Ensure all checks pass
- Keep changes focused and atomic

## Issues and Bug Reports

When reporting bugs, please include:
- Python version
- Cascadeur version
- Operating system
- Steps to reproduce
- Error messages and stack traces

Thank you for contributing!
