---
source_url: https://cascadeur.com/python-api/_generate/csc.update.InterfaceNode.html
html_file: 15326f83cec2657cba26931b23941dae.html
module: csc.update.InterfaceNode
---

# csc.update.InterfaceNode[????](#csc-update-interfacenode "Permalink to this heading")

*class* csc.update.InterfaceNode[????](#csc.update.InterfaceNode "Permalink to this definition")
:   InterfaceNode is a node inside the group that represents its connections with the ouside nodes.
    Its attributes are csc.update.Interface
**Attributes:**

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[????](#csc.update.InterfaceNode.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.InterfaceNode.__init__ "csc.update.InterfaceNode.__init__")(\*args,????\*\*kwargs) |  |
    | [`add_attribute`](../csc.html#csc.update.InterfaceNode.add_attribute "csc.update.InterfaceNode.add_attribute")(self,????name) |  |
    | `attributes`(self,????d) | array of all input and output attributes |
    | [`direction`](../csc.html#csc.update.InterfaceNode.direction "csc.update.InterfaceNode.direction")(self) | -> csc.DirectionValue |
    | `equal_to`(self,????arg0) |  |
    | `full_name`(self) | name with all the parent nodes |
    | `has_input`(self,????name) | check if there is an input with such a name |
    | `has_output`(self,????name) | check if there is an output with such a name |
    | `id`(self) | get uniqui id |
    | `input`(self,????name) | shortcut if node has only one input attribute |
    | `inputs`(self) | array of all the inputes attributes |
    | [`interface_attributes`](../csc.html#csc.update.InterfaceNode.interface_attributes "csc.update.InterfaceNode.interface_attributes")(self) | -> InterfaceAttribute[] |
    | `is_active`(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | `is_fictive`(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | [`move_attribute`](../csc.html#csc.update.InterfaceNode.move_attribute "csc.update.InterfaceNode.move_attribute")(self,????attribute,????position) | attribute: InterfaceAttribute | position: int |
    | `name`(self) | get name |
    | `output`(self,????name) | shortcut if node has only one output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | [`remove_attribute`](../csc.html#csc.update.InterfaceNode.remove_attribute "csc.update.InterfaceNode.remove_attribute")(self,????attribute) | attribute: InterfaceAttribute |
    | `set_name`(self,????name) | rename node |

    \_\_annotations\_\_ *= {}*[????](#csc.update.InterfaceNode.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[????](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[????](#csc.update.InterfaceNode.__module__ "Permalink to this definition")

    add\_attribute(*self: [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) ?? [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[????](#csc.update.InterfaceNode.add_attribute "Permalink to this definition")

    direction(*self: [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")*) ?? [csc.Direction](../csc.html#csc.Direction "csc.Direction")[????](#csc.update.InterfaceNode.direction "Permalink to this definition")
    :   -> csc.DirectionValue

    interface\_attributes(*self: [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")*) ?? [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")][????](#csc.update.InterfaceNode.interface_attributes "Permalink to this definition")
    :   -> InterfaceAttribute[]

    move\_attribute(*self: [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")*, *attribute: [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*, *position: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) ?? [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[????](#csc.update.InterfaceNode.move_attribute "Permalink to this definition")
    :   attribute: InterfaceAttribute | position: int

    remove\_attribute(*self: [csc.update.InterfaceNode](../csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")*, *attribute: [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*) ?? [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[????](#csc.update.InterfaceNode.remove_attribute "Permalink to this definition")
    :   attribute: InterfaceAttribute