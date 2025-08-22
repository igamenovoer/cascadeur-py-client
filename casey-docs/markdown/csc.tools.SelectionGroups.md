[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:46 | Original: cb59375d -->

# csc.tools.SelectionGroups

**Module:** `csc.tools.SelectionGroups`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.SelectionGroups.html)

## Overview

SelectionGroups class.

## Class Definition

```python
class csc.tools.SelectionGroups
```

Represents the SelectionGroups tool within the csc.tools module.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a SelectionGroups instance.

**Parameters:**
- `*args` (tuple): Positional arguments (unspecified).
- `**kwargs` (dict): Keyword arguments (unspecified).

**Returns:**
- None

## Methods

### `core(self) -> object`

Returns the core object associated with SelectionGroups.

**Parameters:**
- None

**Returns:**
- object: Core object.

### `import_file(self, path: str) -> None`

Imports selection groups from a file.

**Parameters:**
- `path` (str): Path to the file to import.

**Returns:**
- None

### `activate(self, arg0, arg1) -> None`

Activates a selection group.

**Parameters:**
- `arg0` (unspecified): Parameter not documented.
- `arg1` (unspecified): Parameter not documented.

**Returns:**
- None

### `deactivate(self, arg0, arg1) -> None`

Deactivates a selection group.

**Parameters:**
- `arg0` (unspecified): Parameter not documented.
- `arg1` (unspecified): Parameter not documented.

**Returns:**
- None

## Usage Example

```python
import csc.tools

# Create SelectionGroups tool instance
sel_groups = csc.tools.SelectionGroups()

# Access core
core_obj = sel_groups.core()

# Import groups from a file
sel_groups.import_file("path/to/selection_groups.json")

# Activate/deactivate (parameters depend on actual API usage)
sel_groups.activate(arg0, arg1)
sel_groups.deactivate(arg0, arg1)
```

## Usage Notes

- Constructor accepts unspecified arguments; refer to higher-level tool initialization context if available.
- The core() method returns a generic object representing the internal core; its interface is not detailed here.
- File path provided to import_file must point to a valid selection groups file.
- Parameters for activate and deactivate are not documented in detail; use with caution and consult sample scripts or additional documentation if available.

## See Also

- csc.tools.selection.Core
- csc.tools.selection.Group
- csc.tools.selection.Mode
- csc.tools.MirrorTool