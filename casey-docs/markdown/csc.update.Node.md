---
source_url: https://cascadeur.com/python-api/_generate/csc.update.Node.html
html_file: 32058fdf37945e4f98a8b945025f81a4.html
module: csc.update.Node
---

# csc.update.Node[??](#csc-update-node "Permalink to this heading")

*class* csc.update.Node[??](#csc.update.Node "Permalink to this definition")
:   Node class represents a generic Node and implements methods that are common for all nodes

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Node.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.Node.__init__ "csc.update.Node.__init__")(\*args,??\*\*kwargs) |  |
    | [`attributes`](../csc.html#csc.update.Node.attributes "csc.update.Node.attributes")(self,??d) | array of all input and output attributes |
    | [`equal_to`](../csc.html#csc.update.Node.equal_to "csc.update.Node.equal_to")(self,??arg0) |  |
    | [`full_name`](../csc.html#csc.update.Node.full_name "csc.update.Node.full_name")(self) | name with all the parent nodes |
    | [`has_input`](../csc.html#csc.update.Node.has_input "csc.update.Node.has_input")(self,??name) | check if there is an input with such a name |
    | [`has_output`](../csc.html#csc.update.Node.has_output "csc.update.Node.has_output")(self,??name) | check if there is an output with such a name |
    | [`id`](../csc.html#csc.update.Node.id "csc.update.Node.id")(self) | get uniqui id |
    | [`input`](../csc.html#csc.update.Node.input "csc.update.Node.input")(self,??name) | shortcut if node has only one input attribute |
    | [`inputs`](../csc.html#csc.update.Node.inputs "csc.update.Node.inputs")(self) | array of all the inputes attributes |
    | [`is_active`](../csc.html#csc.update.Node.is_active "csc.update.Node.is_active")(self) | check whether it is active for current actualities states (see Additional functionality in csc.update.UpdateEditor) |
    | [`is_fictive`](../csc.html#csc.update.Node.is_fictive "csc.update.Node.is_fictive")(self) | whether it is a fictive node (constants, inputs, outputs of a group or external properties) |
    | [`name`](../csc.html#csc.update.Node.name "csc.update.Node.name")(self) | get name |
    | [`output`](../csc.html#csc.update.Node.output "csc.update.Node.output")(self,??name) | shortcut if node has only one output attribute |
    | [`outputs`](../csc.html#csc.update.Node.outputs "csc.update.Node.outputs")(self) | array of all the outputs attributes |
    | [`parent_group`](../csc.html#csc.update.Node.parent_group "csc.update.Node.parent_group")(self) | return parent group (where this group node is located) |
    | [`parent_object`](../csc.html#csc.update.Node.parent_object "csc.update.Node.parent_object")(self) | return object of the node. |
    | [`set_name`](../csc.html#csc.update.Node.set_name "csc.update.Node.set_name")(self,??name) | rename node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.Node.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Node.__module__ "Permalink to this definition")

    attributes(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *d: [csc.Direction](../csc.html#csc.Direction "csc.Direction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.Node.attributes "Permalink to this definition")
    :   array of all input and output attributes

    equal\_to(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *arg0: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.equal_to "Permalink to this definition")

    full\_name(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.Node.full_name "Permalink to this definition")
    :   name with all the parent nodes

    has\_input(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.has_input "Permalink to this definition")
    :   check if there is an input with such a name

    has\_output(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.has_output "Permalink to this definition")
    :   check if there is an output with such a name

    id(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId") | [csc.update.InterfaceId](../csc.html#csc.update.InterfaceId "csc.update.InterfaceId") | [csc.update.External
**Properties:**
- `Id](../csc.html#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") | [csc.update.ConstantDatasId](../csc.html#csc.update.ConstantDatasId "csc.update.ConstantDatasId") | [csc.update.ConstantSettingsId](../csc.html#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") | [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId") | [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId") | [csc.model.SettingFunctionId](../csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") | [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")[??](#csc.update.Node.id "Permalink to this definition")
    :   get uniqui id`

    input(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")[??](#csc.update.Node.input "Permalink to this definition")
    :   shortcut if node has only one input attribute

    inputs(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.Node.inputs "Permalink to this definition")
    :   array of all the inputes attributes

    is\_active(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.is_active "Permalink to this definition")
    :   check whether it is active for current actualities states
        (see Additional functionality in csc.update.UpdateEditor)

    is\_fictive(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.is_fictive "Permalink to this definition")
    :   whether it is a fictive node (constants, inputs, outputs of a group or external properties)

    name(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.Node.name "Permalink to this definition")
    :   get name

    output(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")[??](#csc.update.Node.output "Permalink to this definition")
    :   shortcut if node has only one output attribute

    outputs(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.Node.outputs "Permalink to this definition")
    :   array of all the outputs attributes

    parent\_group(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  domain::update\_editor::Group[??](#csc.update.Node.parent_group "Permalink to this definition")
    :   return parent group (where this group node is located)

    parent\_object(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*)  domain::update\_editor::Object[??](#csc.update.Node.parent_object "Permalink to this definition")
    :   return object of the node. Will return null if this is not an update group

    set\_name(*self: [csc.update.Node](../csc.html#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Node.set_name "Permalink to this definition")
    :   rename node