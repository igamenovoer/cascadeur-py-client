---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html
html_file: 4257a1aca682d3d20e495e0ce53ec793.html
module: csc.layers.Viewer
---

# csc.layers.Viewer 

Viewer class 
This class contains all methods and properties that describe the structure of scene objects' interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.
- top_layer_id – overridden method by ItemId || ItemId[]
- merged_layer – overridden method like static and member LayerId[]
- last_key_pos – overridden method by LayerId[], -> Layer
- frames_count – overridden method by LayerId[], -> int
- significant_frames – overridden method by LayerId{}, -> int{}

top_layer_id – overridden method by ItemId || ItemId[] merged_layer – overridden method like static and member LayerId[] last_key_pos – overridden method by LayerId[], -> Layer frames_count – overridden method by LayerId[], -> int significant_frames – overridden method by LayerId{}, -> int{} Methods __init__ (*args, **kwargs) actual_key_pos (self, pos) all_child_ids (self, id) -> ItemId[] all_included_layer_ids (self, items[, ...]) items : ItemId[] | ignoreLocked : bool (false) | -> LayerId[] all_layer_ids (self) -> LayerId[] all_parent_ids (self, id) -> FolderId[] default_layer_id (self) -> LayerId find_folder (self, id) id : FolderId | -> Folder find_layer (self, id) id : LayerId | -> Layer folder (self, id) id : FolderId | -> Folder folders_map (self) -> <FolderId, Folder>{} for_all_ordered_items (self, arg0) frames_count (*args, **kwargs) Overloaded function. has_item (self, id) -> bool header (self, id) id : ItemId | -> Header is_deep_child (self, item_id, folder_id) -> bool item (self, id) id : ItemId | -> ItemVariant last_key_pos (*args, **kwargs) Overloaded function. layer (self, id) id : LayerId | -> Layer layer_id_by_obj_id (self, id) id : csc.model.ObjectId | -> LayerId layer_id_by_obj_id_or_null (self, id) id : csc.model.ObjectId | -> LayerId layer_ids_by_obj_ids (self, ids) ids : csc.model.ObjectId[] | -> LayerId{} layers_indices (self, id_arr, ignore_locked) -> IndicesContainer layers_map (self) -> <LayerId, Layer>{} merged_layer (self, scene, ids, normalize) obj_ids_by_layer_ids (self, id_arr) -> LayerId[] pos_in_parent (self, id) -> int root_id (self) -> FolderId significant_frames (*args, **kwargs) Overloaded function. top_layer_id (*args, **kwargs) Overloaded function. unlocked_layer_ids (self, id_arr) -> LayerId[] -> ItemId[] items : ItemId[] | ignoreLocked : bool (false) | -> LayerId[] -> LayerId[] -> FolderId[] -> LayerId id : FolderId | -> Folder id : LayerId | -> Layer id : FolderId | -> Folder -> <FolderId, Folder>{} Overloaded function.
1. frames_count(self: csc.layers.Viewer) -> int
2. frames_count(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int

frames_count(self: csc.layers.Viewer) -> int frames_count(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int -> bool id : ItemId | -> Header -> bool id : ItemId | -> ItemVariant Overloaded function.
1. last_key_pos(self: csc.layers.Viewer) -> int
2. last_key_pos(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int

last_key_pos(self: csc.layers.Viewer) -> int last_key_pos(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int id : LayerId | -> Layer id : csc.model.ObjectId | -> LayerId id : csc.model.ObjectId | -> LayerId ids : csc.model.ObjectId[] | -> LayerId{} -> IndicesContainer -> <LayerId, Layer>{} -> LayerId[] -> int -> FolderId Overloaded function.
1. significant_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices
2. significant_frames(self: csc.layers.Viewer, id_arr: set[csc.Guid]) -> domain::scene::layers::index::FramesIndices

significant_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices significant_frames(self: csc.layers.Viewer, id_arr: set[csc.Guid]) -> domain::scene::layers::index::FramesIndices Overloaded function.
1. top_layer_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid
2. top_layer_id(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> csc.Guid

top_layer_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid top_layer_id(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> csc.Guid -> LayerId[]