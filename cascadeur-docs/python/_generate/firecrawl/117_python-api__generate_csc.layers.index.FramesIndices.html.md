# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html

# csc.layers.index.FramesIndices [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html\#csc-layers-index-framesindices "Permalink to this heading")

_class_ csc.layers.index.FramesIndices [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "Permalink to this definition")

FramesIndices class

It helps to work with animation intervals

Variables:

**add** – overridden method by int \|\| FramesIndices

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#id0 "csc.layers.index.FramesIndices.__init__")(\*args, \*\*kwargs) |  |
| [`add`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.add "csc.layers.index.FramesIndices.add")(\*args, \*\*kwargs) | Overloaded function. |
| [`clamp`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.clamp "csc.layers.index.FramesIndices.clamp")(self, min, max) |  |
| [`empty`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.empty "csc.layers.index.FramesIndices.empty")(self) |  |
| [`first`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.first "csc.layers.index.FramesIndices.first")(self) |  |
| [`from_range`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.from_range "csc.layers.index.FramesIndices.from_range")(min, max) | -\> FramesIndices |
| [`intersect_indices`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.intersect_indices "csc.layers.index.FramesIndices.intersect_indices")(l, r) |  |
| [`last`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.last "csc.layers.index.FramesIndices.last")(self) |  |
| [`size`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.size "csc.layers.index.FramesIndices.size")(self) |  |
| [`to_intervals`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.to_intervals "csc.layers.index.FramesIndices.to_intervals")(indices) | -\> FramesInterval\[\] |
| [`union_indices`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.union_indices "csc.layers.index.FramesIndices.union_indices")(l, r) |  |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_, _arg0:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.__eq__ "Permalink to this definition")\_\_hash\_\_ _=None_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#id0 "Permalink to this definition")\_\_iter\_\_( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→Iterator\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.__iter__ "Permalink to this definition")\_\_module\_\_ _='csc.layers.index'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.__module__ "Permalink to this definition")add( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.add "Permalink to this definition")

Overloaded function.

1. add(self: csc.layers.index.FramesIndices, index: int) -> None

2. add(self: csc.layers.index.FramesIndices, other: csc.layers.index.FramesIndices) -> None

3. add(self: csc.layers.index.FramesIndices, indices: set\[int\]) -> None

4. add(self: csc.layers.index.FramesIndices, indices: list\[int\]) -> None


clamp( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_, _min:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _max:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.clamp "Permalink to this definition")empty( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.empty "Permalink to this definition")first( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.first "Permalink to this definition")_static_ from\_range( _min:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _max:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.from_range "Permalink to this definition")

-\> FramesIndices

_static_ intersect\_indices( _l:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_, _r:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.intersect_indices "Permalink to this definition")last( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.last "Permalink to this definition")size( _self:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.size "Permalink to this definition")_static_ to\_intervals( _indices:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.layers.index.FramesInterval](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesInterval.html#csc.layers.index.FramesInterval "csc.layers.index.FramesInterval")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.to_intervals "Permalink to this definition")

-\> FramesInterval\[\]

_static_ union\_indices( _l:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_, _r:[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")_)→[csc.layers.index.FramesIndices](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices") [¶](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices.union_indices "Permalink to this definition")