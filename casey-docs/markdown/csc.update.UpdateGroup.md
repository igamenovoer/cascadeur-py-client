---
source_url: https://cascadeur.com/python-api/_generate/csc.update.UpdateGroup.html
html_file: 6b5b14651c17abfc0711b071dec83621.html
module: csc.update.UpdateGroup
---

# csc.update.UpdateGroup[??](#csc-update-updategroup "Permalink to this heading")

*class* csc.update.UpdateGroup[??](#csc.update.UpdateGroup "Permalink to this definition")
:   UpdateGroup class represents update group node

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.UpdateGroup.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.UpdateGroup.__init__ "csc.update.UpdateGroup.__init__")(\*args,??\*\*kwargs) |  |
    | `add_input`(self,??name) |  |
    | `add_output`(self,??name) |  |
    | `attributes`(self,??d) | array of all input and output attributes |
    | `constant_datas`(self) | get virtual node to access constant datas |
    | `constant_settings`(self) | get virtual node to access constant settings |
    | `create_group`(self,??name) |  |
    | [`create_regular_data`](../csc.html#csc.update.UpdateGroup.create_regular_data "csc.update.UpdateGroup.create_regular_data")(self,??name,??value,??int,??...) |  |
    | [`create_regular_function`](../csc.html#csc.update.UpdateGroup.create_regular_function "csc.update.UpdateGroup.create_regular_function")(self,??name,??function) |  |
    | [`create_setting_data`](../csc.html#csc.update.UpdateGroup.create_setting_data "csc.update.UpdateGroup.create_setting_data")(self,??name,??value,??int],??...) |  |
    | [`create_setting_function`](../csc.html#csc.update.UpdateGroup.create_setting_function "csc.update.UpdateGroup.create_setting_function")(self,??name,??...) |  |
    | [`create_sub_update_group`](../csc.html#csc.update.UpdateGroup.create_sub_update_group "csc.update.UpdateGroup.create_sub_update_group")(self,??arg0) |  |
    | [`create_sub_update_group2`](../csc.html#csc.update.UpdateGroup.create_sub_update_group2 "csc.update.UpdateGroup.create_sub_update_group2")(self,??name,??group\_id) | -> UpdateGroup |
    | `delete_node`(self,??node) |  |
    | `equal_to`(self,??arg0) |  |
    | [`external_properties`](../csc.html#csc.update.UpdateGroup.external_properties "csc.update.UpdateGroup.external_properties")(self) | -> External
**Properties:**
- `|
    | `full_name`(self) | name with all the parent nodes |
    | `group`(self,??nodes,??name) |  |
    | `group_id`(self) | create sub group |
    | [`groups`](../csc.html#csc.update.UpdateGroup.groups "csc.update.UpdateGroup.groups")(self) | -> UpdateGroup{} |
    | `has_input`(self,??name) | check if there is an input with such a name |
    | `has_node`(self,??name) | check whether there is a child node with a given name |
    | `has_output`(self,??name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | `input`(self,??name) | shortcut if node has only one input attribute |
    | `input_interface_node`(self) |  |
    | `inputs`(self) | array of all the inputes attributes |
    | `interface_input`(self,??name) |  |
    | `interface_inputs`(self) | get group attributes as interface attributes |
    | `interface_node`(self,??direction) | access the interface node |
    | `interface_output`(self,??name) |  |
    | `interface_outputs`(self) |  |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | `is_root`(self) |  |
    | `leaf_children`(self) | get all leaf nodes (settings, datas, functions) |
    | `name`(self) | get name |
    | `node`(\*args,??\*\*kwargs) | Overloaded function. |
    | `node_deep`(self,??name) | access node by name or id recursively |
    | `node_with_type`(self,??type\_name,??name) | find node with name and type |
    | `node_with_type_deep`(self,??type\_name,??name) | find node with name and type recursively |
    | `nodes`(self) | get all children (their children are not included) |
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `output_interface_node`(self) |  |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | [`regular_datas`](../csc.html#csc.update.UpdateGroup.regular_datas "csc.update.UpdateGroup.regular_datas")(self) | -> RegularData{} |
    | [`regular_functions`](../csc.html#csc.update.UpdateGroup.regular_functions "csc.update.UpdateGroup.regular_functions")(self) | -> RegularFunction{} |
    | `set_name`(self,??name) | rename node |
    | [`setting_functions`](../csc.html#csc.update.UpdateGroup.setting_functions "csc.update.UpdateGroup.setting_functions")(self) | -> SettingFunction{} |
    | [`settings_datas`](../csc.html#csc.update.UpdateGroup.settings_datas "csc.update.UpdateGroup.settings_datas")(self) | -> SettingsData{} |`

    \_\_annotations\_\_ *= {}*[??](#csc.update.UpdateGroup.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.UpdateGroup.__module__ "Permalink to this definition")

    create\_regular\_data(*self: csc.update.UpdateGroup, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], mode: csc.model.DataMode = <DataMode.Static: 0>*)  [csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")[??](#csc.update.UpdateGroup.create_regular_data "Permalink to this definition")

    create\_regular\_function(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *function: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")[??](#csc.update.UpdateGroup.create_regular_function "Permalink to this definition")

    create\_setting\_data(*self: csc.update.UpdateGroup, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>*)  [csc.update.SettingData](../csc.html#csc.update.SettingData "csc.update.SettingData")[??](#csc.update.UpdateGroup.create_setting_data "Permalink to this definition")

    create\_setting\_function(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *function\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")[??](#csc.update.UpdateGroup.create_setting_function "Permalink to this definition")

    create\_sub\_update\_group(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")[??](#csc.update.UpdateGroup.create_sub_update_group "Permalink to this definition")

    create\_sub\_update\_group2(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *group\_id: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*)  [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")[??](#csc.update.UpdateGroup.create_sub_update_group2 "Permalink to this definition")
    :   -> UpdateGroup

    external\_properties(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [csc.update.External
**Properties:**
- `](../csc.html#csc.update.ExternalProperties "csc.update.ExternalProperties")[??](#csc.update.UpdateGroup.external_properties "Permalink to this definition")
    :   -> ExternalProperties`

    groups(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")][??](#csc.update.UpdateGroup.groups "Permalink to this definition")
    :   -> UpdateGroup{}

    regular\_datas(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.RegularData](../csc.html#csc.update.RegularData "csc.update.RegularData")][??](#csc.update.UpdateGroup.regular_datas "Permalink to this definition")
    :   -> RegularData{}

    regular\_functions(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")][??](#csc.update.UpdateGroup.regular_functions "Permalink to this definition")
    :   -> RegularFunction{}

    setting\_functions(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")][??](#csc.update.UpdateGroup.setting_functions "Permalink to this definition")
    :   -> SettingFunction{}

    settings\_datas(*self: [csc.update.UpdateGroup](../csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.SettingData](../csc.html#csc.update.SettingData "csc.update.SettingData")][??](#csc.update.UpdateGroup.settings_datas "Permalink to this definition")
    :   -> SettingsData{}