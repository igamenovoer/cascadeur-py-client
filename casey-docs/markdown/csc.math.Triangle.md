[CLEAN]

# csc.math.Triangle

**Module:** `csc.math.Triangle`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.math.Triangle.html)

## Overview

The `Triangle` class represents a triangle structure composed of three 3D points. This class provides functionality for working with triangular geometry in 3D space, commonly used in mesh processing and geometric calculations.

## Class Definition

```python
class csc.math.Triangle
```

Structure from three points that represents a triangle in 3D space.

## Constructor

### `__init__(self, point1: Vector3f, point2: Vector3f, point3: Vector3f) -> None`

Creates a new Triangle instance from three 3D points.

**Parameters:**
- `point1` (Vector3f): The first vertex of the triangle
- `point2` (Vector3f): The second vertex of the triangle  
- `point3` (Vector3f): The third vertex of the triangle

**Returns:**
- None

## Attributes

### `point1` (Vector3f)

The first vertex of the triangle. This attribute supports both get and set operations.

**Type:** Vector3f (3D vector with float components)

### `point2` (Vector3f)

The second vertex of the triangle. This attribute supports both get and set operations.

**Type:** Vector3f (3D vector with float components)

### `point3` (Vector3f)

The third vertex of the triangle. This attribute supports both get and set operations.

**Type:** Vector3f (3D vector with float components)

## Usage Example

```python
import csc.math
import numpy as np

# Create triangle vertices as 3D vectors
p1 = np.array([0.0, 0.0, 0.0], dtype=np.float32)  # Origin
p2 = np.array([1.0, 0.0, 0.0], dtype=np.float32)  # Along X-axis
p3 = np.array([0.0, 1.0, 0.0], dtype=np.float32)  # Along Y-axis

# Create a triangle
triangle = csc.math.Triangle(p1, p2, p3)

# Access triangle vertices
vertex1 = triangle.point1
vertex2 = triangle.point2
vertex3 = triangle.point3

print(f"Triangle vertices:")
print(f"Point 1: {vertex1}")
print(f"Point 2: {vertex2}")
print(f"Point 3: {vertex3}")

# Modify triangle vertices
triangle.point1 = np.array([0.5, 0.0, 0.0], dtype=np.float32)
triangle.point2 = np.array([1.5, 0.0, 0.0], dtype=np.float32)
triangle.point3 = np.array([0.5, 1.5, 0.0], dtype=np.float32)

# Triangle can be used with other geometry functions
# For example, with basic_transform_from_triangle
transform = csc.math.basic_transform_from_triangle(triangle)
```

## Usage Notes

- All three points should be Vector3f (3D float vectors) 
- Points define vertices in 3D space forming a triangle
- All attributes (point1, point2, point3) support both read and write operations
- Triangles are commonly used in mesh processing and geometric calculations
- The order of points may affect calculations that depend on triangle orientation
- Can be used with other `csc.math` functions for geometric transformations

## See Also

- `csc.math.basic_transform_from_triangle()` - Function to create transform from triangle
- `csc.domain.assets.Triangle` - Asset-related triangle class
- `Vector3f` - 3D vector representation
- Mesh processing and geometric calculation utilities in Cascadeur