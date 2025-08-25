[CLEAN]

# csc.update.ConstantSettingAttribute

## Overview

Represents an attribute of a constant setting in Cascadeur's update system. It is always an output attribute and can be connected to data functions. Provides utilities to inspect connections, direction, identity, and related node.

## Class Definition

```python
class csc.update.ConstantSettingAttribute
```

## Constructor

### `__init__(*args, **kwargs)`

Constructor for ConstantSettingAttribute; details are undocumented.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- None

## Methods

### `connect(self, attribute)`

Connect this attribute to another attribute; parameter details are partially documented.

**Parameters:**
- `attribute`: NodeAttribute – target attribute to connect

**Returns:**
- undocumented

### `connected_attributes(self) -> NodeAttribute[]`

Returns attributes directly connected to this attribute.

**Parameters:**
- None

**Returns:**
- NodeAttribute[]: connected attributes

### `connected_leaves(self, get_only_first) -> NodeAttribute[]`

Returns connected leaf attributes; the optionality and exact behavior of the flag are undocumented.

**Parameters:**
- `get_only_first`: undocumented (optional) – controls which leaves are returned

**Returns:**
- NodeAttribute[]: connected leaf attributes

### `connected_leaves_in_undirected_graph(self)`

Returns connected leaves considering an undirected graph traversal; details are undocumented.

**Parameters:**
- None

**Returns:**
- undocumented

### `direction(self) -> csc.DirectionValue`

Gets the connection direction value.

**Parameters:**
- None

**Returns:**
- csc.DirectionValue: direction of the attribute

### `disconnect(self, *args, **kwargs)`

Disconnects this attribute; this function is overloaded and specifics are undocumented.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- undocumented

### `id(self) -> AttributeId`

Returns the attribute identifier.

**Parameters:**
- None

**Returns:**
- AttributeId: unique identifier for the attribute

### `is_active(self)`

Indicates whether the attribute is active; details are undocumented.

**Parameters:**
- None

**Returns:**
- undocumented

### `name(self)`

Returns the attribute name; details are undocumented.

**Parameters:**
- None

**Returns:**
- undocumented

### `node(self) -> Node`

Gets the node this attribute belongs to.

**Parameters:**
- None

**Returns:**
- Node: owning node

## Usage Notes

- This attribute is always an output attribute.
- It can be connected with data functions and queried for its connections and metadata.

