---
source_url: https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html
html_file: f6b49b86e8d7e6b675347f83f83d1be5.html
module: csc.math.SizesInterval
---

# csc.math.SizesInterval[??](#csc-math-sizesinterval "Permalink to this heading")

*class* csc.math.SizesInterval[??](#csc.math.SizesInterval "Permalink to this definition")
:   SizesInterval class

    Implements the sizes interval basic methods

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.math.SizesInterval.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.math.SizesInterval) -> None
        2. \_\_init\_\_(self: csc.math.SizesInterval, start: int, end: int) -> None

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.math.SizesInterval.__init__ "csc.math.SizesInterval.__init__")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`construct_in_right_order`](../csc.html#csc.math.SizesInterval.construct_in_right_order "csc.math.SizesInterval.construct_in_right_order")(first,??second) |  |
    | [`contains`](../csc.html#csc.math.SizesInterval.contains "csc.math.SizesInterval.contains")(self,??i) |  |
    | [`empty`](../csc.html#csc.math.SizesInterval.empty "csc.math.SizesInterval.empty")(self) | -> bool |
    | [`end`](../csc.html#csc.math.SizesInterval.end "csc.math.SizesInterval.end")(self) | -> int |
    | [`inside_interval_inclusive`](../csc.html#csc.math.SizesInterval.inside_interval_inclusive "csc.math.SizesInterval.inside_interval_inclusive")(self,??number) |  |
    | [`intersect_intervals`](../csc.html#csc.math.SizesInterval.intersect_intervals "csc.math.SizesInterval.intersect_intervals")(first,??second) |  |
    | [`safe_construct`](../csc.html#csc.math.SizesInterval.safe_construct "csc.math.SizesInterval.safe_construct")(first,??second) |  |
    | [`start`](../csc.html#csc.math.SizesInterval.start "csc.math.SizesInterval.start")(self) | -> int |
    | [`union_overlaping_intervals`](../csc.html#csc.math.SizesInterval.union_overlaping_intervals "csc.math.SizesInterval.union_overlaping_intervals")(first,??second) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.math.SizesInterval.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*, *arg0: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.__eq__ "Permalink to this definition")

    \_\_hash\_\_ *= None*[??](#csc.math.SizesInterval.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.math.SizesInterval) -> None
        2. \_\_init\_\_(self: csc.math.SizesInterval, start: int, end: int) -> None

    \_\_lt\_\_(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*, *arg0: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.__lt__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.SizesInterval.__module__ "Permalink to this definition")

    *static* construct\_in\_right\_order(*first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.construct_in_right_order "Permalink to this definition")

    contains(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*, *i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.contains "Permalink to this definition")

    empty(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.empty "Permalink to this definition")
    :   -> bool

    end(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.math.SizesInterval.end "Permalink to this definition")
    :   -> int

    inside\_interval\_inclusive(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.inside_interval_inclusive "Permalink to this definition")

    *static* intersect\_intervals(*first: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*, *second: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.intersect_intervals "Permalink to this definition")

    *static* safe\_construct(*first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.safe_construct "Permalink to this definition")

    start(*self: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.math.SizesInterval.start "Permalink to this definition")
    :   -> int

    *static* union\_overlaping\_intervals(*first: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*, *second: [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")*)  [csc.math.SizesInterval](../csc.html#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.union_overlaping_intervals "Permalink to this definition")