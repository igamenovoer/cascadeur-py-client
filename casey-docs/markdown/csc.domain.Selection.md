[CLEAN]

# csc.domain.Selection

**Module:** `csc.domain.Selection`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Selection.html)

## Overview

The `Selection` class represents a container for selected objects in the Cascadeur scene. It provides access to both unordered and ordered collections of selected object IDs, supporting both model objects and tool objects within the animation system.

## Class Definition

```python
class csc.domain.Selection
```

The Selection class encapsulates the current state of object selection, providing properties to access selected elements in different organizational formats.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Selection instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Properties

### `ids` (Property)

Gets the set of selected object IDs without ordering information.

**Type:** `Set[csc.model.ObjectId | csc.scene.Tool_object_id]`

**Access:** Read-only property

### `ordered_ids` (Property)

Gets the selected object IDs in their selection order.

**Type:** `List[csc.model.ObjectId | csc.scene.Tool_object_id]` (ordered collection)

**Access:** Read-only property

## Usage Example

```python
import csc.domain
import csc.model

# Get a selection instance from a selector
selector = csc.domain.Selector()
selection = selector.selected()

# Access selected object IDs as a set
selected_ids = selection.ids
print(f"Number of selected objects: {len(selected_ids)}")

# Access selected object IDs in order
ordered_selection = selection.ordered_ids
print(f"First selected object: {ordered_selection[0] if ordered_selection else 'None'}")

# Iterate through selected objects
for obj_id in selection.ids:
    print(f"Selected object ID: {obj_id}")

# Check if specific object is selected
target_id = csc.model.ObjectId()
is_selected = target_id in selection.ids

# Work with ordered selection for operations that depend on selection sequence
for i, obj_id in enumerate(selection.ordered_ids):
    print(f"Selection order {i + 1}: {obj_id}")
```

## Usage Notes

- The Selection class provides two different views of the same selected objects: unordered (set) and ordered (list)
- Use `ids` when you need fast membership testing or set operations
- Use `ordered_ids` when the sequence of selection matters for your operations
- The class supports both model objects and tool objects, allowing flexible scene interaction
- Selection state is typically obtained from a Selector rather than created directly
- The ordered_ids property preserves the chronological order in which objects were selected
- Both properties are read-only, reflecting the immutable nature of a selection snapshot

## See Also

- `csc.domain.Selector` - Main selector class for managing scene selection
- `csc.domain.Select` - Selection configuration and parameters
- `csc.model.ObjectId` - Model object identification system
- `csc.scene.Tool_object_id` - Tool object identification system
- `csc.domain.Pivot` - Pivot operations related to selection