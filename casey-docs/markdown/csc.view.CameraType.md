[CLEAN]

# csc.view.CameraType

## Overview
CameraType is an enumeration in the csc.view module that represents the camera projection mode used in Cascadeur's viewport. It provides two values: ISOMETRIC and PERSPECTIVE. Use it to indicate or query which projection mode is active where supported.

## Class Definition
```python
class CameraType
```

## Constructor

### __init__(self, value)
Initializes an enumeration member.

**Parameters:**
- value: undocumented – input used to select the enumeration member

**Returns:**
- undocumented

## Attributes
- `ISOMETRIC` – enumeration member; undocumented
- `PERSPECTIVE` – enumeration member; undocumented
- `name` – standard enum attribute; undocumented
- `value` – standard enum attribute; undocumented

## Usage Notes
- Compare values using the enum members directly.
- Typical usage selects one of the provided members.

```python
from csc.view import CameraType

mode = CameraType.PERSPECTIVE

if mode is CameraType.ISOMETRIC:
    # handle isometric-specific logic
    pass
```

