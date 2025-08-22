---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html
html_file: 76fc1fb989f2da62df6a649ff557029d.html
module: csc.layers.index.FramesIndices
---

# csc.layers.index.FramesIndices[??](#csc-layers-index-framesindices "Permalink to this heading")

*class* csc.layers.index.FramesIndices[??](#csc.layers.index.FramesIndices "Permalink to this definition")
:   FramesIndices class

    It helps to work with animation intervals

    Variables:
    :   **add** ??? overridden method by int || FramesIndices

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.index.FramesIndices.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](#id0 "csc.layers.index.FramesIndices.__init__")(\*args,??\*\*kwargs) |  |
    | [`add`](#csc.layers.index.FramesIndices.add "csc.layers.index.FramesIndices.add")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`clamp`](#csc.layers.index.FramesIndices.clamp "csc.layers.index.FramesIndices.clamp")(self,??min,??max) |  |
    | [`empty`](#csc.layers.index.FramesIndices.empty "csc.layers.index.FramesIndices.empty")(self) |  |
    | [`first`](#csc.layers.index.FramesIndices.first "csc.layers.index.FramesIndices.first")(self) |  |
    | [`from_range`](#csc.layers.index.FramesIndices.from_range "csc.layers.index.FramesIndices.from_range")(min,??max) | -> FramesIndices |
    | [`intersect_indices`](#csc.layers.index.FramesIndices.intersect_indices "csc.layers.index.FramesIndices.intersect_indices")(l,??r) |  |
    | [`last`](#csc.layers.index.FramesIndices.last "csc.layers.index.FramesIndices.last")(self) |  |
    | [`size`](#csc.layers.index.FramesIndices.size "csc.layers.index.FramesIndices.size")(self) |  |
    | [`to_intervals`](#csc.layers.index.FramesIndices.to_intervals "csc.layers.index.FramesIndices.to_intervals")(indices) | -> FramesInterval[] |
    | [`union_indices`](#csc.layers.index.FramesIndices.union_indices "csc.layers.index.FramesIndices.union_indices")(l,??r) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.index.FramesIndices.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*, *arg0: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.index.FramesIndices.__eq__ "Permalink to this definition")

    \_\_hash\_\_ *= None*[??](#csc.layers.index.FramesIndices.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_iter\_\_(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  Iterator[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][??](#csc.layers.index.FramesIndices.__iter__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers.index'*[??](#csc.layers.index.FramesIndices.__module__ "Permalink to this definition")

    add(*\*args*, *\*\*kwargs*)[??](#csc.layers.index.FramesIndices.add "Permalink to this definition")
    :   Overloaded function.

        1. add(self: csc.layers.index.FramesIndices, index: int) -> None
        2. add(self: csc.layers.index.FramesIndices, other: csc.layers.index.FramesIndices) -> None
        3. add(self: csc.layers.index.FramesIndices, indices: set[int]) -> None
        4. add(self: csc.layers.index.FramesIndices, indices: list[int]) -> None

    clamp(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*, *min: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *max: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")[??](#csc.layers.index.FramesIndices.clamp "Permalink to this definition")

    empty(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.index.FramesIndices.empty "Permalink to this definition")

    first(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.index.FramesIndices.first "Permalink to this definition")

    *static* from\_range(*min: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *max: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")[??](#csc.layers.index.FramesIndices.from_range "Permalink to this definition")
    :   -> FramesIndices

    *static* intersect\_indices(*l: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*, *r: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")[??](#csc.layers.index.FramesIndices.intersect_indices "Permalink to this definition")

    last(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.index.FramesIndices.last "Permalink to this definition")

    size(*self: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.index.FramesIndices.size "Permalink to this definition")

    *static* to\_intervals(*indices: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.layers.index.FramesInterval](csc.layers.index.FramesInterval.html#csc.layers.index.FramesInterval "csc.layers.index.FramesInterval")][??](#csc.layers.index.FramesIndices.to_intervals "Permalink to this definition")
    :   -> FramesInterval[]

    *static* union\_indices(*l: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*, *r: [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [csc.layers.index.FramesIndices](#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")[??](#csc.layers.index.FramesIndices.union_indices "Permalink to this definition")