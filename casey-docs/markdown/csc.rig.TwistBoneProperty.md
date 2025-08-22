[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:38 | Original: a27d10c9 -->

# csc.rig.TwistBoneProperty

**Module:** `csc.rig.TwistBoneProperty`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.rig.TwistBoneProperty.html)

## Overview

Represents twist-related properties for a specific rig bone. Provides access to the bone name and its associated twist properties.

## Class Definition

```python
class csc.rig.TwistBoneProperty
```

Container for a bone's twist configuration in the rig.

## Constructor

### `__init__() -> None`

Initializes a new TwistBoneProperty instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

This class exposes attribute-style properties.

## Attributes

- `bone_name` (property): The name of the bone associated with this twist configuration.
- `twist_properties` (property): The collection or structure holding the twist properties for the bone.

## Usage Example

```python
import csc.rig

# Practical usage example
tbp = csc.rig.TwistBoneProperty()
name = tbp.bone_name
twist = tbp.twist_properties
```

## Usage Notes

- Use bone_name to identify the target bone for which twist properties apply.
- twist_properties provides the twist configuration; inspect or modify according to rigging workflow.
- This class primarily serves as a data container with property accessors.

## See Also

- csc.rig.BoneProperty
- csc.rig.TwistProperty
- csc.rig.QrtData