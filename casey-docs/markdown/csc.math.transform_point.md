[CLEAN]

# csc.math.transform_point

**Module:** `csc.math.transform_point`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.math.transform_point.html)

## Overview

The `transform_point` function applies a transformation to a 3D point. This overloaded function supports transformations using either an OrthogonalTransform object or a 4x4 transformation matrix, providing flexibility for different transformation workflows.

## Function Definition

```python
def transform_point(*args, **kwargs) -> numpy.ndarray[numpy.float32[3, 1]]
```

Overloaded function for transforming 3D points using different transformation representations.

## Overloaded Signatures

### `transform_point(transform: csc.math.OrthogonalTransform, point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]`

Transforms a 3D point using an OrthogonalTransform object.

**Parameters:**
- `transform` (csc.math.OrthogonalTransform): The orthogonal transformation to apply
- `point` (numpy.ndarray[numpy.float32[3, 1]]): The 3D point to transform (Vector3f)

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]]: The transformed 3D point (Vector3f)

### `transform_point(matrix: numpy.ndarray[numpy.float32[4, 4]], point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]`

Transforms a 3D point using a 4x4 transformation matrix.

**Parameters:**
- `matrix` (numpy.ndarray[numpy.float32[4, 4]]): The 4x4 transformation matrix
- `point` (numpy.ndarray[numpy.float32[3, 1]]): The 3D point to transform (Vector3f)

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]]: The transformed 3D point (Vector3f)

## Usage Example

```python
import csc.math
import numpy as np

# Create a 3D point
point = np.array([[1.0], [2.0], [3.0]], dtype=np.float32)

# Method 1: Transform using OrthogonalTransform
# First create an orthogonal transform (example)
triangle = csc.math.Triangle(
    np.array([0.0, 0.0, 0.0], dtype=np.float32),
    np.array([1.0, 0.0, 0.0], dtype=np.float32),
    np.array([0.0, 1.0, 0.0], dtype=np.float32)
)
orthogonal_transform = csc.math.basic_transform_from_triangle(triangle)

# Apply the transformation
transformed_point1 = csc.math.transform_point(orthogonal_transform, point)

# Method 2: Transform using 4x4 matrix
# Create a 4x4 transformation matrix (example: translation)
transformation_matrix = np.array([
    [1.0, 0.0, 0.0, 5.0],  # Translate by 5 units in X
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
], dtype=np.float32)

# Apply the matrix transformation
transformed_point2 = csc.math.transform_point(transformation_matrix, point)

print(f"Original point: {point.flatten()}")
print(f"Transformed with OrthogonalTransform: {transformed_point1.flatten()}")
print(f"Transformed with matrix: {transformed_point2.flatten()}")

# Can be used in transformation chains
point_chain = point
for i in range(3):
    point_chain = csc.math.transform_point(transformation_matrix, point_chain)
    print(f"Step {i+1}: {point_chain.flatten()}")
```

## Usage Notes

- The function is overloaded to accept either OrthogonalTransform objects or 4x4 matrices
- All points should be provided as numpy arrays with shape [3, 1] and float32 dtype
- Transformation matrices should be 4x4 with float32 dtype for homogeneous coordinates
- OrthogonalTransform preserves angles and lengths (rotation + translation)
- Matrix transformation allows for more general transformations including scaling and shearing
- The function returns transformed points in the same format as input (Vector3f)

## See Also

- `csc.math.inverse_transform_point()` - Inverse point transformation
- `csc.math.OrthogonalTransform` - Orthogonal transformation class
- `csc.math.basic_transform_from_triangle()` - Create transform from triangle
- `csc.math.modify_position_by_matrix()` - Alternative matrix transformation
- `numpy` - Required for vector and matrix operations