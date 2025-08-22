[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:42 | Original: 66376418 -->

# csc.tools.attractor.SpaceMode

**Module:** `csc.tools.attractor.SpaceMode`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.SpaceMode.html)

## Overview

Enumeration representing the attractor mode space, with possible values for global and local modes.

## Class Definition

```python
class csc.tools.attractor.SpaceMode
```

Enum defining attractor modes: Global and Local.

## Constructor

### `__init__(self, value) -> None`

Initialize the enum with a specified value.

**Parameters:**
- `value` (Any): Enum value corresponding to one of the defined members.

**Returns:**
- None

## Methods

No additional methods are documented beyond standard enum behavior.

## Attributes

- `Global`: Enum member representing the global attractor mode.
- `Local`: Enum member representing the local attractor mode.
- `name`: The name of the enum member.
- `value`: The value of the enum member.

## Usage Example

```python
from csc.tools.attractor import SpaceMode

# Practical usage example
mode = SpaceMode.Global
print(mode.name)   # "Global"
print(mode.value)  # Underlying value associated with Global
```

## Usage Notes

- Use `SpaceMode.Global` for operations in global space.
- Use `SpaceMode.Local` for operations in local space.
- Standard Enum attributes `name` and `value` are available.

## See Also

- Other attractor-related classes and enums in `csc.tools.attractor`