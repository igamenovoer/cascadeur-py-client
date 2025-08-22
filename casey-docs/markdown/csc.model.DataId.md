[CLEAN]

# csc.model.DataId

**Module:** `csc.model.DataId`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.model.DataId.html)

## Overview

The `DataId` class represents a unique identifier for data elements within the Cascadeur model system. It provides functionality for creating, managing, and converting data identifiers, supporting both string-based initialization and null state checking for robust data identification in model operations and data management workflows.

## Class Definition

```python
class csc.model.DataId
```

The DataId class encapsulates data identification functionality for model elements, providing overloaded constructors and utility methods for data identifier management.

## Constructor (Overloaded)

### `__init__(self, arg0: str) -> None`

Initializes a DataId with a string identifier.

**Parameters:**
- `arg0` (str): String representation of the data identifier

**Returns:**
- None

### `__init__(self) -> None`

Initializes a default DataId instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `is_null(self) -> bool`

Checks whether the data identifier is null or empty.

**Returns:**
- bool: True if the identifier is null/empty, False otherwise

### `null() -> DataId` (Static)

Creates a null data identifier.

**Returns:**
- DataId: A null identifier instance

### `to_string(self) -> str`

Converts the data identifier to its string representation.

**Returns:**
- str: String representation of the identifier

## Usage Example

```python
import csc.model

# Create data ID from string
data_id_from_string = csc.model.DataId("data_element_456")

# Create default data ID
data_id_default = csc.model.DataId()

# Create null data ID
null_data_id = csc.model.DataId.null()

# Check if data ID is null
if data_id_default.is_null():
    print("Data ID is null")

# Convert data ID to string
id_string = data_id_from_string.to_string()
print(f"Data ID as string: {id_string}")

# Use with model operations
import csc.domain

# Data IDs in selection operations
data_ids = set()
data_ids.add(csc.model.DataId("animation_data_001"))
data_ids.add(csc.model.DataId("constraint_data_002"))
data_ids.add(csc.model.DataId("physics_data_003"))

# Process data elements by ID
for data_id in data_ids:
    if not data_id.is_null():
        print(f"Processing data: {data_id.to_string()}")

# Data management workflow
def manage_model_data(data_identifiers):
    """Manage model data elements by their identifiers."""
    processed_data = []
    
    for identifier_string in data_identifiers:
        data_id = csc.model.DataId(identifier_string)
        
        if not data_id.is_null():
            # Process the data element
            processed_data.append({
                'id': data_id,
                'string_id': data_id.to_string(),
                'is_valid': True
            })
        else:
            processed_data.append({
                'id': data_id,
                'string_id': '',
                'is_valid': False
            })
    
    return processed_data

# Example usage with data elements
data_elements = [
    "keyframe_data_001",
    "constraint_data_002", 
    "physics_data_003",
    ""  # Empty string will create null ID
]

processed = manage_model_data(data_elements)
for item in processed:
    print(f"Data ID: {item['string_id']}, Valid: {item['is_valid']}")

# Integration with model viewers and editors
def setup_data_viewer(data_ids):
    """Setup data viewer with specific data elements."""
    valid_ids = []
    
    for data_id in data_ids:
        if isinstance(data_id, str):
            data_id = csc.model.DataId(data_id)
        
        if not data_id.is_null():
            valid_ids.append(data_id)
    
    return valid_ids

# Data selection and filtering
def filter_data_by_pattern(all_data_ids, pattern):
    """Filter data IDs by string pattern."""
    filtered_ids = []
    
    for data_id in all_data_ids:
        id_string = data_id.to_string()
        if pattern in id_string:
            filtered_ids.append(data_id)
    
    return filtered_ids
```

## Usage Notes

- DataId is the primary identifier type for data elements in Cascadeur model operations
- The overloaded constructor provides flexibility for creating identifiers from strings or as defaults
- Null checking with `is_null()` is important before performing operations on the identifier
- String conversion with `to_string()` enables debugging and logging of data identifiers
- Data IDs are commonly used in model operations, data management, and element selection
- This class works alongside other model identifier types for comprehensive element referencing
- Always check for null state when working with data identifiers to avoid errors
- DataId instances are used throughout the model layer for data element referencing

## See Also

- `csc.model.ObjectId` - Object identification system
- `csc.model.BehaviourId` - Behavior identification for model elements
- `csc.model.SettingId` - Setting identification system
- `csc.model.DataViewer` - Data viewing functionality that uses data IDs
- `csc.model.DataEditor` - Data editing operations with identifier management