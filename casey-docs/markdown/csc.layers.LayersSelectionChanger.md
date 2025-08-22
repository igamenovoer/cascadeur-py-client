---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html
html_file: b28b4b90b9c459794d7ddb9ff3f6ec9c.html
module: csc.layers.LayersSelectionChanger
---

# csc.layers.LayersSelectionChanger[??](#csc-layers-layersselectionchanger "Permalink to this heading")

*class* csc.layers.LayersSelectionChanger[??](#csc.layers.LayersSelectionChanger "Permalink to this definition")
:   Layer SelectionChanger class

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.LayersSelectionChanger.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.LayersSelectionChanger.__init__ "csc.layers.LayersSelectionChanger.__init__")(\*args,??\*\*kwargs) |  |
    | [`refresh`](../csc.html#csc.layers.LayersSelectionChanger.refresh "csc.layers.LayersSelectionChanger.refresh")(self) |  |
    | [`selectDefault`](../csc.html#csc.layers.LayersSelectionChanger.selectDefault "csc.layers.LayersSelectionChanger.selectDefault")(self) |  |
    | [`set_full_selection_by_parts`](../csc.html#csc.layers.LayersSelectionChanger.set_full_selection_by_parts "csc.layers.LayersSelectionChanger.set_full_selection_by_parts")(\*args,??\*\*kwargs) | Overloaded function. |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.LayersSelectionChanger.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.LayersSelectionChanger.__module__ "Permalink to this definition")

    refresh(*self: [csc.layers.LayersSelectionChanger](../csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersSelectionChanger.refresh "Permalink to this definition")

    selectDefault(*self: [csc.layers.LayersSelectionChanger](../csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersSelectionChanger.selectDefault "Permalink to this definition")

    set\_full\_selection\_by\_parts(*\*args*, *\*\*kwargs*)[??](#csc.layers.LayersSelectionChanger.set_full_selection_by_parts "Permalink to this definition")
    :   Overloaded function.

        1. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None

           > inds : IndicesContainer
        2. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, itms: list[csc.Guid], first: int, last: int) -> bool