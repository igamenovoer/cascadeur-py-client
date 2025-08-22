[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:46 | Original: 13bf58a3 -->

# csc.tools.selection.Group

**Module:** `csc.tools.selection.Group`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.selection.Group.html)

## Overview

Group class representing a selection group with a set of objects and a pivot object.

## Class Definition

```python
class csc.tools.selection.Group
```

Represents a selection group with:
- objects – std::set<ModelObjectId>
- pivot – ModelObjectId

## Constructor

### `__init__() -> None`

Default constructor.

**Parameters:**
- None

**Returns:**
- None

### `__init__(arg0: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], arg1: Union[csc.model.ObjectId, csc.domain.Tool_object_id]) -> None`

Constructs a Group with specified objects and pivot.

**Parameters:**
- `arg0` (set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]]): Set of object identifiers for the group.
- `arg1` (Union[csc.model.ObjectId, csc.domain.Tool_object_id]): Identifier of the pivot object.

**Returns:**
- None

## Methods

The class provides an overloaded `__init__` constructor as described above. No additional methods are documented.

## Attributes

- `objects`: std::set<ModelObjectId>
- `pivot`: ModelObjectId

## Usage Example

```python
from csc.tools.selection import Group
from csc.model import ObjectId

# Create an empty group
g1 = Group()

# Create a group with objects and a pivot
obj_ids = {ObjectId(1), ObjectId(2)}
pivot_id = ObjectId(1)
g2 = Group(obj_ids, pivot_id)
```

## Usage Notes

- Ensure that all IDs in the objects set and the pivot are valid instances of csc.model.ObjectId or csc.domain.Tool_object_id.
- The pivot should typically be one of the objects in the set.

## See Also

- csc.model.ObjectId
- csc.domain.Tool_object_id
- csc.tools.selection module