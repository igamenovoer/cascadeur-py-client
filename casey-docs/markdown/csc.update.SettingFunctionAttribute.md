---
source_url: https://cascadeur.com/python-api/_generate/csc.update.SettingFunctionAttribute.html
html_file: ced91ce59e58b0ad6d2a3db93777a4a9.html
module: csc.update.SettingFunctionAttribute
---

# csc.update.SettingFunctionAttribute[??](#csc-update-settingfunctionattribute "Permalink to this heading")

*class* csc.update.SettingFunctionAttribute[??](#csc.update.SettingFunctionAttribute "Permalink to this definition")
:   SettingFunctionAttribute represents an attribute of a setting function.
    It can be connected with setting functions or data function activeness attributes.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingFunctionAttribute.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.SettingFunctionAttribute.__init__ "csc.update.SettingFunctionAttribute.__init__")(\*args,??\*\*kwargs) |  |
    | `connect`(self,??attribute) | attribute: NodeAttribute |
    | `connected_attributes`(self) | -> NodeAttribute[] |
    | `connected_leaves`(self[,??get\_only\_first]) | -> NodeAttribute[] |
    | `connected_leaves_in_undirected_graph`(self) |  |
    | `direction`(self) | -> csc.DirectionValue |
    | `disconnect`(\*args,??\*\*kwargs) | Overloaded function. |
    | `id`(self) | -> AttributeId |
    | `is_active`(self) |  |
    | [`is_out_true`](../csc.html#csc.update.SettingFunctionAttribute.is_out_true "csc.update.SettingFunctionAttribute.is_out_true")(self) |  |
    | `name`(self) |  |
    | `node`(self) | -> Node |
    | [`output_id`](../csc.html#csc.update.SettingFunctionAttribute.output_id "csc.update.SettingFunctionAttribute.output_id")(self) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingFunctionAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingFunctionAttribute.__module__ "Permalink to this definition")

    is\_out\_true(*self: [csc.update.SettingFunctionAttribute](../csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.SettingFunctionAttribute.is_out_true "Permalink to this definition")

    output\_id(*self: [csc.update.SettingFunctionAttribute](../csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")*)  [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")[??](#csc.update.SettingFunctionAttribute.output_id "Permalink to this definition")