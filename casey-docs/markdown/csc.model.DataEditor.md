---
source_url: https://cascadeur.com/python-api/_generate/csc.model.DataEditor.html
html_file: eaa75ab470cb971d43a9107fcffc86b2.html
module: csc.model.DataEditor
---

# csc.model.DataEditor 

DataEditor class 
This class has the possibility to edit scene data and their properties.
- add_data – overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data
- add_setting – overridden method by string, Setting.Value || csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting
- add_constant_data – overridden method by string, Data.Value || string, Data.Value, csc.model.DataId -> Data
- add_constant_setting – overridden method by string, Setting.Value || string, Setting.Value, csc.model.SettingId -> Setting
- set_data_value – overridden method by csc.model.DataId&, Data.Value || csc.model.DataId, int{}, Data.Value || csc.model.DataId, int, Data.Value

add_data – overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data add_setting – overridden method by string, Setting.Value || csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting add_constant_data – overridden method by string, Data.Value || string, Data.Value, csc.model.DataId -> Data add_constant_setting – overridden method by string, Setting.Value || string, Setting.Value, csc.model.SettingId -> Setting set_data_value – overridden method by csc.model.DataId&, Data.Value || csc.model.DataId, int{}, Data.Value || csc.model.DataId, int, Data.Value Methods __init__ (*args, **kwargs) add_constant_data (*args, **kwargs) Overloaded function. add_constant_setting (*args, **kwargs) Overloaded function. add_data (*args, **kwargs) Overloaded function. add_description (self, name, id) add_setting (*args, **kwargs) Overloaded function. change_description (self, name, description) cluster_editor (self) -> ClusterEditor copy_data (self, from_to) delete_data (self, id) delete_setting (self, id) remove_description (self, name) reset_description_value (*args, **kwargs) Overloaded function. set_data_value (*args, **kwargs) Overloaded function. set_description_value (*args, **kwargs) Overloaded function. set_setting_value (*args, **kwargs) Overloaded function. Overloaded function.
1. add_constant_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data
2. add_constant_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data

add_constant_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data add_constant_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data Overloaded function.
1. add_constant_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) -> csc.model.Setting
2. add_constant_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting

add_constant_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) -> csc.model.Setting add_constant_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting Overloaded function.
1. add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data -> Data
2. add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data -> Data

add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data
> -> Data

-> Data add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data
> -> Data

-> Data Overloaded function.
1. add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting -> Setting
2. add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting -> Setting

add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting
> -> Setting

-> Setting add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting
> -> Setting

-> Setting -> ClusterEditor Overloaded function.
1. reset_description_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None
2. reset_description_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None

reset_description_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None reset_description_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None Overloaded function.
1. set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
2. set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
3. set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None

set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None Overloaded function.
1. set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None
2. set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None

set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None Overloaded function.
1. set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) -> None
2. set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None

set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) -> None set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None