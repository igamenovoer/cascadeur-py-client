[CLEAN]

# csc.update.ExternalProperty

## Overview
ExternalProperty is an enumeration of external property state flags used by Cascadeur's update system. It identifies whether certain animation or physics-related states apply, such as fixation, forward kinematics, or interpolation. The exact semantics of each member are not described in the available source and remain undocumented here.

## Class Definition
```python
class csc.update.ExternalProperty
```

## Constructor

### __init__(value)
Initializes an enum member with the given value; behavior details are undocumented.

Parameters:
- value: undocumented – underlying value used to construct the enum member.

Returns:
- None

## Attributes
- Fixation – enum member (undocumented)
- IsForwardKinematics – enum member (undocumented)
- KinematicsType – enum member (undocumented)
- InterpolationType – enum member (undocumented)
- IsInterpolation – enum member (undocumented)
- AfterPhysics – enum member (undocumented)
- IsKey – enum member (undocumented)
- name – standard Enum attribute: the member name
- value – standard Enum attribute: the underlying value

## Usage Notes
- Use these members to test or specify external property states when interacting with the API.
- Exact meanings of the flags can be context-dependent and are undocumented in the provided source.

