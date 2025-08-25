[CLEAN]

# csc.layers.Editor

## Overview
Editor provides operations for managing the structure of scene objects' interpolation properties in Cascadeur. It works with a hierarchy of layers organized into folders, allowing creation, deletion, movement, and configuration of layers and items. The class also exposes controls for visibility, locking, and section/interpolation adjustments.

## Class Definition
```python
class csc.layers.Editor
```

## Constructor

### __init__(*args, **kwargs)
Initializes a new Editor instance; details are undocumented.

Parameters:
- *args: undocumented
- **kwargs: undocumented

## Methods

### change_section(self, arg0, arg1, arg2)
Changes a section; specifics are undocumented.

Parameters:
- arg0: undocumented
- arg1: undocumented
- arg2: undocumented

Returns:
- undocumented

### clear(self)
Clears editor state; specifics are undocumented.

Returns:
- undocumented

### create_folder(self, name, parent, withDefaultLayer=True, pos=None) -> FolderId
Creates a folder within the layer hierarchy.

Parameters:
- name: string – undocumented
- parent: FolderId – undocumented
- withDefaultLayer: bool – undocumented (default: true)
- pos: int | None – undocumented

Returns:
- FolderId: undocumented

### create_layer(self, name, parent, pos=None) -> FolderId
Creates a layer within the specified folder.

Parameters:
- name: string – undocumented
- parent: FolderId – undocumented
- pos: int | None – undocumented

Returns:
- FolderId: undocumented

### delete_empty_folders(self)
Deletes empty folders; specifics are undocumented.

Returns:
- undocumented

### delete_empty_layers(self)
Deletes empty layers; specifics are undocumented.

Returns:
- undocumented

### delete_folder(self, id)
Deletes a folder by identifier; specifics are undocumented.

Parameters:
- id: undocumented

Returns:
- undocumented

### delete_layer(self, id)
Deletes a layer by identifier; specifics are undocumented.

Parameters:
- id: undocumented

Returns:
- undocumented

### find_header(self, arg0) -> Header
Finds and returns a header; specifics are undocumented.

Parameters:
- arg0: undocumented

Returns:
- Header: undocumented

### insert_layer(self, layer, pos=None)
Inserts a layer at a given position; specifics are undocumented.

Parameters:
- layer: Layer – undocumented
- pos: int | None – undocumented

Returns:
- undocumented

### move_item(self, item_id, folder_id, pos=None)
Moves an item to a folder, optionally at a specific position.

Parameters:
- item_id: undocumented
- folder_id: undocumented
- pos: int | None – undocumented

Returns:
- undocumented

### normalize_sections(self, scene)
Normalizes sections in the given scene; specifics are undocumented.

Parameters:
- scene: undocumented

Returns:
- undocumented

### set_default(self)
Resets editor settings to defaults; specifics are undocumented.

Returns:
- undocumented

### set_fixed_interpolation_if_need(self, id: csc.Guid, start: int, end: int) -> bool
Ensures fixed interpolation over a range if required.

Parameters:
- id: csc.Guid – undocumented
- start: int – undocumented
- end: int – undocumented

Returns:
- bool: undocumented

### set_fixed_interpolation_if_need(self, id: csc.Guid, frame: int) -> bool
Ensures fixed interpolation at a frame if required.

Parameters:
- id: csc.Guid – undocumented
- frame: int – undocumented

Returns:
- bool: undocumented

### set_fixed_interpolation_or_key_if_need(self, ...)
Sets fixed interpolation or inserts a key if required; exact signature is undocumented.

Returns:
- undocumented

### set_locked_for_item(self, is_l, id)
Sets the locked state for an item.

Parameters:
- is_l: bool – undocumented
- id: ItemId – undocumented

Returns:
- undocumented

### set_locked_for_layer(self, is_l, id)
Sets the locked state for a layer.

Parameters:
- is_l: bool – undocumented
- id: LayerId – undocumented

Returns:
- undocumented

### set_name(self, name, id)
Sets the name for an item or layer; specifics are undocumented.

Parameters:
- name: undocumented
- id: undocumented

Returns:
- undocumented

### set_section(self, section, pos: int, id)
Sets a section at a position for an item.

Parameters:
- section: Section – undocumented
- pos: int – undocumented
- id: ItemId – undocumented

Returns:
- undocumented

### set_sections(self, arg0, domain, arg1)
Sets multiple sections; specifics and parameter roles are undocumented.

Parameters:
- arg0: undocumented
- domain: undocumented
- arg1: undocumented

Returns:
- undocumented

Notes:
- Documentation mentions a mapping like "<Pos, Section>{}" and an "id: LayerId", but parameter names are not clearly specified.

### set_visible_for_item(self, is_v, id)
Sets the visibility state for an item.

Parameters:
- is_v: bool – undocumented
- id: ItemId – undocumented

Returns:
- undocumented

### set_visible_for_layer(self, is_v, id)
Sets the visibility state for a layer.

Parameters:
- is_v: bool – undocumented
- id: LayerId – undocumented

Returns:
- undocumented

### unset_section(self, pos: int, id)
Removes a section at the given position for an item.

Parameters:
- pos: int – undocumented
- id: ItemId – undocumented

Returns:
- undocumented

## Usage Notes
- Identifiers such as ItemId, LayerId, FolderId, and Guid are opaque types from the Cascadeur API.
- Some signatures and behaviors are partially documented; refer to the official source for authoritative details.

