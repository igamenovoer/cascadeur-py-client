[CLEAN]

# csc.update.ConstantSettings

## Overview

ConstantSettings represents a node for holding constant settings within the Cascadeur update system. It can appear wherever constant values are needed and connects via inputs and outputs like other nodes. Use it to provide fixed values to other parts of an update graph. Detailed behavior is largely undocumented in the source material.

## Class Definition

```python
class csc.update.ConstantSettings
```

## Constructor

### `__init__(*args, **kwargs)`

Initialize a ConstantSettings node; details are undocumented.

**Parameters:**
- `*args`: undocumented – undocumented
- `**kwargs`: undocumented – undocumented

## Methods

### `add_setting(self, name, value)`

Add a setting with the given name and value.

**Parameters:**
- `name`: undocumented – setting name
- `value`: Setting.Value – setting value

**Returns:**
- undocumented

### `attributes(self, d)`

Return all input and output attributes.

**Parameters:**
- `d`: undocumented – undocumented

**Returns:**
- array of all input and output attributes

### `equal_to(self, arg0)`

Equality check; undocumented.

**Parameters:**
- `arg0`: undocumented – value or node to compare

**Returns:**
- undocumented

### `full_name(self)`

Return the full name including parent nodes.

**Parameters:**
- none

**Returns:**
- name with all the parent nodes

### `has_input(self, name)`

Check if there is an input with the given name.

**Parameters:**
- `name`: undocumented – input name to check

**Returns:**
- undocumented

### `has_output(self, name)`

Check if there is an output with the given name.

**Parameters:**
- `name`: undocumented – output name to check

**Returns:**
- undocumented

### `id(self)`

Return a unique identifier for this node.

**Parameters:**
- none

**Returns:**
- unique id

### `input(self, name)`

Get an input attribute by name; serves as a shortcut when the node has only one input.

**Parameters:**
- `name`: undocumented – input name

**Returns:**
- input attribute (undocumented)

### `inputs(self)`

Return all input attributes.

**Parameters:**
- none

**Returns:**
- array of all input attributes

### `is_active(self)`

Check whether the node is active for the current actualities states.

**Parameters:**
- none

**Returns:**
- undocumented

### `is_fictive(self)`

Return whether this is a fictive node (e.g., constants, group I/O, or external properties).

**Parameters:**
- none

**Returns:**
- undocumented

### `name(self)`

Get the node name.

**Parameters:**
- none

**Returns:**
- name

### `output(self, name)`

Get an output attribute by name; serves as a shortcut when the node has only one output.

**Parameters:**
- `name`: undocumented – output name

**Returns:**
- output attribute (undocumented)

### `outputs(self)`

Return all output attributes.

**Parameters:**
- none

**Returns:**
- array of all output attributes

### `parent_group(self)`

Return the parent group in which this node is located.

**Parameters:**
- none

**Returns:**
- parent group

### `parent_object(self)`

Return the underlying object of the node.

**Parameters:**
- none

**Returns:**
- node object

### `set_name(self, name)`

Rename the node.

**Parameters:**
- `name`: undocumented – new name

**Returns:**
- undocumented

## Attributes

- `value`: Setting.Value – undocumented

## Usage Notes

- Method behavior and types are largely undocumented in the source; verify against the Cascadeur version you use.
- Some methods may be properties in practice; treat names and returns accordingly based on actual API behavior.

