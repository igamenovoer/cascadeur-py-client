---
source_url: https://cascadeur.com/python-api/_generate/csc.update.SettingData.html
html_file: c07143915f3c82f5c3fc4ba773667abe.html
module: csc.update.SettingData
---

# csc.update.SettingData 

SettingData class represents a node that calculates same operation, done with settings.
It can comprise bool or std::int8_t (Min: -128, Max: 127) value, please be carefull when you set this. Methods __init__ (*args, **kwargs) attributes (self, d) array of all input and output attributes data_id (self) get setting unique id equal_to (self, arg0) full_name (self) name with all the parent nodes has_input (self, name) check if there is an input with such a name has_output (self, name) check if there is an output with such a name id (self) get uniqui id input (self, name) shortcut if node has only one input attribute inputs (self) array of all the inputes attributes is_active (self) check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) is_fictive (self) whether it is a fictive node (constants, inputs, outputs of a group or external properties) name (self) get name output (self) output attribute outputs (self) array of all the outputs attributes parent_group (self) return parent group (where this group node is located) parent_object (self) return object of the node. set_name (self, name) rename node set_value (*args, **kwargs) Overloaded function. value (*args, **kwargs) Overloaded function. get setting unique id output attribute Overloaded function.
1. set_value(self: csc.update.SettingData, value: Union[bool, int]) -> None set setting value
2. set_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) -> None set setting value

set_value(self: csc.update.SettingData, value: Union[bool, int]) -> None
> set setting value

set setting value set_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) -> None
> set setting value

set setting value Overloaded function.
1. value(self: csc.update.SettingData) -> Union[bool, int] get setting value
2. value(self: csc.update.SettingData, frame: int) -> Union[bool, int] get setting value

value(self: csc.update.SettingData) -> Union[bool, int]
> get setting value

get setting value value(self: csc.update.SettingData, frame: int) -> Union[bool, int]
> get setting value

get setting value