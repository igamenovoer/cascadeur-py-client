[CLEAN]

# csc.math.Rotation

**Module:** `csc.math.Rotation`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html)

## Overview

The `Rotation` class represents a 3D rotation using Euler angles implementation. This class provides methods for creating rotations from various representations (angle-axis, Euler angles, quaternions, rotation matrices) and converting between different rotation formats commonly used in 3D graphics and animation.

## Class Definition

```python
class csc.math.Rotation
```

The Rotation class encapsulates rotation operations and provides conversion methods between different rotation representations.

## Constructor

### `__init__(self) -> None`

Creates a new Rotation instance (likely identity rotation by default).

**Returns:**
- None

## Static Factory Methods

### `from_angle_axis(*args, **kwargs) -> csc.math.Rotation`

Creates a rotation from an angle and rotation axis. This method has multiple overloaded signatures:

**Overloaded signatures:**
1. `from_angle_axis(angle: float, axis: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation`
2. `from_angle_axis(angle_axis: csc.math.AngleAxis) -> csc.math.Rotation`

**Parameters:**
- `angle` (float): The rotation angle in radians
- `axis` (numpy.ndarray): The rotation axis as a 3D vector
- `angle_axis` (csc.math.AngleAxis): An AngleAxis object containing both angle and axis

**Returns:**
- csc.math.Rotation: A new Rotation instance from the angle-axis representation

### `from_euler(*args, **kwargs) -> csc.math.Rotation`

Creates a rotation from Euler angles. This method has multiple overloaded signatures:

**Overloaded signatures:**
1. `from_euler(x: float, y: float, z: float) -> csc.math.Rotation`
2. `from_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation`

**Parameters:**
- `x` (float): Rotation around X-axis in radians
- `y` (float): Rotation around Y-axis in radians
- `z` (float): Rotation around Z-axis in radians
- `vec3f` (numpy.ndarray): 3D vector containing X, Y, Z Euler angles

**Returns:**
- csc.math.Rotation: A new Rotation instance from Euler angles

### `from_quaternion(*args, **kwargs) -> csc.math.Rotation`

Creates a rotation from a quaternion. This method has multiple overloaded signatures:

**Overloaded signatures:**
1. `from_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation`
2. `from_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation`

**Parameters:**
- `w` (float): W (scalar) component of the quaternion
- `x` (float): X component of the quaternion
- `y` (float): Y component of the quaternion
- `z` (float): Z component of the quaternion
- `quaternion` (csc.math.Quaternion): A Quaternion object

**Returns:**
- csc.math.Rotation: A new Rotation instance from the quaternion

### `from_rotation_matrix(matrix: numpy.ndarray) -> csc.math.Rotation`

Creates a rotation from a rotation matrix.

**Parameters:**
- `matrix` (numpy.ndarray): The rotation matrix

**Returns:**
- csc.math.Rotation: A new Rotation instance from the matrix

## Conversion Methods

### `to_angle_axis(self) -> csc.math.AngleAxis`

Converts the rotation to angle-axis representation.

**Returns:**
- csc.math.AngleAxis: The rotation as an angle-axis object

### `to_euler_angles(self) -> numpy.ndarray`

Converts the rotation to Euler angles.

**Returns:**
- numpy.ndarray: 3D vector containing the Euler angles

### `to_euler_angles_x_y_z(self) -> numpy.ndarray`

Converts the rotation to Euler angles in X-Y-Z order.

**Returns:**
- numpy.ndarray: 3D vector containing X-Y-Z Euler angles

### `to_quaternion(self) -> csc.math.Quaternion`

Converts the rotation to a quaternion.

**Returns:**
- csc.math.Quaternion: The rotation as a quaternion

### `to_rotation_matrix(self) -> numpy.ndarray`

Converts the rotation to a rotation matrix.

**Returns:**
- numpy.ndarray: The rotation matrix

## Usage Example

```python
import csc.math
import numpy as np

# Create rotation from Euler angles
rotation = csc.math.Rotation.from_euler(0.5, 1.0, 0.2)  # X, Y, Z angles in radians

# Create rotation from vector of Euler angles
euler_vec = np.array([[0.5], [1.0], [0.2]], dtype=np.float32)
rotation = csc.math.Rotation.from_euler(euler_vec)

# Create rotation from quaternion components
rotation = csc.math.Rotation.from_quaternion(1.0, 0.0, 0.0, 0.0)  # Identity quaternion

# Create rotation from existing quaternion
quat = csc.math.Quaternion(1.0, 0.0, 0.0, 0.0)
rotation = csc.math.Rotation.from_quaternion(quat)

# Create rotation from angle-axis
axis = np.array([[0.0], [0.0], [1.0]], dtype=np.float32)  # Z-axis
rotation = csc.math.Rotation.from_angle_axis(np.pi / 4, axis)  # 45-degree rotation

# Convert to different representations
quaternion = rotation.to_quaternion()
euler_angles = rotation.to_euler_angles()
xyz_euler = rotation.to_euler_angles_x_y_z()
angle_axis = rotation.to_angle_axis()
matrix = rotation.to_rotation_matrix()

# Chain conversions
rotation1 = csc.math.Rotation.from_euler(0.1, 0.2, 0.3)
rotation2 = csc.math.Rotation.from_quaternion(rotation1.to_quaternion())
```

## Usage Notes

- The class uses Euler angles as its internal representation
- All angle parameters should be in radians
- Multiple factory methods allow creation from various rotation representations
- Conversion methods enable interoperability with different rotation formats
- Use appropriate conversion method based on your target format needs
- Euler angles are subject to gimbal lock in certain orientations

## See Also

- `csc.math.Quaternion` - Quaternion class for rotation operations
- `csc.math.AngleAxis` - Angle-axis rotation representation
- `numpy` - Required for vector and matrix operations
- 3D rotation mathematics and Euler angle documentation