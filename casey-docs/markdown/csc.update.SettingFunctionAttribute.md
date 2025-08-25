[CLEAN]

# csc.update.SettingFunctionAttribute

## Overview

SettingFunctionAttribute represents an attribute of a setting function within the Cascadeur update system. It can be connected to setting functions or to the activeness attributes of data functions. The API provides ways to inspect connections, query basic metadata (id, name, node), and check direction and activity state.

## Class Definition

```python
class csc.update.SettingFunctionAttribute
```

## Constructor

### `__init__(*args, **kwargs)`

Initializes a SettingFunctionAttribute instance.

**Parameters:**
- `*args`: undocumented – positional arguments
- `**kwargs`: undocumented – keyword arguments

## Methods

### `connect(self, attribute)`

Connects this attribute to another attribute.

**Parameters:**
- `attribute`: NodeAttribute – attribute to connect

**Returns:**
- undocumented

### `connected_attributes(self) -> NodeAttribute[]`

Returns attributes directly connected to this attribute.

**Returns:**
- NodeAttribute[]: connected attributes

### `connected_leaves(self, get_only_first) -> NodeAttribute[]`

Returns leaf attributes reachable from this attribute; can limit to the first leaf.

**Parameters:**
- `get_only_first`: undocumented – optional flag (behavior undocumented)

**Returns:**
- NodeAttribute[]: connected leaf attributes

### `connected_leaves_in_undirected_graph(self)`

Returns leaf attributes considering connections as an undirected graph.

**Returns:**
- undocumented

### `direction(self) -> csc.DirectionValue`

Gets the direction of this attribute.

**Returns:**
- `csc.DirectionValue`: direction value

### `disconnect(*args, **kwargs)`

Disconnects this attribute; behavior is overloaded.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- undocumented

### `id(self) -> AttributeId`

Gets the unique identifier of this attribute.

**Returns:**
- `AttributeId`: attribute identifier

### `is_active(self)`

Checks whether this attribute is active.

**Returns:**
- undocumented

### `is_out_true(self)`

Checks whether the output state of this attribute is true.

**Returns:**
- undocumented

### `name(self)`

Gets the name of this attribute.

**Returns:**
- undocumented

### `node(self) -> Node`

Gets the owning node of this attribute.

**Returns:**
- `Node`: owning node

### `output_id(self)`

Gets the output identifier of this attribute.

**Returns:**
- undocumented

## Usage Notes

- Can be connected with setting functions or data function activeness attributes.
- Some parameters and return types are undocumented; consult the original API documentation for details.

