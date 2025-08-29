# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.Editor.html

# csc.layers.Editor [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html\#csc-layers-editor "Permalink to this heading")

_class_ csc.layers.Editor [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor "Permalink to this definition")

Editor class

This class contains all methods and properties that need to edit the structure of scene objects’ interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.

Variables:

- **create\_folder** – name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId

- **create\_layer** – name : string, parent : FolderId, pos : int or None, -> FolderId

- **set\_fixed\_interpolation\_if\_need** – overridden method by ItemId, int, int \|\| LayerId, int (frame)

- **set\_fixed\_interpolation\_or\_key\_if\_need** – overridden method by LayerId, int, bool


\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.__init__ "csc.layers.Editor.__init__")(\*args, \*\*kwargs) |  |
| [`change_section`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.change_section "csc.layers.Editor.change_section")(self, arg0, arg1, arg2) |  |
| [`clear`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.clear "csc.layers.Editor.clear")(self) |  |
| [`create_folder`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.create_folder "csc.layers.Editor.create_folder")(self, name, parent\[, ...\]) | name : string \| parent : FolderId \| withDefaultLayer : bool (true) \| pos : int or None \| -> FolderId |
| [`create_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.create_layer "csc.layers.Editor.create_layer")(self, name, parent\[, pos\]) | name : string \| parent : FolderId \| pos : int or None \| -> FolderId |
| [`delete_empty_folders`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_empty_folders "csc.layers.Editor.delete_empty_folders")(self) |  |
| [`delete_empty_layers`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_empty_layers "csc.layers.Editor.delete_empty_layers")(self) |  |
| [`delete_folder`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_folder "csc.layers.Editor.delete_folder")(self, id) |  |
| [`delete_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_layer "csc.layers.Editor.delete_layer")(self, id) |  |
| [`find_header`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.find_header "csc.layers.Editor.find_header")(self, arg0) | -\> Header |
| [`insert_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.insert_layer "csc.layers.Editor.insert_layer")(self, layer, pos) | layer : Layer \| pos : int or None |
| [`move_item`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.move_item "csc.layers.Editor.move_item")(self, item\_id, folder\_id\[, pos\]) | pos : int or None |
| [`normalize_sections`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.normalize_sections "csc.layers.Editor.normalize_sections")(self, scene) |  |
| [`set_default`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_default "csc.layers.Editor.set_default")(self) |  |
| [`set_fixed_interpolation_if_need`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_fixed_interpolation_if_need "csc.layers.Editor.set_fixed_interpolation_if_need")(\*args, \*\*kwargs) | Overloaded function. |
| [`set_fixed_interpolation_or_key_if_need`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_fixed_interpolation_or_key_if_need "csc.layers.Editor.set_fixed_interpolation_or_key_if_need")(self, ...) |  |
| [`set_locked_for_item`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_locked_for_item "csc.layers.Editor.set_locked_for_item")(self, is\_l, id) | isL : bool \| id : ItemId |
| [`set_locked_for_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_locked_for_layer "csc.layers.Editor.set_locked_for_layer")(self, is\_l, id) | isL : bool \| id : LayerId |
| [`set_name`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_name "csc.layers.Editor.set_name")(self, name, id) |  |
| [`set_section`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_section "csc.layers.Editor.set_section")(self, section, pos, id) | section : Section \| pos : int \| id : ItemId |
| [`set_sections`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_sections "csc.layers.Editor.set_sections")(self, arg0, domain, arg1) | section : <Pos, Section>{} \| id : LayerId |
| [`set_visible_for_item`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_visible_for_item "csc.layers.Editor.set_visible_for_item")(self, is\_v, id) | isV : bool \| id : ItemId |
| [`set_visible_for_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_visible_for_layer "csc.layers.Editor.set_visible_for_layer")(self, is\_v, id) | isV : bool \| id : LayerId |
| [`unset_section`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.unset_section "csc.layers.Editor.unset_section")(self, pos, id) | pos : int \| id : ItemId |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.__module__ "Permalink to this definition")change\_section( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _arg2:Callable_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.change_section "Permalink to this definition")clear( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.clear "Permalink to this definition")create\_folder( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _parent:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _with\_default\_layer:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=True_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")=None_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.create_folder "Permalink to this definition")

name : string \| parent : FolderId \| withDefaultLayer : bool (true) \| pos : int or None \| -> FolderId

create\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _parent:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")=None_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.create_layer "Permalink to this definition")

name : string \| parent : FolderId \| pos : int or None \| -> FolderId

delete\_empty\_folders( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.delete_empty_folders "Permalink to this definition")delete\_empty\_layers( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.delete_empty_layers "Permalink to this definition")delete\_folder( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.delete_folder "Permalink to this definition")delete\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.delete_layer "Permalink to this definition")find\_header( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.find_header "Permalink to this definition")

-\> Header

insert\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _layer:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.insert_layer "Permalink to this definition")

layer : Layer \| pos : int or None

move\_item( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _item\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _folder\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.move_item "Permalink to this definition")

pos : int or None

normalize\_sections( _self:csc.layers.Editor_, _scene:domain::scene::Scene_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.normalize_sections "Permalink to this definition")set\_default( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_default "Permalink to this definition")set\_fixed\_interpolation\_if\_need( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_fixed_interpolation_if_need "Permalink to this definition")

Overloaded function.

1. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool

2. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool


set\_fixed\_interpolation\_or\_key\_if\_need( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _frame:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _set\_key:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_fixed_interpolation_or_key_if_need "Permalink to this definition")set\_locked\_for\_item( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_l:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_locked_for_item "Permalink to this definition")

isL : bool \| id : ItemId

set\_locked\_for\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_l:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_locked_for_layer "Permalink to this definition")

isL : bool \| id : LayerId

set\_name( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_name "Permalink to this definition")set\_section( _self:csc.layers.Editor_, _section:domain::scene::layers::layer::Section_, _pos:int_, _id:csc.Guid_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_section "Permalink to this definition")

section : Section \| pos : int \| id : ItemId

set\_sections( _self:csc.layers.Editor,arg0:dict\[int,domain::scene::layers::layer::Section\],arg1:csc.Guid_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_sections "Permalink to this definition")

section : <Pos, Section>{} \| id : LayerId

set\_visible\_for\_item( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_v:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_visible_for_item "Permalink to this definition")

isV : bool \| id : ItemId

set\_visible\_for\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_v:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.set_visible_for_layer "Permalink to this definition")

isV : bool \| id : LayerId

unset\_section( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Editor.html#csc.layers.Editor.unset_section "Permalink to this definition")

pos : int \| id : ItemId