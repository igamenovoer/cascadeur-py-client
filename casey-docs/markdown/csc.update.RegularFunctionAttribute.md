[CLEAN]

# csc.update.RegularFunctionAttribute

## Overview
RegularFunctionAttribute represents an attribute of a data function within Cascadeur’s update system. It can be connected to data attributes and queried for its connectivity and direction in the graph. Use it to inspect or modify relationships between function outputs and node attributes. Some parameter and return details are undocumented in the source.

## Class Definition
```python
class csc.update.RegularFunctionAttribute:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a RegularFunctionAttribute instance.

- Parameters:
  - *args: undocumented
  - **kwargs: undocumented
- Returns: undocumented

## Methods

### `connect(self, attribute)`
Connects this function attribute to a data attribute.

- Parameters:
  - attribute: NodeAttribute – data attribute to connect
- Returns: undocumented

### `connected_attributes(self) -> NodeAttribute[]`
Returns attributes currently connected to this function attribute.

- Parameters: none
- Returns: NodeAttribute[] – connected attributes

### `connected_leaves(self, get_only_first)`
Returns connected leaf attributes.

- Parameters:
  - get_only_first: optional – undocumented
- Returns: NodeAttribute[] – connected leaves

### `connected_leaves_in_undirected_graph(self)`
Returns connected leaves considering the graph as undirected.

- Parameters: none
- Returns: undocumented

### `direction(self) -> csc.DirectionValue`
Returns the connection direction for this attribute.

- Parameters: none
- Returns: csc.DirectionValue – undocumented

### `disconnect(*args, **kwargs)`
Disconnects attributes from this function attribute (overloaded).

- Parameters:
  - *args: undocumented
  - **kwargs: undocumented
- Returns: undocumented
- Notes: Overloaded function; specific signatures are undocumented.

### `id(self) -> AttributeId`
Returns the identifier of this attribute.

- Parameters: none
- Returns: AttributeId – attribute identifier

### `is_active(self)`
Reports whether this attribute is active.

- Parameters: none
- Returns: undocumented

### `name(self)`
Returns the name of this attribute.

- Parameters: none
- Returns: undocumented

### `node(self) -> Node`
Returns the owning node.

- Parameters: none
- Returns: Node – owning node reference

## Usage Notes
- Several method details are undocumented in the available source; consult the original API documentation for complete behavior and types where necessary.
- Use connection/query methods to traverse or manage graph relationships in the update system.

