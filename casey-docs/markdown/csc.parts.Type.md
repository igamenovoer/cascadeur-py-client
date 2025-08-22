[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:42 | Original: e9101a92 -->

# csc.parts.Type

**Module:** `csc.parts.Type`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.parts.Type.html)

## Overview

Type of the parts, enum.

- Elementary: includes only regular and setting functions + regular and setting data + connections that link them
- UpdateGroup: sub update groups and their elementary entities + connections that link them
- Object: includes all related entities of some object
- ObjectGroup: includes all objects and sub object groups and all related entities
- SelectedObjects: selected objects from different groups

## Class Definition

```python
class csc.parts.Type
```

Enumeration of part types. Members:
- Elementary
- UpdateGroup
- Object
- ObjectGroup
- SelectedObjects

Common enum attributes:
- name
- value

## Constructor

### `__init__(self, value) -> None`

Initialize the enum with a value corresponding to one of the defined members.

**Parameters:**
- `value` (Any): Initialization value corresponding to an enum member.

**Returns:**
- None

## Methods

### `__init__(self, value) -> None`

Initialize the enum with a value corresponding to one of the defined members.

**Parameters:**
- `value` (Any): Initialization value corresponding to an enum member.

**Returns:**
- None

## Usage Example

```python
import csc.parts

# Accessing enum members directly
instance = csc.parts.Type.Object

# Using common Enum attributes
print(instance.name)   # 'Object'
print(instance.value)  # underlying value associated with 'Object'
```

## Usage Notes

- Elementary: includes only regular and setting functions + regular and setting data + connections that link them
- UpdateGroup: sub update groups and their elementary entities + connections that link them
- Object: includes all related entities of some object
- ObjectGroup: includes all objects and sub object groups and all related entities
- SelectedObjects: selected objects from different groups
- Enum members also expose standard attributes:
  - name: the member name as a string
  - value: the underlying value associated with the member

## See Also

- csc.parts