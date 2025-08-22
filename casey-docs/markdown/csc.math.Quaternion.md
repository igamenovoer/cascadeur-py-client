---
source_url: https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html
html_file: 2bb91c237a838b8889bff2f4c1ab0344.html
module: csc.math.Quaternion
---

# csc.math.Quaternion[??](#csc-math-quaternion "Permalink to this heading")

*class* csc.math.Quaternion[??](#csc.math.Quaternion "Permalink to this definition")
:   Quaternion class

    This class is useful to calculate rotation operations.

    \_\_init\_\_(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*, *w: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *z: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Quaternion.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.math.Quaternion.__init__ "csc.math.Quaternion.__init__")(self,??w,??x,??y,??z) |  |
    | [`from_two_vectors`](../csc.html#csc.math.Quaternion.from_two_vectors "csc.math.Quaternion.from_two_vectors")(arg0,??arg1) |  |
    | [`identity`](../csc.html#csc.math.Quaternion.identity "csc.math.Quaternion.identity")() |  |
    | [`inverse`](../csc.html#csc.math.Quaternion.inverse "csc.math.Quaternion.inverse")(self) |  |
    | [`w`](../csc.html#csc.math.Quaternion.w "csc.math.Quaternion.w")(self) |  |
    | [`x`](../csc.html#csc.math.Quaternion.x "csc.math.Quaternion.x")(self) |  |
    | [`y`](../csc.html#csc.math.Quaternion.y "csc.math.Quaternion.y")(self) |  |
    | [`z`](../csc.html#csc.math.Quaternion.z "csc.math.Quaternion.z")(self) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.math.Quaternion.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*, *w: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *z: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Quaternion.__module__ "Permalink to this definition")

    \_\_mul\_\_(*\*args*, *\*\*kwargs*)[??](#csc.math.Quaternion.__mul__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_mul\_\_(self: csc.math.Quaternion, arg0: csc.math.Quaternion) -> csc.math.Quaternion
        2. \_\_mul\_\_(self: csc.math.Quaternion, arg0: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]

    *static* from\_two\_vectors(*arg0: numpy.ndarray[numpy.float32[3, 1]]*, *arg1: numpy.ndarray[numpy.float32[3, 1]]*)  [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Quaternion.from_two_vectors "Permalink to this definition")

    *static* identity()  [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Quaternion.identity "Permalink to this definition")

    inverse(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*)  [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Quaternion.inverse "Permalink to this definition")

    w(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.w "Permalink to this definition")

    x(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.x "Permalink to this definition")

    y(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.y "Permalink to this definition")

    z(*self: [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.z "Permalink to this definition")