[CLEAN]

# csc.update.SettingDataAttribute

## Overview
SettingDataAttribute represents an attribute of a setting. It can be connected to other setting-related attributes and queried for its connections and direction. This class provides helpers to inspect connected attributes and leaves, as well as access to identity and owning node information. Detailed parameter types and behaviors are largely undocumented in the provided source.

## Class Definition
```python
class csc.update.SettingDataAttribute
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a SettingDataAttribute instance.

- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented

## Methods

### `connect(self, attribute)`
Connects this attribute to another attribute.

- Parameters:
  - `attribute`: NodeAttribute – undocumented
- Returns: undocumented

### `connected_attributes(self) -> NodeAttribute[]`
Returns the attributes directly connected to this attribute.

- Parameters: none
- Returns: `NodeAttribute[]` – undocumented

### `connected_leaves(self, get_only_first) -> NodeAttribute[]`
Returns leaf attributes reachable from this attribute.

- Parameters:
  - `get_only_first`: undocumented
- Returns: `NodeAttribute[]` – undocumented

### `connected_leaves_in_undirected_graph(self)`
Returns leaf attributes when treating the connection graph as undirected.

- Parameters: none
- Returns: undocumented

### `direction(self) -> csc.DirectionValue`
Gets the connection direction for this attribute.

- Parameters: none
- Returns: `csc.DirectionValue` – undocumented

### `disconnect(*args, **kwargs)`
Disconnects this attribute (overloaded; specific signatures are undocumented).

- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented
- Returns: undocumented

### `id(self) -> AttributeId`
Returns the identifier of this attribute.

- Parameters: none
- Returns: `AttributeId` – undocumented

### `is_active(self)`
Indicates whether the attribute is active.

- Parameters: none
- Returns: undocumented

### `name(self)`
Returns the name of the attribute.

- Parameters: none
- Returns: undocumented

### `node(self) -> Node`
Returns the node that owns this attribute.

- Parameters: none
- Returns: `Node` – undocumented

## Attributes

- `attribute`: NodeAttribute – underlying attribute reference (undocumented)

## Usage Notes

- Many parameter types and behaviors are undocumented; consult original source if available.
- Connection queries may depend on graph directionality; use the undirected variant when needed.

