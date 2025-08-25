[CLEAN]

# csc.update.InterfaceAttribute

## Overview
Represents a group attribute that can be connected to other attributes within Cascadeur's node groups. An interface attribute may belong to an input/output node inside a group or to the group node itself in the parent layout. Each attribute has a “paired” counterpart with the same ID and name, conceptually two sides of one attribute but implemented as separate objects. Details not shown below are undocumented in the source material.

## Class Definition
```python
class InterfaceAttribute:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor for InterfaceAttribute; details are undocumented.

**Parameters:**
- args: undocumented – variable positional arguments
- kwargs: undocumented – variable keyword arguments

## Methods

### `connect(attribute: NodeAttribute)`
Connect this interface attribute to another attribute.

**Parameters:**
- attribute: NodeAttribute – attribute to connect

**Returns:**
- undocumented

### `connected_attributes() -> NodeAttribute[]`
Return attributes directly connected to this interface attribute.

**Parameters:**
- none

**Returns:**
- NodeAttribute[]: connected attributes

### `connected_leaves(get_only_first: undocumented = undocumented) -> NodeAttribute[]`
Return leaf attributes connected to this attribute.

**Parameters:**
- get_only_first: undocumented – optional; default undocumented

**Returns:**
- NodeAttribute[]: connected leaf attributes

### `connected_leaves_in_undirected_graph()`
Return connected leaves in an undirected-graph interpretation.

**Parameters:**
- none

**Returns:**
- undocumented

### `direction() -> csc.DirectionValue`
Get the direction value of this interface attribute.

**Parameters:**
- none

**Returns:**
- csc.DirectionValue: undocumented

### `disconnect(*args, **kwargs)`
Disconnect this attribute; overload details are undocumented.

**Parameters:**
- args: undocumented – variable positional arguments
- kwargs: undocumented – variable keyword arguments

**Returns:**
- undocumented

**Notes:**
- Overloaded function; specific overloads are undocumented.

### `group_attribute_id()`
Get the group attribute identifier.

**Parameters:**
- none

**Returns:**
- undocumented

### `id() -> AttributeId`
Get this attribute’s ID.

**Parameters:**
- none

**Returns:**
- AttributeId: identifier of the attribute

### `is_active()`
Check whether this attribute is active.

**Parameters:**
- none

**Returns:**
- undocumented

### `name()`
Get this attribute’s name.

**Parameters:**
- none

**Returns:**
- undocumented

### `node() -> Node`
Get the node this attribute belongs to.

**Parameters:**
- none

**Returns:**
- Node: owning node

### `other_side()`
Get the paired “other side” of this interface attribute.

**Parameters:**
- none

**Returns:**
- undocumented

### `set_name(name: undocumented)`
Rename the attribute.

**Parameters:**
- name: undocumented – new attribute name

**Returns:**
- undocumented

## Usage Notes
- Interface attributes come in paired sides with the same ID and name; they are separate objects representing two sides of one conceptual attribute.
- Behavior not explicitly stated above is undocumented; refer to the official API page for details.

