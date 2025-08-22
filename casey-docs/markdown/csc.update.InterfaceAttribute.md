---
source_url: https://cascadeur.com/python-api/_generate/csc.update.InterfaceAttribute.html
html_file: 315aa8480783fda14fefbb3acca4de14.html
module: csc.update.InterfaceAttribute
---

# csc.update.InterfaceAttribute[??](#csc-update-interfaceattribute "Permalink to this heading")

*class* csc.update.InterfaceAttribute[??](#csc.update.InterfaceAttribute "Permalink to this definition")
:   InterfaceAttribute represents a group attribute.
    Can be potentially connected to any attribute.

    Interface attribute can be:
    1. An attribute of input/output node inside the group
    2. An attribute of the group node itself, in the parent group layout (outside the group)
    We will call this attributes ???paired???. For each attribute there is a paired one. They have the same attribute ids and names.
    Sometimes it???s easier to think of them as of one attribute that has 2 sides. But in terms of this class this are two separate objects.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.InterfaceAttribute.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.InterfaceAttribute.__init__ "csc.update.InterfaceAttribute.__init__")(\*args,??\*\*kwargs) |  |
    | `connect`(self,??attribute) | attribute: NodeAttribute |
    | `connected_attributes`(self) | -> NodeAttribute[] |
    | `connected_leaves`(self[,??get\_only\_first]) | -> NodeAttribute[] |
    | `connected_leaves_in_undirected_graph`(self) |  |
    | `direction`(self) | -> csc.DirectionValue |
    | `disconnect`(\*args,??\*\*kwargs) | Overloaded function. |
    | [`group_attribute_id`](../csc.html#csc.update.InterfaceAttribute.group_attribute_id "csc.update.InterfaceAttribute.group_attribute_id")(self) | get the group attribute id |
    | `id`(self) | -> AttributeId |
    | `is_active`(self) |  |
    | `name`(self) |  |
    | `node`(self) | -> Node |
    | [`other_side`](../csc.html#csc.update.InterfaceAttribute.other_side "csc.update.InterfaceAttribute.other_side")(self) | Get the paired attribute (e.g. |
    | [`set_name`](../csc.html#csc.update.InterfaceAttribute.set_name "csc.update.InterfaceAttribute.set_name")(self,??name) | Rename the attribute |

    \_\_annotations\_\_ *= {}*[??](#csc.update.InterfaceAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.InterfaceAttribute.__module__ "Permalink to this definition")

    group\_attribute\_id(*self: [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*)  [csc.update.GroupAttributeId](../csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId")[??](#csc.update.InterfaceAttribute.group_attribute_id "Permalink to this definition")
    :   get the group attribute id

    other\_side(*self: [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*)  [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.InterfaceAttribute.other_side "Permalink to this definition")
    :   Get the paired attribute (e.g. the other side of the attribute)

    set\_name(*self: [csc.update.InterfaceAttribute](../csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceAttribute.set_name "Permalink to this definition")
    :   Rename the attribute