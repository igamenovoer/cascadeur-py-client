---
source_url: https://cascadeur.com/python-api/_generate/csc.update.SettingData.html
html_file: c07143915f3c82f5c3fc4ba773667abe.html
module: csc.update.SettingData
---

# csc.update.SettingData[??](#csc-update-settingdata "Permalink to this heading")

*class* csc.update.SettingData[??](#csc.update.SettingData "Permalink to this definition")
:   SettingData class represents a node that calculates same operation, done with settings.
    It can comprise bool or std::int8\_t (Min: -128, Max: 127) value, please be carefull when you set this.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingData.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.SettingData.__init__ "csc.update.SettingData.__init__")(\*args,??\*\*kwargs) |  |
    | `attributes`(self,??d) | array of all input and output attributes |
    | [`data_id`](../csc.html#csc.update.SettingData.data_id "csc.update.SettingData.data_id")(self) | get setting unique id |
    | `equal_to`(self,??arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | `has_input`(self,??name) | check if there is an input with such a name |
    | `has_output`(self,??name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | `input`(self,??name) | shortcut if node has only one input attribute |
    | `inputs`(self) | array of all the inputes attributes |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | `name`(self) | get name |
    | [`output`](../csc.html#csc.update.SettingData.output "csc.update.SettingData.output")(self) | output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | `set_name`(self,??name) | rename node |
    | [`set_value`](../csc.html#csc.update.SettingData.set_value "csc.update.SettingData.set_value")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`value`](../csc.html#csc.update.SettingData.value "csc.update.SettingData.value")(\*args,??\*\*kwargs) | Overloaded function. |

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingData.__module__ "Permalink to this definition")

    data\_id(*self: [csc.update.SettingData](../csc.html#csc.update.SettingData "csc.update.SettingData")*)  [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")[??](#csc.update.SettingData.data_id "Permalink to this definition")
    :   get setting unique id

    output(*self: [csc.update.SettingData](../csc.html#csc.update.SettingData "csc.update.SettingData")*)  [csc.update.SettingDataAttribute](../csc.html#csc.update.SettingDataAttribute "csc.update.SettingDataAttribute")[??](#csc.update.SettingData.output "Permalink to this definition")
    :   output attribute

    set\_value(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingData.set_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_value(self: csc.update.SettingData, value: Union[bool, int]) -> None

           > set setting value
        2. set\_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) -> None

           > set setting value

    value(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingData.value "Permalink to this definition")
    :   Overloaded function.

        1. value(self: csc.update.SettingData) -> Union[bool, int]

           > get setting value
        2. value(self: csc.update.SettingData, frame: int) -> Union[bool, int]

           > get setting value