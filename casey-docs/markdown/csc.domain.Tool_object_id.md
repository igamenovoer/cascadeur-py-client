[CLEAN]

# csc.domain.Tool_object_id

**Module:** `csc.domain.Tool_object_id`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Tool_object_id.html)

## Overview

The `Tool_object_id` class represents a unique identifier for tool objects within the Cascadeur animation system. It provides functionality for creating, managing, and converting tool object identifiers, supporting both string-based initialization and null state checking.

## Class Definition

```python
class csc.domain.Tool_object_id
```

The Tool_object_id class encapsulates identification functionality for tool objects, providing overloaded constructors and utility methods for identifier management.

## Constructor (Overloaded)

### `__init__(self, arg0: str) -> None`

Initializes a Tool_object_id with a string identifier.

**Parameters:**
- `arg0` (str): String representation of the tool object identifier

**Returns:**
- None

### `__init__(self) -> None`

Initializes a default Tool_object_id instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `is_null(self) -> bool`

Checks whether the tool object identifier is null or empty.

**Returns:**
- bool: True if the identifier is null/empty, False otherwise

### `null() -> Tool_object_id` (Static)

Creates a null tool object identifier.

**Returns:**
- Tool_object_id: A null identifier instance

### `to_string(self) -> str`

Converts the tool object identifier to its string representation.

**Returns:**
- str: String representation of the identifier

## Usage Example

```python
import csc.domain

# Create tool object ID from string
tool_id_from_string = csc.domain.Tool_object_id("tool_123")

# Create default tool object ID
tool_id_default = csc.domain.Tool_object_id()

# Create null tool object ID
null_tool_id = csc.domain.Tool_object_id.null()

# Check if tool ID is null
if tool_id_default.is_null():
    print("Tool ID is null")

# Convert tool ID to string
id_string = tool_id_from_string.to_string()
print(f"Tool ID as string: {id_string}")

# Use with selection operations
selector = csc.domain.Selector()
selection = selector.selected()

# Tool object IDs can be used in selection
tool_ids = set()
for obj_id in selection.ids:
    if isinstance(obj_id, csc.domain.Tool_object_id):
        tool_ids.add(obj_id)
        print(f"Found tool object: {obj_id.to_string()}")

# Check for null state before operations
if not tool_id_from_string.is_null():
    # Safe to use the tool ID
    tool_string = tool_id_from_string.to_string()
```

## Usage Notes

- Tool_object_id is used alongside csc.model.ObjectId to support different types of scene objects
- The overloaded constructor provides flexibility for creating identifiers from strings or as defaults
- Null checking with `is_null()` is important before performing operations on the identifier
- String conversion with `to_string()` enables debugging and logging of tool identifiers
- Tool object IDs are commonly used in selection operations and scene manipulation
- This class integrates with the selection system to support tool-based workflows
- Always check for null state when working with tool identifiers to avoid errors

## See Also

- `csc.model.ObjectId` - Model object identification system
- `csc.domain.Selection` - Selection container that can hold tool object IDs
- `csc.domain.Selector` - Scene selection operations that work with tool objects
- `csc.domain.Select` - Selection configuration for tool objects