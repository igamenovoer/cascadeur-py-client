[CLEAN]

# csc.update.InterfaceNode

## Overview
InterfaceNode represents a node inside a group that models its connections to nodes outside the group. It provides ways to query and manage input and output interface attributes and their direction. It can report whether it is active for current actualities states and whether it is a fictive node (e.g., constants, group inputs/outputs, or external properties). Identification and parent references are also available.

## Class Definition
```python
class csc.update.InterfaceNode
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor (undocumented).

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- None

## Methods

### `add_attribute(name)`
Add an interface attribute (details undocumented).

**Parameters:**
- `name`: undocumented – attribute name

**Returns:**
- undocumented

### `attributes(d)`
Return array of all input and output attributes.

**Parameters:**
- `d`: undocumented – selector or filter

**Returns:**
- array of attributes (undocumented element type)

### `direction() -> csc.DirectionValue`
Get the node's direction.

**Parameters:**
- None

**Returns:**
- csc.DirectionValue

### `equal_to(arg0)`
Check equality with the provided object (semantics undocumented).

**Parameters:**
- `arg0`: undocumented – object to compare

**Returns:**
- undocumented

### `full_name()`
Get the fully qualified name including all parent nodes.

**Parameters:**
- None

**Returns:**
- undocumented

### `has_input(name)`
Check whether there is an input with the given name.

**Parameters:**
- `name`: undocumented – input name

**Returns:**
- undocumented

### `has_output(name)`
Check whether there is an output with the given name.

**Parameters:**
- `name`: undocumented – output name

**Returns:**
- undocumented

### `id()`
Get the unique id.

**Parameters:**
- None

**Returns:**
- undocumented

### `input(name)`
Shortcut to access an input attribute when the node has only one input attribute.

**Parameters:**
- `name`: undocumented – input name

**Returns:**
- undocumented

### `inputs()`
Return the array of input attributes.

**Parameters:**
- None

**Returns:**
- array of attributes (undocumented element type)

### `interface_attributes() -> InterfaceAttribute[]`
Return the list of interface attributes.

**Parameters:**
- None

**Returns:**
- InterfaceAttribute[]

### `is_active()`
Check whether the node is active for current actualities states.

**Parameters:**
- None

**Returns:**
- undocumented

### `is_fictive()`
Determine whether the node is fictive (constants, group inputs/outputs, or external properties).

**Parameters:**
- None

**Returns:**
- undocumented

### `move_attribute(attribute: InterfaceAttribute, position: int)`
Move an interface attribute to a new position.

**Parameters:**
- `attribute`: InterfaceAttribute – attribute to move
- `position`: int – target position

**Returns:**
- undocumented

### `name()`
Get the node's name.

**Parameters:**
- None

**Returns:**
- undocumented

### `output(name)`
Shortcut to access an output attribute when the node has only one output attribute.

**Parameters:**
- `name`: undocumented – output name

**Returns:**
- undocumented

### `outputs()`
Return the array of output attributes.

**Parameters:**
- None

**Returns:**
- array of attributes (undocumented element type)

### `parent_group()`
Return the parent group where this node is located.

**Parameters:**
- None

**Returns:**
- undocumented

### `parent_object()`
Return the underlying object of the node.

**Parameters:**
- None

**Returns:**
- undocumented

### `remove_attribute(attribute: InterfaceAttribute)`
Remove an interface attribute.

**Parameters:**
- `attribute`: InterfaceAttribute – attribute to remove

**Returns:**
- undocumented

### `set_name(name)`
Rename the node.

**Parameters:**
- `name`: undocumented – new name

**Returns:**
- undocumented

## Usage Notes
- input(name) and output(name) are shortcuts intended for nodes with a single input or output attribute.
- is_active() depends on current actualities states (see csc.update.UpdateEditor); behavior is otherwise undocumented.
- is_fictive() indicates nodes that represent constants, group inputs/outputs, or external properties.

