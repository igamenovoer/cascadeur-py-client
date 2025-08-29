# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.Selector.html

# csc.layers.Selector [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html\#csc-layers-selector "Permalink to this heading")

_class_ csc.layers.Selector [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector "Permalink to this definition")

Selector class

This class contains methods to observe and to set selected layers and folders

Variables:

**set\_full\_selection\_by\_parts** – overridden method by ItemId\[\] (itms), int (first), int (last) \|\| IndicesContainer (inds)

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.__init__ "csc.layers.Selector.__init__")(\*args, \*\*kwargs) |  |
| [`all_included_layer_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.all_included_layer_ids "csc.layers.Selector.all_included_layer_ids")(self\[, ignore\_locked\]) | ignoreLocked : bool (false) \| -> LayerId\[\] |
| [`all_included_layer_indices`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.all_included_layer_indices "csc.layers.Selector.all_included_layer_indices")(self, ignore\_locked) | ignoreLocked : bool (false) \| -> IndicesContainer |
| [`is_selected`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.is_selected "csc.layers.Selector.is_selected")(self, id) |  |
| [`select_default`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.select_default "csc.layers.Selector.select_default")(self) |  |
| [`selection`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.selection "csc.layers.Selector.selection")(self) | -\> IndicesContainer |
| [`set_full_selection_by_parts`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.set_full_selection_by_parts "csc.layers.Selector.set_full_selection_by_parts")(\*args, \*\*kwargs) | Overloaded function. |
| [`set_uncheckable_folder_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.set_uncheckable_folder_id "csc.layers.Selector.set_uncheckable_folder_id")(self, id, uncheckable) | id : ItemId \| uncheckable : bool |
| [`top_layer_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.top_layer_id "csc.layers.Selector.top_layer_id")(self) |  |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.__module__ "Permalink to this definition")all\_included\_layer\_ids( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.all_included_layer_ids "Permalink to this definition")

ignoreLocked : bool (false) \| -> LayerId\[\]

all\_included\_layer\_indices( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→domain::scene::layers::index::IndicesContainer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.all_included_layer_indices "Permalink to this definition")

ignoreLocked : bool (false) \| -> IndicesContainer

is\_selected( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.is_selected "Permalink to this definition")select\_default( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.select_default "Permalink to this definition")selection( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_)→domain::scene::layers::index::IndicesContainer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.selection "Permalink to this definition")

-\> IndicesContainer

set\_full\_selection\_by\_parts( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.set_full_selection_by_parts "Permalink to this definition")

Overloaded function.

1. set\_full\_selection\_by\_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None


> inds : IndicesContainer

2. set\_full\_selection\_by\_parts(self: csc.layers.Selector, itms: list\[csc.Guid\], first: int, last: int) -> None


set\_uncheckable\_folder\_id( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _uncheckable:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.set_uncheckable_folder_id "Permalink to this definition")

id : ItemId \| uncheckable : bool

top\_layer\_id( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Selector.html#csc.layers.Selector.top_layer_id "Permalink to this definition")