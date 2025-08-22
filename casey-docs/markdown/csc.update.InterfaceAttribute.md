---
source_url: https://cascadeur.com/python-api/_generate/csc.update.InterfaceAttribute.html
html_file: 315aa8480783fda14fefbb3acca4de14.html
module: csc.update.InterfaceAttribute
---

# csc.update.InterfaceAttribute 

InterfaceAttribute represents a group attribute.
Can be potentially connected to any attribute. Interface attribute can be:
1. An attribute of input/output node inside the group
2. An attribute of the group node itself, in the parent group layout (outside the group)
We will call this attributes âpairedâ. For each attribute there is a paired one. They have the same attribute ids and names.
Sometimes it's easier to think of them as of one attribute that has 2 sides. But in terms of 
this class this are two separate objects. Methods __init__ (*args, **kwargs) connect (self, attribute) attribute: NodeAttribute connected_attributes (self) -> NodeAttribute[] connected_leaves (self[, get_only_first]) -> NodeAttribute[] connected_leaves_in_undirected_graph (self) direction (self) -> csc.DirectionValue disconnect (*args, **kwargs) Overloaded function. group_attribute_id (self) get the group attribute id id (self) -> AttributeId is_active (self) name (self) node (self) -> Node other_side (self) Get the paired attribute (e.g. set_name (self, name) Rename the attribute get the group attribute id Get the paired attribute (e.g. the other side of the attribute) Rename the attribute