---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Selector.html
html_file: 92ff7297ba42f99dd901779ce81f2a57.html
module: csc.layers.Selector
---

# csc.layers.Selector[??](#csc-layers-selector "Permalink to this heading")

*class* csc.layers.Selector[??](#csc.layers.Selector "Permalink to this definition")
:   Selector class

    This class contains methods to observe and to set selected layers and folders

    Variables:
    :   **set\_full\_selection\_by\_parts** ??? overridden method by ItemId[] (itms), int (first), int (last) || IndicesContainer (inds)

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Selector.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.Selector.__init__ "csc.layers.Selector.__init__")(\*args,??\*\*kwargs) |  |
    | [`all_included_layer_ids`](../csc.html#csc.layers.Selector.all_included_layer_ids "csc.layers.Selector.all_included_layer_ids")(self[,??ignore\_locked]) | ignoreLocked : bool (false) | -> LayerId[] |
    | [`all_included_layer_indices`](../csc.html#csc.layers.Selector.all_included_layer_indices "csc.layers.Selector.all_included_layer_indices")(self,??ignore\_locked) | ignoreLocked : bool (false) | -> IndicesContainer |
    | [`is_selected`](../csc.html#csc.layers.Selector.is_selected "csc.layers.Selector.is_selected")(self,??id) |  |
    | [`select_default`](../csc.html#csc.layers.Selector.select_default "csc.layers.Selector.select_default")(self) |  |
    | [`selection`](../csc.html#csc.layers.Selector.selection "csc.layers.Selector.selection")(self) | -> IndicesContainer |
    | [`set_full_selection_by_parts`](../csc.html#csc.layers.Selector.set_full_selection_by_parts "csc.layers.Selector.set_full_selection_by_parts")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`set_uncheckable_folder_id`](../csc.html#csc.layers.Selector.set_uncheckable_folder_id "csc.layers.Selector.set_uncheckable_folder_id")(self,??id,??uncheckable) | id : ItemId | uncheckable : bool |
    | [`top_layer_id`](../csc.html#csc.layers.Selector.top_layer_id "csc.layers.Selector.top_layer_id")(self) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Selector.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Selector.__module__ "Permalink to this definition")

    all\_included\_layer\_ids(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](../csc.html#csc.Guid "csc.Guid")][??](#csc.layers.Selector.all_included_layer_ids "Permalink to this definition")
    :   ignoreLocked : bool (false) | -> LayerId[]

    all\_included\_layer\_indices(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  domain::scene::layers::index::IndicesContainer[??](#csc.layers.Selector.all_included_layer_indices "Permalink to this definition")
    :   ignoreLocked : bool (false) | -> IndicesContainer

    is\_selected(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Selector.is_selected "Permalink to this definition")

    select\_default(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Selector.select_default "Permalink to this definition")

    selection(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*)  domain::scene::layers::index::IndicesContainer[??](#csc.layers.Selector.selection "Permalink to this definition")
    :   -> IndicesContainer

    set\_full\_selection\_by\_parts(*\*args*, *\*\*kwargs*)[??](#csc.layers.Selector.set_full_selection_by_parts "Permalink to this definition")
    :   Overloaded function.

        1. set\_full\_selection\_by\_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None

           > inds : IndicesContainer
        2. set\_full\_selection\_by\_parts(self: csc.layers.Selector, itms: list[csc.Guid], first: int, last: int) -> None

    set\_uncheckable\_folder\_id(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *uncheckable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Selector.set_uncheckable_folder_id "Permalink to this definition")
    :   id : ItemId | uncheckable : bool

    top\_layer\_id(*self: [csc.layers.Selector](../csc.html#csc.layers.Selector "csc.layers.Selector")*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.Selector.top_layer_id "Permalink to this definition")