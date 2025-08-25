[CLEAN]

# csc.update.ConstantDataAttribute

## Overview

ConstantDataAttribute represents an attribute of a constant regular data object in the update system. It is always an output attribute. It can be connected to setting functions or data functions activities. The API exposes utilities to connect/disconnect and to inspect connectivity, identity, and direction.

## Class Definition

```python
class csc.update.ConstantDataAttribute:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a ConstantDataAttribute instance.

- Parameters: undocumented
- Returns: undocumented

## Methods

### `connect(self, attribute: NodeAttribute)`
Connect this output attribute to the given target attribute.

- Parameters:
  - attribute: NodeAttribute – target attribute to connect to
- Returns: undocumented

### `connected_attributes(self) -> NodeAttribute[]`
Return the attributes directly connected to this attribute.

- Returns: NodeAttribute[] – connected attributes

### `connected_leaves(self[, get_only_first]) -> NodeAttribute[]`
Return leaf attributes reachable from this attribute.

- Parameters:
  - get_only_first: undocumented – optional flag; meaning undocumented
- Returns: NodeAttribute[] – connected leaf attributes

### `connected_leaves_in_undirected_graph(self)`
Return leaves when considering the graph as undirected.

- Returns: undocumented

### `direction(self) -> csc.DirectionValue`
Get the direction of this attribute.

- Returns: csc.DirectionValue – attribute direction

### `disconnect(self, *args, **kwargs)`
Disconnect this attribute from connected attributes.

- Parameters:
  - *args: undocumented – overload parameters
  - **kwargs: undocumented – overload parameters
- Returns: undocumented
- Notes: Overloaded function

### `id(self) -> AttributeId`
Get the identifier of this attribute.

- Returns: AttributeId – attribute identifier

### `is_active(self)`
Whether this attribute is active.

- Returns: undocumented

### `name(self)`
Get the name of this attribute.

- Returns: undocumented

### `node(self) -> Node`
Get the owning node of this attribute.

- Returns: Node – owning node

## Usage Notes

- This attribute is output-only.
- Can be connected to setting functions or data functions activities.
- Some parameter and return types are undocumented in the source.

