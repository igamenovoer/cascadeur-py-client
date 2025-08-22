---
source_url: https://cascadeur.com/python-api/_generate/csc.model.DataViewer.html
html_file: f5393cbf10f3d1f9636580b7e912fc87.html
module: csc.model.DataViewer
---

# csc.model.DataViewer 

DataViewer class 
This class allows to view scene data and their properties.
- get_data_value – overridden method by id : csc.model.DataId || csc.model.DataId, int (frame) -> Data.Value
- get_behaviour_property – overridden method by : csc.model.BehaviourId, string -> Data.Value || csc.model.BehaviourId, string, int (frame) -> Setiing.Value

get_data_value – overridden method by id : csc.model.DataId || csc.model.DataId, int (frame) -> Data.Value get_behaviour_property – overridden method by : csc.model.BehaviourId, string -> Data.Value || csc.model.BehaviourId, string, int (frame) -> Setiing.Value Methods __init__ (*args, **kwargs) cluster_viewer (self) -> ClusterViewer get_all_data_id (self, object_id) -> csc.model.DataId[] get_all_settings_id (self, object_id) -> csc.model.SettingId[] get_animation_size (self) -> int get_behaviour_default_data_value (self, id, name) id : csc.model.Beh id | name : string | -> csc.model.DataValue get_behaviour_property (*args, **kwargs) Overloaded function. get_data (self, id) id : csc.model.DataId | -> Data get_data_id (self, id, name) id : csc.model.ObjectId | name : string | -> csc.model.DataId get_data_value (*args, **kwargs) Overloaded function. get_description_by_name (self, arg0) -> string get_description_names (self) -> string[] get_description_value (*args, **kwargs) Overloaded function. get_setting (self, id) id : csc.model.SettingId | -> Setting get_setting_id (self, id, name) id : csc.model.ObjectId | name : string | -> csc.model.DataId get_setting_value (*args, **kwargs) Overloaded function. union_get_data_value (self, data_id[, frame]) id : csc.model.DataId | -> Data.Value -> ClusterViewer -> csc.model.DataId[] -> csc.model.SettingId[] -> int id : csc.model.Beh id | name : string | -> csc.model.DataValue Overloaded function.
1. get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
2. get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union[bool, int]

get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union[bool, int] id : csc.model.DataId | -> Data id : csc.model.ObjectId | name : string | -> csc.model.DataId Overloaded function.
1. get_data_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
2. get_data_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

get_data_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] get_data_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] -> string -> string[] Overloaded function.
1. get_description_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str id : csc.model.DataId -> string
2. get_description_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str id : csc.model.SettingId -> string

get_description_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str
> id : csc.model.DataId -> string

id : csc.model.DataId -> string get_description_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str
> id : csc.model.SettingId -> string

id : csc.model.SettingId -> string id : csc.model.SettingId | -> Setting id : csc.model.ObjectId | name : string | -> csc.model.DataId Overloaded function.
1. get_setting_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union[bool, int] id : csc.model.SettingId | -> Setting.Value
2. get_setting_value(self: csc.model.DataViewer, setting_id: csc.model.SettingId, position: int) -> Union[bool, int] id : csc.model.SettingId, position : int | -> Setting.Value

get_setting_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union[bool, int]
> id : csc.model.SettingId | -> Setting.Value

id : csc.model.SettingId | -> Setting.Value get_setting_value(self: csc.model.DataViewer, setting_id: csc.model.SettingId, position: int) -> Union[bool, int]
> id : csc.model.SettingId, position : int | -> Setting.Value

id : csc.model.SettingId, position : int | -> Setting.Value id : csc.model.DataId | -> Data.Value