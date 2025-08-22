[CLEAN]

# csc.math.Quaternion

**Module:** `csc.math.Quaternion`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html)

## Overview

The `Quaternion` class represents a quaternion for 3D rotation operations. This class provides methods for quaternion arithmetic and rotation calculations commonly used in 3D graphics and animation.

## Class Definition

```python
class csc.math.Quaternion
```

## Constructor

### `__init__(self, w: float, x: float, y: float, z: float) -> None`

Creates a new Quaternion instance with the specified components.

**Parameters:**
- `w` (float): The w (scalar) component of the quaternion
- `x` (float): The x component of the quaternion  
- `y` (float): The y component of the quaternion
- `z` (float): The z component of the quaternion

**Returns:**
- None

## Static Methods

### `from_two_vectors(arg0, arg1) -> csc.math.Quaternion`

Creates a quaternion representing the rotation from one vector to another.

**Parameters:**
- `arg0`: The first vector
- `arg1`: The second vector

**Returns:**
- csc.math.Quaternion: A quaternion representing the rotation between the vectors

### `identity() -> csc.math.Quaternion`

Creates an identity quaternion (no rotation).

**Returns:**
- csc.math.Quaternion: An identity quaternion (1, 0, 0, 0)

## Instance Methods

### `inverse(self) -> csc.math.Quaternion`

Returns the inverse of this quaternion.

**Returns:**
- csc.math.Quaternion: The inverse quaternion

### `w(self) -> float`

Gets the w (scalar) component of the quaternion.

**Returns:**
- float: The w component value

### `x(self) -> float`

Gets the x component of the quaternion.

**Returns:**
- float: The x component value

### `y(self) -> float`

Gets the y component of the quaternion.

**Returns:**
- float: The y component value

### `z(self) -> float`

Gets the z component of the quaternion.

**Returns:**
- float: The z component value

## Operator Overloads

### `__mul__(self, other) -> Union[csc.math.Quaternion, numpy.ndarray]`

Multiplies this quaternion with another quaternion or applies it to a 3D vector.

**Overloaded signatures:**
1. `__mul__(self, other: csc.math.Quaternion) -> csc.math.Quaternion`
2. `__mul__(self, other: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]`

**Parameters:**
- `other`: Either another quaternion or a 3D vector as numpy array

**Returns:**
- csc.math.Quaternion: Result of quaternion multiplication (when multiplying quaternions)
- numpy.ndarray: Rotated vector (when applying quaternion to a vector)

## Usage Example

```python
import csc.math
import numpy as np

# Create a quaternion
quat = csc.math.Quaternion(1.0, 0.0, 0.0, 0.0)  # Identity quaternion

# Get quaternion components
w_val = quat.w()
x_val = quat.x()
y_val = quat.y()
z_val = quat.z()

# Create identity quaternion
identity = csc.math.Quaternion.identity()

# Get inverse quaternion
inverse_quat = quat.inverse()

# Quaternion multiplication
quat1 = csc.math.Quaternion(1.0, 0.0, 0.0, 0.0)
quat2 = csc.math.Quaternion(0.0, 1.0, 0.0, 0.0)
result_quat = quat1 * quat2

# Apply quaternion to a vector
vector = np.array([[1.0], [0.0], [0.0]], dtype=np.float32)
rotated_vector = quat * vector

# Create quaternion from two vectors
vec1 = np.array([1.0, 0.0, 0.0])
vec2 = np.array([0.0, 1.0, 0.0])
rotation_quat = csc.math.Quaternion.from_two_vectors(vec1, vec2)
```

## Usage Notes

- Quaternions are used to represent rotations in 3D space
- The identity quaternion (1, 0, 0, 0) represents no rotation
- Quaternion multiplication is used to combine rotations
- Quaternions can be applied directly to 3D vectors to rotate them
- Use `from_two_vectors()` to create a rotation between two direction vectors

## See Also

- `csc.math` - Other mathematical utilities for 3D operations
- `numpy` - Required for vector operations
- 3D rotation and quaternion mathematics references