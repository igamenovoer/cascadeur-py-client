[CLEAN]

# csc.math.modify_position_by_matrix

## Overview
Utility function in the Cascadeur Python API for applying a 3×3 matrix to a 3D position vector. It returns a new position vector with the transformation applied. Specific behavior beyond performing the matrix operation is undocumented.

## Function Definition
```python
def modify_position_by_matrix(
    matrix: numpy.ndarray[numpy.float32[3, 3]],
    position: numpy.ndarray[numpy.float32[3, 1]]
) -> numpy.ndarray[numpy.float32[3, 1]]:
    ...
```

Transforms a 3D position vector by the given 3×3 matrix.

**Parameters:**
- matrix: numpy.ndarray[numpy.float32[3, 3]] – transformation matrix; exact semantics are undocumented.
- position: numpy.ndarray[numpy.float32[3, 1]] – input position vector; documented shape is 3×1 float32.

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]] – resulting position vector (documented as Vector3f).

## Usage Notes
- Input and output types are documented with numpy.float32 and fixed shapes (3×3 for matrix, 3×1 for vectors); other shapes or dtypes are undocumented.
- No further constraints (e.g., normalization, specific coordinate system) are documented.

