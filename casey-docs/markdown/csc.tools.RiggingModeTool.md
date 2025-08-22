[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:45 | Original: 5d522a58 -->

# csc.tools.RiggingModeTool

**Module:** `csc.tools.RiggingModeTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.RiggingModeTool.html)

## Overview

Rigging mode tool class providing methods to manage rigging-related data such as joints data, layer identifiers, and preserved settings within Cascadeur.

## Class Definition

```python
class csc.tools.RiggingModeTool
```

Tool class for rigging mode operations and data management.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a RiggingModeTool instance.

**Parameters:**
- `*args` (tuple): Positional arguments (unspecified).
- `**kwargs` (dict): Keyword arguments (unspecified).

**Returns:**
- None

## Methods

### `erase_joints_data(arg0) -> None`

Erases joints data.

**Parameters:**
- `arg0` (unknown): Parameter for specifying data to erase.

**Returns:**
- None

### `erase_layer_id_by_object_ids(arg0) -> None`

Erases layer ID(s) associated with specified object IDs.

**Parameters:**
- `arg0` (unknown): Object IDs or related data.

**Returns:**
- None

### `erase_layers_ids(arg0) -> None`

Erases layer IDs.

**Parameters:**
- `arg0` (unknown): Layer identifiers or related data.

**Returns:**
- None

### `erase_preserved_data(arg0) -> None`

Erases preserved data.

**Parameters:**
- `arg0` (unknown): Preserved data or selector.

**Returns:**
- None

### `erase_preserved_object_ids(arg0) -> None`

Erases preserved object IDs.

**Parameters:**
- `arg0` (unknown): Object IDs or related data.

**Returns:**
- None

### `erase_preserved_setting(arg0) -> None`

Erases preserved setting.

**Parameters:**
- `arg0` (unknown): Setting key or related data.

**Returns:**
- None

### `get_joints_data() -> unknown`

Retrieves joints data.

**Parameters:**
- None

**Returns:**
- unknown: Joints data.

### `get_layer_id_by_object_ids() -> unknown`

Retrieves a layer ID mapped by object IDs.

**Parameters:**
- None

**Returns:**
- unknown: Layer ID information.

### `get_layers_ids() -> unknown`

Retrieves layer IDs.

**Parameters:**
- None

**Returns:**
- unknown: Layer IDs.

### `get_preserved_data() -> unknown`

Retrieves preserved data.

**Parameters:**
- None

**Returns:**
- unknown: Preserved data.

### `get_preserved_object_ids() -> unknown`

Retrieves preserved object IDs.

**Parameters:**
- None

**Returns:**
- unknown: Preserved object IDs.

### `get_preserved_setting() -> unknown`

Retrieves preserved setting.

**Parameters:**
- None

**Returns:**
- unknown: Preserved setting.

### `set_joints_data(arg0, arg1) -> None`

Sets joints data.

**Parameters:**
- `arg0` (unknown): Target or key.
- `arg1` (unknown): Joints data value.

**Returns:**
- None

### `set_layers_ids(arg0, arg1) -> None`

Sets layer IDs.

**Parameters:**
- `arg0` (unknown): Target or key.
- `arg1` (unknown): Layer IDs value.

**Returns:**
- None

### `set_preserved_data(arg0, arg1) -> None`

Sets preserved data.

**Parameters:**
- `arg0` (unknown): Target or key.
- `arg1` (unknown): Data value.

**Returns:**
- None

### `set_preserved_object_ids(arg0, arg1) -> None`

Sets preserved object IDs.

**Parameters:**
- `arg0` (unknown): Target or key.
- `arg1` (unknown): Object IDs value.

**Returns:**
- None

### `set_preserved_setting(arg0, arg1) -> None`

Sets preserved setting.

**Parameters:**
- `arg0` (unknown): Setting key or target.
- `arg1` (unknown): Setting value.

**Returns:**
- None

### `set_undo_redo_context(arg0, arg1, ...) -> None`

Sets undo/redo context.

**Parameters:**
- `arg0` (unknown): Context parameter.
- `arg1` (unknown): Context parameter.
- `...` (unknown): Additional context parameters.

**Returns:**
- None

## Usage Example

```python
import csc.tools

tool = csc.tools.RiggingModeTool()
# Example: set and get preserved setting (parameters are unknown)
tool.set_preserved_setting('some_key', 'some_value')
setting = tool.get_preserved_setting()
```

## Usage Notes

- Parameter types are unspecified in the source and may depend on Cascadeur’s internal data structures.
- Use getter methods to inspect current data before applying erase or set operations.
- The undo/redo context should be configured when performing batch operations to maintain a clean action history.

## See Also

- Other tools in the `csc.tools` module