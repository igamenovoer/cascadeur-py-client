[CLEAN]

# csc.update.RegularData

## Overview
RegularData represents a data node in Cascadeur's update system. It can be Static or Animation data and exposes input/output attributes, identity, and hierarchy information. For Animation data, values may be accessed or set per frame, with interpolation controls such as Euler filtering, explicit linear mode, and configurable lerp mode. The API allows querying actual/active state, connectivity, and parent relationships, and reading or writing values.

## Class Definition
```python
class csc.update.RegularData
```

## Constructor

### `__init__(*args, **kwargs)`
Create a RegularData instance.
- Parameters:
  - args: undocumented – positional arguments.
  - kwargs: undocumented – keyword arguments.

## Methods

### `actuality()`
Output attribute providing the actuality status.
- Returns: undocumented.

### `attribute(d)`
Get attribute by direction.
- Parameters:
  - d: undocumented – direction specifier.
- Returns: undocumented.

### `attributes(d)`
Return all input and/or output attributes for a given direction.
- Parameters:
  - d: undocumented – direction specifier.
- Returns: undocumented.

### `data_id()`
Get the data identifier.
- Returns: undocumented.

### `equal_to(arg0)`
Check equality with another object/value.
- Parameters:
  - arg0: undocumented – object or value to compare.
- Returns: undocumented.

### `full_name()`
Get the name with all parent nodes.
- Returns: undocumented.

### `get_apply_euler_filter()`
Get the current "apply Euler filter" setting.
- Returns: undocumented.

### `get_explicit_linear()`
Get the current explicit-linear interpolation setting.
- Returns: undocumented.

### `get_lerp_mode()`
Get the current lerp mode.
- Returns: undocumented.

### `has_input(name)`
Check if there is an input with the given name.
- Parameters:
  - name: undocumented – input name to check.
- Returns: undocumented.

### `has_output(name)`
Check if there is an output with the given name.
- Parameters:
  - name: undocumented – output name to check.
- Returns: undocumented.

### `id()`
Get a unique id.
- Returns: undocumented.

### `input()`
Get the input attribute.
- Returns: undocumented.

### `inputs()`
Get all input attributes.
- Returns: undocumented.

### `is_active()`
Check whether it is active for the current actuality states.
- Returns: undocumented.
- Notes: See additional functionality in csc.update.UpdateEditor.

### `is_actual()`
Check if this data is set to actual.
- Returns: undocumented.
- Notes: See additional functionality in csc.update.UpdateEditor.

### `is_fictive()`
Whether this is a fictive node (e.g., constants, group I/O, external properties).
- Returns: undocumented.

### `mode()`
Check if data is Animation or Static.
- Returns: undocumented.

### `name()`
Get the name.
- Returns: undocumented.

### `output()`
Get the output attribute.
- Returns: undocumented.

### `outputs()`
Get all output attributes.
- Returns: undocumented.

### `parent_group()`
Return the parent group (location of this group node).
- Returns: undocumented.

### `parent_object()`
Return the object of the node.
- Returns: undocumented.

### `remove_period()`
In interpolation, remove the existing period.
- Returns: undocumented.

### `set_actual(act)`
Set this data as actual.
- Parameters:
  - act: undocumented – actuality flag/value.
- Returns: undocumented.
- Notes: See additional functionality in csc.update.UpdateEditor.

### `set_apply_euler_filter(apply_euler_filter)`
Set the "apply Euler filter" option.
- Parameters:
  - apply_euler_filter: undocumented.
- Returns: undocumented.

### `set_description_value(name)`
Set description value.
- Parameters:
  - name: undocumented.
- Returns: undocumented.

### `set_explicit_linear(explicit_linear)`
Set the explicit-linear interpolation mode.
- Parameters:
  - explicit_linear: undocumented.
- Returns: undocumented.

### `set_lerp_mode(mode)`
Set the lerp mode (can be slerp for Vector3 data).
- Parameters:
  - mode: undocumented.
- Returns: undocumented.

### `set_name(name)`
Rename the node.
- Parameters:
  - name: undocumented – new name.
- Returns: undocumented.

### `set_period(period)`
In interpolation, fix the period to provide smoothness.
- Parameters:
  - period: undocumented.
- Returns: undocumented.

### `set_value(v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None`
Set the data value.
- Parameters:
  - v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – value to set.
- Returns: None.
- Notes: For Animation data, a frame may be required.

### `set_value(v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], frame: int) -> None`
Set the data value at a specific frame.
- Parameters:
  - v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – value to set.
  - frame: int – target frame.
- Returns: None.

### `value() -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]`
Get the current data value.
- Returns: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]].
- Notes: For Animation data, a frame may be required.

### `value(frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]`
Get the data value at a specific frame.
- Parameters:
  - frame: int – target frame.
- Returns: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]].

## Usage Notes
- If the data is Animation, value access and setting may require a frame parameter.
- Lerp mode can be set (e.g., slerp for Vector3 data); Euler filtering and explicit-linear options affect interpolation behavior.
- Fictive nodes include constants, group I/O, and external properties.

