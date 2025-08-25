[CLEAN]

# csc.model.ModelEditor

## Overview
ModelEditor provides basic methods to edit the scene model in Cascadeur. It includes operations for adding and removing objects, working with layers, and accessing related editors and the viewer. Specific parameter types and behaviors are not fully documented here; unknown details are marked as undocumented.

## Class Definition
```python
class csc.model.ModelEditor
```

## Constructor

### `__init__(*args, **kwargs)`
Creates a ModelEditor instance.
- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented
- Returns: None

## Methods

### `add_object() -> csc.model.ObjectId`
Adds a new object to the scene model.
- Parameters: none
- Returns: `csc.model.ObjectId` – undocumented

### `add_object(id: csc.model.ObjectId) -> csc.model.ObjectId`
Adds the specified object to the scene model.
- Parameters:
  - `id`: `csc.model.ObjectId` – undocumented
- Returns: `csc.model.ObjectId` – undocumented

### `behaviour_editor() -> BehaviourEditor`
Returns the behaviour editor associated with the model.
- Parameters: none
- Returns: `BehaviourEditor` – undocumented

### `data_editor() -> DataEditor`
Returns the data editor associated with the model.
- Parameters: none
- Returns: `DataEditor` – undocumented

### `delete_objects(ids, close_connections=None)`
Deletes the specified objects from the scene model.
- Parameters:
  - `ids`: undocumented
  - `close_connections` (optional): undocumented
- Returns: undocumented

### `fit_animation_size_by_layers()`
Fits or adjusts animation size based on layers.
- Parameters: none
- Returns: undocumented

### `get_viewer()`
Returns the viewer instance associated with the model.
- Parameters: none
- Returns: undocumented

### `init_default_constants()`
Initializes default constants for the model editor.
- Parameters: none
- Returns: undocumented

### `layers() -> csc.layers.Layers`
Returns the layers collection.
- Parameters: none
- Returns: `csc.layers.Layers`

### `layers_editor() -> csc.layers.Editor`
Returns the layers editor.
- Parameters: none
- Returns: `csc.layers.Editor`

### `layers_selector() -> csc.layers.Selector`
Returns the layers selector.
- Parameters: none
- Returns: `csc.layers.Selector`

### `move_obj_ids_in_layers(objIds=None)`
Moves object IDs within layers.
- Parameters:
  - `objIds` (optional): undocumented
- Returns: undocumented

### `move_objects_to_layer(ids, target_layer_id)`
Moves the specified objects to a target layer.
- Parameters:
  - `ids`: undocumented
  - `target_layer_id`: undocumented
- Returns: undocumented

### `set_fixed_interpolation_if_need(...)`
Sets fixed interpolation if needed.
- Parameters: undocumented
- Returns: undocumented
- Notes: Signature is variadic/undocumented.

### `set_object_name(id, name)`
Sets an object's name.
- Parameters:
  - `id`: undocumented
  - `name`: undocumented
- Returns: undocumented

### `set_object_type_name(id, name)`
Sets an object's type name.
- Parameters:
  - `id`: undocumented
  - `name`: undocumented
- Returns: undocumented
- Notes: Overloaded function; details undocumented.

## Usage Notes
- This documentation reflects available signatures; parameter types and behaviors marked as undocumented should be validated against the official Cascadeur API reference.
- Editor accessors (behaviour_editor, data_editor, layers_editor, layers_selector) return helper editors for specialized operations.

