---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.index.IndicesContainer.html
html_file: c27c8f3c4586c89070f42473d1002ed0.html
module: csc.layers.index.IndicesContainer
---

# csc.layers.index.IndicesContainer[??](#csc-layers-index-indicescontainer "Permalink to this heading")

*class* csc.layers.index.IndicesContainer[??](#csc.layers.index.IndicesContainer "Permalink to this definition")
:   IndicesContainer class

    Contains of indices items in the structure std::map<ItemId, FramesIndices>

    Variables:
    :   * **all\_frame\_indices** ??? overridden method by int (sizeLimit)
        * **frames\_interval** ??? overridden method by int (sizeLimit)

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.index.IndicesContainer.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.layers.index.IndicesContainer) -> None
        2. \_\_init\_\_(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None
        3. \_\_init\_\_(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](#id0 "csc.layers.index.IndicesContainer.__init__")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`add`](#csc.layers.index.IndicesContainer.add "csc.layers.index.IndicesContainer.add")(self,??other\_container) | otherContainer : IndicesContainer |
    | [`add_frame_indices`](#csc.layers.index.IndicesContainer.add_frame_indices "csc.layers.index.IndicesContainer.add_frame_indices")(self,??frame\_indices) | frame\_indices: int{} |
    | [`add_item`](#csc.layers.index.IndicesContainer.add_item "csc.layers.index.IndicesContainer.add_item")(self,??item\_indices) | itemIndices : ItemIndices |
    | [`all_frame_indices`](#csc.layers.index.IndicesContainer.all_frame_indices "csc.layers.index.IndicesContainer.all_frame_indices")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`cell_indices`](#csc.layers.index.IndicesContainer.cell_indices "csc.layers.index.IndicesContainer.cell_indices")(self) | -> CellIndex[] |
    | [`delete_empty_items`](#csc.layers.index.IndicesContainer.delete_empty_items "csc.layers.index.IndicesContainer.delete_empty_items")(self) |  |
    | [`direct_indices`](#csc.layers.index.IndicesContainer.direct_indices "csc.layers.index.IndicesContainer.direct_indices")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`frames_interval`](#csc.layers.index.IndicesContainer.frames_interval "csc.layers.index.IndicesContainer.frames_interval")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`is_empty`](#csc.layers.index.IndicesContainer.is_empty "csc.layers.index.IndicesContainer.is_empty")(self) |  |
    | [`item_ids`](#csc.layers.index.IndicesContainer.item_ids "csc.layers.index.IndicesContainer.item_ids")(self) | -> Guid[] |
    | [`item_indices`](#csc.layers.index.IndicesContainer.item_indices "csc.layers.index.IndicesContainer.item_indices")(self,??id) | -> FramesIndices |
    | [`items_indices`](#csc.layers.index.IndicesContainer.items_indices "csc.layers.index.IndicesContainer.items_indices")(self) | -> ItemIndices[] |
    | [`rect`](#csc.layers.index.IndicesContainer.rect "csc.layers.index.IndicesContainer.rect")(self) | -> RectIndicesContainer |
    | [`set_frame_indices`](#csc.layers.index.IndicesContainer.set_frame_indices "csc.layers.index.IndicesContainer.set_frame_indices")(self,??start,??end) | start, end : int |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.index.IndicesContainer.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*, *arg0: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.__eq__ "Permalink to this definition")

    \_\_hash\_\_ *= None*[??](#csc.layers.index.IndicesContainer.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.layers.index.IndicesContainer) -> None
        2. \_\_init\_\_(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None
        3. \_\_init\_\_(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None

    \_\_module\_\_ *= 'csc.layers.index'*[??](#csc.layers.index.IndicesContainer.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*, *arg0: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.__ne__ "Permalink to this definition")

    add(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*, *other\_container: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.add "Permalink to this definition")
    :   otherContainer : IndicesContainer

    add\_frame\_indices(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*, *frame\_indices: [csc.layers.index.FramesIndices](csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.add_frame_indices "Permalink to this definition")
    :   frame\_indices: int{}

    add\_item(*self: csc.layers.index.IndicesContainer*, *item\_indices: domain::scene::layers::index::ItemIndices*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.add_item "Permalink to this definition")
    :   itemIndices : ItemIndices

    all\_frame\_indices(*\*args*, *\*\*kwargs*)[??](#csc.layers.index.IndicesContainer.all_frame_indices "Permalink to this definition")
    :   Overloaded function.

        1. all\_frame\_indices(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesIndices
        2. all\_frame\_indices(self: csc.layers.index.IndicesContainer, size\_limit: int) -> csc.layers.index.FramesIndices

    cell\_indices(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.layers.index.CellIndex](csc.layers.index.CellIndex.html#csc.layers.index.CellIndex "csc.layers.index.CellIndex")][??](#csc.layers.index.IndicesContainer.cell_indices "Permalink to this definition")
    :   -> CellIndex[]

    delete\_empty\_items(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.delete_empty_items "Permalink to this definition")

    direct\_indices(*\*args*, *\*\*kwargs*)[??](#csc.layers.index.IndicesContainer.direct_indices "Permalink to this definition")
    :   Overloaded function.

        1. direct\_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices]
        2. direct\_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices]

    frames\_interval(*\*args*, *\*\*kwargs*)[??](#csc.layers.index.IndicesContainer.frames_interval "Permalink to this definition")
    :   Overloaded function.

        1. frames\_interval(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesInterval
        2. frames\_interval(self: csc.layers.index.IndicesContainer, size\_limit: int) -> csc.layers.index.FramesInterval

    is\_empty(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.is_empty "Permalink to this definition")

    item\_ids(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](../csc.html#csc.Guid "csc.Guid")][??](#csc.layers.index.IndicesContainer.item_ids "Permalink to this definition")
    :   -> Guid[]

    item\_indices(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [csc.layers.index.FramesIndices](csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices")[??](#csc.layers.index.IndicesContainer.item_indices "Permalink to this definition")
    :   -> FramesIndices

    items\_indices(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  list[domain::scene::layers::index::ItemIndices][??](#csc.layers.index.IndicesContainer.items_indices "Permalink to this definition")
    :   -> ItemIndices[]

    rect(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*)  [csc.layers.index.RectIndicesContainer](csc.layers.index.RectIndicesContainer.html#csc.layers.index.RectIndicesContainer "csc.layers.index.RectIndicesContainer")[??](#csc.layers.index.IndicesContainer.rect "Permalink to this definition")
    :   -> RectIndicesContainer

    set\_frame\_indices(*self: [csc.layers.index.IndicesContainer](#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.index.IndicesContainer.set_frame_indices "Permalink to this definition")
    :   start, end : int