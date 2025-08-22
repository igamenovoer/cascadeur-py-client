---
source_url: https://cascadeur.com/python-api/_generate/csc.update.RegularFunction.html
html_file: 1194ef04dcc089dc9e82aa5b249b9074.html
module: csc.update.RegularFunction
---

# csc.update.RegularFunction[??](#csc-update-regularfunction "Permalink to this heading")

*class* csc.update.RegularFunction[??](#csc.update.RegularFunction "Permalink to this definition")
:   RegularFunction class represents a node that calculates same operation, done with datas.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularFunction.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.RegularFunction.__init__ "csc.update.RegularFunction.__init__")(\*args,??\*\*kwargs) |  |
    | [`activity`](../csc.html#csc.update.RegularFunction.activity "csc.update.RegularFunction.activity")(self) | activity attributes |
    | [`arguments`](../csc.html#csc.update.RegularFunction.arguments "csc.update.RegularFunction.arguments")(self) | its input arguments |
    | `attributes`(self,??d) | array of all input and output attributes |
    | [`decrease_vector`](../csc.html#csc.update.RegularFunction.decrease_vector "csc.update.RegularFunction.decrease_vector")(self,??path,??direction) | method that decreases vector attribute |
    | `equal_to`(self,??arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | [`func_id`](../csc.html#csc.update.RegularFunction.func_id "csc.update.RegularFunction.func_id")(self) | its id |
    | `has_input`(self,??name) | check if there is an input with such a name |
    | `has_output`(self,??name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | [`increase_vector`](../csc.html#csc.update.RegularFunction.increase_vector "csc.update.RegularFunction.increase_vector")(self,??path,??direction) | method that increases vector attribute |
    | `input`(self,??name) | shortcut if node has only one input attribute |
    | `inputs`(self) | array of all the inputes attributes |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | [`is_convertible`](../csc.html#csc.update.RegularFunction.is_convertible "csc.update.RegularFunction.is_convertible")(self) | check whether this function will make it to the resulting data graph |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | `name`(self) | get name |
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | [`remove_attribute`](../csc.html#csc.update.RegularFunction.remove_attribute "csc.update.RegularFunction.remove_attribute")(self,??attribute) | method that removes one in vector attribute |
    | [`resize_vector_inputs`](../csc.html#csc.update.RegularFunction.resize_vector_inputs "csc.update.RegularFunction.resize_vector_inputs")(self,??count,??path) | method that resizes input vector attribute |
    | [`resize_vector_outputs`](../csc.html#csc.update.RegularFunction.resize_vector_outputs "csc.update.RegularFunction.resize_vector_outputs")(self,??count,??path) | method that resizes output vector attribute |
    | [`results`](../csc.html#csc.update.RegularFunction.results "csc.update.RegularFunction.results")(self) | its output arguments |
    | [`set_convertible`](../csc.html#csc.update.RegularFunction.set_convertible "csc.update.RegularFunction.set_convertible")(self,??convertible) | set the state of the function, whether it will be used or not |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularFunction.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularFunction.__module__ "Permalink to this definition")

    activity(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*)  [csc.update.ActivityAttribute](../csc.html#csc.update.ActivityAttribute "csc.update.ActivityAttribute")[??](#csc.update.RegularFunction.activity "Permalink to this definition")
    :   activity attributes

    arguments(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.RegularFunctionAttribute](../csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")][??](#csc.update.RegularFunction.arguments "Permalink to this definition")
    :   its input arguments

    decrease\_vector(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *direction: [csc.Direction](../csc.html#csc.Direction "csc.Direction")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.decrease_vector "Permalink to this definition")
    :   method that decreases vector attribute

    func\_id(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*)  [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")[??](#csc.update.RegularFunction.func_id "Permalink to this definition")
    :   its id

    increase\_vector(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *direction: [csc.Direction](../csc.html#csc.Direction "csc.Direction")*)  [csc.update.RegularFunctionAttribute](../csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")[??](#csc.update.RegularFunction.increase_vector "Permalink to this definition")
    :   method that increases vector attribute

    is\_convertible(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularFunction.is_convertible "Permalink to this definition")
    :   check whether this function will make it to the resulting data graph

    remove\_attribute(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*, *attribute: [csc.update.RegularFunctionAttribute](../csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.remove_attribute "Permalink to this definition")
    :   method that removes one in vector attribute

    resize\_vector\_inputs(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.resize_vector_inputs "Permalink to this definition")
    :   method that resizes input vector attribute

    resize\_vector\_outputs(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.resize_vector_outputs "Permalink to this definition")
    :   method that resizes output vector attribute

    results(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.RegularFunctionAttribute](../csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")][??](#csc.update.RegularFunction.results "Permalink to this definition")
    :   its output arguments

    set\_convertible(*self: [csc.update.RegularFunction](../csc.html#csc.update.RegularFunction "csc.update.RegularFunction")*, *convertible: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.set_convertible "Permalink to this definition")
    :   set the state of the function, whether it will be used or not