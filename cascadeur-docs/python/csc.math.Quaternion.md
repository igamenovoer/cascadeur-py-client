# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html

# csc.math.Quaternion [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html\#csc-math-quaternion "Permalink to this heading")

_class_ csc.math.Quaternion [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion "Permalink to this definition")

Quaternion class

This class is useful to calculate rotation operations.

\_\_init\_\_( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_, _w:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _x:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _y:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _z:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.__init__ "csc.math.Quaternion.__init__")(self, w, x, y, z) |  |
| [`from_two_vectors`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.from_two_vectors "csc.math.Quaternion.from_two_vectors")(arg0, arg1) |  |
| [`identity`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.identity "csc.math.Quaternion.identity")() |  |
| [`inverse`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.inverse "csc.math.Quaternion.inverse")(self) |  |
| [`w`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.w "csc.math.Quaternion.w")(self) |  |
| [`x`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.x "csc.math.Quaternion.x")(self) |  |
| [`y`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.y "csc.math.Quaternion.y")(self) |  |
| [`z`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.z "csc.math.Quaternion.z")(self) |  |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_, _w:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _x:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _y:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _z:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.__module__ "Permalink to this definition")\_\_mul\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.__mul__ "Permalink to this definition")

Overloaded function.

1. \_\_mul\_\_(self: csc.math.Quaternion, arg0: csc.math.Quaternion) -> csc.math.Quaternion

2. \_\_mul\_\_(self: csc.math.Quaternion, arg0: `numpy.ndarray[numpy.float32[3, 1]]`) -> `numpy.ndarray[numpy.float32[3, 1]]`


_static_ from\_two\_vectors( _arg0:`numpy.ndarray[numpy.float32[3,1]]`_, _arg1:`numpy.ndarray[numpy.float32[3,1]]`_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.from_two_vectors "Permalink to this definition")_static_ identity()→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.identity "Permalink to this definition")inverse( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.inverse "Permalink to this definition")w( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.w "Permalink to this definition")x( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.x "Permalink to this definition")y( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.y "Permalink to this definition")z( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.Quaternion.html#csc.math.Quaternion.z "Permalink to this definition")