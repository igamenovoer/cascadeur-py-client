---
source_url: https://cascadeur.com/python-api/_generate/csc.update.NodeAttribute.html
html_file: a282415e2babc5e3ad4044894a27c70b.html
module: csc.update.NodeAttribute
---

# csc.update.NodeAttribute[??](#csc-update-nodeattribute "Permalink to this heading")

*class* csc.update.NodeAttribute[??](#csc.update.NodeAttribute "Permalink to this definition")
:   NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute.

    Variables:
    :   **disconnect** ??? overridden method with parameter attribute: NodeAttribute

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.NodeAttribute.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.NodeAttribute.__init__ "csc.update.NodeAttribute.__init__")(\*args,??\*\*kwargs) |  |
    | [`connect`](../csc.html#csc.update.NodeAttribute.connect "csc.update.NodeAttribute.connect")(self,??attribute) | attribute: NodeAttribute |
    | [`connected_attributes`](../csc.html#csc.update.NodeAttribute.connected_attributes "csc.update.NodeAttribute.connected_attributes")(self) | -> NodeAttribute[] |
    | [`connected_leaves`](../csc.html#csc.update.NodeAttribute.connected_leaves "csc.update.NodeAttribute.connected_leaves")(self[,??get\_only\_first]) | -> NodeAttribute[] |
    | [`connected_leaves_in_undirected_graph`](../csc.html#csc.update.NodeAttribute.connected_leaves_in_undirected_graph "csc.update.NodeAttribute.connected_leaves_in_undirected_graph")(self) |  |
    | [`direction`](../csc.html#csc.update.NodeAttribute.direction "csc.update.NodeAttribute.direction")(self) | -> csc.DirectionValue |
    | [`disconnect`](../csc.html#csc.update.NodeAttribute.disconnect "csc.update.NodeAttribute.disconnect")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`id`](../csc.html#csc.update.NodeAttribute.id "csc.update.NodeAttribute.id")(self) | -> AttributeId |
    | [`is_active`](../csc.html#csc.update.NodeAttribute.is_active "csc.update.NodeAttribute.is_active")(self) |  |
    | [`name`](../csc.html#csc.update.NodeAttribute.name "csc.update.NodeAttribute.name")(self) |  |
    | [`node`](../csc.html#csc.update.NodeAttribute.node "csc.update.NodeAttribute.node")(self) | -> Node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.NodeAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.NodeAttribute.__module__ "Permalink to this definition")

    connect(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*, *attribute: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.NodeAttribute.connect "Permalink to this definition")
    :   attribute: NodeAttribute

    connected\_attributes(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.NodeAttribute.connected_attributes "Permalink to this definition")
    :   -> NodeAttribute[]

    connected\_leaves(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*, *get\_only\_first: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.NodeAttribute.connected_leaves "Permalink to this definition")
    :   -> NodeAttribute[]

    connected\_leaves\_in\_undirected\_graph(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.NodeAttribute.connected_leaves_in_undirected_graph "Permalink to this definition")

    direction(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [csc.Direction](../csc.html#csc.Direction "csc.Direction")[??](#csc.update.NodeAttribute.direction "Permalink to this definition")
    :   -> csc.DirectionValue

    disconnect(*\*args*, *\*\*kwargs*)[??](#csc.update.NodeAttribute.disconnect "Permalink to this definition")
    :   Overloaded function.

        1. disconnect(self: csc.update.NodeAttribute) -> None
        2. disconnect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) -> None

    id(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [csc.update.RegularFunctionAttributeId](../csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](../csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](../csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](../csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](../csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](../csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](../csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](../csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")[??](#csc.update.NodeAttribute.id "Permalink to this definition")
    :   -> AttributeId

    is\_active(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.NodeAttribute.is_active "Permalink to this definition")

    name(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.NodeAttribute.name "Permalink to this definition")

    node(*self: [csc.update.NodeAttribute](../csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  domain::update\_editor::Node[??](#csc.update.NodeAttribute.node "Permalink to this definition")
    :   -> Node