[CLEAN]

# csc.update.ExternalPropertyAttribute

## Overview

ExternalPropertyAttribute represents an attribute of the external properties of an update. It is always an output attribute. It is settings-based and can be connected with setting functions or data functions activity. The class provides methods to establish and inspect connections, and to query direction and identifiers.

## Class Definition

```python
class csc.update.ExternalPropertyAttribute
```

## Constructor

### `__init__(*args, **kwargs)`

Constructor for ExternalPropertyAttribute.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

## Methods

### `connect(attribute: NodeAttribute)`

Connect this attribute to another attribute.

**Parameters:**
- `attribute`: NodeAttribute – undocumented

**Returns:**
- undocumented

### `connected_attributes() -> NodeAttribute[]`

Return the attributes directly connected to this attribute.

**Parameters:**
- none

**Returns:**
- `NodeAttribute[]`: undocumented

### `connected_leaves(get_only_first)` -> NodeAttribute[]`

Return connected leaf attributes.

**Parameters:**
- `get_only_first`: undocumented (optional)

**Returns:**
- `NodeAttribute[]`: undocumented

### `connected_leaves_in_undirected_graph()`

Return connected leaves considering an undirected graph.

**Parameters:**
- none

**Returns:**
- undocumented

### `direction() -> csc.DirectionValue`

Get the direction of this attribute.

**Parameters:**
- none

**Returns:**
- `csc.DirectionValue`: undocumented

### `disconnect(*args, **kwargs)`

Disconnect this attribute (overloaded function).

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- undocumented

### `id() -> AttributeId`

Get the identifier of this attribute.

**Parameters:**
- none

**Returns:**
- `AttributeId`: undocumented

### `is_active()`

Check whether the attribute is active.

**Parameters:**
- none

**Returns:**
- undocumented

### `name()`

Get the name of the attribute.

**Parameters:**
- none

**Returns:**
- undocumented

### `node() -> Node`

Get the node associated with this attribute.

**Parameters:**
- none

**Returns:**
- `Node`: undocumented

## Usage Notes

- This attribute is always an output attribute.
- Connection details and parameter specifics are undocumented; refer to original API documentation for precise behavior.

