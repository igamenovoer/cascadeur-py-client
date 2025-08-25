[CLEAN]

# csc.model.DataViewer

## Overview

DataViewer provides read-only access to scene data, settings, and behaviour properties in Cascadeur. It lets you query identifiers, retrieve values (optionally at a specific frame), and inspect descriptions. Several methods are overloaded to support both current and per-frame value access. Return types may include primitives, matrices, quaternions, and other engine-specific types.

## Class Definition

```python
class csc.model.DataViewer
```

## Constructor

### `__init__(*args, **kwargs)`

Initialize a DataViewer instance (details undocumented).

- Parameters:
  - args: undocumented
  - kwargs: undocumented
- Returns: None

## Methods

### `cluster_viewer(self) -> ClusterViewer`

Return the associated cluster viewer (details undocumented).

- Parameters: none
- Returns: ClusterViewer

### `get_all_data_id(self, object_id) -> csc.model.DataId[]`

Return all data IDs for the given object.

- Parameters:
  - object_id: undocumented
- Returns: csc.model.DataId[]

### `get_all_settings_id(self, object_id) -> csc.model.SettingId[]`

Return all setting IDs for the given object.

- Parameters:
  - object_id: undocumented
- Returns: csc.model.SettingId[]

### `get_animation_size(self) -> int`

Return the size of the animation (e.g., number of frames; exact meaning undocumented).

- Parameters: none
- Returns: int

### `get_behaviour_default_data_value(self, id: csc.model.BehaviourId, name: str) -> csc.model.DataValue`

Return the default data value for a behaviour property.

- Parameters:
  - id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
- Returns: csc.model.DataValue

### `get_behaviour_property(self, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]`

Return a behaviour property value at a specific frame.

- Parameters:
  - id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - frame: int – frame index
- Returns: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

### `get_behaviour_property(self, id: csc.model.BehaviourId, name: str) -> Union[bool, int]`

Return a behaviour property value (current/default, details undocumented).

- Parameters:
  - id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
- Returns: Union[bool, int]

### `get_data(self, id: csc.model.DataId) -> Data`

Return the Data object for the given data ID.

- Parameters:
  - id: csc.model.DataId – undocumented
- Returns: Data

### `get_data_id(self, id: csc.model.ObjectId, name: str) -> csc.model.DataId`

Resolve a data ID by object ID and property name.

- Parameters:
  - id: csc.model.ObjectId – undocumented
  - name: str – undocumented
- Returns: csc.model.DataId

### `get_data_value(self, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]`

Return a data value.

- Parameters:
  - id: csc.model.DataId – undocumented
- Returns: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

### `get_data_value(self, id: csc.model.DataId, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]`

Return a data value at a specific frame.

- Parameters:
  - id: csc.model.DataId – undocumented
  - frame: int – frame index
- Returns: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

### `get_description_by_name(self, arg0) -> string`

Return the description for a property by name.

- Parameters:
  - arg0: undocumented
- Returns: string

### `get_description_names(self) -> string[]`

Return all available description names.

- Parameters: none
- Returns: string[]

### `get_description_value(self, id: csc.model.DataId) -> str`

Return a description string for a data ID.

- Parameters:
  - id: csc.model.DataId – undocumented
- Returns: str

### `get_description_value(self, id: csc.model.SettingId) -> str`

Return a description string for a setting ID.

- Parameters:
  - id: csc.model.SettingId – undocumented
- Returns: str

### `get_setting(self, id: csc.model.SettingId) -> Setting`

Return the Setting object for the given setting ID.

- Parameters:
  - id: csc.model.SettingId – undocumented
- Returns: Setting

### `get_setting_id(self, id: csc.model.ObjectId, name: str) -> csc.model.DataId`

Resolve a setting ID by object ID and name.

- Parameters:
  - id: csc.model.ObjectId – undocumented
  - name: str – undocumented
- Returns: csc.model.DataId

### `get_setting_value(self, id: csc.model.SettingId) -> Union[bool, int]`

Return a setting value.

- Parameters:
  - id: csc.model.SettingId – undocumented
- Returns: Union[bool, int]

### `get_setting_value(self, setting_id: csc.model.SettingId, position: int) -> Union[bool, int]`

Return a setting value at a given position.

- Parameters:
  - setting_id: csc.model.SettingId – undocumented
  - position: int – undocumented
- Returns: Union[bool, int]

### `union_get_data_value(self, data_id: csc.model.DataId) -> Data.Value`

Return a unified data value (details undocumented).

- Parameters:
  - data_id: csc.model.DataId – undocumented
- Returns: Data.Value

### `union_get_data_value(self, data_id: csc.model.DataId, frame: int) -> Data.Value`

Return a unified data value at a specific frame.

- Parameters:
  - data_id: csc.model.DataId – undocumented
  - frame: int – frame index
- Returns: Data.Value

## Usage Notes

- Many accessors are overloaded; specifying a frame typically retrieves a value for that frame.
- Types reflect engine-specific values (e.g., rotations, matrices, quaternions) and may vary by property.

