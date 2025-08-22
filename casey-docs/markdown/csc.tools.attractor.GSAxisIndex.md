[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:42 | Original: 6e7dc405 -->

# csc.tools.attractor.GSAxisIndex

**Module:** `csc.tools.attractor.GSAxisIndex`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.GSAxisIndex.html)

## Overview

Enumeration representing GeneralSettings::RotationAxis with possible values X, Y, and Z.

## Class Definition

```python
class csc.tools.attractor.GSAxisIndex
```

Enumeration class for rotation axes.

## Constructor

### `__init__(self, value) -> None`

Initialize the enumeration with a specific value.

**Parameters:**
- `value` (Any): The value to initialize the enum member with.

**Returns:**
- None

## Methods

No additional methods are documented beyond those provided by the enumeration base (e.g., name, value).

## Usage Example

```python
import csc.tools.attractor.GSAxisIndex as GSAxisIndex

# Practical usage example
axis_x = GSAxisIndex.X
axis_y = GSAxisIndex.Y
axis_z = GSAxisIndex.Z

# Accessing enum attributes
name = axis_x.name
val = axis_x.value
```

## Usage Notes

- Available members: X, Y, Z.
- Enum members provide standard attributes:
  - name: the member name (e.g., "X").
  - value: the underlying value associated with the member.

## See Also

- Related classes and modules: GeneralSettings::RotationAxis enum