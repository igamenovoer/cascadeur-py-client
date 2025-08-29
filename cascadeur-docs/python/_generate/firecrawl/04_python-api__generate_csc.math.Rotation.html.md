# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.math.Rotation.html

# csc.math.Rotation [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html\#csc-math-rotation "Permalink to this heading")

_class_ csc.math.Rotation [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation "Permalink to this definition")

Rotation class

The Euler angles implementation.

\_\_init\_\_( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.__init__ "csc.math.Rotation.__init__")(self) |  |
| [`from_angle_axis`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_angle_axis "csc.math.Rotation.from_angle_axis")(\*args, \*\*kwargs) | Overloaded function. |
| [`from_euler`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_euler "csc.math.Rotation.from_euler")(\*args, \*\*kwargs) | Overloaded function. |
| [`from_quaternion`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_quaternion "csc.math.Rotation.from_quaternion")(\*args, \*\*kwargs) | Overloaded function. |
| [`from_rotation_matrix`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_rotation_matrix "csc.math.Rotation.from_rotation_matrix")(arg0) |  |
| [`to_angle_axis`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_angle_axis "csc.math.Rotation.to_angle_axis")(self) |  |
| [`to_euler_angles`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_euler_angles "csc.math.Rotation.to_euler_angles")(self) |  |
| [`to_euler_angles_x_y_z`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_euler_angles_x_y_z "csc.math.Rotation.to_euler_angles_x_y_z")(self) |  |
| [`to_quaternion`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_quaternion "csc.math.Rotation.to_quaternion")(self) |  |
| [`to_rotation_matrix`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_rotation_matrix "csc.math.Rotation.to_rotation_matrix")(self) |  |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.__module__ "Permalink to this definition")_static_ from\_angle\_axis( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.from_angle_axis "Permalink to this definition")

Overloaded function.

1. from\_angle\_axis(arg0: float, arg1: `numpy.ndarray[numpy.float32[3, 1]]`) -> csc.math.Rotation

2. from\_angle\_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation


_static_ from\_euler( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.from_euler "Permalink to this definition")

Overloaded function.

1. from\_euler(x: float, y: float, z: float) -> csc.math.Rotation

2. from\_euler(vec3f: `numpy.ndarray[numpy.float32[3, 1]]`) -> csc.math.Rotation


_static_ from\_quaternion( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.from_quaternion "Permalink to this definition")

Overloaded function.

1. from\_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation

2. from\_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation


_static_ from\_rotation\_matrix( _arg0:`numpy.ndarray[numpy.float32[3,3]]`_)→[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.from_rotation_matrix "Permalink to this definition")to\_angle\_axis( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis") [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.to_angle_axis "Permalink to this definition")to\_euler\_angles( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→`numpy.ndarray[numpy.float32[3,1]]` [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.to_euler_angles "Permalink to this definition")to\_euler\_angles\_x\_y\_z( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→`numpy.ndarray[numpy.float32[3,1]]` [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.to_euler_angles_x_y_z "Permalink to this definition")to\_quaternion( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.to_quaternion "Permalink to this definition")to\_rotation\_matrix( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→`numpy.ndarray[numpy.float32[3,3]]` [¶](https://cascadeur.com/python-api/_generate/csc.math.Rotation.html#csc.math.Rotation.to_rotation_matrix "Permalink to this definition")