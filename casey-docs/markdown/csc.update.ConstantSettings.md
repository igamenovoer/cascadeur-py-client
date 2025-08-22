---
source_url: https://cascadeur.com/python-api/_generate/csc.update.ConstantSettings.html
html_file: 0f15fbfcfb9f3d428522c92e830f7a5d.html
module: csc.update.ConstantSettings
---

# csc.update.ConstantSettings 

ConstantSettings represents a node of constant settings. It is present in any place. Methods __init__ (*args, **kwargs) add_setting (self, name, value) value: Setting.Value attributes (self, d) array of all input and output attributes equal_to (self, arg0) full_name (self) name with all the parent nodes has_input (self, name) check if there is an input with such a name has_output (self, name) check if there is an output with such a name id (self) get uniqui id input (self, name) shortcut if node has only one input attribute inputs (self) array of all the inputes attributes is_active (self) check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) is_fictive (self) whether it is a fictive node (constants, inputs, outputs of a group or external properties) name (self) get name output (self, name) shortcut if node has only one output attribute outputs (self) array of all the outputs attributes parent_group (self) return parent group (where this group node is located) parent_object (self) return object of the node. set_name (self, name) rename node value: Setting.Value