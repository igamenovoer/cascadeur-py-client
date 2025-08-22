---
source_url: https://cascadeur.com/python-api/_generate/csc.update.Group.html
html_file: a740954f8e6cee0eabdf5910e5f0e708.html
module: csc.update.Group
---

# csc.update.Group[??](#csc-update-group "Permalink to this heading")

*class* csc.update.Group[??](#csc.update.Group "Permalink to this definition")
:   Group class

    Variables:
    :   **node** ??? overridden by name || node, access node by name or id

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Group.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.Group.__init__ "csc.update.Group.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_input`](../csc.html#csc.update.Group.add_input "csc.update.Group.add_input")(self,??name) |  |
    | [`add_output`](../csc.html#csc.update.Group.add_output "csc.update.Group.add_output")(self,??name) |  |
    | `attributes`(self,??d) | array of all input and output attributes |
    | [`constant_datas`](../csc.html#csc.update.Group.constant_datas "csc.update.Group.constant_datas")(self) | get virtual node to access constant datas |
    | [`constant_settings`](../csc.html#csc.update.Group.constant_settings "csc.update.Group.constant_settings")(self) | get virtual node to access constant settings |
    | [`create_group`](../csc.html#csc.update.Group.create_group "csc.update.Group.create_group")(self,??name) |  |
    | [`delete_node`](../csc.html#csc.update.Group.delete_node "csc.update.Group.delete_node")(self,??node) |  |
    | `equal_to`(self,??arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | [`group`](../csc.html#csc.update.Group.group "csc.update.Group.group")(self,??nodes,??name) |  |
    | [`group_id`](../csc.html#csc.update.Group.group_id "csc.update.Group.group_id")(self) | create sub group |
    | `has_input`(self,??name) | check if there is an input with such a name |
    | [`has_node`](../csc.html#csc.update.Group.has_node "csc.update.Group.has_node")(self,??name) | check whether there is a child node with a given name |
    | `has_output`(self,??name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | `input`(self,??name) | shortcut if node has only one input attribute |
    | [`input_interface_node`](../csc.html#csc.update.Group.input_interface_node "csc.update.Group.input_interface_node")(self) |  |
    | `inputs`(self) | array of all the inputes attributes |
    | [`interface_input`](../csc.html#csc.update.Group.interface_input "csc.update.Group.interface_input")(self,??name) |  |
    | [`interface_inputs`](../csc.html#csc.update.Group.interface_inputs "csc.update.Group.interface_inputs")(self) | get group attributes as interface attributes |
    | [`interface_node`](../csc.html#csc.update.Group.interface_node "csc.update.Group.interface_node")(self,??direction) | access the interface node |
    | [`interface_output`](../csc.html#csc.update.Group.interface_output "csc.update.Group.interface_output")(self,??name) |  |
    | [`interface_outputs`](../csc.html#csc.update.Group.interface_outputs "csc.update.Group.interface_outputs")(self) |  |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | [`is_root`](../csc.html#csc.update.Group.is_root "csc.update.Group.is_root")(self) |  |
    | [`leaf_children`](../csc.html#csc.update.Group.leaf_children "csc.update.Group.leaf_children")(self) | get all leaf nodes (settings, datas, functions) |
    | `name`(self) | get name |
    | [`node`](../csc.html#csc.update.Group.node "csc.update.Group.node")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`node_deep`](../csc.html#csc.update.Group.node_deep "csc.update.Group.node_deep")(self,??name) | access node by name or id recursively |
    | [`node_with_type`](../csc.html#csc.update.Group.node_with_type "csc.update.Group.node_with_type")(self,??type\_name,??name) | find node with name and type |
    | [`node_with_type_deep`](../csc.html#csc.update.Group.node_with_type_deep "csc.update.Group.node_with_type_deep")(self,??type\_name,??name) | find node with name and type recursively |
    | [`nodes`](../csc.html#csc.update.Group.nodes "csc.update.Group.nodes")(self) | get all children (their children are not included) |
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | [`output_interface_node`](../csc.html#csc.update.Group.output_interface_node "csc.update.Group.output_interface_node")(self) |  |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.Group.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Group.__module__ "Permalink to this definition")

    add\_input(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.add_input "Permalink to this definition")

    add\_output(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.add_output "Permalink to this definition")

    constant\_datas(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [csc.update.ConstantDatas](../csc.html#csc.update.ConstantDatas "csc.update.ConstantDatas")[??](#csc.update.Group.constant_datas "Permalink to this definition")
    :   get virtual node to access constant datas

    constant\_settings(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [csc.update.ConstantSettings](../csc.html#csc.update.ConstantSettings "csc.update.ConstantSettings")[??](#csc.update.Group.constant_settings "Permalink to this definition")
    :   get virtual node to access constant settings

    create\_group(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")[??](#csc.update.Group.create_group "Permalink to this definition")

    delete\_node(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *node: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Group.delete_node "Permalink to this definition")

    group(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *nodes: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")[??](#csc.update.Group.group "Permalink to this definition")

    group\_id(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")[??](#csc.update.Group.group_id "Permalink to this definition")
    :   create sub group

    has\_node(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Group.has_node "Permalink to this definition")
    :   check whether there is a child node with a given name

    input\_interface\_node(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")[??](#csc.update.Group.input_interface_node "Permalink to this definition")

    interface\_input(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.interface_input "Permalink to this definition")

    interface\_inputs(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")][??](#csc.update.Group.interface_inputs "Permalink to this definition")
    :   get group attributes as interface attributes

    interface\_node(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *direction: [csc.Direction](../csc.html#csc.Direction "csc.Direction")*)  [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")[??](#csc.update.Group.interface_node "Permalink to this definition")
    :   access the interface node

    interface\_output(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.interface_output "Permalink to this definition")

    interface\_outputs(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")][??](#csc.update.Group.interface_outputs "Permalink to this definition")

    is\_root(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")[??](#csc.update.Group.is_root "Permalink to this definition")

    leaf\_children(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")][??](#csc.update.Group.leaf_children "Permalink to this definition")
    :   get all leaf nodes (settings, datas, functions)

    node(*\*args*, *\*\*kwargs*)[??](#csc.update.Group.node "Permalink to this definition")
    :   Overloaded function.

        1. node(self: csc.update.Group, name: str) -> csc.update.Node
        2. node(self: csc.update.Group, node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.External
**Properties:**
- Id, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) -> csc.update.Node

    node\_deep(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")[??](#csc.update.Group.node_deep "Permalink to this definition")
    :   access node by name or id recursively

    node\_with\_type(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *type\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")[??](#csc.update.Group.node_with_type "Permalink to this definition")
    :   find node with name and type

    node\_with\_type\_deep(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*, *type\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")[??](#csc.update.Group.node_with_type_deep "Permalink to this definition")
    :   find node with name and type recursively

    nodes(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")][??](#csc.update.Group.nodes "Permalink to this definition")
    :   get all children (their children are not included)

    output\_interface\_node(*self: [csc.update.Group](../csc.html#csc.update.Group "csc.update.Group")*)  [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")[??](#csc.update.Group.output_interface_node "Permalink to this definition")