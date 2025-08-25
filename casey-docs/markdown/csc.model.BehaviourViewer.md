[CLEAN]

# csc.model.BehaviourViewer

## Overview

BehaviourViewer allows viewing and querying of behaviours and their properties in a Cascadeur scene. It provides lookups by behaviour name, type, or owner object and returns identifiers for related assets, data, settings, references, and objects. The API primarily returns IDs rather than concrete objects and includes helpers to inspect names, property types, visibility, and validity.

## Class Definition

```python
class csc.model.BehaviourViewer
```

## Constructor

### `__init__(*args, **kwargs)`

undocumented.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

## Methods

### `behaviour_id(object_id: csc.model.ObjectId, behaviour_name: str) -> csc.model.BehaviourId`

undocumented.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented
- `behaviour_name`: str – undocumented

**Returns:**
- csc.model.BehaviourId – undocumented

### `get_behaviour_asset(behaviour_id: csc.model.BehaviourId, name: str) -> csc.model.BehaviourId`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- csc.model.BehaviourId – undocumented

### `get_behaviour_asset_range(behaviour_id: csc.model.BehaviourId, name: str) -> list[csc.model.BehaviourId]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- list[csc.model.BehaviourId] – undocumented

### `get_behaviour_by_name(object_id: csc.model.ObjectId, behaviour_name: str) -> csc.model.BehaviourId`

undocumented.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented
- `behaviour_name`: str – undocumented

**Returns:**
- csc.model.BehaviourId – undocumented

### `get_behaviour_data(behaviour_id: csc.model.BehaviourId, name: str) -> csc.model.DataId`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- csc.model.DataId – undocumented

### `get_behaviour_data_range(behaviour_id: csc.model.BehaviourId, name: str) -> list[csc.model.DataId]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- list[csc.model.DataId] – undocumented

### `get_behaviour_name(behaviour_id: csc.model.BehaviourId) -> str`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented

**Returns:**
- str – undocumented

### `get_behaviour_object(behaviour_id: csc.model.BehaviourId, name: str) -> csc.model.ObjectId`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- csc.model.ObjectId – undocumented

### `get_behaviour_objects_range(behaviour_id: csc.model.BehaviourId, name: str) -> list[csc.model.ObjectId]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- list[csc.model.ObjectId] – undocumented

### `get_behaviour_owner(behaviour_id: csc.model.BehaviourId) -> csc.model.ObjectId`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented

**Returns:**
- csc.model.ObjectId – undocumented

### `get_behaviour_property_names(behaviour_id: csc.model.BehaviourId) -> list[str]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented

**Returns:**
- list[str] – undocumented

### `get_behaviour_reference(behaviour_id: csc.model.BehaviourId, name: str) -> csc.model.BehaviourId`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- csc.model.BehaviourId – undocumented

### `get_behaviour_reference_range(behaviour_id: csc.model.BehaviourId, name: str) -> list[csc.model.BehaviourId]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- list[csc.model.BehaviourId] – undocumented

### `get_behaviour_setting(behaviour_id: csc.model.BehaviourId, name: str) -> csc.model.SettingId`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- csc.model.SettingId – undocumented

### `get_behaviour_settings_range(behaviour_id: csc.model.BehaviourId, name: str) -> list[csc.model.SettingId]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- list[csc.model.SettingId] – undocumented

### `get_behaviour_string(behaviour_id: csc.model.BehaviourId, name: str) -> str`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- str – undocumented

### `get_behaviours(type_name: str) -> list[csc.model.BehaviourId]`

undocumented.

**Parameters:**
- `type_name`: str – undocumented

**Returns:**
- list[csc.model.BehaviourId] – undocumented

### `get_behaviours(object_id: csc.model.ObjectId) -> list[csc.model.BehaviourId]`

undocumented.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented

**Returns:**
- list[csc.model.BehaviourId] – undocumented

### `get_children(object_id: csc.model.ObjectId) -> undocumented`

undocumented.

**Parameters:**
- `object_id`: csc.model.ObjectId – undocumented

**Returns:**
- undocumented – undocumented

### `get_property_type(behaviour_id: csc.model.BehaviourId, name: str) -> list[Type]`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented
- `name`: str – undocumented

**Returns:**
- list[Type] – undocumented

### `is_hidden(behaviour_id: csc.model.BehaviourId) -> bool`

undocumented.

**Parameters:**
- `behaviour_id`: csc.model.BehaviourId – undocumented

**Returns:**
- bool – undocumented

### `is_valid_behaviour_type(behaviour_name: str) -> bool`

undocumented.

**Parameters:**
- `behaviour_name`: str – undocumented

**Returns:**
- bool – undocumented

## Usage Notes

- Many methods return identifiers (IDs) rather than concrete objects.
- For behavior-specific semantics and ID dereferencing, consult the Cascadeur Python API.

