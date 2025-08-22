---
source_url: https://cascadeur.com/python-api/_generate/csc.model.DataEditor.html
html_file: eaa75ab470cb971d43a9107fcffc86b2.html
module: csc.model.DataEditor
---

# csc.model.DataEditor[??](#csc-model-dataeditor "Permalink to this heading")

*class* csc.model.DataEditor[??](#csc.model.DataEditor "Permalink to this definition")
:   DataEditor class

    This class has the possibility to edit scene data and their properties.

    Variables:
    :   * **add\_data** ??? overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data
        * **add\_setting** ??? overridden method by string, Setting.Value || csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting
        * **add\_constant\_data** ??? overridden method by string, Data.Value || string, Data.Value, csc.model.DataId -> Data
        * **add\_constant\_setting** ??? overridden method by string, Setting.Value || string, Setting.Value, csc.model.SettingId -> Setting
        * **set\_data\_value** ??? overridden method by csc.model.DataId&, Data.Value || csc.model.DataId, int{}, Data.Value || csc.model.DataId, int, Data.Value

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.DataEditor.__init__ "csc.model.DataEditor.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_constant_data`](../csc.html#csc.model.DataEditor.add_constant_data "csc.model.DataEditor.add_constant_data")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`add_constant_setting`](../csc.html#csc.model.DataEditor.add_constant_setting "csc.model.DataEditor.add_constant_setting")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`add_data`](../csc.html#csc.model.DataEditor.add_data "csc.model.DataEditor.add_data")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`add_description`](../csc.html#csc.model.DataEditor.add_description "csc.model.DataEditor.add_description")(self,??name,??id) |  |
    | [`add_setting`](../csc.html#csc.model.DataEditor.add_setting "csc.model.DataEditor.add_setting")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`change_description`](../csc.html#csc.model.DataEditor.change_description "csc.model.DataEditor.change_description")(self,??name,??description) |  |
    | [`cluster_editor`](../csc.html#csc.model.DataEditor.cluster_editor "csc.model.DataEditor.cluster_editor")(self) | -> ClusterEditor |
    | [`copy_data`](../csc.html#csc.model.DataEditor.copy_data "csc.model.DataEditor.copy_data")(self,??from\_to) |  |
    | [`delete_data`](../csc.html#csc.model.DataEditor.delete_data "csc.model.DataEditor.delete_data")(self,??id) |  |
    | [`delete_setting`](../csc.html#csc.model.DataEditor.delete_setting "csc.model.DataEditor.delete_setting")(self,??id) |  |
    | [`remove_description`](../csc.html#csc.model.DataEditor.remove_description "csc.model.DataEditor.remove_description")(self,??name) |  |
    | [`reset_description_value`](../csc.html#csc.model.DataEditor.reset_description_value "csc.model.DataEditor.reset_description_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`set_data_value`](../csc.html#csc.model.DataEditor.set_data_value "csc.model.DataEditor.set_data_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`set_description_value`](../csc.html#csc.model.DataEditor.set_description_value "csc.model.DataEditor.set_description_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`set_setting_value`](../csc.html#csc.model.DataEditor.set_setting_value "csc.model.DataEditor.set_setting_value")(\*args,??\*\*kwargs) | Overloaded function. |

    \_\_annotations\_\_ *= {}*[??](#csc.model.DataEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DataEditor.__module__ "Permalink to this definition")

    add\_constant\_data(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_constant_data "Permalink to this definition")
    :   Overloaded function.

        1. add\_constant\_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data
        2. add\_constant\_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data

    add\_constant\_setting(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_constant_setting "Permalink to this definition")
    :   Overloaded function.

        1. add\_constant\_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) -> csc.model.Setting
        2. add\_constant\_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting

    add\_data(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_data "Permalink to this definition")
    :   Overloaded function.

        1. add\_data(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data

           > -> Data
        2. add\_data(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data

           > -> Data

    add\_description(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.add_description "Permalink to this definition")

    add\_setting(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_setting "Permalink to this definition")
    :   Overloaded function.

        1. add\_setting(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting

           > -> Setting
        2. add\_setting(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting

           > -> Setting

    change\_description(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.change_description "Permalink to this definition")

    cluster\_editor(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*)  [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")[??](#csc.model.DataEditor.cluster_editor "Permalink to this definition")
    :   -> ClusterEditor

    copy\_data(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*, *from\_to: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId"), [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.copy_data "Permalink to this definition")

    delete\_data(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*, *id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.delete_data "Permalink to this definition")

    delete\_setting(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*, *id: [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.delete_setting "Permalink to this definition")

    remove\_description(*self: [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.remove_description "Permalink to this definition")

    reset\_description\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.reset_description_value "Permalink to this definition")
    :   Overloaded function.

        1. reset\_description\_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None
        2. reset\_description\_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None

    set\_data\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.set_data_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
        2. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
        3. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None

    set\_description\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.set_description_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_description\_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None
        2. set\_description\_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None

    set\_setting\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.set_setting_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_setting\_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) -> None
        2. set\_setting\_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None