# Installing cascadeur-py-client to Cascadeur

The enhanced `pip_for_cascadeur.py` script now supports installing local packages (including this project) into Cascadeur's embedded Python environment.

## Features

The script now mimics pip's interface and supports:
- Installing local packages with `install .` or `install /path/to/project`
- Editable/development installations with `-e` flag
- PyPI packages with `install package-name`
- Requirements files with `-r requirements.txt`
- Uninstalling packages (including editable installs)

## Prerequisites

1. Ensure you have the `cas-installer` environment active (Python 3.11 for binary compatibility):
```bash
pixi shell -e cas-installer
```

2. Set the `CASCADEUR_PATH` environment variable to your Cascadeur installation, or the script will try to auto-detect it:
```bash
# Windows example
set CASCADEUR_PATH=C:\Users\%USERNAME%\AppData\Local\Cascadeur

# Or let the script auto-detect
```

## Usage Examples

### Install the cascadeur-py-client project

#### Editable Installation (Development Mode)
This creates a `.pth` file linking to your development directory:
```bash
python scripts/pip_for_cascadeur.py install -e .
```

#### Regular Installation
This copies the package files to Cascadeur's site-packages:
```bash
python scripts/pip_for_cascadeur.py install .
```

### Install from a specific path
```bash
python scripts/pip_for_cascadeur.py install /path/to/another/project
python scripts/pip_for_cascadeur.py install -e /path/to/another/project
```

### Install PyPI packages
```bash
python scripts/pip_for_cascadeur.py install requests numpy==1.24.0
```

### Install from requirements file
```bash
python scripts/pip_for_cascadeur.py install -r requirements-cascadeur.txt
```

### List installed packages
```bash
# Basic list
python scripts/pip_for_cascadeur.py list

# Detailed with site-packages info
python scripts/pip_for_cascadeur.py list --verbose

# Freeze format (for requirements.txt)
python scripts/pip_for_cascadeur.py list --format freeze

# JSON format
python scripts/pip_for_cascadeur.py list --format json
```

### Uninstall packages
```bash
# Uninstall with confirmation
python scripts/pip_for_cascadeur.py uninstall cascadeur-py-client

# Uninstall without confirmation
python scripts/pip_for_cascadeur.py uninstall -y cascadeur-py-client
```

## How It Works

### Regular Installation
For regular installations, the script uses `pip install --target` to install packages directly into Cascadeur's site-packages directory.

### Editable Installation
For editable installations (with `-e`), the script:
1. Installs dependencies using pip
2. Creates a `.pth` file in Cascadeur's site-packages
3. The `.pth` file contains the path to your project's source directory
4. This allows Cascadeur to import your package without copying files

### Site-packages Locations
The script looks for Cascadeur's site-packages in:
- `{CASCADEUR_PATH}/Lib/site-packages` (sysconfig location)
- `{CASCADEUR_PATH}/python/Lib/site-packages` (sys.path location)

## Troubleshooting

### Cannot find Cascadeur
Set the `CASCADEUR_PATH` environment variable:
```bash
set CASCADEUR_PATH=C:\Path\To\Cascadeur
```

### Import errors after installation
Ensure you're using Python 3.11 (matching Cascadeur's version):
```bash
pixi shell -e cas-installer
python --version  # Should show Python 3.11.x
```

### Dependencies not installing
The script attempts to install dependencies automatically. If this fails, install them manually:
```bash
python scripts/pip_for_cascadeur.py install pydantic aiohttp jsonrpc
```

## Complete Installation Example

```bash
# 1. Activate the correct Python environment
pixi shell -e cas-installer

# 2. Install the project in editable mode
python scripts/pip_for_cascadeur.py install -e .

# 3. Verify installation
python scripts/pip_for_cascadeur.py list

# 4. Test in Cascadeur
# Open Cascadeur and in a Python script:
# from cascadeur_py_client.server import caslogger
# logger = caslogger.logger
# logger.info("It works!")
```

## Notes

- The script maintains compatibility with the original pip-like interface
- Editable installs are perfect for development - changes to your code are immediately reflected in Cascadeur
- Regular installs are better for production deployment
- The script handles both Windows and Unix-like systems
- Type hints are fully implemented (mypy compliant)