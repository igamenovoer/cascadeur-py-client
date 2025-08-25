[CLEAN]

# csc.update.ActivityAttribute

## Overview
ActivityAttribute represents a boolean flag indicating whether a data function is active. When true the function is active; when false it is inactive; when unset the function is treated as always active. This attribute is input-only and participates in a node graph via connections to other attributes.

## Class Definition
```python
class csc.update.ActivityAttribute
```

## Constructor
### `__init__(*args, **kwargs)`
Initializes an ActivityAttribute instance; detailed behavior is undocumented.

Parameters:
- `*args`: undocumented – additional positional arguments.
- `**kwargs`: undocumented – additional keyword arguments.

Returns:
- None

## Methods
### `connect(attribute: NodeAttribute)`
Connect this attribute to another node attribute.

Parameters:
- `attribute`: NodeAttribute – target attribute to connect to.

Returns:
- undocumented

### `connected_attributes() -> list[NodeAttribute]`
Return attributes directly connected to this attribute.

Returns:
- list[NodeAttribute] – connected attributes.

### `connected_leaves(get_only_first: undocumented = undocumented) -> list[NodeAttribute]`
Return leaf attributes reachable from this attribute; exact traversal semantics are undocumented.

Parameters:
- `get_only_first`: undocumented – optional flag controlling selection; default is undocumented.

Returns:
- list[NodeAttribute] – reachable leaf attributes.

### `connected_leaves_in_undirected_graph()`
Return leaf attributes considering an undirected version of the graph; specifics are undocumented.

Returns:
- undocumented

### `direction() -> csc.DirectionValue`
Return the connection direction for this attribute.

Returns:
- csc.DirectionValue – undocumented

### `disconnect(*args, **kwargs)`
Disconnect this attribute from other attributes; this method is overloaded.

Parameters:
- `*args`: undocumented – overload-specific positional arguments.
- `**kwargs`: undocumented – overload-specific keyword arguments.

Returns:
- undocumented

### `id() -> AttributeId`
Return the identifier of this attribute.

Returns:
- AttributeId – undocumented

### `is_active() -> bool`
Report whether the associated function is considered active.

Returns:
- bool – True if active, False otherwise.

Notes:
- If the value is not set, the function is treated as always active.

### `name()`
Return the name of this attribute.

Returns:
- undocumented

### `node() -> Node`
Return the node that owns this attribute.

Returns:
- Node – undocumented

## Usage Notes
- This is an input-only attribute; it is not intended to be written by the system at runtime.
- When unset, the function is considered always active; otherwise a boolean value governs activity.
- Use the connection helpers to inspect graph relationships or to attach/detach this attribute from others.

