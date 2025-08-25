[CLEAN]

# csc.update.Node

## Overview
csc.update.Node represents a generic node in the update system and provides behavior common to all nodes. It lets you query inputs and outputs, retrieve names and identifiers, and navigate relationships to parent groups and objects. The API also exposes checks for activation state and whether a node is fictive (e.g., constants or group I/O). This is a foundational building block used by update editors and related tooling.

## Class Definition
```python
class Node
```

## Constructor

### `__init__(*args, **kwargs)`
Initialize a Node instance. Details are undocumented.

**Parameters:**
- `*args`: undocumented – implementation-specific arguments
- `**kwargs`: undocumented – implementation-specific keyword arguments

**Returns:**
- None

## Methods

### `attributes(d)`
Return all input and output attributes. Further details are undocumented.

**Parameters:**
- `d`: undocumented – undocumented

**Returns:**
- undocumented

### `equal_to(arg0)`
Check whether this node is equal to another. Further details are undocumented.

**Parameters:**
- `arg0`: undocumented – object to compare against

**Returns:**
- undocumented

### `full_name()`
Get the node name including all parent nodes.

**Parameters:**
- None

**Returns:**
- undocumented

### `has_input(name)`
Check if there is an input with the given name.

**Parameters:**
- `name`: undocumented – input name to check

**Returns:**
- undocumented

### `has_output(name)`
Check if there is an output with the given name.

**Parameters:**
- `name`: undocumented – output name to check

**Returns:**
- undocumented

### `id()`
Get a unique identifier for the node.

**Parameters:**
- None

**Returns:**
- undocumented

### `input(name)`
Access an input attribute by name; may act as a shortcut when the node has only one input attribute.

**Parameters:**
- `name`: undocumented – input name

**Returns:**
- undocumented

### `inputs()`
Return all input attributes.

**Parameters:**
- None

**Returns:**
- undocumented

### `is_active()`
Check whether the node is active for the current actualities states.

**Parameters:**
- None

**Returns:**
- undocumented

**Notes:**
- See Additional functionality in csc.update.UpdateEditor.

### `is_fictive()`
Check whether this is a fictive node (e.g., constants, inputs/outputs of a group, or external properties).

**Parameters:**
- None

**Returns:**
- undocumented

### `name()`
Get the node name.

**Parameters:**
- None

**Returns:**
- undocumented

### `output(name)`
Access an output attribute by name; may act as a shortcut when the node has only one output attribute.

**Parameters:**
- `name`: undocumented – output name

**Returns:**
- undocumented

### `outputs()`
Return all output attributes.

**Parameters:**
- None

**Returns:**
- undocumented

### `parent_group()`
Return the parent group in which this group node is located.

**Parameters:**
- None

**Returns:**
- undocumented

### `parent_object()`
Return the object of the node.

**Parameters:**
- None

**Returns:**
- undocumented

**Notes:**
- Will return null if this is not an update group.

### `set_name(name)`
Rename the node.

**Parameters:**
- `name`: undocumented – new node name

**Returns:**
- undocumented

## Usage Notes
- Some behaviors depend on the update editor context; consult csc.update.UpdateEditor for additional functionality.
- Input/output accessors may behave as shortcuts when only a single attribute exists on that side.

