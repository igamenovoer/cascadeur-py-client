[CLEAN]

# csc.Guid

**Module:** `csc.Guid`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.Guid.html)

## Overview

The `Guid` class represents a globally unique identifier (GUID) in the Cascadeur system. It provides functionality for creating, manipulating, and working with unique identifiers.

## Class Definition

```python
class csc.Guid
```

The Guid class encapsulates a unique identifier and provides methods for GUID operations.

## Constructor

The constructor is overloaded to support different initialization methods:

### `__init__(self, arg0: str) -> None`

Creates a new Guid from a string representation.

**Parameters:**
- `arg0` (str): String representation of the GUID

**Returns:**
- None

### `__init__(self) -> None`

Creates a new empty/null Guid instance.

**Returns:**
- None

## Methods

### `is_null(self) -> bool`

Checks if the GUID is null or empty.

**Returns:**
- bool: True if the GUID is null, False otherwise

### `null() -> csc.Guid` (static)

Creates and returns a null GUID instance.

**Returns:**
- csc.Guid: A null GUID instance

### `to_string(self) -> str`

Converts the GUID to its string representation.

**Returns:**
- str: String representation of the GUID

## Usage Example

```python
import csc

# Create a null GUID
null_guid = csc.Guid()

# Create a GUID from string
guid_str = "550e8400-e29b-41d4-a716-446655440000"
guid = csc.Guid(guid_str)

# Check if GUID is null
if guid.is_null():
    print("GUID is null")

# Get string representation
guid_string = guid.to_string()

# Create a null GUID using static method
null_guid_static = csc.Guid.null()
```

## Usage Notes

- The constructor supports both string initialization and default (null) initialization
- Use `is_null()` to check if a GUID is empty or uninitialized
- The `null()` static method provides a convenient way to create null GUIDs
- String format follows standard GUID/UUID formatting conventions

## See Also

- Standard UUID documentation for GUID format specifications
- Other Cascadeur identifier classes