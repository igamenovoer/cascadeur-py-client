[CLEAN]

# csc.math.inverse_transform_point

## Overview
Applies the inverse of an orthogonal transform to a 3D point. This is typically used to convert a point from world (or parent) space into the local space defined by the transform. The function works with 32-bit floating-point vector data.

## Function Definition
```python
def inverse_transform_point(transform: OrthogonalTransform, point: numpy.ndarray) -> numpy.ndarray
```

**Parameters:**
- transform: OrthogonalTransform – undocumented
- point: numpy.ndarray (float32, 3D vector) – 3D point to transform

**Returns:**
- numpy.ndarray (float32, 3D vector): transformed point (Vector3f)

## Usage Notes
- Intended for inverse spatial conversion (e.g., world-to-local) relative to the provided transform.
- Specific construction details of OrthogonalTransform and edge-case behavior are undocumented.

