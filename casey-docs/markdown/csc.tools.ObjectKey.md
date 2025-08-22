[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:45 | Original: 8ac49b36 -->

# csc.tools.ObjectKey

**Module:** `csc.tools.ObjectKey`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.ObjectKey.html)

## Overview

Represents a key identifying an object within Cascadeur tools. Provides properties for object path and behaviour names, and supports equality and hashing for use in collections.

## Class Definition

```python
class csc.tools.ObjectKey
```

A lightweight key object with comparable and hashable semantics, exposing path and behaviour name properties.

## Constructor

### `__init__() -> None`

Creates a new ObjectKey instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__eq__(arg0: csc.tools.ObjectKey) -> bool`

Checks equality with another ObjectKey.

**Parameters:**
- `arg0` (csc.tools.ObjectKey): Another ObjectKey to compare against.

**Returns:**
- bool: True if both keys are equal, otherwise False.

### `__ne__(arg0: csc.tools.ObjectKey) -> bool`

Checks inequality with another ObjectKey.

**Parameters:**
- `arg0` (csc.tools.ObjectKey): Another ObjectKey to compare against.

**Returns:**
- bool: True if keys are not equal, otherwise False.

### `__hash__() -> int`

Returns the hash value of the ObjectKey.

**Parameters:**
- None

**Returns:**
- int: Hash value suitable for hashed collections.

## Attributes

- `__annotations__`: {}
- `__module__`: 'csc.tools'

## Properties

### `behaviour_name`

The behaviour name associated with the object key.

### `path_name`

The path name associated with the object key.

## Usage Example

```python
from csc.tools import ObjectKey

# Create an ObjectKey
key1 = ObjectKey()
key2 = ObjectKey()

# Use in a set or as dict key due to hashing support
unique_keys = {key1, key2}

# Compare keys
are_equal = (key1 == key2)

# Access properties
bn = key1.behaviour_name
pn = key1.path_name
```

## Usage Notes

- ObjectKey instances are hashable and can be used in sets and as dictionary keys.
- Equality and inequality operators are implemented for reliable comparisons.
- Properties `behaviour_name` and `path_name` are read via attribute access.

## See Also

- csc.tools.DataKey
- csc.tools.JointData