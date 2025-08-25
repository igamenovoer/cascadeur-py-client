[CLEAN]

# csc.update.RegularDataAttribute

## Overview
RegularDataAttribute represents an attribute of regular data within Cascadeur's update graph.  
It can be connected to other node attributes and participates in graph connectivity used by data functions.  
Use it to query connected attributes, evaluate graph direction, and access identifying information like node and id.

## Class Definition
```python
class csc.update.RegularDataAttribute
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a RegularDataAttribute instance.

- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented

## Methods

### `connect(self, attribute)`
Connects this attribute to another node attribute.

- Parameters:
  - `attribute`: NodeAttribute – undocumented
- Returns: undocumented

### `connected_attributes(self) -> NodeAttribute[]`
Returns attributes directly connected to this attribute.

- Parameters: none
- Returns: NodeAttribute[] – undocumented

### `connected_leaves(self, get_only_first)`
Returns leaf attributes reachable from this attribute.

- Parameters:
  - `get_only_first`: undocumented
- Returns: NodeAttribute[] – undocumented
- Notes: Parameter appears optional in the upstream documentation.

### `connected_leaves_in_undirected_graph(self)`
Returns leaf attributes considering the graph as undirected.

- Parameters: none documented
- Returns: undocumented

### `direction(self) -> csc.DirectionValue`
Gets the connection direction for this attribute.

- Parameters: none
- Returns: `csc.DirectionValue` – undocumented

### `disconnect(self, *args, **kwargs)`
Disconnects this attribute (overloaded function).

- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented
- Returns: undocumented
- Notes: Overloaded behavior is undocumented.

### `id(self) -> AttributeId`
Returns the identifier of this attribute.

- Parameters: none
- Returns: `AttributeId` – undocumented

### `is_active(self)`
Indicates whether this attribute is active.

- Parameters: none
- Returns: undocumented

### `name(self)`
Returns the name of this attribute.

- Parameters: none
- Returns: undocumented

### `node(self) -> Node`
Returns the node this attribute belongs to.

- Parameters: none
- Returns: `Node` – undocumented

## Usage Notes
- Specific parameter types and behaviors are minimally documented; refer to the original API reference for details.
- When unsure about overloads or return structures, inspect objects at runtime or consult upstream examples.

