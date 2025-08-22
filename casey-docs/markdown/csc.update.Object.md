---
source_url: https://cascadeur.com/python-api/_generate/csc.update.Object.html
html_file: 89d0191657651c669280023b96781356.html
module: csc.update.Object
---

# csc.update.Object 

Object class represents an object node. Functionality is limited - it's better to use update group node instead. Methods __init__ (*args, **kwargs) add_input (self, name) -> InterfaceAttribute add_output (self, name) -> InterfaceAttribute attributes (self, d) array of all input and output attributes equal_to (self, arg0) full_name (self) name with all the parent nodes has_input (self, name) check if there is an input with such a name has_output (self, name) check if there is an output with such a name id (self) get uniqui id input (self, name) shortcut if node has only one input attribute inputs (self) array of all the inputes attributes is_active (self) check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) is_fictive (self) whether it is a fictive node (constants, inputs, outputs of a group or external properties) name (self) get name object_id (self) output (self, name) shortcut if node has only one output attribute outputs (self) array of all the outputs attributes parent_group (self) return parent group (where this group node is located) parent_object (self) return object of the node. root_group (self) -> UpdateGroup set_name (self, name) rename node -> InterfaceAttribute -> InterfaceAttribute -> UpdateGroup