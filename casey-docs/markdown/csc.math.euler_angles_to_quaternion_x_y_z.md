[CLEAN]

# csc.math.euler_angles_to_quaternion_x_y_z

## Overview
Converts Euler angles to a quaternion representation in Cascadeur's math module. Accepts a NumPy array of three float32 values representing Euler angles and returns a csc.math.Quaternion. The precise angle units (degrees or radians) and exact rotation convention are undocumented in the source; the name implies X, Y, Z order.

## Function Definition
```python
def euler_angles_to_quaternion_x_y_z(
    euler_angles: numpy.ndarray[numpy.float32[3, 1]],
) -> csc.math.Quaternion
```

## Usage Notes
- Input shape: 3×1 float32 NumPy array.
- Rotation order and angle units: undocumented.

