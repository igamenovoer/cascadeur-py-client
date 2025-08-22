[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:42 | Original: 6e2e4630 -->

# csc.tools.attractor.GSPhysicsType

**Module:** `csc.tools.attractor.GSPhysicsType`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.GSPhysicsType.html)

## Overview

GeneralSettings::RotationAxis enum with members FrameRelax and InterpolationRelax.

## Class Definition

```python
class csc.tools.attractor.GSPhysicsType
```

Enumeration representing physics types: FrameRelax and InterpolationRelax.

## Constructor

### `__init__(self, value) -> None`

Constructs an enum member with the given value.

**Parameters:**
- `value` (unknown): Enum value corresponding to a member.

**Returns:**
- None

## Methods

No additional methods documented beyond the enum constructor.

## Attributes

- `FrameRelax`: Enum member.
- `InterpolationRelax`: Enum member.
- `name`: The name of the enum member.
- `value`: The value of the enum member.

## Usage Example

```python
import csc.tools.attractor.GSPhysicsType as GSPhysicsType

# Practical usage example
mode = GSPhysicsType.FrameRelax
print(mode.name, mode.value)
```

## Usage Notes

- Use FrameRelax or InterpolationRelax to specify the desired physics type.
- Access enum metadata via the name and value attributes.

## See Also

- Other GeneralSettings-related enums and tools within csc.tools.attractor