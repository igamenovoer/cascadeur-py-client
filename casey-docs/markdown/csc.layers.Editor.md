---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Editor.html
html_file: 0b35b482bea100a95ec2a4146446e41e.html
module: csc.layers.Editor
---

# csc.layers.Editor 

Editor class 
This class contains all methods and properties that need to edit the structure of scene objects' interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.
- create_folder – name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId
- create_layer – name : string, parent : FolderId, pos : int or None, -> FolderId
- set_fixed_interpolation_if_need – overridden method by ItemId, int, int || LayerId, int (frame)
- set_fixed_interpolation_or_key_if_need – overridden method by LayerId, int, bool

create_folder – name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId create_layer – name : string, parent : FolderId, pos : int or None, -> FolderId set_fixed_interpolation_if_need – overridden method by ItemId, int, int || LayerId, int (frame) set_fixed_interpolation_or_key_if_need – overridden method by LayerId, int, bool Methods __init__ (*args, **kwargs) change_section (self, arg0, arg1, arg2) clear (self) create_folder (self, name, parent[, ...]) name : string | parent : FolderId | withDefaultLayer : bool (true) | pos : int or None | -> FolderId create_layer (self, name, parent[, pos]) name : string | parent : FolderId | pos : int or None | -> FolderId delete_empty_folders (self) delete_empty_layers (self) delete_folder (self, id) delete_layer (self, id) find_header (self, arg0) -> Header insert_layer (self, layer, pos) layer : Layer | pos : int or None move_item (self, item_id, folder_id[, pos]) pos : int or None normalize_sections (self, scene) set_default (self) set_fixed_interpolation_if_need (*args, **kwargs) Overloaded function. set_fixed_interpolation_or_key_if_need (self, ...) set_locked_for_item (self, is_l, id) isL : bool | id : ItemId set_locked_for_layer (self, is_l, id) isL : bool | id : LayerId set_name (self, name, id) set_section (self, section, pos, id) section : Section | pos : int | id : ItemId set_sections (self, arg0, domain, arg1) section : <Pos, Section>{} | id : LayerId set_visible_for_item (self, is_v, id) isV : bool | id : ItemId set_visible_for_layer (self, is_v, id) isV : bool | id : LayerId unset_section (self, pos, id) pos : int | id : ItemId name : string | parent : FolderId | withDefaultLayer : bool (true) | pos : int or None | -> FolderId name : string | parent : FolderId | pos : int or None | -> FolderId -> Header layer : Layer | pos : int or None pos : int or None Overloaded function.
1. set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool
2. set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool

set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool isL : bool | id : ItemId isL : bool | id : LayerId section : Section | pos : int | id : ItemId section : <Pos, Section>{} | id : LayerId isV : bool | id : ItemId isV : bool | id : LayerId pos : int | id : ItemId