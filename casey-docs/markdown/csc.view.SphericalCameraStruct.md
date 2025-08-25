[CLEAN]

# csc.view.SphericalCameraStruct

## Overview

SphericalCameraStruct represents a camera configuration within the csc.view module. It contains a 3D position, a 3D target, and a camera type value. It is used to pass or read camera state in the API; detailed behavior and constraints are undocumented.

## Class Definition

```python
class csc.view.SphericalCameraStruct
```

## Constructor

### `__init__(self)`

Initialize a new SphericalCameraStruct instance.

**Returns:**
- None

## Attributes

- position: Vector3f – get/set; undocumented details.
- target: Vector3f – get/set; undocumented details.
- type: CameraType – get/set; undocumented details.

## Usage Notes

- Properties are reported as get/set; specific validation, defaults, and side effects are undocumented.
- Types Vector3f and CameraType refer to API-defined types in the Cascadeur environment.

