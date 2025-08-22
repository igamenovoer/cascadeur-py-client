[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:36 | Original: 46d3dd23 -->

# csc.parts.Buffer

**Module:** `csc.parts.Buffer`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.parts.Buffer.html)

## Overview

Buffer class. Provides methods to operate parts of the scene.

## Class Definition

```python
class csc.parts.Buffer
```

Represents a buffer for managing and manipulating parts of the scene.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a Buffer instance.

**Parameters:**
- `*args` (tuple): Variable positional arguments.
- `**kwargs` (dict): Variable keyword arguments.

**Returns:**
- None

## Methods

### `get([source_dir]) -> Any`

Retrieve data from the buffer, optionally from a specified source directory.

**Parameters:**
- `source_dir` (optional): Source directory.

**Returns:**
- Any: Retrieved data.

### `get_parts_info_by_id(self) -> Any`

Get parts information by identifier.

**Parameters:**
- None

**Returns:**
- Any: Parts information.

### `get_src_dir(self) -> Any`

Get the source directory.

**Parameters:**
- None

**Returns:**
- Any: Source directory.

### `insert_elementary_by_id(self, arg0, arg1, arg2) -> Any`

Insert an elementary item by identifier.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `arg2`: Parameter.

**Returns:**
- Any: Result of insertion.

### `insert_elementary_by_path(self, arg0, arg1, arg2) -> Any`

Insert an elementary item by path.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `arg2`: Parameter.

**Returns:**
- Any: Result of insertion.

### `insert_object_by_id(self, arg0, arg1, arg2, arg3) -> Any`

Insert a single object by identifier.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `arg2`: Parameter.
- `arg3`: Parameter.

**Returns:**
- Any: Result of insertion.

### `insert_object_by_path(self, arg0, arg1, ...) -> Any`

Insert a single object by path.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `...`: Additional parameters.

**Returns:**
- Any: Result of insertion.

### `insert_objects_by_id(self, arg0, arg1, arg2, ...) -> Any`

Insert multiple objects by identifiers.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `arg2`: Parameter.
- `...`: Additional parameters.

**Returns:**
- Any: Result of insertion.

### `insert_objects_by_path(self, arg0, arg1, ...) -> Any`

Insert multiple objects by paths.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `...`: Additional parameters.

**Returns:**
- Any: Result of insertion.

### `insert_selected_objects_by_path(self, arg0, ...) -> Any`

Insert selected objects by path.

**Parameters:**
- `arg0`: Parameter.
- `...`: Additional parameters.

**Returns:**
- Any: Result of insertion.

### `insert_update_group_by_id(self, arg0, arg1, arg2) -> Any`

Insert an update group by identifier.

**Parameters:**
- `arg0`: Parameter.
- `arg1`: Parameter.
- `arg2`: Parameter.

**Returns:**
- Any: Result of insertion.

### `insert_update_group_by_path(self, arg0, ...) -> Any`

Insert an update group by path.

**Parameters:**
- `arg0`: Parameter.
- `...`: Additional parameters.

**Returns:**
- Any: Result of insertion.

### `refresh(self) -> Any`

Refresh the buffer state.

**Parameters:**
- None

**Returns:**
- Any: Result of the operation.

### `reset_cache(self) -> Any`

Reset internal cache.

**Parameters:**
- None

**Returns:**
- Any: Result of the operation.

### `take_elementary_to_parts(self, part_name, ...) -> Any`

Take an elementary item to parts by part name.

**Parameters:**
- `part_name`: Part name.
- `...`: Additional parameters.

**Returns:**
- Any: Result of the operation.

### `take_object_to_parts(self, part_name, from, ...) -> Any`

Take a single object to parts by part name and source.

**Parameters:**
- `part_name`: Part name.
- `from`: Source.
- `...`: Additional parameters.

**Returns:**
- Any: Result of the operation.

### `take_objects_to_parts(self, part_name, from, ...) -> Any`

Take multiple objects to parts by part name and source.

**Parameters:**
- `part_name`: Part name.
- `from`: Source.
- `...`: Additional parameters.

**Returns:**
- Any: Result of the operation.

### `take_selected_objects_to_parts(self, ...) -> Any`

Take selected objects to parts.

**Parameters:**
- `...`: Parameters as required.

**Returns:**
- Any: Result of the operation.

### `take_update_group_to_parts(self, part_name, ...) -> Any`

Take an update group to parts by part name.

**Parameters:**
- `part_name`: Part name.
- `...`: Additional parameters.

**Returns:**
- Any: Result of the operation.

## Usage Example

```python
import csc.parts

buf = csc.parts.Buffer()
buf.refresh()
info = buf.get()
```

## Usage Notes

- Method signatures are partially unspecified; refer to the official documentation for exact parameter types and meanings.
- Use insert_* methods to add items by id or path.
- Use take_* methods to move items into parts.
- Call refresh and reset_cache to manage buffer state.

## See Also

- Other classes in the csc.parts module