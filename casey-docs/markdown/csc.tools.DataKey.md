[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:44 | Original: b4cd6143 -->

# csc.tools.DataKey

**Module:** `csc.tools.DataKey`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.DataKey.html)

## Overview

DataKey represents a key that references specific data associated with an object in the Cascadeur tools module. It provides identity and hashing, and exposes properties for the data name and the related object key.

## Class Definition

```python
class csc.tools.DataKey
```

A lightweight key object with equality and hashing semantics, exposing data_name and object_key properties.

## Constructor

### `__init__() -> None`

Default constructor for DataKey.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__eq__(self: csc.tools.DataKey, arg0: csc.tools.DataKey) -> bool`

Check equality with another DataKey.

**Parameters:**
- `arg0` (csc.tools.DataKey): Another DataKey to compare with.

**Returns:**
- bool: True if both keys are equal, False otherwise.

### `__ne__(self: csc.tools.DataKey, arg0: csc.tools.DataKey) -> bool`

Check inequality with another DataKey.

**Parameters:**
- `arg0` (csc.tools.DataKey): Another DataKey to compare with.

**Returns:**
- bool: True if keys are not equal, False otherwise.

### `__hash__(self: csc.tools.DataKey) -> int`

Return the hash value of the DataKey.

**Parameters:**
- None

**Returns:**
- int: Hash value.

## Attributes

- `__annotations__`: {}
- `__module__`: 'csc.tools'

## Properties

### `data_name`

Name of the data referenced by this key.

### `object_key`

Object key associated with this data.

## Usage Example

```python
import csc.tools

# Create a DataKey instance
dk = csc.tools.DataKey()

# Access properties (read-only properties exposed by the API)
name = dk.data_name
obj_key = dk.object_key

# Use hashing and equality
s = {dk}
same = (dk == csc.tools.DataKey())
```

## Usage Notes

- DataKey supports equality and hashing; it can be used as a dictionary key or stored in sets.
- The properties data_name and object_key are read-only properties exposed by the API.
- Instances constructed with the default constructor may require population by the Cascadeur system before properties hold meaningful values.

## See Also

- csc.tools.ObjectKey
- csc.tools.ObjectKey-related utilities within the tools module