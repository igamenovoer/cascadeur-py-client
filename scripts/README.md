# Cascadeur Package Management

This directory contains scripts for managing Python packages in Cascadeur's embedded Python environment.

## Problem

Cascadeur uses an embedded Python interpreter (no `python.exe`), making it impossible to use pip directly. The Python environment is:
- **Isolated**: Ignores environment variables (`ignore_environment: 1`)
- **Restricted**: No stdin/stdout/stderr for console I/O
- **Embedded**: Runs through `cascadeur.exe`, not a standalone Python

## Solution

We use an external Python environment (`cas-installer`) with matching Python version (3.11) to install packages into Cascadeur's site-packages directory.

## Setup

1. **Create the installer environment:**
```bash
pixi install --environment cas-installer
```

2. **Set Cascadeur path (optional):**
```bash
# Windows
set CASCADEUR_PATH=C:\Users\%USERNAME%\AppData\Local\Cascadeur

# Or specify in each command
python scripts/install_to_cascadeur.py --cascadeur-path "C:\path\to\cascadeur" ...
```

## Usage

### Activate the installer environment
```bash
pixi shell -e cas-installer
```

### Install packages
```bash
# Install a single package
python scripts/install_to_cascadeur.py requests

# Install specific version
python scripts/install_to_cascadeur.py "numpy==1.24.0"

# Install multiple packages
python scripts/install_to_cascadeur.py requests aiohttp pydantic

# Install from requirements file
python scripts/install_to_cascadeur.py -r requirements-cascadeur.txt

# Upgrade existing packages
python scripts/install_to_cascadeur.py --upgrade requests

# Install without dependencies
python scripts/install_to_cascadeur.py --no-deps mypackage
```

### List installed packages
```bash
# Table format (default)
python scripts/list_cascadeur_packages.py

# pip freeze format
python scripts/list_cascadeur_packages.py --format freeze

# JSON format
python scripts/list_cascadeur_packages.py --format json
```

### Using pixi tasks (shorthand)
```bash
# From cas-installer environment
pixi run -e cas-installer cas-install requests
pixi run -e cas-installer cas-list
```

## Important Notes

### Binary Compatibility
- The `cas-installer` environment uses Python 3.11 to match Cascadeur's version
- Binary wheels (.pyd files on Windows) must be compatible with Python 3.11
- Pure Python packages are generally safe to install

### Package Limitations
Some packages may not work in Cascadeur's restricted environment:
- Packages requiring console I/O won't work (no stdin/stdout)
- Packages depending on environment variables may fail
- GUI packages (tkinter, PyQt, etc.) likely won't work

### Tested Packages
Known to work:
- `requests` - HTTP library
- `aiohttp` - Async HTTP client/server
- `pydantic` - Data validation
- `jsonrpc` - JSON-RPC implementation

### Site-packages Locations
Cascadeur may have multiple site-packages directories:
- `%LOCALAPPDATA%\Cascadeur\Lib\site-packages`
- `%LOCALAPPDATA%\Cascadeur\python\Lib\site-packages`

The scripts automatically detect and use the appropriate location.

## Troubleshooting

### Cascadeur not found
Set the `CASCADEUR_PATH` environment variable or use `--cascadeur-path` argument.

### Permission errors
Run with administrator privileges if installing to Program Files location.

### Import errors in Cascadeur
- Check Python version compatibility (must be 3.11)
- Verify all dependencies are installed (`--no-deps` skips them)
- Some packages may be incompatible with Cascadeur's restricted environment

### Finding Cascadeur's Python info
Run the inspection script inside Cascadeur:
```python
# In Cascadeur's script editor
exec(open(r"D:\path\to\cascadeur_python_info.py").read())
```

Then check the output file in temp directory or specified location.