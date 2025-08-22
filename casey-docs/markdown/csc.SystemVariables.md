[CLEAN]

# csc.SystemVariables

**Module:** `csc.SystemVariables`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.SystemVariables.html)

## Overview

The `SystemVariables` class provides access to system and version information about the Cascadeur application. It offers static methods to retrieve Git-related version data and system metadata.

## Class Definition

```python
class csc.SystemVariables
```

This class serves as a utility to access build and version information from the Cascadeur system.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a SystemVariables instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Static Methods

### `git_count() -> str`

Returns the Git commit count for the current build.

**Returns:**
- str: The number of Git commits in the build's history

### `git_date() -> str`

Returns the date of the Git commit used for the current build.

**Returns:**
- str: The commit date in string format

### `git_sha() -> str`

Returns the Git SHA hash of the commit used for the current build.

**Returns:**
- str: The Git commit SHA hash

### `git_version() -> str`

Returns the Git version string for the current build.

**Returns:**
- str: The Git version information

## Usage Example

```python
import csc

# Create SystemVariables instance
sys_vars = csc.SystemVariables()

# Get Git information
commit_count = csc.SystemVariables.git_count()
commit_date = csc.SystemVariables.git_date()
commit_sha = csc.SystemVariables.git_sha()
git_version = csc.SystemVariables.git_version()

print(f"Build Information:")
print(f"Git Count: {commit_count}")
print(f"Git Date: {commit_date}")
print(f"Git SHA: {commit_sha}")
print(f"Git Version: {git_version}")

# Use for version checking or debugging
def get_build_info():
    return {
        'count': csc.SystemVariables.git_count(),
        'date': csc.SystemVariables.git_date(),
        'sha': csc.SystemVariables.git_sha(),
        'version': csc.SystemVariables.git_version()
    }

build_info = get_build_info()
```

## Usage Notes

- All version information methods are static and can be called without instantiating the class
- Useful for debugging, logging, and version verification
- Git information reflects the build used to compile the Cascadeur Python API
- The returned values are strings and may need parsing for specific use cases

## See Also

- `csc.Version` - Version class for semantic versioning
- System logging and debugging utilities in Cascadeur