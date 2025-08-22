[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:42 | Original: fdd5ce6d -->

# csc.tools.attractor.GSRotationAxis

**Module:** `csc.tools.attractor.GSRotationAxis`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.GSRotationAxis.html)

## Overview

Enumeration representing general rotation axis options: X, Y, Z, Whole, and Empty. This enum is part of GeneralSettings and is used to specify rotation axis behavior in tools and attractors.

## Class Definition

```python
class csc.tools.attractor.GSRotationAxis
```

GeneralSettings::RotationAxis enum with members X, Y, Z, Whole, and Empty.

## Constructor

### `__init__(self, value) -> None`

Initializes the enum with a specific value corresponding to one of the defined members.

**Parameters:**
- `value` (Any): Enum value corresponding to one of the members X, Y, Z, Whole, or Empty.

**Returns:**
- None

## Methods

No additional methods are documented beyond the enum constructor.

## Attributes

- `X`: Enum member representing the X rotation axis.
- `Y`: Enum member representing the Y rotation axis.
- `Z`: Enum member representing the Z rotation axis.
- `Whole`: Enum member representing the whole rotation (all axes).
- `Empty`: Enum member representing an empty or unspecified rotation axis.
- `name`: The name of the enum member.
- `value`: The value of the enum member.

## Usage Example

```python
from csc.tools.attractor import GSRotationAxis

# Practical usage example
axis = GSRotationAxis(GSRotationAxis.X.value)
if axis == GSRotationAxis.X:
    print("Using X rotation axis")
```

## Usage Notes

- Use the predefined members (X, Y, Z, Whole, Empty) to specify the desired rotation axis.
- When storing or comparing values, prefer comparing to the enum members rather than raw values.
- The `name` and `value` attributes are available for introspection and serialization purposes.

## See Also

- Other GeneralSettings enums and related attractor tool configurations