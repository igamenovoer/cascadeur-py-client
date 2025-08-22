[CLEAN]

# csc.Version

**Module:** `csc.Version`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.Version.html)

## Overview

The `Version` class represents version information in the Cascadeur system. It implements version handling with major, minor, and patch components following semantic versioning conventions.

## Class Definition

```python
class csc.Version
```

The Version class encapsulates version information and provides methods for version manipulation and string conversion.

## Constructor

### `__init__(self, major: int, minor: int, patch: int) -> None`

Creates a new Version instance with the specified version components.

**Parameters:**
- `major` (int): The major version number
- `minor` (int): The minor version number  
- `patch` (int): The patch version number

**Returns:**
- None

## Methods

### `from_string(arg0: str) -> csc.Version` (static)

Creates a Version instance from a string representation.

**Parameters:**
- `arg0` (str): String representation of the version (e.g., "1.2.3")

**Returns:**
- csc.Version: A new Version instance parsed from the string

### `to_string(self) -> str`

Converts the version to its string representation.

**Returns:**
- str: String representation of the version in "major.minor.patch" format

## Attributes

### `major` (int)

The major version number. This attribute supports both get and set operations.

### `minor` (int)

The minor version number. This attribute supports both get and set operations.

### `patch` (int)

The patch version number. This attribute supports both get and set operations.

## Usage Example

```python
import csc

# Create a version instance
version = csc.Version(1, 2, 3)

# Access version components
print(f"Major: {version.major}")
print(f"Minor: {version.minor}")
print(f"Patch: {version.patch}")

# Modify version components
version.major = 2
version.minor = 0
version.patch = 0

# Convert to string
version_str = version.to_string()  # "2.0.0"

# Create version from string
version_from_str = csc.Version.from_string("3.1.4")
```

## Usage Notes

- Follows semantic versioning (SemVer) conventions with major.minor.patch format
- All version components are integers
- Version attributes support both read and write operations
- String parsing and generation use standard "x.y.z" format
- Use `from_string()` static method to parse version strings

## See Also

- [Semantic Versioning Specification](https://semver.org/)
- Cascadeur application versioning