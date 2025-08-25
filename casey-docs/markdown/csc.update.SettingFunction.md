[CLEAN]

# csc.update.SettingFunction

## Overview
SettingFunction represents a function node within Cascadeur’s setting/update graph. It provides access to the node’s name, identity, hierarchy, inputs/outputs, and status flags. The API also exposes helpers for working with vector inputs and determining whether a node is active, convertible, or fictive. Details about parameter and return types are largely undocumented.

## Class Definition
```python
class SettingFunction:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`
Initialize a SettingFunction instance.
- Parameters:
  - args: undocumented – positional arguments
  - kwargs: undocumented – keyword arguments
- Returns: undocumented

## Methods

### `arguments()`
Return input attributes for the node.
- Parameters: none
- Returns: undocumented

### `attributes(d)`
Return an array of all input and output attributes.
- Parameters:
  - d: undocumented – selector/context
- Returns: undocumented

### `decrease_input_vector(index)`
Decrease the size of a vector input attribute at the given index.
- Parameters:
  - index: undocumented – position within the vector input
- Returns: undocumented

### `equal_to(arg0)`
Check whether this node is equal to the given object.
- Parameters:
  - arg0: undocumented – object to compare
- Returns: undocumented

### `full_name()`
Get the full name including parent nodes.
- Parameters: none
- Returns: undocumented

### `func_id()`
Get the function’s id.
- Parameters: none
- Returns: undocumented

### `has_input(name)`
Check whether an input with the given name exists.
- Parameters:
  - name: undocumented – input name
- Returns: undocumented

### `has_output(name)`
Check whether an output with the given name exists.
- Parameters:
  - name: undocumented – output name
- Returns: undocumented

### `id()`
Get a unique id for this node.
- Parameters: none
- Returns: undocumented

### `increase_input_vector(index)`
Increase the size of a vector input attribute at the given index.
- Parameters:
  - index: undocumented – position within the vector input
- Returns: undocumented

### `input(name)`
Return the input attribute by name (shortcut for single-input nodes).
- Parameters:
  - name: undocumented – input name
- Returns: undocumented

### `inputs()`
Return an array of all input attributes.
- Parameters: none
- Returns: undocumented

### `is_active()`
Check whether the node is active for the current actuality/state.
- Parameters: none
- Returns: undocumented

### `is_convertible()`
Check whether this function will be included in the resulting setting graph.
- Parameters: none
- Returns: undocumented

### `is_fictive()`
Whether the node is fictive (e.g., constants, group inputs/outputs, or external properties).
- Parameters: none
- Returns: undocumented

### `name()`
Get the node’s name.
- Parameters: none
- Returns: undocumented

### `output(name)`
Return the output attribute by name (shortcut for single-output nodes).
- Parameters:
  - name: undocumented – output name
- Returns: undocumented

### `outputs()`
Return an array of all output attributes.
- Parameters: none
- Returns: undocumented

### `parent_group()`
Return the parent group where this node is located.
- Parameters: none
- Returns: undocumented

### `parent_object()`
Return the underlying object of the node.
- Parameters: none
- Returns: undocumented

### `remove_attribute(attribute)`
Remove one attribute from a vector input.
- Parameters:
  - attribute: undocumented – attribute to remove
- Returns: undocumented

### `resize_vector_inputs(index, count)`
Resize a vector input attribute to the specified count.
- Parameters:
  - index: undocumented – which vector input to resize
  - count: undocumented – new size
- Returns: undocumented

### `results()`
Return the output attributes.
- Parameters: none
- Returns: undocumented

### `set_convertible(convertible)`
Set whether this function will be used in the resulting setting graph.
- Parameters:
  - convertible: undocumented – desired state
- Returns: undocumented

### `set_name(name)`
Rename the node.
- Parameters:
  - name: undocumented – new name
- Returns: undocumented

## Usage Notes
- Parameter and return types are not documented; consult the original API reference for specifics and usage constraints.
- Vector input helpers (increase/decrease/resize) imply index-based operations; ensure index validity in calling code.

