[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:45 | Original: e38f2f96 -->

# csc.tools.selection.Core

**Module:** `csc.tools.selection.Core`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.selection.Core.html)

## Overview

Core class for working with selection groups, providing methods to get, set, and process selection groups.

## Class Definition

```python
class csc.tools.selection.Core
```

Core class managing selection groups and related operations.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a Core instance.

**Parameters:**
- `*args` (tuple): Variable positional arguments.
- `**kwargs` (dict): Variable keyword arguments.

**Returns:**
- None

## Methods

### `get_group(self, idx) -> Group`

Retrieves a selection group by its index.

**Parameters:**
- `idx` (GroupIndex): Index of the group to retrieve.

**Returns:**
- Group: The requested selection group.

### `get_groups(self) -> std::map<GroupIndex, Group>`

Returns all selection groups.

**Parameters:**
- None

**Returns:**
- std::map<GroupIndex, Group>: A map of group indices to groups.

### `process(self, index, mode) -> None`

Processes a group based on the provided index and mode.

**Parameters:**
- `index` (GroupIndex): Index of the group to process.
- `mode` (Any): Processing mode.

**Returns:**
- None

### `set_group(self, index, group) -> None`

Sets or updates a selection group at the specified index.

**Parameters:**
- `index` (GroupIndex): Index at which to set the group.
- `group` (Group): Group to set.

**Returns:**
- None

### `set_groups(self, groups) -> None`

Sets all selection groups.

**Parameters:**
- `groups` (std::map<GroupIndex, Group>): A map of group indices to groups.

**Returns:**
- None

## Usage Example

```python
import csc.tools.selection as selection

core = selection.Core()

# Set a single group
# core.set_group(index, group)

# Get a single group
# group = core.get_group(index)

# Set multiple groups
# core.set_groups(groups_map)

# Retrieve all groups
# groups = core.get_groups()

# Process a group
# core.process(index, mode)
```

## Usage Notes

- Ensure valid GroupIndex and Group objects are used when getting or setting groups.
- Use get_groups and set_groups to manage multiple groups efficiently.
- The process method behavior depends on the provided mode; ensure the mode is supported by your workflow.

## See Also

- Related selection tools and group management utilities within the Cascadeur Python API