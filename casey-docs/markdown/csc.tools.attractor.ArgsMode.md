[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:40 | Original: d8deee93 -->

# csc.tools.attractor.ArgsMode

**Module:** `csc.tools.attractor.ArgsMode`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.ArgsMode.html)

## Overview

Enum representing attractor modes: Previous, Next, Inertial, InverseInertial, Average, and Interpolation.

## Class Definition

```python
class csc.tools.attractor.ArgsMode
```

Enumeration of attractor modes.

## Constructor

### `__init__(value) -> None`

Initializes the enum with a specific value.

**Parameters:**
- `value` (Any): Enum value to initialize the instance.

**Returns:**
- None

## Methods

No additional methods documented beyond standard enum behavior.

## Attributes

- `Previous`
- `Next`
- `Inertial`
- `InverseInertial`
- `Average`
- `Interpolation`
- `name`
- `value`

## Usage Example

```python
from csc.tools.attractor import ArgsMode

# Practical usage example
mode = ArgsMode.Previous
print(mode.name, mode.value)
```

## Usage Notes

- Use the provided enum members to specify attractor modes.
- `name` returns the enum member name; `value` returns its underlying value.

## See Also

- Other attractor-related tools and enums in `csc.tools.attractor`