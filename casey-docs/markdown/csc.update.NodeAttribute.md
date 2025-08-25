[CLEAN]

# csc.update.NodeAttribute

## Overview

NodeAttribute represents a generic node attribute within Cascadeur's update system. It provides operations to connect or disconnect attributes, query connection topology (direct connections and leaves), and inspect metadata such as direction, id, name, and the owning node. Use it to manage graph relationships between nodes' attributes.

## Class Definition

```python
class csc.update.NodeAttribute
```

## Constructor

### `__init__(self, *args, **kwargs)`

Constructor for NodeAttribute.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

## Methods

### `connect(self, attribute: csc.update.NodeAttribute)`

Connect this attribute to another attribute.

**Parameters:**
- `attribute`: csc.update.NodeAttribute – undocumented

**Returns:**
- undocumented

### `disconnect(self) -> None`

Disconnect this attribute from all connected attributes.

**Returns:**
- None

### `disconnect(self, attribute: csc.update.NodeAttribute) -> None`

Disconnect this attribute from the specified attribute.

**Parameters:**
- `attribute`: csc.update.NodeAttribute – undocumented

**Returns:**
- None

### `connected_attributes(self) -> NodeAttribute[]`

Return attributes directly connected to this attribute.

**Returns:**
- `NodeAttribute[]`: undocumented

### `connected_leaves(self[, get_only_first]) -> NodeAttribute[]`

Return leaf attributes reachable from this attribute.

**Parameters:**
- `get_only_first`: undocumented, optional

**Returns:**
- `NodeAttribute[]`: undocumented

### `connected_leaves_in_undirected_graph(self)`

Return leaf attributes considering the graph as undirected.

**Returns:**
- undocumented

### `direction(self) -> csc.DirectionValue`

Get the connection direction of this attribute.

**Returns:**
- `csc.DirectionValue`: undocumented

### `id(self) -> AttributeId`

Get the identifier of this attribute.

**Returns:**
- `AttributeId`: undocumented

### `is_active(self)`

Report whether this attribute is active.

**Returns:**
- undocumented

### `name(self)`

Get the name of this attribute.

**Returns:**
- undocumented

### `node(self) -> Node`

Get the node that owns this attribute.

**Returns:**
- `Node`: undocumented

## Usage Notes

- Types and behavioral details are minimally documented here; consult the original source for specifics.

