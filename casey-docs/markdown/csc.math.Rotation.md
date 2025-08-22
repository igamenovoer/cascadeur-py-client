---
source_url: https://cascadeur.com/python-api/_generate/csc.math.Rotation.html
html_file: ac3d8a63cbeaebc160c80d746aa65bbc.html
module: csc.math.Rotation
---

# csc.math.Rotation 

Rotation class The Euler angles implementation. Methods __init__ (self) from_angle_axis (*args, **kwargs) Overloaded function. from_euler (*args, **kwargs) Overloaded function. from_quaternion (*args, **kwargs) Overloaded function. from_rotation_matrix (arg0) to_angle_axis (self) to_euler_angles (self) to_euler_angles_x_y_z (self) to_quaternion (self) to_rotation_matrix (self) Overloaded function.
1. from_angle_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation
2. from_angle_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation

from_angle_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation from_angle_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation Overloaded function.
1. from_euler(x: float, y: float, z: float) -> csc.math.Rotation
2. from_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation

from_euler(x: float, y: float, z: float) -> csc.math.Rotation from_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation Overloaded function.
1. from_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation
2. from_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation

from_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation from_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation