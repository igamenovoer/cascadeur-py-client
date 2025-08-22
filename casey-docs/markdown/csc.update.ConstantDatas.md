---
source_url: https://cascadeur.com/python-api/_generate/csc.update.ConstantDatas.html
html_file: 8736fa6198095e25a940e7a6dac7cfb3.html
module: csc.update.ConstantDatas
---

# csc.update.ConstantDatas[??](#csc-update-constantdatas "Permalink to this heading")

*class* csc.update.ConstantDatas[??](#csc.update.ConstantDatas "Permalink to this definition")
:   ConstantDatas represents a node of constant datas. It is present in any place.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantDatas.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.ConstantDatas.__init__ "csc.update.ConstantDatas.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_data`](../csc.html#csc.update.ConstantDatas.add_data "csc.update.ConstantDatas.add_data")(self,??name,??value) | value: Data.Value |
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
    | `output`(self,??name) | shortcut if node has only one output attribute |
    | `outputs`(self) | array of all the outputs attributes |
    | `parent_group`(self) | return parent group (where this group node is located) |
    | `parent_object`(self) | return object of the node. |
    | `set_name`(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantDatas.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantDatas.__module__ "Permalink to this definition")

    add\_data(*self: [csc.update.ConstantDatas](../csc.html#csc.update.ConstantDatas "csc.update.ConstantDatas")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](../csc.html#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](../csc.html#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ConstantDatas.add_data "Permalink to this definition")
    :   value: Data.Value