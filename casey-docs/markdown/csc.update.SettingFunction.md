---
source_url: https://cascadeur.com/python-api/_generate/csc.update.SettingFunction.html
html_file: 60ef1b5ccd904b3e53b68d32ae4a576c.html
module: csc.update.SettingFunction
---

# csc.update.SettingFunction[??](#csc-update-settingfunction "Permalink to this heading")

*class* csc.update.SettingFunction[??](#csc.update.SettingFunction "Permalink to this definition")
:   SettingFunction class

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingFunction.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.SettingFunction.__init__ "csc.update.SettingFunction.__init__")(\*args,??\*\*kwargs) |  |
    | [`arguments`](../csc.html#csc.update.SettingFunction.arguments "csc.update.SettingFunction.arguments")(self) | input attributes |
    | `attributes`(self,??d) | array of all input and output attributes |
    | [`decrease_input_vector`](../csc.html#csc.update.SettingFunction.decrease_input_vector "csc.update.SettingFunction.decrease_input_vector")(self,??index) | method that decreases input vector attribute |
    | `equal_to`(self,??arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | [`func_id`](../csc.html#csc.update.SettingFunction.func_id "csc.update.SettingFunction.func_id")(self) | its id |
    | `has_input`(self,??name) | check if there is an input with such a name |
    | `has_output`(self,??name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | [`increase_input_vector`](../csc.html#csc.update.SettingFunction.increase_input_vector "csc.update.SettingFunction.increase_input_vector")(self,??index) | method that increases input vector attribute |
    | `input`(self,??name) | shortcut if node has only one input attribute |
    | `inputs`(self) | array of all the inputes attributes |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | [`is_convertible`](../csc.html#csc.update.SettingFunction.is_convertible "csc.update.SettingFunction.is_convertible")(self) | check whether this function will make it to the resulting setting graph |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | `name`(self) | get name |
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | [`remove_attribute`](../csc.html#csc.update.SettingFunction.remove_attribute "csc.update.SettingFunction.remove_attribute")(self,??attribute) | method that removes one in input vector attribute |
    | [`resize_vector_inputs`](../csc.html#csc.update.SettingFunction.resize_vector_inputs "csc.update.SettingFunction.resize_vector_inputs")(self,??index,??count) | method that resizes input vector attribute |
    | [`results`](../csc.html#csc.update.SettingFunction.results "csc.update.SettingFunction.results")(self) | output attributes |
    | [`set_convertible`](../csc.html#csc.update.SettingFunction.set_convertible "csc.update.SettingFunction.set_convertible")(self,??convertible) | set the state of the function, whether it will be used or not |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingFunction.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingFunction.__module__ "Permalink to this definition")

    arguments(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.SettingFunctionAttribute](../csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")][??](#csc.update.SettingFunction.arguments "Permalink to this definition")
    :   input attributes

    decrease\_input\_vector(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.decrease_input_vector "Permalink to this definition")
    :   method that decreases input vector attribute

    func\_id(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*)  [csc.model.SettingFunctionId](../csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")[??](#csc.update.SettingFunction.func_id "Permalink to this definition")
    :   its id

    increase\_input\_vector(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.update.SettingFunctionAttribute](../csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")[??](#csc.update.SettingFunction.increase_input_vector "Permalink to this definition")
    :   method that increases input vector attribute

    is\_convertible(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.SettingFunction.is_convertible "Permalink to this definition")
    :   check whether this function will make it to the resulting setting graph

    remove\_attribute(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*, *attribute: [csc.update.SettingFunctionAttribute](../csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.remove_attribute "Permalink to this definition")
    :   method that removes one in input vector attribute

    resize\_vector\_inputs(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.resize_vector_inputs "Permalink to this definition")
    :   method that resizes input vector attribute

    results(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.SettingFunctionAttribute](../csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")][??](#csc.update.SettingFunction.results "Permalink to this definition")
    :   output attributes

    set\_convertible(*self: [csc.update.SettingFunction](../csc.html#csc.update.SettingFunction "csc.update.SettingFunction")*, *convertible: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.set_convertible "Permalink to this definition")
    :   set the state of the function, whether it will be used or not