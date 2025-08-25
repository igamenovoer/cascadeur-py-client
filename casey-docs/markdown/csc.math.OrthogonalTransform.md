[CLEAN]

# csc.math.OrthogonalTransform

## Overview
OrthogonalTransform represents a transform defined by a position and a rotation. It provides get/set accessors for both components and can be constructed with defaults or with explicit values. The detailed behavior and defaults are not documented in the source snippet. Use this class where an orthogonal (rotation + translation) transform is required.

## Class Definition
```python
class csc.math.OrthogonalTransform:
    ...
```

## Constructor

### `__init__(self) -> None`
Constructs an OrthogonalTransform with default position and rotation (defaults are undocumented).

Returns:
- None

### `__init__(self, position: numpy.ndarray[numpy.float32[3, 1]], rotate: csc.math.Quaternion) -> None`
Constructs an OrthogonalTransform with the specified position and rotation.

Parameters:
- position: numpy.ndarray[numpy.float32[3, 1]] – Position vector (undocumented)
- rotate: csc.math.Quaternion – Rotation (undocumented)

Returns:
- None

## Attributes
- position: Vector3f – Get/set (undocumented)
- rotation: Rotation – Get/set (undocumented)

## Usage Notes
- Behavior of default-constructed instances (exact values) is undocumented.
- No additional methods beyond constructors and attributes are documented here.

