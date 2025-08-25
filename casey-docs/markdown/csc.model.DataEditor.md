[CLEAN]

# csc.model.DataEditor

## Overview

DataEditor provides capabilities to add, edit, and remove scene data and settings in Cascadeur. It supports setting values at specific frames, managing descriptions, and working with both data and settings identifiers. Several methods are overloaded to accept different argument combinations. Exact behaviors for some utility methods are undocumented in the provided source.

## Class Definition

```python
class csc.model.DataEditor:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new DataEditor instance.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

## Methods

### `add_constant_data(arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data`

Adds a constant data entry by name.

**Parameters:**
- `arg0`: str – undocumented
- `arg1`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented

**Returns:**
- `csc.model.Data`: the created data

### `add_constant_data(name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data`

Adds a constant data entry with an explicit id.

**Parameters:**
- `name`: str – undocumented
- `value`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented
- `id`: csc.model.DataId – undocumented

**Returns:**
- `csc.model.Data`: the created data

### `add_constant_setting(arg0: str, arg1: Union[bool, int]) -> csc.model.Setting`

Adds a constant setting by name.

**Parameters:**
- `arg0`: str – undocumented
- `arg1`: Union[bool, int] – undocumented

**Returns:**
- `csc.model.Setting`: the created setting

### `add_constant_setting(name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting`

Adds a constant setting with an explicit id.

**Parameters:**
- `name`: str – undocumented
- `value`: Union[bool, int] – undocumented
- `id`: csc.model.SettingId – undocumented

**Returns:**
- `csc.model.Setting`: the created setting

### `add_data(object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data`

Adds a data entry to an object with the given mode and value.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented
- `name`: str – undocumented
- `mode`: csc.model.DataMode – undocumented
- `value`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented

**Returns:**
- `csc.model.Data`: the created data

### `add_data(object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data`

Adds a data entry to an object with an explicit id.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented
- `name`: str – undocumented
- `mode`: csc.model.DataMode – undocumented
- `value`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented
- `id`: csc.model.DataId – undocumented

**Returns:**
- `csc.model.Data`: the created data

### `add_description(name, id)`

Adds a description entry for a given name and id.

**Parameters:**
- `name`: undocumented
- `id`: undocumented

**Returns:**
- None

### `add_setting(object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting`

Adds a setting to an object with an optional mode.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented
- `name`: str – undocumented
- `value`: Union[bool, int] – undocumented
- `mode`: csc.model.SettingMode – undocumented (default: <SettingMode.Static: 0>)

**Returns:**
- `csc.model.Setting`: the created setting

### `add_setting(object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting`

Adds a setting to an object with an explicit id.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented
- `name`: str – undocumented
- `value`: Union[bool, int] – undocumented
- `mode`: csc.model.SettingMode – undocumented
- `id`: csc.model.SettingId – undocumented

**Returns:**
- `csc.model.Setting`: the created setting

### `change_description(name, description)`

Changes the description text for a given name.

**Parameters:**
- `name`: undocumented
- `description`: undocumented

**Returns:**
- None

### `cluster_editor() -> ClusterEditor`

Returns a ClusterEditor interface.

**Parameters:**
- None

**Returns:**
- `ClusterEditor`: undocumented

### `copy_data(from_to)`

Copies data between identifiers.

**Parameters:**
- `from_to`: undocumented

**Returns:**
- None

### `delete_data(id)`

Deletes a data entry.

**Parameters:**
- `id`: undocumented

**Returns:**
- None

### `delete_setting(id)`

Deletes a setting entry.

**Parameters:**
- `id`: undocumented

**Returns:**
- None

### `remove_description(name)`

Removes a description entry for the given name.

**Parameters:**
- `name`: undocumented

**Returns:**
- None

### `reset_description_value(id: csc.model.DataId) -> None`

Resets the description value for a data id.

**Parameters:**
- `id`: csc.model.DataId – undocumented

**Returns:**
- None

### `reset_description_value(id: csc.model.SettingId) -> None`

Resets the description value for a setting id.

**Parameters:**
- `id`: csc.model.SettingId – undocumented

**Returns:**
- None

### `set_data_value(id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None`

Sets the value for a data id.

**Parameters:**
- `id`: csc.model.DataId – undocumented
- `value`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented

**Returns:**
- None

### `set_data_value(id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None`

Sets the value for a data id at multiple frames.

**Parameters:**
- `id`: csc.model.DataId – undocumented
- `frames`: set[int] – undocumented
- `value`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented

**Returns:**
- None

### `set_data_value(id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None`

Sets the value for a data id at a specific frame.

**Parameters:**
- `id`: csc.model.DataId – undocumented
- `frame`: int – undocumented
- `value`: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] – undocumented

**Returns:**
- None

### `set_description_value(name: str, id: csc.model.DataId) -> None`

Sets a description association for a data id.

**Parameters:**
- `name`: str – undocumented
- `id`: csc.model.DataId – undocumented

**Returns:**
- None

### `set_description_value(name: str, id: csc.model.SettingId) -> None`

Sets a description association for a setting id.

**Parameters:**
- `name`: str – undocumented
- `id`: csc.model.SettingId – undocumented

**Returns:**
- None

### `set_setting_value(id: csc.model.SettingId, value: Union[bool, int]) -> None`

Sets a setting value.

**Parameters:**
- `id`: csc.model.SettingId – undocumented
- `value`: Union[bool, int] – undocumented

**Returns:**
- None

### `set_setting_value(id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None`

Sets a setting value at a specific frame.

**Parameters:**
- `id`: csc.model.SettingId – undocumented
- `frame`: int – undocumented
- `value`: Union[bool, int] – undocumented

**Returns:**
- None

## Usage Notes

- Many methods are overloaded; use the signature that matches your data types and availability of ids.
- Parameter semantics for some methods are undocumented; consult Cascadeur’s Python API for details.
- Frame-based variants allow setting time-dependent values.

