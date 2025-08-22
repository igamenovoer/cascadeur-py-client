[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:39 | Original: 157a86a7 -->

# csc.tools.ActivateDeactivate

**Module:** `csc.tools.ActivateDeactivate`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.ActivateDeactivate.html)

## Overview

ActivateDeactivate class.

## Class Definition

```python
class csc.tools.ActivateDeactivate
```

A utility class providing methods to activate and deactivate objects within a session.

## Constructor

### `__init__(*args, **kwargs) -> None`

Default constructor.

**Parameters:**
- `*args` (Any): Positional arguments (unspecified).
- `**kwargs` (Any): Keyword arguments (unspecified).

**Returns:**
- None

## Methods

### `activate(self, arg0: csc.domain.Session, arg1: dict[csc.model.ObjectId, csc.model.ObjectId]) -> bool`

Activate objects in the given session.

**Parameters:**
- `arg0` (csc.domain.Session): The active session.
- `arg1` (dict[csc.model.ObjectId, csc.model.ObjectId]): Mapping of object identifiers.

**Returns:**
- bool: Activation result.

### `deactivate(self, arg0: csc.domain.Session, arg1: set[csc.model.ObjectId]) -> None`

Deactivate objects in the given session.

**Parameters:**
- `arg0` (csc.domain.Session): The active session.
- `arg1` (set[csc.model.ObjectId]): Set of object identifiers to deactivate.

**Returns:**
- None

## Usage Example

```python
import csc.tools

tool = csc.tools.ActivateDeactivate()

# Suppose you have a session and object ids
session = ...  # csc.domain.Session
mapping = {obj_id_src: obj_id_dst}  # dict[csc.model.ObjectId, csc.model.ObjectId]
result = tool.activate(session, mapping)

to_deactivate = {obj_id_dst}  # set[csc.model.ObjectId]
tool.deactivate(session, to_deactivate)
```

## Usage Notes

- Ensure a valid csc.domain.Session instance is provided for both activation and deactivation.
- For activate, supply a dictionary mapping source to target csc.model.ObjectId values.
- For deactivate, provide a set of csc.model.ObjectId values to be deactivated.

## See Also

- csc.domain.Session
- csc.model.ObjectId