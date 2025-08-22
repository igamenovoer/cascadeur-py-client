---
source_url: https://cascadeur.com/python-api/_generate/csc.math.Rotation.html
html_file: ac3d8a63cbeaebc160c80d746aa65bbc.html
module: csc.math.Rotation
---

# csc.math.Rotation[??](#csc-math-rotation "Permalink to this heading")

*class* csc.math.Rotation[??](#csc.math.Rotation "Permalink to this definition")
:   Rotation class

    The Euler angles implementation.

    \_\_init\_\_(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Rotation.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.math.Rotation.__init__ "csc.math.Rotation.__init__")(self) |  |
    | [`from_angle_axis`](../csc.html#csc.math.Rotation.from_angle_axis "csc.math.Rotation.from_angle_axis")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`from_euler`](../csc.html#csc.math.Rotation.from_euler "csc.math.Rotation.from_euler")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`from_quaternion`](../csc.html#csc.math.Rotation.from_quaternion "csc.math.Rotation.from_quaternion")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`from_rotation_matrix`](../csc.html#csc.math.Rotation.from_rotation_matrix "csc.math.Rotation.from_rotation_matrix")(arg0) |  |
    | [`to_angle_axis`](../csc.html#csc.math.Rotation.to_angle_axis "csc.math.Rotation.to_angle_axis")(self) |  |
    | [`to_euler_angles`](../csc.html#csc.math.Rotation.to_euler_angles "csc.math.Rotation.to_euler_angles")(self) |  |
    | [`to_euler_angles_x_y_z`](../csc.html#csc.math.Rotation.to_euler_angles_x_y_z "csc.math.Rotation.to_euler_angles_x_y_z")(self) |  |
    | [`to_quaternion`](../csc.html#csc.math.Rotation.to_quaternion "csc.math.Rotation.to_quaternion")(self) |  |
    | [`to_rotation_matrix`](../csc.html#csc.math.Rotation.to_rotation_matrix "csc.math.Rotation.to_rotation_matrix")(self) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.math.Rotation.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Rotation.__module__ "Permalink to this definition")

    *static* from\_angle\_axis(*\*args*, *\*\*kwargs*)[??](#csc.math.Rotation.from_angle_axis "Permalink to this definition")
    :   Overloaded function.

        1. from\_angle\_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation
        2. from\_angle\_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation

    *static* from\_euler(*\*args*, *\*\*kwargs*)[??](#csc.math.Rotation.from_euler "Permalink to this definition")
    :   Overloaded function.

        1. from\_euler(x: float, y: float, z: float) -> csc.math.Rotation
        2. from\_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation

    *static* from\_quaternion(*\*args*, *\*\*kwargs*)[??](#csc.math.Rotation.from_quaternion "Permalink to this definition")
    :   Overloaded function.

        1. from\_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation
        2. from\_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation

    *static* from\_rotation\_matrix(*arg0: numpy.ndarray[numpy.float32[3, 3]]*)  [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")[??](#csc.math.Rotation.from_rotation_matrix "Permalink to this definition")

    to\_angle\_axis(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  [csc.math.AngleAxis](../csc.html#csc.math.AngleAxis "csc.math.AngleAxis")[??](#csc.math.Rotation.to_angle_axis "Permalink to this definition")

    to\_euler\_angles(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Rotation.to_euler_angles "Permalink to this definition")

    to\_euler\_angles\_x\_y\_z(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Rotation.to_euler_angles_x_y_z "Permalink to this definition")

    to\_quaternion(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Rotation.to_quaternion "Permalink to this definition")

    to\_rotation\_matrix(*self: [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation")*)  numpy.ndarray[numpy.float32[3, 3]][??](#csc.math.Rotation.to_rotation_matrix "Permalink to this definition")