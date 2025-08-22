[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:44 | Original: d99e64dd -->

# csc.tools.JointData

**Module:** `csc.tools.JointData`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.JointData.html)

## Overview

JointData represents joint-related data in the csc.tools module, exposing properties for local transform and visibility.

## Class Definition

```python
class csc.tools.JointData
```

A data container class providing access to local position, rotation, scale, and visibility of a joint.

## Constructor

### `__init__(self) -> None`

Initializes a JointData instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__init__(self) -> None`

Initializes a JointData instance.

**Parameters:**
- None

**Returns:**
- None

## Attributes

- `__annotations__`: {}
- `__module__`: 'csc.tools'
- `local_position` (property): Local position of the joint.
- `local_rotation` (property): Local rotation of the joint.
- `local_scale` (property): Local scale of the joint.
- `visibility` (property): Visibility state of the joint.

## Usage Example

```python
import csc.tools

# Practical usage example
jd = csc.tools.JointData()
# Access properties
pos = jd.local_position
rot = jd.local_rotation
scl = jd.local_scale
vis = jd.visibility
```

## Usage Notes

- Properties provide access to local transform components and visibility; specific types and mutability are not detailed in the source page.
- Instantiate with the default constructor before accessing properties.

## See Also

- csc.tools.MirrorTool
- csc.tools.ObjectKey
- csc.tools.DataKey