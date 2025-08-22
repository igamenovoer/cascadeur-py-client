---
source_url: https://cascadeur.com/python-api/_generate/csc.update.ConstantSettings.html
html_file: 0f15fbfcfb9f3d428522c92e830f7a5d.html
module: csc.update.ConstantSettings
---

# csc.update.ConstantSettings[??](#csc-update-constantsettings "Permalink to this heading")

*class* csc.update.ConstantSettings[??](#csc.update.ConstantSettings "Permalink to this definition")
:   ConstantSettings represents a node of constant settings. It is present in any place.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantSettings.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.ConstantSettings.__init__ "csc.update.ConstantSettings.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_setting`](../csc.html#csc.update.ConstantSettings.add_setting "csc.update.ConstantSettings.add_setting")(self,??name,??value) | value: Setting.Value |
    | `attributes`(self,??d) | array of all input and output attributes |
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
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantSettings.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantSettings.__module__ "Permalink to this definition")

    add\_setting(*self: [csc.update.ConstantSettings](../csc.html#csc.update.ConstantSettings "csc.update.ConstantSettings")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ConstantSettings.add_setting "Permalink to this definition")
    :   value: Setting.Value