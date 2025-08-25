[CLEAN]

# csc.update.RegularFunction

## Overview
RegularFunction represents a node in Cascadeur’s update/data graph that performs a defined computation over inputs to produce outputs. It manages named input and output attributes (including vector attributes) and can participate in groups within a larger graph. Nodes can be marked as convertible (included in the resulting data graph) or as fictive (e.g., constants, group I/O, or external properties). Specific parameter types and return values are undocumented.

## Class Definition
```python
class RegularFunction:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor for RegularFunction; parameters and behavior are undocumented.

Parameters:
- `*args`: undocumented – variable positional arguments
- `**kwargs`: undocumented – keyword arguments

Returns:
- None

## Methods

### `activity(self)`
Returns activity-related attributes for the node; exact structure is undocumented.

Returns:
- undocumented

### `arguments(self)`
Returns the input arguments of the node; exact structure is undocumented.

Returns:
- undocumented

### `attributes(self, d)`
Returns all input and output attributes; the meaning of `d` is undocumented.

Parameters:
- `d`: undocumented – filter or context

Returns:
- undocumented

### `decrease_vector(self, path, direction)`
Decreases a vector attribute referenced by path; exact semantics are undocumented.

Parameters:
- `path`: undocumented – attribute path
- `direction`: undocumented – adjustment direction or amount

Returns:
- undocumented

### `equal_to(self, arg0)`
Compares the node to another object; comparison details are undocumented.

Parameters:
- `arg0`: undocumented – object to compare

Returns:
- undocumented

### `full_name(self)`
Returns the full hierarchical name including parent nodes.

Returns:
- undocumented

### `func_id(self)`
Returns the function identifier of the node.

Returns:
- undocumented

### `has_input(self, name)`
Checks whether an input attribute with the given name exists.

Parameters:
- `name`: undocumented – input attribute name

Returns:
- undocumented

### `has_output(self, name)`
Checks whether an output attribute with the given name exists.

Parameters:
- `name`: undocumented – output attribute name

Returns:
- undocumented

### `id(self)`
Returns the unique identifier of the node.

Returns:
- undocumented

### `increase_vector(self, path, direction)`
Increases a vector attribute referenced by path; exact semantics are undocumented.

Parameters:
- `path`: undocumented – attribute path
- `direction`: undocumented – adjustment direction or amount

Returns:
- undocumented

### `input(self, name)`
Returns a specific input attribute by name (shortcut when only one exists).

Parameters:
- `name`: undocumented – input attribute name

Returns:
- undocumented

### `inputs(self)`
Returns all input attributes.

Returns:
- undocumented

### `is_active(self)`
Indicates whether the node is active for the current actuality/state; criteria are undocumented.

Returns:
- undocumented

### `is_convertible(self)`
Indicates whether this node will be included in the resulting data graph.

Returns:
- undocumented

### `is_fictive(self)`
Indicates whether this node is fictive (e.g., constants, group I/O, or external properties).

Returns:
- undocumented

### `name(self)`
Returns the node’s name.

Returns:
- undocumented

### `output(self, name)`
Returns a specific output attribute by name (shortcut when only one exists).

Parameters:
- `name`: undocumented – output attribute name

Returns:
- undocumented

### `outputs(self)`
Returns all output attributes.

Returns:
- undocumented

### `parent_group(self)`
Returns the parent group in which this node is located.

Returns:
- undocumented

### `parent_object(self)`
Returns the underlying object of the node.

Returns:
- undocumented

### `remove_attribute(self, attribute)`
Removes one element from a vector attribute; exact behavior is undocumented.

Parameters:
- `attribute`: undocumented – attribute or element identifier

Returns:
- undocumented

### `resize_vector_inputs(self, count, path)`
Resizes an input vector attribute.

Parameters:
- `count`: undocumented – new size
- `path`: undocumented – attribute path

Returns:
- undocumented

### `resize_vector_outputs(self, count, path)`
Resizes an output vector attribute.

Parameters:
- `count`: undocumented – new size
- `path`: undocumented – attribute path

Returns:
- undocumented

### `results(self)`
Returns the output arguments of the node; exact structure is undocumented.

Returns:
- undocumented

### `set_convertible(self, convertible)`
Sets whether this node should be included in the resulting data graph.

Parameters:
- `convertible`: undocumented – truthy/flag value

Returns:
- undocumented

### `set_name(self, name)`
Renames the node.

Parameters:
- `name`: undocumented – new name

Returns:
- undocumented

## Usage Notes
- Names, paths, and vector operations are interface concepts specific to Cascadeur’s update graph; their exact types and error behaviors are undocumented here.
- Use existence checks (has_input/has_output) before accessing attributes by name to avoid runtime errors.
- Convertible and fictive flags influence graph export/inclusion; default behaviors are undocumented.

