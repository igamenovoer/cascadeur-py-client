---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ModelEditor.html
html_file: dbc6362aebe211be60307113c12bfeaa.html
module: csc.model.ModelEditor
---

# csc.model.ModelEditor 

ModelEditor class Represents basic methods to edit the scene model add_object – overridden method by GroupId -> csc.model.ObjectId Methods __init__ (*args, **kwargs) add_object (*args, **kwargs) Overloaded function. behaviour_editor (self) -> BehaviourEditor data_editor (self) -> DataEditor delete_objects (self, ids[, close_connections]) fit_animation_size_by_layers (self) get_viewer (self) init_default_constants (self) layers (self) -> csc.layers.Layers layers_editor (self) -> csc.layers.Editor layers_selector (self) -> csc.layers.Selector move_obj_ids_in_layers (self[, objIds]) move_objects_to_layer (self, ids, target_layer_id) set_fixed_interpolation_if_need (self, ...[, ...]) set_object_name (self, id, name) set_object_type_name (self, id, name) Overloaded function.
1. add_object(self: csc.model.ModelEditor) -> csc.model.ObjectId
2. add_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId

add_object(self: csc.model.ModelEditor) -> csc.model.ObjectId add_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId -> BehaviourEditor -> DataEditor -> csc.layers.Layers -> csc.layers.Editor -> csc.layers.Selector