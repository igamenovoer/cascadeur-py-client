[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:39 | Original: 0a9b4894 -->

# csc.rig.TwistProperty

**Module:** `csc.rig.TwistProperty`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.rig.TwistProperty.html)

## Overview

Represents a rig twist property with access to related identifiers and twist parameters. Provides properties for joint path, object id, twist axis, and twist strength.

## Class Definition

```python
class csc.rig.TwistProperty
```

Container for twist-related rigging data and attributes.

## Constructor

### `__init__() -> None`

Initializes a TwistProperty instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__init__() -> None`

Initializes a TwistProperty instance.

**Parameters:**
- None

**Returns:**
- None

## Attributes

- `joint_path_name` (property): Joint path name associated with the twist property.
- `object_id` (property): Object identifier related to the twist property.
- `twist_axis` (property): Axis along which the twist is applied.
- `twist_strength` (property): Strength of the twist effect.
- `__annotations__` (dict): Type annotations dictionary.
- `__module__` (str): Module name where the class is defined (`'csc.rig'`).

## Usage Example

```python
import csc.rig

tp = csc.rig.TwistProperty()
# Access properties (getters/setters as provided by the API)
jp = tp.joint_path_name
oid = tp.object_id
axis = tp.twist_axis
strength = tp.twist_strength
```

## Usage Notes

- Properties such as joint_path_name, object_id, twist_axis, and twist_strength are exposed as properties; consult the API environment for supported get/set behavior.
- This class encapsulates twist configuration for rig elements and is typically used within rigging workflows.

## See Also

- csc.rig.BoneProperty
- csc.rig.TwistBoneProperty
- csc.rig.AddElementData