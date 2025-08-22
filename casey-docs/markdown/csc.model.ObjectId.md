[CLEAN]

# csc.model.ObjectId

**Module:** `csc.model.ObjectId`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.model.ObjectId.html)

## Overview

The `ObjectId` class represents a unique identifier for model objects within the Cascadeur system. It provides functionality for creating, managing, and converting object identifiers, supporting both string-based initialization and null state checking for robust object identification in animation workflows.

## Class Definition

```python
class csc.model.ObjectId
```

The ObjectId class encapsulates object identification functionality for model elements, providing overloaded constructors and utility methods for identifier management.

## Constructor (Overloaded)

### `__init__(self, arg0: str) -> None`

Initializes an ObjectId with a string identifier.

**Parameters:**
- `arg0` (str): String representation of the object identifier

**Returns:**
- None

### `__init__(self) -> None`

Initializes a default ObjectId instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `is_null(self) -> bool`

Checks whether the object identifier is null or empty.

**Returns:**
- bool: True if the identifier is null/empty, False otherwise

### `null() -> ObjectId` (Static)

Creates a null object identifier.

**Returns:**
- ObjectId: A null identifier instance

### `to_string(self) -> str`

Converts the object identifier to its string representation.

**Returns:**
- str: String representation of the identifier

## Usage Example

```python
import csc.model

# Create object ID from string
obj_id_from_string = csc.model.ObjectId("model_object_123")

# Create default object ID
obj_id_default = csc.model.ObjectId()

# Create null object ID
null_obj_id = csc.model.ObjectId.null()

# Check if object ID is null
if obj_id_default.is_null():
    print("Object ID is null")

# Convert object ID to string
id_string = obj_id_from_string.to_string()
print(f"Object ID as string: {id_string}")

# Use with scene operations
import csc.domain

selector = csc.domain.Selector()
selection = selector.selected()

# Object IDs can be used in selection operations
model_ids = set()
for obj_id in selection.ids:
    if isinstance(obj_id, csc.model.ObjectId):
        model_ids.add(obj_id)
        print(f"Found model object: {obj_id.to_string()}")

# Check for null state before operations
if not obj_id_from_string.is_null():
    # Safe to use the object ID
    obj_string = obj_id_from_string.to_string()
    print(f"Processing object: {obj_string}")

# Use in selection operations
object_ids = {csc.model.ObjectId("object1"), csc.model.ObjectId("object2")}
selector.select(
    ids=object_ids,
    mode=csc.domain.SelectorMode.NewSelection
)
```

## Usage Notes

- ObjectId is the primary identifier type for model objects in Cascadeur scenes
- The overloaded constructor provides flexibility for creating identifiers from strings or as defaults
- Null checking with `is_null()` is important before performing operations on the identifier
- String conversion with `to_string()` enables debugging and logging of object identifiers
- Object IDs are commonly used in selection operations and scene manipulation
- This class works alongside `csc.domain.Tool_object_id` to support different types of scene objects
- Always check for null state when working with object identifiers to avoid errors
- ObjectId instances are used throughout the model layer for object referencing

## See Also

- `csc.domain.Tool_object_id` - Tool object identification system
- `csc.domain.Selection` - Selection container that can hold object IDs
- `csc.domain.Selector` - Scene selection operations that work with object IDs
- `csc.model.ModelViewer` - Model viewing functionality that uses object IDs
- `csc.model.DataId` - Data identification for model elements