[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:38 | Original: 29603328 -->

# csc.rig.BoneProperty

**Module:** `csc.rig.BoneProperty`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.rig.BoneProperty.html)

## Overview

BoneProperty represents a rigging-related property associated with a bone. It provides access to identifiers and names related to a specific bone and its joint path in the rig.

## Class Definition

```python
class csc.rig.BoneProperty
```

A class encapsulating bone-related identifiers and properties within the rigging system.

## Constructor

### `__init__(self) -> None`

Initializes a new BoneProperty instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__init__(self) -> None`

Initializes a new BoneProperty instance.

**Parameters:**
- None

**Returns:**
- None

## Attributes

- `__annotations__`: {}
- `__module__`: 'csc.rig'
- `bone_name` (property): Bone name associated with this property.
- `joint_path_name` (property): Joint path name associated with this property.
- `object_id` (property): Object identifier associated with this property.
- `required_field` (property): Indicates a required field for this property.

## Usage Example

```python
from csc.rig import BoneProperty

# Create a BoneProperty instance
bp = BoneProperty()

# Access properties (read-only/property attributes)
name = bp.bone_name
joint_path = bp.joint_path_name
obj_id = bp.object_id
is_required = bp.required_field
```

## Usage Notes

- The listed attributes are properties; their mutability and exact types are determined by the underlying API.
- Use these properties to query metadata for a bone within a rig.
- Construction does not require arguments.

## See Also

- csc.rig.AddElementData
- csc.rig.TwistProperty
- csc.rig.TwistBoneProperty
- csc.rig.QrtData