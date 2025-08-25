[CLEAN]

# csc.update.ActualityAttribute

## Overview
ActualityAttribute indicates whether data is actual at the start of a graph update. It is always an output attribute. It can be connected using setting functions. Direct connections with data functions activity are not supported; use a copy setting function instead.

## Class Definition
```python
class csc.update.ActualityAttribute:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor for ActualityAttribute.
- Parameters: undocumented

## Methods

### `connect(self, attribute)`
Connects this attribute to another attribute via a setting function.
- Parameters:
  - attribute: NodeAttribute – undocumented
- Returns: undocumented

### `connected_attributes(self) -> NodeAttribute[]`
Returns attributes connected to this attribute.
- Parameters: none
- Returns: NodeAttribute[] – undocumented

### `connected_leaves(self, get_only_first=None) -> NodeAttribute[]`
Returns connected leaf attributes, optionally only the first.
- Parameters:
  - get_only_first: undocumented – optional
- Returns: NodeAttribute[] – undocumented

### `connected_leaves_in_undirected_graph(self)`
Returns connected leaves in an undirected graph context.
- Parameters: none
- Returns: undocumented

### `direction(self) -> csc.DirectionValue`
Gets the attribute direction.
- Parameters: none
- Returns: csc.DirectionValue – undocumented

### `disconnect(*args, **kwargs)`
Disconnects this attribute (overloaded function).
- Parameters: undocumented
- Returns: undocumented
- Notes: Overloaded; argument forms are undocumented.

### `id(self) -> AttributeId`
Returns the identifier of this attribute.
- Parameters: none
- Returns: AttributeId – undocumented

### `is_active(self)`
Reports whether the attribute is active.
- Parameters: none
- Returns: undocumented

### `name(self)`
Returns the attribute name.
- Parameters: none
- Returns: undocumented

### `node(self) -> Node`
Returns the owning node.
- Parameters: none
- Returns: Node – undocumented

## Usage Notes
- This is always an output attribute.
- Use setting functions to connect this attribute.
- Direct connections with data functions activity are not supported; use a copy setting function instead.

