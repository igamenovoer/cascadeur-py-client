---
source_url: https://cascadeur.com/python-api/_generate/csc.update.RegularData.html
html_file: 8fe79620ce85c240cf8ecb310da0ad63.html
module: csc.update.RegularData
---

# csc.update.RegularData[??](#csc-update-regulardata "Permalink to this heading")

*class* csc.update.RegularData[??](#csc.update.RegularData "Permalink to this definition")
:   RegularData class represents a node of a data.

    Variables:
    :   * **value** ??? overridden method by frame, get data value (requires frame if Animation data)
        * **set\_value** ??? overridden method by frame, set data value (requires frame if Animation data)

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularData.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.RegularData.__init__ "csc.update.RegularData.__init__")(\*args,??\*\*kwargs) |  |
    | [`actuality`](../csc.html#csc.update.RegularData.actuality "csc.update.RegularData.actuality")(self) | output attribute, that provides actuality status |
    | [`attribute`](../csc.html#csc.update.RegularData.attribute "csc.update.RegularData.attribute")(self,??d) | get attribute by direction |
    | `attributes`(self,??d) | array of all input and output attributes |
    | [`data_id`](../csc.html#csc.update.RegularData.data_id "csc.update.RegularData.data_id")(self) |  |
    | `equal_to`(self,??arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | [`get_apply_euler_filter`](../csc.html#csc.update.RegularData.get_apply_euler_filter "csc.update.RegularData.get_apply_euler_filter")(self) | get apply euler filter |
    | [`get_explicit_linear`](../csc.html#csc.update.RegularData.get_explicit_linear "csc.update.RegularData.get_explicit_linear")(self) | get explicit linear |
    | [`get_lerp_mode`](../csc.html#csc.update.RegularData.get_lerp_mode "csc.update.RegularData.get_lerp_mode")(self) | get lerp mode |
    | `has_input`(self,??name) | check if there is an input with such a name |
    | `has_output`(self,??name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | [`input`](../csc.html#csc.update.RegularData.input "csc.update.RegularData.input")(self) | input attribute |
    | `inputs`(self) | array of all the inputes attributes |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | [`is_actual`](../csc.html#csc.update.RegularData.is_actual "csc.update.RegularData.is_actual")(self) | check if this data is set to actual (see Additional functionality in csc.update.UpdateEditor) |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | [`mode`](../csc.html#csc.update.RegularData.mode "csc.update.RegularData.mode")(self) | Check if data is Animation or Static |
    | `name`(self) | get name |
    | [`output`](../csc.html#csc.update.RegularData.output "csc.update.RegularData.output")(self) | output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | [`remove_period`](../csc.html#csc.update.RegularData.remove_period "csc.update.RegularData.remove_period")(self) | in interpolation, remove period |
    | [`set_actual`](../csc.html#csc.update.RegularData.set_actual "csc.update.RegularData.set_actual")(self,??act) | set this data as actual (see Additional functionality in csc.update.UpdateEditor) |
    | [`set_apply_euler_filter`](../csc.html#csc.update.RegularData.set_apply_euler_filter "csc.update.RegularData.set_apply_euler_filter")(self,??apply\_euler\_filter) | set apply euler filter |
    | [`set_description_value`](../csc.html#csc.update.RegularData.set_description_value "csc.update.RegularData.set_description_value")(self,??name) | setDescriptionValue |
    | [`set_explicit_linear`](../csc.html#csc.update.RegularData.set_explicit_linear "csc.update.RegularData.set_explicit_linear")(self,??explicit\_linear) | set explicit linear |
    | [`set_lerp_mode`](../csc.html#csc.update.RegularData.set_lerp_mode "csc.update.RegularData.set_lerp_mode")(self,??mode) | can be slerp for Vector3 datas. |
    | `set_name`(self,??name) | rename node |
    | [`set_period`](../csc.html#csc.update.RegularData.set_period "csc.update.RegularData.set_period")(self,??period) | in interpolation, if perion is provided, the data will be "fixed" to provide smoothness |
    | [`set_value`](../csc.html#csc.update.RegularData.set_value "csc.update.RegularData.set_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`value`](../csc.html#csc.update.RegularData.value "csc.update.RegularData.value")(\*args,??\*\*kwargs) | Overloaded function. |

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularData.__module__ "Permalink to this definition")

    actuality(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [csc.update.ActualityAttribute](../csc.html#csc.update.ActualityAttribute "csc.update.ActualityAttribute")[??](#csc.update.RegularData.actuality "Permalink to this definition")
    :   output attribute, that provides actuality status

    attribute(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *d: [csc.Direction](../csc.html#csc.Direction "csc.Direction")*)  [csc.update.RegularDataAttribute](../csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute")[??](#csc.update.RegularData.attribute "Permalink to this definition")
    :   get attribute by direction

    data\_id(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")[??](#csc.update.RegularData.data_id "Permalink to this definition")

    get\_apply\_euler\_filter(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularData.get_apply_euler_filter "Permalink to this definition")
    :   get apply euler filter

    get\_explicit\_linear(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularData.get_explicit_linear "Permalink to this definition")
    :   get explicit linear

    get\_lerp\_mode(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [csc.model.LerpMode](../csc.html#csc.model.LerpMode "csc.model.LerpMode")[??](#csc.update.RegularData.get_lerp_mode "Permalink to this definition")
    :   get lerp mode

    input(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [csc.update.RegularDataAttribute](../csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute")[??](#csc.update.RegularData.input "Permalink to this definition")
    :   input attribute

    is\_actual(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularData.is_actual "Permalink to this definition")
    :   check if this data is set to actual (see Additional functionality in csc.update.UpdateEditor)

    mode(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [csc.model.DataMode](../csc.html#csc.model.DataMode "csc.model.DataMode")[??](#csc.update.RegularData.mode "Permalink to this definition")
    :   Check if data is Animation or Static

    output(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [csc.update.RegularDataAttribute](../csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute")[??](#csc.update.RegularData.output "Permalink to this definition")
    :   output attribute

    remove\_period(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.remove_period "Permalink to this definition")
    :   in interpolation, remove period

    set\_actual(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *act: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_actual "Permalink to this definition")
    :   set this data as actual (see Additional functionality in csc.update.UpdateEditor)

    set\_apply\_euler\_filter(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *apply\_euler\_filter: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_apply_euler_filter "Permalink to this definition")
    :   set apply euler filter

    set\_description\_value(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_description_value "Permalink to this definition")
    :   setDescriptionValue

    set\_explicit\_linear(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *explicit\_linear: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_explicit_linear "Permalink to this definition")
    :   set explicit linear

    set\_lerp\_mode(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *mode: [csc.model.LerpMode](../csc.html#csc.model.LerpMode "csc.model.LerpMode")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_lerp_mode "Permalink to this definition")
    :   can be slerp for Vector3 datas. Used in interpolation

    set\_period(*self: [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")*, *period: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_period "Permalink to this definition")
    :   in interpolation, if perion is provided, the data will be ???fixed??? to provide smoothness

    set\_value(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularData.set_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
        2. set\_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], frame: int) -> None

    value(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularData.value "Permalink to this definition")
    :   Overloaded function.

        1. value(self: csc.update.RegularData) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
        2. value(self: csc.update.RegularData, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]