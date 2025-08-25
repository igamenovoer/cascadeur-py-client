[CLEAN]

# csc.layers.Viewer

## Overview
Viewer provides access to the hierarchy of animation layers and folders that describe scene objects’ interpolation properties. It exposes methods for querying layers, folders, headers, items, and keyframe-related indices. Many methods support working with sets or lists of identifiers to operate on multiple layers at once. Type names and return values are kept as referenced in the source.

## Class Definition
```python
class csc.layers.Viewer
```

## Constructor

### `__init__(*args, **kwargs)`
Undocumented.

**Parameters:**
- args: undocumented – undocumented
- kwargs: undocumented – undocumented

**Returns:**
- undocumented – undocumented

## Methods

### `actual_key_pos(pos)`
Undocumented.

**Parameters:**
- pos: undocumented – undocumented

**Returns:**
- undocumented – undocumented

### `all_child_ids(id) -> ItemId[]`
Undocumented.

**Parameters:**
- id: undocumented – undocumented

**Returns:**
- ItemId[] – undocumented

### `all_included_layer_ids(items, ignoreLocked: bool = False) -> LayerId[]`
Undocumented.

**Parameters:**
- items: ItemId[] – undocumented
- ignoreLocked: bool – optional; default False

**Returns:**
- LayerId[] – undocumented

### `all_layer_ids() -> LayerId[]`
Undocumented.

**Returns:**
- LayerId[] – undocumented

### `all_parent_ids(id) -> FolderId[]`
Undocumented.

**Parameters:**
- id: undocumented – undocumented

**Returns:**
- FolderId[] – undocumented

### `default_layer_id() -> LayerId`
Undocumented.

**Returns:**
- LayerId – undocumented

### `find_folder(id: FolderId) -> Folder`
Undocumented.

**Parameters:**
- id: FolderId – undocumented

**Returns:**
- Folder – undocumented

### `find_layer(id: LayerId) -> Layer`
Undocumented.

**Parameters:**
- id: LayerId – undocumented

**Returns:**
- Layer – undocumented

### `folder(id: FolderId) -> Folder`
Undocumented.

**Parameters:**
- id: FolderId – undocumented

**Returns:**
- Folder – undocumented

### `folders_map() -> <FolderId, Folder>{}`
Undocumented.

**Returns:**
- <FolderId, Folder>{} – undocumented

### `for_all_ordered_items(arg0)`
Undocumented.

**Parameters:**
- arg0: undocumented – undocumented

**Returns:**
- undocumented – undocumented

### `frames_count() -> int`
Undocumented.

**Returns:**
- int – undocumented

### `frames_count(id_arr: list[csc.Guid]) -> int`
Undocumented.

**Parameters:**
- id_arr: list[csc.Guid] – undocumented

**Returns:**
- int – undocumented

### `has_item(id) -> bool`
Undocumented.

**Parameters:**
- id: undocumented – undocumented

**Returns:**
- bool – undocumented

### `header(id: ItemId) -> Header`
Undocumented.

**Parameters:**
- id: ItemId – undocumented

**Returns:**
- Header – undocumented

### `is_deep_child(item_id, folder_id) -> bool`
Undocumented.

**Parameters:**
- item_id: undocumented – undocumented
- folder_id: undocumented – undocumented

**Returns:**
- bool – undocumented

### `item(id: ItemId) -> ItemVariant`
Undocumented.

**Parameters:**
- id: ItemId – undocumented

**Returns:**
- ItemVariant – undocumented

### `last_key_pos() -> int`
Undocumented.

**Returns:**
- int – undocumented

### `last_key_pos(id_arr: list[csc.Guid]) -> int`
Undocumented.

**Parameters:**
- id_arr: list[csc.Guid] – undocumented

**Returns:**
- int – undocumented

### `layer(id: LayerId) -> Layer`
Undocumented.

**Parameters:**
- id: LayerId – undocumented

**Returns:**
- Layer – undocumented

### `layer_id_by_obj_id(id: csc.model.ObjectId) -> LayerId`
Undocumented.

**Parameters:**
- id: csc.model.ObjectId – undocumented

**Returns:**
- LayerId – undocumented

### `layer_id_by_obj_id_or_null(id: csc.model.ObjectId) -> LayerId`
Undocumented.

**Parameters:**
- id: csc.model.ObjectId – undocumented

**Returns:**
- LayerId – undocumented

### `layer_ids_by_obj_ids(ids: csc.model.ObjectId[]) -> LayerId{}`
Undocumented.

**Parameters:**
- ids: csc.model.ObjectId[] – undocumented

**Returns:**
- LayerId{} – undocumented

### `layers_indices(id_arr, ignore_locked) -> IndicesContainer`
Undocumented.

**Parameters:**
- id_arr: undocumented – undocumented
- ignore_locked: undocumented – undocumented

**Returns:**
- IndicesContainer – undocumented

### `layers_map() -> <LayerId, Layer>{}`
Undocumented.

**Returns:**
- <LayerId, Layer>{} – undocumented

### `merged_layer(scene, ids, normalize)`
Undocumented.

**Parameters:**
- scene: undocumented – undocumented
- ids: undocumented – undocumented
- normalize: undocumented – undocumented

**Returns:**
- undocumented – undocumented

### `obj_ids_by_layer_ids(id_arr) -> LayerId[]`
Undocumented.

**Parameters:**
- id_arr: undocumented – undocumented

**Returns:**
- LayerId[] – undocumented

### `pos_in_parent(id) -> int`
Undocumented.

**Parameters:**
- id: undocumented – undocumented

**Returns:**
- int – undocumented

### `root_id() -> FolderId`
Undocumented.

**Returns:**
- FolderId – undocumented

### `significant_frames() -> domain::scene::layers::index::FramesIndices`
Undocumented.

**Returns:**
- domain::scene::layers::index::FramesIndices – undocumented

### `significant_frames(id_arr: set[csc.Guid]) -> domain::scene::layers::index::FramesIndices`
Undocumented.

**Parameters:**
- id_arr: set[csc.Guid] – undocumented

**Returns:**
- domain::scene::layers::index::FramesIndices – undocumented

### `top_layer_id(id: csc.Guid) -> csc.Guid`
Undocumented.

**Parameters:**
- id: csc.Guid – undocumented

**Returns:**
- csc.Guid – undocumented

### `top_layer_id(id_arr: list[csc.Guid]) -> csc.Guid`
Undocumented.

**Parameters:**
- id_arr: list[csc.Guid] – undocumented

**Returns:**
- csc.Guid – undocumented

### `unlocked_layer_ids(id_arr) -> LayerId[]`
Undocumented.

**Parameters:**
- id_arr: undocumented – undocumented

**Returns:**
- LayerId[] – undocumented

## Usage Notes
- Method signatures and type names are preserved as shown in the source; many are undocumented beyond their names and types.
- Overloaded methods are listed as separate signatures for clarity.

