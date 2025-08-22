[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:41 | Original: 3aeaa63f -->

# csc.tools.attractor.GSAxisFlag

**Module:** `csc.tools.attractor.GSAxisFlag`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.GSAxisFlag.html)

## Overview

Enumeration representing GeneralSettings::RotationAxis with possible values for rotation axis selection.

## Class Definition

```python
class csc.tools.attractor.GSAxisFlag
```

Enumeration of rotation axes.

## Constructor

### `__init__(value) -> None`

Initializes the enumeration with a specific value.

**Parameters:**
- `value` (Any): Enum value corresponding to one of the defined members.

**Returns:**
- None

## Methods

No additional methods are documented for this enumeration.

## Attributes

Enumeration members:
- `X`
- `Y`
- `Z`
- `XYZ`
- `Empty`

Standard enum attributes:
- `name`
- `value`

## Usage Example

```python
import csc.tools.attractor

# Practical usage example
axis = csc.tools.attractor.GSAxisFlag.X
print(axis.name, axis.value)
```

## Usage Notes

- Use these enum members to specify rotation axis settings.
- Access the selected member's name via `.name` and its underlying value via `.value`.

## See Also

- Related classes and modules in csc.tools.attractor