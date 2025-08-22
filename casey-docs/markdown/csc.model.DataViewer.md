---
source_url: https://cascadeur.com/python-api/_generate/csc.model.DataViewer.html
html_file: f5393cbf10f3d1f9636580b7e912fc87.html
module: csc.model.DataViewer
---

# csc.model.DataViewer[??](#csc-model-dataviewer "Permalink to this heading")

*class* csc.model.DataViewer[??](#csc.model.DataViewer "Permalink to this definition")
:   DataViewer class

    This class allows to view scene data and their properties.

    Variables:
    :   * **get\_data\_value** ??? overridden method by id : csc.model.DataId || csc.model.DataId, int (frame) -> Data.Value
        * **get\_behaviour\_property** ??? overridden method by : csc.model.BehaviourId, string -> Data.Value || csc.model.BehaviourId, string, int (frame) -> Setiing.Value

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.DataViewer.__init__ "csc.model.DataViewer.__init__")(\*args,??\*\*kwargs) |  |
    | [`cluster_viewer`](../csc.html#csc.model.DataViewer.cluster_viewer "csc.model.DataViewer.cluster_viewer")(self) | -> ClusterViewer |
    | [`get_all_data_id`](../csc.html#csc.model.DataViewer.get_all_data_id "csc.model.DataViewer.get_all_data_id")(self,??object\_id) | -> csc.model.DataId[] |
    | [`get_all_settings_id`](../csc.html#csc.model.DataViewer.get_all_settings_id "csc.model.DataViewer.get_all_settings_id")(self,??object\_id) | -> csc.model.SettingId[] |
    | [`get_animation_size`](../csc.html#csc.model.DataViewer.get_animation_size "csc.model.DataViewer.get_animation_size")(self) | -> int |
    | [`get_behaviour_default_data_value`](../csc.html#csc.model.DataViewer.get_behaviour_default_data_value "csc.model.DataViewer.get_behaviour_default_data_value")(self,??id,??name) | id : csc.model.Beh id | name : string | -> csc.model.DataValue |
    | [`get_behaviour_property`](../csc.html#csc.model.DataViewer.get_behaviour_property "csc.model.DataViewer.get_behaviour_property")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`get_data`](../csc.html#csc.model.DataViewer.get_data "csc.model.DataViewer.get_data")(self,??id) | id : csc.model.DataId | -> Data |
    | [`get_data_id`](../csc.html#csc.model.DataViewer.get_data_id "csc.model.DataViewer.get_data_id")(self,??id,??name) | id : csc.model.ObjectId | name : string | -> csc.model.DataId |
    | [`get_data_value`](../csc.html#csc.model.DataViewer.get_data_value "csc.model.DataViewer.get_data_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`get_description_by_name`](../csc.html#csc.model.DataViewer.get_description_by_name "csc.model.DataViewer.get_description_by_name")(self,??arg0) | -> string |
    | [`get_description_names`](../csc.html#csc.model.DataViewer.get_description_names "csc.model.DataViewer.get_description_names")(self) | -> string[] |
    | [`get_description_value`](../csc.html#csc.model.DataViewer.get_description_value "csc.model.DataViewer.get_description_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`get_setting`](../csc.html#csc.model.DataViewer.get_setting "csc.model.DataViewer.get_setting")(self,??id) | id : csc.model.SettingId | -> Setting |
    | [`get_setting_id`](../csc.html#csc.model.DataViewer.get_setting_id "csc.model.DataViewer.get_setting_id")(self,??id,??name) | id : csc.model.ObjectId | name : string | -> csc.model.DataId |
    | [`get_setting_value`](../csc.html#csc.model.DataViewer.get_setting_value "csc.model.DataViewer.get_setting_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`union_get_data_value`](../csc.html#csc.model.DataViewer.union_get_data_value "csc.model.DataViewer.union_get_data_value")(self,??data\_id[,??frame]) | id : csc.model.DataId | -> Data.Value |

    \_\_annotations\_\_ *= {}*[??](#csc.model.DataViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DataViewer.__module__ "Permalink to this definition")

    cluster\_viewer(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*)  [csc.model.ClusterViewer](../csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")[??](#csc.model.DataViewer.cluster_viewer "Permalink to this definition")
    :   -> ClusterViewer

    get\_all\_data\_id(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *object\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")][??](#csc.model.DataViewer.get_all_data_id "Permalink to this definition")
    :   -> csc.model.DataId[]

    get\_all\_settings\_id(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *object\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")][??](#csc.model.DataViewer.get_all_settings_id "Permalink to this definition")
    :   -> csc.model.SettingId[]

    get\_animation\_size(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataViewer.get_animation_size "Permalink to this definition")
    :   -> int

    get\_behaviour\_default\_data\_value(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataViewer.get_behaviour_default_data_value "Permalink to this definition")
    :   id : csc.model.Beh id | name : string | -> csc.model.DataValue

    get\_behaviour\_property(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_behaviour_property "Permalink to this definition")
    :   Overloaded function.

        1. get\_behaviour\_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
        2. get\_behaviour\_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union[bool, int]

    get\_data(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [csc.model.Data](../csc.html#csc.model.Data "csc.model.Data")[??](#csc.model.DataViewer.get_data "Permalink to this definition")
    :   id : csc.model.DataId | -> Data

    get\_data\_id(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")[??](#csc.model.DataViewer.get_data_id "Permalink to this definition")
    :   id : csc.model.ObjectId | name : string | -> csc.model.DataId

    get\_data\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_data_value "Permalink to this definition")
    :   Overloaded function.

        1. get\_data\_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
        2. get\_data\_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

    get\_description\_by\_name(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.DataViewer.get_description_by_name "Permalink to this definition")
    :   -> string

    get\_description\_names(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][??](#csc.model.DataViewer.get_description_names "Permalink to this definition")
    :   -> string[]

    get\_description\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_description_value "Permalink to this definition")
    :   Overloaded function.

        1. get\_description\_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str

           > id : csc.model.DataId -> string
        2. get\_description\_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str

           > id : csc.model.SettingId -> string

    get\_setting(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")*)  [csc.model.Setting](../csc.html#csc.model.Setting "csc.model.Setting")[??](#csc.model.DataViewer.get_setting "Permalink to this definition")
    :   id : csc.model.SettingId | -> Setting

    get\_setting\_id(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")[??](#csc.model.DataViewer.get_setting_id "Permalink to this definition")
    :   id : csc.model.ObjectId | name : string | -> csc.model.DataId

    get\_setting\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_setting_value "Permalink to this definition")
    :   Overloaded function.

        1. get\_setting\_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union[bool, int]

           > id : csc.model.SettingId | -> Setting.Value
        2. get\_setting\_value(self: csc.model.DataViewer, setting\_id: csc.model.SettingId, position: int) -> Union[bool, int]

           > id : csc.model.SettingId, position : int | -> Setting.Value

    union\_get\_data\_value(*self: [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")*, *data\_id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = 0*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]][??](#csc.model.DataViewer.union_get_data_value "Permalink to this definition")
    :   id : csc.model.DataId | -> Data.Value