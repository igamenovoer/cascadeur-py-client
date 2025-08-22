[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:36 | Original: 93295ece -->

# csc.parts.Info

**Module:** `csc.parts.Info`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.parts.Info.html)

## Overview

Info class providing access to basic part information including type, name, path, and object identifier.

## Class Definition

```python
class csc.parts.Info
```

Represents information about a part, exposing attributes for its type, name, path, and object ID.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes an Info instance.

**Parameters:**
- `*args` (tuple): Positional arguments (details not specified in source).
- `**kwargs` (dict): Keyword arguments (details not specified in source).

**Returns:**
- None

## Methods

(No additional methods documented.)

## Attributes

- `type` (csc.parts.Type): Get csc.parts.Type
- `name` (str): Get string
- `path` (str): Get string
- `object_id` (csc.model.ObjectId): Get csc.model.ObjectId

## Usage Example

```python
import csc.parts

# Practical usage example
info = csc.parts.Info()
t = info.type
n = info.name
p = info.path
oid = info.object_id
```

## Usage Notes

- Attribute access returns basic metadata about the part.
- Types referenced include csc.parts.Type and csc.model.ObjectId.
- Constructor arguments are not documented; instantiate accordingly to your context in the Cascadeur API.

## See Also

- csc.parts.Type
- csc.model.ObjectId