---
source_url: https://cascadeur.com/python-api/_generate/csc.update.Object.html
html_file: 89d0191657651c669280023b96781356.html
module: csc.update.Object
---

# csc.update.Object[??](#csc-update-object "Permalink to this heading")

*class* csc.update.Object[??](#csc.update.Object "Permalink to this definition")
:   Object class represents an object node. Functionality is limited - it???s better to use update group node instead.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Object.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.Object.__init__ "csc.update.Object.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_input`](../csc.html#csc.update.Object.add_input "csc.update.Object.add_input")(self,??name) | -> InterfaceAttribute |
    | [`add_output`](../csc.html#csc.update.Object.add_output "csc.update.Object.add_output")(self,??name) | -> InterfaceAttribute |
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
    | [`object_id`](../csc.html#csc.update.Object.object_id "csc.update.Object.object_id")(self) |  |
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | [`root_group`](../csc.html#csc.update.Object.root_group "csc.update.Object.root_group")(self) | -> UpdateGroup |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.Object.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Object.__module__ "Permalink to this definition")

    add\_input(*self: [csc.update.Object](../csc.html#csc.update.Object "csc.update.Object")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Object.add_input "Permalink to this definition")
    :   -> InterfaceAttribute

    add\_output(*self: [csc.update.Object](../csc.html#csc.update.Object "csc.update.Object")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Object.add_output "Permalink to this definition")
    :   -> InterfaceAttribute

    object\_id(*self: [csc.update.Object](../csc.html#csc.update.Object "csc.update.Object")*)  [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.update.Object.object_id "Permalink to this definition")

    root\_group(*self: [csc.update.Object](../csc.html#csc.update.Object "csc.update.Object")*)  domain::update\_editor::UpdateGroup[??](#csc.update.Object.root_group "Permalink to this definition")
    :   -> UpdateGroup