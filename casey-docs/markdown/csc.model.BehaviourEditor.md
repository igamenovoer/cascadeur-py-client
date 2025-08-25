[CLEAN]

# csc.model.BehaviourEditor

## Overview

BehaviourEditor provides operations to create, modify, and manage behaviours attached to scene objects. It supports adding, setting, erasing, and hiding behaviour properties such as assets, data, model objects, references, and settings. Methods typically operate on identifiers like BehaviourId, ObjectId, AssetId, DataId, and SettingId. Parameter semantics are largely undocumented in the source material.

## Class Definition

```python
class csc.model.BehaviourEditor
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a BehaviourEditor instance.
- Parameters are undocumented.

## Methods

### `add_behaviour(self, object_id: csc.model.ObjectId, behaviour_type: str) -> csc.model.BehaviourId`
Adds a new behaviour of the specified type to the given object.
- Parameters:
  - object_id: csc.model.ObjectId – undocumented
  - behaviour_type: str – undocumented
- Returns: csc.model.BehaviourId – undocumented
- Notes: Overloaded.

### `add_behaviour(self, object_id: csc.model.ObjectId, behaviour_type: str, behaviour_id: csc.model.BehaviourId) -> csc.model.BehaviourId`
Adds a behaviour with an explicit id to the given object.
- Parameters:
  - object_id: csc.model.ObjectId – undocumented
  - behaviour_type: str – undocumented
  - behaviour_id: csc.model.BehaviourId – undocumented
- Returns: csc.model.BehaviourId – undocumented
- Notes: Overloaded.

### `add_behaviour_asset_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, asset_id: csc.domain.AssetId)`
Adds an asset reference to a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - asset_id: csc.domain.AssetId – undocumented
- Returns: undocumented

### `add_behaviour_data_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, data_id: csc.model.DataId)`
Adds a data reference to a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - data_id: csc.model.DataId – undocumented
- Returns: undocumented

### `add_behaviour_model_object_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, mo_id: csc.model.ObjectId)`
Adds a model object reference to a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - mo_id: csc.model.ObjectId – undocumented
- Returns: undocumented

### `add_behaviour_reference_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, beh_id: csc.model.BehaviourId)`
Adds a behaviour reference to a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - beh_id: csc.model.BehaviourId – undocumented
- Returns: undocumented

### `add_behaviour_setting_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, setting_id: csc.model.SettingId)`
Adds a setting reference to a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - setting_id: csc.model.SettingId – undocumented
- Returns: undocumented

### `delete_behaviour(self, behaviour_id: csc.model.BehaviourId)`
Deletes a behaviour by id.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
- Returns: undocumented

### `delete_behaviours(self, objects_id: {csc.model.ObjectId})`
Deletes behaviours associated with a collection of object ids.
- Parameters:
  - objects_id: {csc.model.ObjectId} – undocumented
- Returns: undocumented

### `erase_behaviour_data_from_range(self, behaviour_id: csc.model.BehaviourId, name: str, data_id: csc.model.DataId)`
Erases a data reference from a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - data_id: csc.model.DataId – undocumented
- Returns: undocumented

### `erase_behaviour_model_object_from_range(self, behaviour_id: csc.model.BehaviourId, name: str, mo_id: csc.model.ObjectId)`
Erases a model object reference from a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - mo_id: csc.model.ObjectId – undocumented
- Returns: undocumented

### `erase_behaviour_reference_from_range(self, behaviour_id: csc.model.BehaviourId, name: str, beh_id: csc.model.BehaviourId)`
Erases a behaviour reference from a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - beh_id: csc.model.BehaviourId – undocumented
- Returns: undocumented

### `erase_behaviour_setting_from_range(self, behaviour_id: csc.model.BehaviourId, name: str, setting_id: csc.model.SettingId)`
Erases a setting reference from a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - setting_id: csc.model.SettingId – undocumented
- Returns: undocumented

### `get_viewer(self)`
Returns the associated viewer object.
- Parameters: none
- Returns: undocumented

### `hide_behaviour(self, behaviour_id: csc.model.BehaviourId, hidden: bool = True) -> bool`
Hides or shows a behaviour.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - hidden: bool – undocumented (default True)
- Returns: bool – undocumented

### `set_behaviour_asset(self, behaviour_id: csc.model.BehaviourId, name: str, asset_id: csc.domain.AssetId)`
Sets an asset reference on a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - asset_id: csc.domain.AssetId – undocumented
- Returns: undocumented

### `set_behaviour_data(self, behaviour_id: csc.model.BehaviourId, name: str, dataId: csc.model.DataId)`
Sets a data reference on a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - dataId: csc.model.DataId – undocumented
- Returns: undocumented

### `set_behaviour_data_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, inserted_ids: csc.model.DataId)`
Sets data references to a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - inserted_ids: csc.model.DataId – undocumented
- Returns: undocumented

### `set_behaviour_field_value(self, behaviour_id: csc.model.BehaviourId, name: str, name_value: str)`
Sets a string value for a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - name_value: str – undocumented
- Returns: undocumented

### `set_behaviour_model_object(self, behaviour_id: csc.model.BehaviourId, name: str, mo_id: csc.model.ObjectId)`
Sets a model object reference on a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - mo_id: csc.model.ObjectId – undocumented
- Returns: undocumented

### `set_behaviour_model_objects_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, inserted_ids: csc.model.ObjectId[])`
Sets model object references on a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - inserted_ids: csc.model.ObjectId[] – undocumented
- Returns: undocumented

### `set_behaviour_reference(self, behaviour_id: csc.model.BehaviourId, name: str, beh_id: csc.model.BehaviourId)`
Sets a behaviour reference on a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - beh_id: csc.model.BehaviourId – undocumented
- Returns: undocumented

### `set_behaviour_references_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, inserted_ids: csc.model.BehaviourId[])`
Sets behaviour references on a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - inserted_ids: csc.model.BehaviourId[] – undocumented
- Returns: undocumented

### `set_behaviour_setting(self, behaviour_id: csc.model.BehaviourId, name: str, setting_id: csc.model.SettingId)`
Sets a setting reference on a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - setting_id: csc.model.SettingId – undocumented
- Returns: undocumented

### `set_behaviour_settings_to_range(self, behaviour_id: csc.model.BehaviourId, name: str, inserted_ids: csc.model.SettingId[])`
Sets setting references on a behaviour field over a range.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - inserted_ids: csc.model.SettingId[] – undocumented
- Returns: undocumented

### `set_behaviour_string(self, behaviour_id: csc.model.BehaviourId, name: str, str: str)`
Sets a string value on a behaviour field.
- Parameters:
  - behaviour_id: csc.model.BehaviourId – undocumented
  - name: str – undocumented
  - str: str – undocumented
- Returns: undocumented

## Usage Notes

- Types and parameter purposes reflect the original API listings and are otherwise undocumented.
- Method behavior details (side effects, range semantics, validation) are not described in the source material.

