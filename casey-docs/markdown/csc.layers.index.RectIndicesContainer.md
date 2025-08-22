[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:48 | Original: a4b7149a -->

# csc.layers.index.RectIndicesContainer

**Module:** `csc.layers.index.RectIndicesContainer`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.layers.index.RectIndicesContainer.html)

## Overview

RectIndicesContainer class. This is a container of items that are placed in the rect indices.

## Class Definition

```python
class csc.layers.index.RectIndicesContainer
```

Container for managing item IDs associated with rectangular frame indices.

## Constructor

Overloaded constructor.

### `__init__(self) -> None`

Initializes a RectIndicesContainer.

**Parameters:**
- None

**Returns:**
- None

### `__init__(self, item_ids: list[csc.Guid], frames_indices: csc.layers.index.FramesIndices) -> None`

Initializes a RectIndicesContainer with item IDs and frames indices.

**Parameters:**
- `item_ids` (list[csc.Guid]): List of item IDs.
- `frames_indices` (csc.layers.index.FramesIndices): Frames indices.

**Returns:**
- None

## Methods

### `add_item_id(self, item_id)`

Adds an item ID.

**Parameters:**
- `item_id`: Item identifier to add.

### `contains(self, item_id)`

Checks whether the container contains the specified item ID.

**Parameters:**
- `item_id`: Item identifier to check.

### `frames_indices(self) -> FramesIndices`

Returns the frames indices.

**Returns:**
- FramesIndices: Frames indices.

### `item_ids(self) -> ItemId[]`

Returns the item IDs.

**Returns:**
- ItemId[]: List of item IDs.

### `set_frames_indices(self, frames_indices)`

Sets the frames indices.

**Parameters:**
- `frames_indices`: Frames indices to set.

### `set_item_ids(self, item_ids)`

Sets the item IDs.

**Parameters:**
- `item_ids`: Item identifiers to set.

## Usage Example

```python
import csc.layers.index

# Create an empty container
container = csc.layers.index.RectIndicesContainer()

# Add an item ID
container.add_item_id(item_id)

# Check if an item ID exists
exists = container.contains(item_id)

# Get frames indices and item IDs
fi = container.frames_indices()
ids = container.item_ids()

# Set frames indices and item IDs
container.set_frames_indices(fi)
container.set_item_ids(ids)
```

## Usage Notes

- Use the parameterless constructor to create an empty container, or the overloaded constructor to initialize with item IDs and frames indices.
- The exact return types for some methods are not specified beyond what is shown; use introspection or refer to the API in your environment if needed.
- Ensure that item IDs and frames indices are provided in the expected formats used by your project.

## See Also

- `csc.layers.index.FramesIndices`