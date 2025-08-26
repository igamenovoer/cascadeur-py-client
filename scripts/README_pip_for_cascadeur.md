# Pip for Cascadeur

A pip-like package manager for Cascadeur's embedded Python environment.

## Background

Cascadeur uses an embedded Python (no standalone python.exe) that runs through cascadeur.exe. This tool allows you to manage Python packages in Cascadeur's site-packages directory using an external Python installation.

## Installation

Requires Python 3.7+ with pip installed. If using pixi:

```bash
pixi run -e cas-installer python scripts/pip_for_cascadeur.py [command]
```

## Usage

### List installed packages

```bash
# Default table format
python pip_for_cascadeur.py list

# pip freeze format
python pip_for_cascadeur.py list --format freeze

# JSON format
python pip_for_cascadeur.py list --format json

# Verbose (shows site-packages info)
python pip_for_cascadeur.py list -v
```

### Install packages

```bash
# Install a package
python pip_for_cascadeur.py install numpy

# Install multiple packages
python pip_for_cascadeur.py install numpy scipy pandas

# Install specific version
python pip_for_cascadeur.py install numpy==1.24.0

# Upgrade package
python pip_for_cascadeur.py install -U numpy

# Install from requirements file
python pip_for_cascadeur.py install -r requirements.txt

# Install without dependencies
python pip_for_cascadeur.py install --no-deps some-package

# Force reinstall
python pip_for_cascadeur.py install --force-reinstall numpy
```

### Uninstall packages

```bash
# Uninstall a package (will ask for confirmation)
python pip_for_cascadeur.py uninstall numpy

# Uninstall without confirmation
python pip_for_cascadeur.py uninstall -y numpy

# Uninstall multiple packages
python pip_for_cascadeur.py uninstall numpy scipy pandas
```

## Configuration

The tool automatically detects Cascadeur installation using:
1. `CASCADEUR_PATH` environment variable
2. Standard application paths via `platformdirs`
3. OS-specific default locations

To specify a custom Cascadeur path:

```bash
python pip_for_cascadeur.py --cascadeur-path /path/to/cascadeur list
```

## Site-packages Location

Cascadeur's site-packages are typically located at:
- Windows: `{cascadeur}/python/Lib/site-packages`
- Additional: `{cascadeur}/Lib/site-packages` (sysconfig location)

The tool automatically detects and uses the appropriate location.

## Examples

```bash
# Install common packages for animation work
python pip_for_cascadeur.py install numpy scipy matplotlib

# Check what's installed
python pip_for_cascadeur.py list

# Export installed packages to requirements
python pip_for_cascadeur.py list --format freeze > cascadeur_requirements.txt

# Reinstall from requirements on another machine
python pip_for_cascadeur.py install -r cascadeur_requirements.txt

# Upgrade all packages (example with common ones)
python pip_for_cascadeur.py install -U numpy scipy matplotlib

# Clean uninstall
python pip_for_cascadeur.py uninstall -y numpy scipy matplotlib
```