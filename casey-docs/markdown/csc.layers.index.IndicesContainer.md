[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:42 | Original: d2ee6b4d -->

# csc.layers.index.IndicesContainer

**Module:** `csc.layers.index.IndicesContainer`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.layers.index.IndicesContainer.html)

## Overview

IndicesContainer class. Contains indices items in the structure std::map<ItemId, FramesIndices>.
- all_frame_indices – overridden method by int (sizeLimit)
- frames_interval – overridden method by int (sizeLimit)

## Class Definition

```python
class csc.layers.index.IndicesContainer
```

Container for indices items organized by item identifiers and their frame indices.

## Constructor

### `__init__(self: csc.layers.index.IndicesContainer) -> None`

Default constructor.

**Parameters:**
- None

**Returns:**
- None

### `__init__(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None`

Constructs the container from a list of cell indices.

**Parameters:**
- `arg0` (list[csc.layers.index.CellIndex]): List of cell indices.

**Returns:**
- None

### `__init__(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None`

Constructs the container from item IDs and their frames indices.

**Parameters:**
- `start` (list[csc.Guid]): List of item IDs.
- `end` (csc.layers.index.FramesIndices): Frames indices associated with the items.

**Returns:**
- None

## Methods

### `add(self, other_container)`

Adds contents from another container.

**Parameters:**
- `other_container` (IndicesContainer): otherContainer : IndicesContainer

**Returns:**
- None

### `add_frame_indices(self, frame_indices)`

Adds frame indices.

**Parameters:**
- `frame_indices` (int{}): frame_indices: int{}

**Returns:**
- None

### `add_item(self, item_indices)`

Adds item indices.

**Parameters:**
- `item_indices` (ItemIndices): itemIndices : ItemIndices

**Returns:**
- None

### `all_frame_indices(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesIndices`

Returns all frame indices.

**Parameters:**
- None

**Returns:**
- csc.layers.index.FramesIndices

### `all_frame_indices(self: csc.layers.index.IndicesContainer, size_limit: int) -> csc.layers.index.FramesIndices`

Returns all frame indices with a size limit.

**Parameters:**
- `size_limit` (int): Maximum number of items/frames to include.

**Returns:**
- csc.layers.index.FramesIndices

### `cell_indices(self) -> CellIndex[]`

Returns cell indices.

**Parameters:**
- None

**Returns:**
- CellIndex[]

### `delete_empty_items(self)`

Deletes empty items.

**Parameters:**
- None

**Returns:**
- None

### `direct_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices]`

Returns direct indices mapping.

**Parameters:**
- None

**Returns:**
- dict[csc.Guid, csc.layers.index.FramesIndices]

### `direct_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices]`

Returns direct indices mapping.

**Parameters:**
- None

**Returns:**
- dict[csc.Guid, csc.layers.index.FramesIndices]

### `frames_interval(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesInterval`

Returns frames interval.

**Parameters:**
- None

**Returns:**
- csc.layers.index.FramesInterval

### `frames_interval(self: csc.layers.index.IndicesContainer, size_limit: int) -> csc.layers.index.FramesInterval`

Returns frames interval with a size limit.

**Parameters:**
- `size_limit` (int): Maximum number of items/frames to include.

**Returns:**
- csc.layers.index.FramesInterval

### `is_empty(self)`

Checks if the container is empty.

**Parameters:**
- None

**Returns:**
- Unspecified

### `item_ids(self) -> Guid[]`

Returns item IDs.

**Parameters:**
- None

**Returns:**
- Guid[]

### `item_indices(self, id) -> FramesIndices`

Returns frames indices for a specific item.

**Parameters:**
- `id`: Item identifier (type not specified in source).

**Returns:**
- FramesIndices

### `items_indices(self) -> ItemIndices[]`

Returns all items indices.

**Parameters:**
- None

**Returns:**
- ItemIndices[]

### `rect(self) -> RectIndicesContainer`

Returns a rectangular indices container.

**Parameters:**
- None

**Returns:**
- RectIndicesContainer

### `set_frame_indices(self, start, end)`

Sets frame interval.

**Parameters:**
- `start` (int): start, end : int
- `end` (int): start, end : int

**Returns:**
- None

## Usage Example

```python
import csc.layers.index

# Create an empty container
container = csc.layers.index.IndicesContainer()

# Check if it is empty
empty = container.is_empty()

# Retrieve all frame indices (no limit)
all_frames = container.all_frame_indices()

# Retrieve frames interval with a size limit
interval = container.frames_interval(100)

# Get item IDs
ids = container.item_ids()
```

## Usage Notes

- all_frame_indices and frames_interval have overloaded variants that accept an integer size_limit.
- direct_indices returns a mapping from csc.Guid to csc.layers.index.FramesIndices.
- Parameter types such as ItemIndices, FramesIndices, FramesInterval, CellIndex, RectIndicesContainer, and Guid refer to types in the csc API.
- Where return types are not specified in the source, they are left unspecified here.

## See Also

- csc.layers.index.FramesIndices
- csc.layers.index.FramesInterval
- csc.layers.index.CellIndex
- csc.layers.index.ItemIndices
- csc.layers.index.RectIndicesContainer
- csc.Guid