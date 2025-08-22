[CLEAN]

# csc.layers.index.CellIndex

**Module:** `csc.layers.index.CellIndex`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.layers.index.CellIndex.html)

## Overview

The `CellIndex` class represents an index structure for identifying specific cells within the layers system. It combines a frame index and item identifier to uniquely locate animation cells within the layer hierarchy, providing essential indexing functionality for animation layer operations.

## Class Definition

```python
class csc.layers.index.CellIndex
```

The CellIndex class serves as a coordinate system for locating specific cells within animation layers, using frame-based indexing and unique item identification.

## Constructor (Overloaded)

### `__init__(self) -> None`

Creates a default CellIndex instance with empty values.

**Returns:**
- None

### `__init__(self, frame_index: int, item_id: csc.Guid) -> None`

Creates a CellIndex with specific frame and item identification.

**Parameters:**
- `frame_index` (int): The frame position within the layer
- `item_id` (csc.Guid): Unique identifier for the item

**Returns:**
- None

## Methods

### `is_valid(self) -> bool`

Checks whether the cell index contains valid data.

**Returns:**
- bool: True if the index is valid, False otherwise

## Attributes

### `frame_index -> int`

The frame position within the layer timeline.

**Type:** int  
**Access:** Read-only

### `item_id -> csc.Guid`

Unique identifier for the referenced item.

**Type:** csc.Guid  
**Access:** Read-only

## Usage Example

```python
import csc.layers.index
import csc

# Create a default cell index
cell_index = csc.layers.index.CellIndex()

# Check if the default index is valid
if not cell_index.is_valid():
    print("Default cell index is invalid")

# Create a specific cell index
item_guid = csc.Guid("12345678-1234-5678-9ABC-123456789ABC")
specific_index = csc.layers.index.CellIndex(10, item_guid)

# Access index properties
print(f"Frame index: {specific_index.frame_index}")
print(f"Item ID: {specific_index.item_id}")

# Validate the specific index
if specific_index.is_valid():
    print("Cell index is valid and ready to use")

# Working with layer cells
def locate_animation_cell(frame: int, item_id: str):
    """Create a cell index for animation data lookup."""
    guid = csc.Guid(item_id)
    cell_index = csc.layers.index.CellIndex(frame, guid)
    
    if cell_index.is_valid():
        return cell_index
    else:
        raise ValueError("Invalid cell index parameters")

# Animation frame navigation
def get_keyframe_cells(start_frame: int, end_frame: int, item_id: str):
    """Get cell indices for a range of frames."""
    guid = csc.Guid(item_id)
    cells = []
    
    for frame in range(start_frame, end_frame + 1):
        cell = csc.layers.index.CellIndex(frame, guid)
        if cell.is_valid():
            cells.append(cell)
    
    return cells

# Example usage in layer operations
start_frame = 1
end_frame = 30
object_id = "animation-object-001"

# Get all cell indices for the animation range
animation_cells = get_keyframe_cells(start_frame, end_frame, object_id)
print(f"Created {len(animation_cells)} valid cell indices")
```

## Usage Notes

- CellIndex provides precise location addressing within animation layers
- Frame indexing starts from the beginning of the layer timeline
- Item IDs use GUID format for unique identification across the system
- Validation with `is_valid()` is recommended before using cell indices in operations
- The default constructor creates an invalid index that must be configured before use
- Cell indices are essential for layer data access and modification operations
- Both frame and item ID are required for meaningful cell identification

## See Also

- `csc.Guid` - Unique identifier implementation
- `csc.layers.index.FramesIndices` - Frame range indexing
- `csc.layers.index.FramesInterval` - Frame interval management
- `csc.layers.index.IndicesContainer` - Index container operations
- `csc.layers.layer.Cell` - Cell data structure and operations