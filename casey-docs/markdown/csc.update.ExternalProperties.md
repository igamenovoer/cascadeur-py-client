---
source_url: https://cascadeur.com/python-api/_generate/csc.update.ExternalProperties.html
html_file: 5e7e28ce53dab8628f17728f3d7c1065.html
module: csc.update.ExternalProperties
---

# csc.update.External
**Properties:**
- `[??](#csc-update-externalproperties "Permalink to this heading")`

*class* csc.update.External
**Properties:**
- `[??](#csc.update.ExternalProperties "Permalink to this definition")
:   ExternalProperties represents a node of external properties.
    (E.g. is this update called during interpolation or not)
    It is represent in any place.`

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.External
**Properties:**
- .__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.External
**Properties:**
- `.__init__ "csc.update.ExternalProperties.__init__")(\*args,??\*\*kwargs) |  |
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
    | [`property_outputs`](../csc.html#csc.update.ExternalProperties.property_outputs "csc.update.ExternalProperties.property_outputs")(self) |  |
    | `set_name`(self,??name) | rename node |`

    \_\_annotations\_\_ *= {}*[??](#csc.update.External
**Properties:**
- .__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.External
**Properties:**
- .__module__ "Permalink to this definition")

    property\_outputs(*self: [csc.update.External
**Properties:**
- `](../csc.html#csc.update.ExternalProperties "csc.update.ExternalProperties")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.ExternalPropertyAttribute](../csc.html#csc.update.ExternalPropertyAttribute "csc.update.ExternalPropertyAttribute")][??](#csc.update.ExternalProperties.property_outputs "Permalink to this definition")`