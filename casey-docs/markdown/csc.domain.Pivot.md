---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.Pivot.html
html_file: 5ab5d82b64a60c64dbbd12f879d67e5b.html
module: csc.domain.Pivot
---

# csc.domain.Pivot[??](#csc-domain-pivot "Permalink to this heading")

*class* csc.domain.Pivot[??](#csc.domain.Pivot "Permalink to this definition")
:   Pivot class

    Represents basic Pivot methods.

    Variables:
    :   * **position** ??? overridden method by ??? || int (frame) || int, StatePivot (pivot)
        * **rotation** ??? overridden method by ??? || int (frame) || int, StatePivot (pivot)

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Pivot.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.domain.Pivot.__init__ "csc.domain.Pivot.__init__")(\*args,??\*\*kwargs) |  |
    | [`center_of_top_objects`](../csc.html#csc.domain.Pivot.center_of_top_objects "csc.domain.Pivot.center_of_top_objects")(self,??arg0) |  |
    | [`position`](../csc.html#csc.domain.Pivot.position "csc.domain.Pivot.position")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`rotation`](../csc.html#csc.domain.Pivot.rotation "csc.domain.Pivot.rotation")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`select`](../csc.html#csc.domain.Pivot.select "csc.domain.Pivot.select")(self,??entity\_id) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Pivot.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Pivot.__module__ "Permalink to this definition")

    center\_of\_top\_objects(*self: [csc.domain.Pivot](../csc.html#csc.domain.Pivot "csc.domain.Pivot")*, *arg0: Callable[[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](../csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")], numpy.ndarray[numpy.float32[3, 1]]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.domain.Pivot.center_of_top_objects "Permalink to this definition")

    position(*\*args*, *\*\*kwargs*)[??](#csc.domain.Pivot.position "Permalink to this definition")
    :   Overloaded function.

        1. position(self: csc.domain.Pivot) -> numpy.ndarray[numpy.float32[3, 1]]
        2. position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray[numpy.float32[3, 1]]
        3. position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]]

    rotation(*\*args*, *\*\*kwargs*)[??](#csc.domain.Pivot.rotation "Permalink to this definition")
    :   Overloaded function.

        1. rotation(self: csc.domain.Pivot) -> csc.math.Quaternion
        2. rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion
        3. rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion

    select(*self: [csc.domain.Pivot](../csc.html#csc.domain.Pivot "csc.domain.Pivot")*, *entity\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](../csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Pivot.select "Permalink to this definition")