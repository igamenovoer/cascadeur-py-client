---
source_url: https://cascadeur.com/python-api/_generate/csc.update.InterfaceNode.html
html_file: 15326f83cec2657cba26931b23941dae.html
module: csc.update.InterfaceNode
---

# csc.update.InterfaceNode 

InterfaceNode is a node inside the group that represents its connections with the ouside nodes.
Its attributes are csc.update.InterfaceAttributes Methods __init__ (*args, **kwargs) add_attribute (self, name) attributes (self, d) array of all input and output attributes direction (self) -> csc.DirectionValue equal_to (self, arg0) full_name (self) name with all the parent nodes has_input (self, name) check if there is an input with such a name has_output (self, name) check if there is an output with such a name id (self) get uniqui id input (self, name) shortcut if node has only one input attribute inputs (self) array of all the inputes attributes interface_attributes (self) -> InterfaceAttribute[] is_active (self) check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) is_fictive (self) whether it is a fictive node (constants, inputs, outputs of a group or external properties) move_attribute (self, attribute, position) attribute: InterfaceAttribute | position: int name (self) get name output (self, name) shortcut if node has only one output attribute outputs (self) array of all the outputs attributes parent_group (self) return parent group (where this group node is located) parent_object (self) return object of the node. remove_attribute (self, attribute) attribute: InterfaceAttribute set_name (self, name) rename node -> csc.DirectionValue -> InterfaceAttribute[] attribute: InterfaceAttribute | position: int attribute: InterfaceAttribute