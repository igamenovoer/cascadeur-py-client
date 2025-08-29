# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html

# csc.math.SizesInterval [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html\#csc-math-sizesinterval "Permalink to this heading")

_class_ csc.math.SizesInterval [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval "Permalink to this definition")

SizesInterval class

Implements the sizes interval basic methods

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.math.SizesInterval) -> None

2. \_\_init\_\_(self: csc.math.SizesInterval, start: int, end: int) -> None


Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__init__ "csc.math.SizesInterval.__init__")(\*args, \*\*kwargs) | Overloaded function. |
| [`construct_in_right_order`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.construct_in_right_order "csc.math.SizesInterval.construct_in_right_order")(first, second) |  |
| [`contains`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.contains "csc.math.SizesInterval.contains")(self, i) |  |
| [`empty`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.empty "csc.math.SizesInterval.empty")(self) | -\> bool |
| [`end`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.end "csc.math.SizesInterval.end")(self) | -\> int |
| [`inside_interval_inclusive`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.inside_interval_inclusive "csc.math.SizesInterval.inside_interval_inclusive")(self, number) |  |
| [`intersect_intervals`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.intersect_intervals "csc.math.SizesInterval.intersect_intervals")(first, second) |  |
| [`safe_construct`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.safe_construct "csc.math.SizesInterval.safe_construct")(first, second) |  |
| [`start`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.start "csc.math.SizesInterval.start")(self) | -\> int |
| [`union_overlaping_intervals`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.union_overlaping_intervals "csc.math.SizesInterval.union_overlaping_intervals")(first, second) |  |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _arg0:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.__eq__ "Permalink to this definition")\_\_hash\_\_ _=None_ [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#id0 "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.math.SizesInterval) -> None

2. \_\_init\_\_(self: csc.math.SizesInterval, start: int, end: int) -> None


\_\_lt\_\_( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _arg0:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.__lt__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.__module__ "Permalink to this definition")_static_ construct\_in\_right\_order( _first:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _second:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.construct_in_right_order "Permalink to this definition")contains( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _i:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.contains "Permalink to this definition")empty( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.empty "Permalink to this definition")

-\> bool

end( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.end "Permalink to this definition")

-\> int

inside\_interval\_inclusive( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _number:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.inside_interval_inclusive "Permalink to this definition")_static_ intersect\_intervals( _first:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _second:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.intersect_intervals "Permalink to this definition")_static_ safe\_construct( _first:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _second:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.safe_construct "Permalink to this definition")start( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.start "Permalink to this definition")

-\> int

_static_ union\_overlaping\_intervals( _first:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _second:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/_generate/csc.math.SizesInterval.html#csc.math.SizesInterval.union_overlaping_intervals "Permalink to this definition")