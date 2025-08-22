[CLEAN]

# csc.layers.Layer

**Module:** `csc.layers.Layer`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html)

## Overview

The `Layer` class is the basic element in Cascadeur's animation system that implements intervals and sections to set interpolation properties of scene objects. Layers organize animation data and provide access to keyframes, sections, and interpolation settings for objects across time.

## Class Definition

```python
class csc.layers.Layer
```

The Layer class manages animation data organization, including keyframes, sections, and interpolation properties for scene objects over time.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a Layer instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Properties

### `header` (Header)

Gets the layer header containing metadata and properties.

**Returns:**
- Header: The layer header object

### `is_locked` (bool)

Gets whether the layer is locked for editing.

**Returns:**
- bool: True if the layer is locked, False otherwise

### `is_visible` (bool)

Gets whether the layer is visible in the interface.

**Returns:**
- bool: True if the layer is visible, False otherwise

### `obj_ids` (csc.model.ObjectId{})

Gets the collection of object IDs associated with this layer.

**Returns:**
- csc.model.ObjectId{}: Set of object identifiers

### `sections` (std::map<Pos, Section>)

Gets the sections mapped by position within the layer.

**Returns:**
- std::map<Pos, Section>: Map of positions to sections

## Methods

### `actual_key(self, pos: int) -> Key`

Gets the actual key at the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- Key: The key object at the position

### `actual_key_pos(self, pos: int) -> int`

Gets the actual position of the key at the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- int: The actual key position

### `actual_section(self, pos: int) -> Section`

Gets the actual section containing the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- Section: The section containing the position

### `actual_section_pos(self, pos: int) -> int`

Gets the actual position of the section containing the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- int: The actual section position

### `find_section(self, pos: int) -> Section`

Finds the section at the specified position.

**Parameters:**
- `pos` (int): The position to search

**Returns:**
- Section: The section at the position

### `interval(self, pos: int) -> Interval`

Gets the interval at the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- Interval: The interval object at the position

### `is_key(self, pos: int) -> bool`

Checks if there is a key at the specified position.

**Parameters:**
- `pos` (int): The position to check

**Returns:**
- bool: True if there is a key at the position, False otherwise

### `is_key_or_fixed(self, pos: int) -> bool`

Checks if there is a key or fixed value at the specified position.

**Parameters:**
- `pos` (int): The position to check

**Returns:**
- bool: True if there is a key or fixed value at the position, False otherwise

### `key(self, pos: int) -> Key`

Gets the key at the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- Key: The key object at the position

### `key_frame_indices(self) -> FramesIndices`

Gets the indices of all keyframes in the layer.

**Returns:**
- FramesIndices: Collection of keyframe indices

### `last_key_pos(self) -> int`

Gets the position of the last key in the layer.

**Returns:**
- int: The position of the last key

### `section(self, pos: int) -> Section`

Gets the section at the specified position.

**Parameters:**
- `pos` (int): The position to query

**Returns:**
- Section: The section object at the position

## Usage Example

```python
import csc.layers

# Typically layers are obtained from the layers viewer/editor
app = csc.app.get_application()
scene = app.get_scene_manager().get_current_scene()
layers_viewer = scene.layers_viewer()

# Get layers from the viewer (example workflow)
# layer = layers_viewer.get_layer_by_index(0)

# Access layer properties
# header = layer.header
# is_locked = layer.is_locked
# is_visible = layer.is_visible
# object_ids = layer.obj_ids
# sections = layer.sections

# Work with keys and positions
# frame_pos = 30
# has_key = layer.is_key(frame_pos)
# if has_key:
#     key = layer.key(frame_pos)
#     actual_key = layer.actual_key(frame_pos)

# Work with sections and intervals
# section = layer.section(frame_pos)
# interval = layer.interval(frame_pos)
# actual_section = layer.actual_section(frame_pos)

# Get keyframe information
# keyframe_indices = layer.key_frame_indices()
# last_key_position = layer.last_key_pos()

# Check for fixed values or keys
# has_key_or_fixed = layer.is_key_or_fixed(frame_pos)

print("Layer analysis complete")
```

## Usage Notes

- Layers organize animation data for multiple objects across time
- Use position-based methods to query keys, sections, and intervals at specific frames
- Keys represent keyframes with specific values at specific times
- Sections define interpolation behavior between keys
- Intervals manage temporal relationships and interpolation properties
- Object IDs link the layer to specific scene objects
- Layer visibility and locking affect editing capabilities
- Layers are typically managed through the layers viewer and editor systems

## See Also

- `csc.layers.Viewer` - Layer viewing functionality
- `csc.layers.Editor` - Layer editing functionality
- `csc.layers.layer.Key` - Keyframe representation
- `csc.layers.layer.Section` - Section representation
- `csc.layers.layer.Interval` - Interval representation
- `csc.layers.Header` - Layer header information
- Animation and interpolation system in Cascadeur