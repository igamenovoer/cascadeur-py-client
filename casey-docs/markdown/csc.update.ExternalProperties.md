[CLEAN]

# csc.update.ExternalProperties

## Overview
ExternalProperties represents a node of external properties in the csc.update system. It can appear anywhere and is used to reflect information such as whether an update is called during interpolation. The API exposes methods to query inputs/outputs, naming, hierarchy, activation state, and related details.

## Class Definition
```python
class csc.update.ExternalProperties
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a new ExternalProperties node.
**Parameters:**
- `*args`: undocumented – positional arguments
- `**kwargs`: undocumented – keyword arguments
**Returns:** undocumented

## Methods

### `attributes(self, d)`
Returns all input and output attributes.
**Parameters:**
- `d`: undocumented – undocumented
**Returns:** undocumented

### `equal_to(self, arg0)`
Undocumented method.
**Parameters:**
- `arg0`: undocumented – undocumented
**Returns:** undocumented

### `full_name(self)`
Returns the name with all parent nodes included.
**Returns:** undocumented

### `has_input(self, name)`
Checks whether there is an input with the given name.
**Parameters:**
- `name`: undocumented – attribute name to check
**Returns:** undocumented

### `has_output(self, name)`
Checks whether there is an output with the given name.
**Parameters:**
- `name`: undocumented – attribute name to check
**Returns:** undocumented

### `id(self)`
Returns a unique identifier for this node.
**Returns:** undocumented

### `input(self, name)`
Shortcut for accessing the input attribute when the node has only one input.
**Parameters:**
- `name`: undocumented – attribute name
**Returns:** undocumented

### `inputs(self)`
Returns all input attributes.
**Returns:** undocumented

### `is_active(self)`
Checks whether the node is active for the current actualities states.
**Returns:** undocumented
**Notes:** Mentioned in context of additional functionality in csc.update.UpdateEditor.

### `is_fictive(self)`
Returns whether the node is fictive (e.g., constants, group inputs/outputs, or external properties).
**Returns:** undocumented

### `name(self)`
Returns the node name.
**Returns:** undocumented

### `output(self, name)`
Shortcut for accessing the output attribute when the node has only one output.
**Parameters:**
- `name`: undocumented – attribute name
**Returns:** undocumented

### `outputs(self)`
Returns all output attributes.
**Returns:** undocumented

### `parent_group(self)`
Returns the parent group in which this node is located.
**Returns:** undocumented

### `parent_object(self)`
Returns the object associated with this node.
**Returns:** undocumented

### `property_outputs(self)`
Undocumented method.
**Returns:** undocumented

### `set_name(self, name)`
Renames the node.
**Parameters:**
- `name`: undocumented – new name
**Returns:** undocumented

## Usage Notes
- Many details of this API are undocumented; method behavior may depend on the broader csc.update system.
- Names and identifiers are intended for navigation and grouping within update graphs.

