[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:38 | Original: c5026152 -->

# csc.rig.QrtData

**Module:** `csc.rig.QrtData`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.rig.QrtData.html)

## Overview

QrtData is a rig-related data container in the csc.rig module. It provides properties for configuring rig parameters such as body, limb hinge directions, alignment behaviors, layer creation, and twist settings.

## Class Definition

```python
class csc.rig.QrtData
```

Represents rig configuration data with several readable properties.

## Constructor

### `__init__() -> None`

Initializes a QrtData instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__init__() -> None`

Initializes the object.

**Parameters:**
- None

**Returns:**
- None

## Attributes

- `body` (property): Body-related data for the rig.
- `hinge_arm_direction` (property): Hinge direction configuration for arms.
- `hinge_leg_direction` (property): Hinge direction configuration for legs.
- `is_align_pelvis` (property): Flag indicating whether pelvis alignment is enabled.
- `is_create_layers` (property): Flag indicating whether layers should be created.
- `is_replace_existing` (property): Flag indicating whether existing data should be replaced.
- `is_spline_ik` (property): Flag indicating whether spline IK is enabled.
- `left_hand` (property): Left hand configuration/data.
- `right_hand` (property): Right hand configuration/data.
- `twists` (property): Twist configuration/data.

## Usage Example

```python
from csc.rig import QrtData

# Create and configure QrtData
qrt = QrtData()

# Access properties (read current configuration)
body_data = qrt.body
arm_dir = qrt.hinge_arm_direction
leg_dir = qrt.hinge_leg_direction
align_pelvis = qrt.is_align_pelvis
create_layers = qrt.is_create_layers
replace_existing = qrt.is_replace_existing
use_spline_ik = qrt.is_spline_ik
left_hand_cfg = qrt.left_hand
right_hand_cfg = qrt.right_hand
twists_cfg = qrt.twists
```

## Usage Notes

- Properties are exposed as attributes; their mutability and exact types are not specified in the source page.
- Use QrtData to read or pass rig configuration data where required by other rigging tools or APIs in csc.rig.
- Default values and detailed structures for the properties are not documented on the source page.

## See Also

- csc.rig.AddElementData
- csc.rig.BoneProperty
- csc.rig.TwistProperty
- csc.rig.TwistBoneProperty