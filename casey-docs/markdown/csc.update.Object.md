[CLEAN]

# csc.update.Object

## Overview
Object represents an object node in the Cascadeur update graph. Its functionality is limited and, in most cases, an update group node should be preferred. It provides basic access to identity (name/IDs), hierarchy (parent/root groups), and connections via input/output attributes.

## Class Definition
```python
class csc.update.Object
```

## Constructor

### `__init__(*args, **kwargs)`
Initialize a new Object node (details undocumented).

**Parameters:**
- args: undocumented – variable positional arguments (undocumented)
- kwargs: undocumented – variable keyword arguments (undocumented)

## Methods

### `add_input(self, name) -> InterfaceAttribute`
Add an input attribute with the given name.

**Parameters:**
- name: undocumented – input attribute name

**Returns:**
- InterfaceAttribute: undocumented

### `add_output(self, name) -> InterfaceAttribute`
Add an output attribute with the given name.

**Parameters:**
- name: undocumented – output attribute name

**Returns:**
- InterfaceAttribute: undocumented

### `attributes(self, d)`
Return all input and output attributes.

**Parameters:**
- d: undocumented – undocumented

**Returns:**
- undocumented

### `equal_to(self, arg0)`
Check equality with the given object.

**Parameters:**
- arg0: undocumented – object/value to compare

**Returns:**
- undocumented

### `full_name(self)`
Return the full hierarchical name including parent nodes.

**Returns:**
- undocumented

### `has_input(self, name)`
Check whether an input with the given name exists.

**Parameters:**
- name: undocumented – input attribute name

**Returns:**
- undocumented

### `has_output(self, name)`
Check whether an output with the given name exists.

**Parameters:**
- name: undocumented – output attribute name

**Returns:**
- undocumented

### `id(self)`
Return the unique identifier of the node.

**Returns:**
- undocumented

### `input(self, name)`
Return an input attribute by name; for single-input nodes this acts as a shortcut.

**Parameters:**
- name: undocumented – input attribute name

**Returns:**
- undocumented

### `inputs(self)`
Return all input attributes.

**Returns:**
- undocumented

### `is_active(self)`
Return whether the node is active for the current actuality states.

**Returns:**
- undocumented

### `is_fictive(self)`
Return whether the node is fictive (e.g., constants, group inputs/outputs, external properties).

**Returns:**
- undocumented

### `name(self)`
Return the node’s name.

**Returns:**
- undocumented

### `object_id(self)`
Return the node’s object identifier.

**Returns:**
- undocumented

### `output(self, name)`
Return an output attribute by name; for single-output nodes this acts as a shortcut.

**Parameters:**
- name: undocumented – output attribute name

**Returns:**
- undocumented

### `outputs(self)`
Return all output attributes.

**Returns:**
- undocumented

### `parent_group(self)`
Return the parent update group that contains this node.

**Returns:**
- undocumented

### `parent_object(self)`
Return the underlying object of this node.

**Returns:**
- undocumented

### `root_group(self) -> UpdateGroup`
Return the root update group.

**Returns:**
- UpdateGroup: undocumented

### `set_name(self, name)`
Rename the node.

**Parameters:**
- name: undocumented – new name

**Returns:**
- undocumented

## Usage Notes
- Functionality is limited; when possible, prefer using an update group node instead.
- Many parameter and return types are undocumented in the source; consult the official Cascadeur Python API for authoritative details.

