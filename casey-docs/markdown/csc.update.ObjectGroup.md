---
source_url: https://cascadeur.com/python-api/_generate/csc.update.ObjectGroup.html
html_file: 59e5f9a5bb0772b6b661bb0eba22357f.html
module: csc.update.ObjectGroup
---

# csc.update.ObjectGroup[??](#csc-update-objectgroup "Permalink to this heading")

*class* csc.update.ObjectGroup[??](#csc.update.ObjectGroup "Permalink to this definition")
:   ObjectGroup class represents object group node

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ObjectGroup.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.ObjectGroup.__init__ "csc.update.ObjectGroup.__init__")(\*args,??\*\*kwargs) |  |
    | `add_input`(self,??name) |  |
    | `add_output`(self,??name) |  |
    | `attributes`(self,??d) | array of all input and output attributes |
    | `constant_datas`(self) | get virtual node to access constant datas |
    | `constant_settings`(self) | get virtual node to access constant settings |
    | `create_group`(self,??name) |  |
    | [`create_object`](../csc.html#csc.update.ObjectGroup.create_object "csc.update.ObjectGroup.create_object")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`create_sub_object_group`](../csc.html#csc.update.ObjectGroup.create_sub_object_group "csc.update.ObjectGroup.create_sub_object_group")(self,??name) | -> ObjectGroup |
    | `delete_node`(self,??node) |  |
    | `equal_to`(self,??arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | `group`(self,??nodes,??name) |  |
    | `group_id`(self) | create sub group |
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
    | [`object_groups`](../csc.html#csc.update.ObjectGroup.object_groups "csc.update.ObjectGroup.object_groups")(self) | -> ObjectGroup{} |
    | [`objects`](../csc.html#csc.update.ObjectGroup.objects "csc.update.ObjectGroup.objects")(self) | -> Object{} |
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `output_interface_node`(self) |  |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.ObjectGroup.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ObjectGroup.__module__ "Permalink to this definition")

    create\_object(*\*args*, *\*\*kwargs*)[??](#csc.update.ObjectGroup.create_object "Permalink to this definition")
    :   Overloaded function.

        1. create\_object(self: csc.update.ObjectGroup, name: str) -> csc.update.Object
        2. create\_object(self: csc.update.ObjectGroup, name: str, id: csc.model.ObjectId) -> csc.update.Object

    create\_sub\_object\_group(*self: [csc.update.ObjectGroup](../csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.ObjectGroup](../csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")[??](#csc.update.ObjectGroup.create_sub_object_group "Permalink to this definition")
    :   -> ObjectGroup

    object\_groups(*self: [csc.update.ObjectGroup](../csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.ObjectGroup](../csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")][??](#csc.update.ObjectGroup.object_groups "Permalink to this definition")
    :   -> ObjectGroup{}

    objects(*self: [csc.update.ObjectGroup](../csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Object](../csc.html#csc.update.Object "csc.update.Object")][??](#csc.update.ObjectGroup.objects "Permalink to this definition")
    :   -> Object{}