# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html

# csc.layers.LayersSelectionChanger [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html\#csc-layers-layersselectionchanger "Permalink to this heading")

_class_ csc.layers.LayersSelectionChanger [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger "Permalink to this definition")

Layer SelectionChanger class

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.__init__ "csc.layers.LayersSelectionChanger.__init__")(\*args, \*\*kwargs) |  |
| [`refresh`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.refresh "csc.layers.LayersSelectionChanger.refresh")(self) |  |
| [`selectDefault`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.selectDefault "csc.layers.LayersSelectionChanger.selectDefault")(self) |  |
| [`set_full_selection_by_parts`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.set_full_selection_by_parts "csc.layers.LayersSelectionChanger.set_full_selection_by_parts")(\*args, \*\*kwargs) | Overloaded function. |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger.__module__ "Permalink to this definition")refresh( _self:[csc.layers.LayersSelectionChanger](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger.refresh "Permalink to this definition")selectDefault( _self:[csc.layers.LayersSelectionChanger](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger.selectDefault "Permalink to this definition")set\_full\_selection\_by\_parts( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersSelectionChanger.html#csc.layers.LayersSelectionChanger.set_full_selection_by_parts "Permalink to this definition")

Overloaded function.

1. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None


> inds : IndicesContainer

2. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, itms: list\[csc.Guid\], first: int, last: int) -> bool