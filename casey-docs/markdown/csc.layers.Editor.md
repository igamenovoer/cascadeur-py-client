---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Editor.html
html_file: 0b35b482bea100a95ec2a4146446e41e.html
module: csc.layers.Editor
---

# csc.layers.Editor[??](#csc-layers-editor "Permalink to this heading")

*class* csc.layers.Editor[??](#csc.layers.Editor "Permalink to this definition")
:   Editor class

    This class contains all methods and properties that need to edit the structure of scene objects??? interpolation properties.
    The structure is represented in the hierarchy of layers divided by folders.

    Variables:
    :   * **create\_folder** ??? name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId
        * **create\_layer** ??? name : string, parent : FolderId, pos : int or None, -> FolderId
        * **set\_fixed\_interpolation\_if\_need** ??? overridden method by ItemId, int, int || LayerId, int (frame)
        * **set\_fixed\_interpolation\_or\_key\_if\_need** ??? overridden method by LayerId, int, bool

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Editor.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.Editor.__init__ "csc.layers.Editor.__init__")(\*args,??\*\*kwargs) |  |
    | [`change_section`](../csc.html#csc.layers.Editor.change_section "csc.layers.Editor.change_section")(self,??arg0,??arg1,??arg2) |  |
    | [`clear`](../csc.html#csc.layers.Editor.clear "csc.layers.Editor.clear")(self) |  |
    | [`create_folder`](../csc.html#csc.layers.Editor.create_folder "csc.layers.Editor.create_folder")(self,??name,??parent[,??...]) | name : string | parent : FolderId | withDefaultLayer : bool (true) | pos : int or None | -> FolderId |
    | [`create_layer`](../csc.html#csc.layers.Editor.create_layer "csc.layers.Editor.create_layer")(self,??name,??parent[,??pos]) | name : string | parent : FolderId | pos : int or None | -> FolderId |
    | [`delete_empty_folders`](../csc.html#csc.layers.Editor.delete_empty_folders "csc.layers.Editor.delete_empty_folders")(self) |  |
    | [`delete_empty_layers`](../csc.html#csc.layers.Editor.delete_empty_layers "csc.layers.Editor.delete_empty_layers")(self) |  |
    | [`delete_folder`](../csc.html#csc.layers.Editor.delete_folder "csc.layers.Editor.delete_folder")(self,??id) |  |
    | [`delete_layer`](../csc.html#csc.layers.Editor.delete_layer "csc.layers.Editor.delete_layer")(self,??id) |  |
    | [`find_header`](../csc.html#csc.layers.Editor.find_header "csc.layers.Editor.find_header")(self,??arg0) | -> Header |
    | [`insert_layer`](../csc.html#csc.layers.Editor.insert_layer "csc.layers.Editor.insert_layer")(self,??layer,??pos) | layer : Layer | pos : int or None |
    | [`move_item`](../csc.html#csc.layers.Editor.move_item "csc.layers.Editor.move_item")(self,??item\_id,??folder\_id[,??pos]) | pos : int or None |
    | [`normalize_sections`](../csc.html#csc.layers.Editor.normalize_sections "csc.layers.Editor.normalize_sections")(self,??scene) |  |
    | [`set_default`](../csc.html#csc.layers.Editor.set_default "csc.layers.Editor.set_default")(self) |  |
    | [`set_fixed_interpolation_if_need`](../csc.html#csc.layers.Editor.set_fixed_interpolation_if_need "csc.layers.Editor.set_fixed_interpolation_if_need")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`set_fixed_interpolation_or_key_if_need`](../csc.html#csc.layers.Editor.set_fixed_interpolation_or_key_if_need "csc.layers.Editor.set_fixed_interpolation_or_key_if_need")(self,??...) |  |
    | [`set_locked_for_item`](../csc.html#csc.layers.Editor.set_locked_for_item "csc.layers.Editor.set_locked_for_item")(self,??is\_l,??id) | isL : bool | id : ItemId |
    | [`set_locked_for_layer`](../csc.html#csc.layers.Editor.set_locked_for_layer "csc.layers.Editor.set_locked_for_layer")(self,??is\_l,??id) | isL : bool | id : LayerId |
    | [`set_name`](../csc.html#csc.layers.Editor.set_name "csc.layers.Editor.set_name")(self,??name,??id) |  |
    | [`set_section`](../csc.html#csc.layers.Editor.set_section "csc.layers.Editor.set_section")(self,??section,??pos,??id) | section : Section | pos : int | id : ItemId |
    | [`set_sections`](../csc.html#csc.layers.Editor.set_sections "csc.layers.Editor.set_sections")(self,??arg0,??domain,??arg1) | section : <Pos, Section>{} | id : LayerId |
    | [`set_visible_for_item`](../csc.html#csc.layers.Editor.set_visible_for_item "csc.layers.Editor.set_visible_for_item")(self,??is\_v,??id) | isV : bool | id : ItemId |
    | [`set_visible_for_layer`](../csc.html#csc.layers.Editor.set_visible_for_layer "csc.layers.Editor.set_visible_for_layer")(self,??is\_v,??id) | isV : bool | id : LayerId |
    | [`unset_section`](../csc.html#csc.layers.Editor.unset_section "csc.layers.Editor.unset_section")(self,??pos,??id) | pos : int | id : ItemId |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Editor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Editor.__module__ "Permalink to this definition")

    change\_section(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *arg2: Callable*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.change_section "Permalink to this definition")

    clear(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.clear "Permalink to this definition")

    create\_folder(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *parent: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *with\_default\_layer: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = None*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.Editor.create_folder "Permalink to this definition")
    :   name : string | parent : FolderId | withDefaultLayer : bool (true) | pos : int or None | -> FolderId

    create\_layer(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *parent: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = None*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.Editor.create_layer "Permalink to this definition")
    :   name : string | parent : FolderId | pos : int or None | -> FolderId

    delete\_empty\_folders(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_empty_folders "Permalink to this definition")

    delete\_empty\_layers(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_empty_layers "Permalink to this definition")

    delete\_folder(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_folder "Permalink to this definition")

    delete\_layer(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_layer "Permalink to this definition")

    find\_header(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *arg0: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Editor.find_header "Permalink to this definition")
    :   -> Header

    insert\_layer(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *layer: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.insert_layer "Permalink to this definition")
    :   layer : Layer | pos : int or None

    move\_item(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *item\_id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *folder\_id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = None*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.move_item "Permalink to this definition")
    :   pos : int or None

    normalize\_sections(*self: csc.layers.Editor*, *scene: domain::scene::Scene*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.normalize_sections "Permalink to this definition")

    set\_default(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_default "Permalink to this definition")

    set\_fixed\_interpolation\_if\_need(*\*args*, *\*\*kwargs*)[??](#csc.layers.Editor.set_fixed_interpolation_if_need "Permalink to this definition")
    :   Overloaded function.

        1. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool
        2. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool

    set\_fixed\_interpolation\_or\_key\_if\_need(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *set\_key: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Editor.set_fixed_interpolation_or_key_if_need "Permalink to this definition")

    set\_locked\_for\_item(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *is\_l: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_locked_for_item "Permalink to this definition")
    :   isL : bool | id : ItemId

    set\_locked\_for\_layer(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *is\_l: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_locked_for_layer "Permalink to this definition")
    :   isL : bool | id : LayerId

    set\_name(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_name "Permalink to this definition")

    set\_section(*self: csc.layers.Editor*, *section: domain::scene::layers::layer::Section*, *pos: int*, *id: csc.Guid*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_section "Permalink to this definition")
    :   section : Section | pos : int | id : ItemId

    set\_sections(*self: csc.layers.Editor, arg0: dict[int, domain::scene::layers::layer::Section], arg1: csc.Guid*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_sections "Permalink to this definition")
    :   section : <Pos, Section>{} | id : LayerId

    set\_visible\_for\_item(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *is\_v: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_visible_for_item "Permalink to this definition")
    :   isV : bool | id : ItemId

    set\_visible\_for\_layer(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *is\_v: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_visible_for_layer "Permalink to this definition")
    :   isV : bool | id : LayerId

    unset\_section(*self: [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.unset_section "Permalink to this definition")
    :   pos : int | id : ItemId