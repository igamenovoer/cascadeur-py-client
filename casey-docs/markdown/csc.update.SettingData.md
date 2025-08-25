[CLEAN]

# csc.update.SettingData

## Overview
SettingData represents an update-graph node that performs an operation controlled by a setting. It stores either a boolean or an 8‑bit integer value (range −128 to 127). The class provides helpers for node identity, naming, graph relations (inputs/outputs, parent), and per-frame value access. Use frame-specific overloads to read or write values at a given frame.

## Class Definition
```python
class csc.update.SettingData
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a SettingData node; parameters are undocumented.

Parameters:
- args: undocumented
- kwargs: undocumented

## Methods

### `attributes(d)`
Returns the array of all input and output attributes; details are undocumented.

Parameters:
- d: undocumented

Returns:
- undocumented (array of input and output attributes)

### `data_id()`
Gets the setting’s unique id.

Returns:
- undocumented

### `equal_to(arg0)`
Compares against the provided value or object; details are undocumented.

Parameters:
- arg0: undocumented

Returns:
- undocumented

### `full_name()`
Returns the name including parent node path.

Returns:
- undocumented

### `has_input(name)`
Checks whether there is an input with the given name.

Parameters:
- name: undocumented

Returns:
- undocumented (whether the input exists)

### `has_output(name)`
Checks whether there is an output with the given name.

Parameters:
- name: undocumented

Returns:
- undocumented (whether the output exists)

### `id()`
Gets the unique id of the node.

Returns:
- undocumented

### `input(name)`
Returns an input attribute by name (shortcut if node has only one input); details are undocumented.

Parameters:
- name: undocumented

Returns:
- undocumented

### `inputs()`
Returns the collection of all input attributes.

Returns:
- undocumented (array of input attributes)

### `is_active()`
Checks whether the node is active for the current actualities states.

Returns:
- undocumented

### `is_fictive()`
Indicates whether this is a fictive node (constants, group I/O, or external properties).

Returns:
- undocumented

### `name()`
Gets the node name.

Returns:
- undocumented

### `output(name)`
Returns an output attribute by name.

Parameters:
- name: undocumented

Returns:
- undocumented

### `outputs()`
Returns the collection of all output attributes.

Returns:
- undocumented (array of output attributes)

### `parent_group()`
Returns the parent group where this node is located.

Returns:
- undocumented

### `parent_object()`
Returns the object of the node.

Returns:
- undocumented

### `set_name(name)`
Renames the node.

Parameters:
- name: undocumented

Returns:
- undocumented

### `set_value(value: bool | int) -> None`
Sets the setting value.

Parameters:
- value: bool | int – setting value

Returns:
- None

### `set_value(value: bool | int, frame: int) -> None`
Sets the setting value at a specific frame.

Parameters:
- value: bool | int – setting value
- frame: int – frame index

Returns:
- None

### `value() -> bool | int`
Gets the current setting value.

Returns:
- bool | int – setting value

### `value(frame: int) -> bool | int`
Gets the setting value at a specific frame.

Parameters:
- frame: int – frame index

Returns:
- bool | int – setting value

## Usage Notes
- Integer values are limited to the int8 range (−128 to 127); out-of-range values may be invalid.
- Choose value type (bool vs int) consistently across usage.
- Use the frame-specific overloads to read or write values tied to a particular frame.

