[CLEAN]

# csc.domain.Select

**Module:** `csc.domain.Select`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Select.html)

## Overview

The `Select` class represents properties of the current selection state of the scene in Cascadeur. It provides access to selected object IDs, pivot information, filtering options, selection modes, and type filtering capabilities.

## Class Definition

```python
class csc.domain.Select
```

The Select class encapsulates the current selection state and provides properties for managing scene selection.

## Constructor

### `__init__(self)`

Initializes a new Select instance.

## Attributes

### `object_ids` (Get/Set)

A set of selected object IDs. Contains objects of type `csc.model.ObjectId` or `csc.scene.Tool_object_id`.

**Type:** `Set[csc.model.ObjectId | csc.scene.Tool_object_id]`

### `pivot_id` (Get/Set)

The ID of the selected pivot object.

**Type:** `csc.model.ObjectId | csc.scene.Tool_object_id`

### `filter` (Get/Set)

The selector filter configuration for the current selection.

**Type:** `csc.scene.SelectorFilter`

### `mode` (Get/Set)

The selection mode configuration.

**Type:** `csc.scene.SelectorMode`

### `types_filter` (Get/Set)

A set of strings representing type filters for selection.

**Type:** `Set[str]`

## Usage Example

```python
import csc.domain
import csc.model
import csc.scene

# Create a selection instance
selection = csc.domain.Select()

# Access and modify selected object IDs
object_id = csc.model.ObjectId()
selection.object_ids = {object_id}

# Set pivot ID
pivot_id = csc.model.ObjectId()
selection.pivot_id = pivot_id

# Configure selection filter
selection.filter = csc.scene.SelectorFilter()

# Set selection mode
selection.mode = csc.scene.SelectorMode()

# Set type filters
selection.types_filter = {"mesh", "bone", "constraint"}

# Access current selection state
current_objects = selection.object_ids
current_pivot = selection.pivot_id
current_filter = selection.filter
print(f"Selected objects: {len(current_objects)}")
```

## Usage Notes

- The Select class provides a comprehensive interface for managing scene selection state
- Object IDs can be either model objects or tool objects depending on the context
- The pivot ID represents the object that serves as the transformation pivot
- Selection filters control which types of objects can be selected
- Selection modes determine the behavior of selection operations
- Type filters allow limiting selection to specific object types using string identifiers
- All attributes support both get and set operations for flexible selection management

## See Also

- `csc.model.ObjectId` - Model object identification
- `csc.scene.Tool_object_id` - Tool object identification  
- `csc.scene.SelectorFilter` - Selection filtering configuration
- `csc.scene.SelectorMode` - Selection mode configuration
- `csc.domain.Selector` - Main selector class for scene element selection