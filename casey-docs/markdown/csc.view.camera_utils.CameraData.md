[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:47 | Original: bba7bf04 -->

# csc.view.camera_utils.CameraData

**Module:** `csc.view.camera_utils.CameraData`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.view.camera_utils.CameraData.html)

## Overview

CameraData class. Represents camera-related data and provides access to its identifier, name, and whether it is a custom camera.

## Class Definition

```python
class csc.view.camera_utils.CameraData
```

Represents data for a camera entity in the view module.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a CameraData instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

**Returns:**
- None

## Methods

### `id(self) -> csc.model.ObjectId`

Returns the identifier of the camera.

**Parameters:**
- None

**Returns:**
- csc.model.ObjectId: The camera object identifier.

### `isCustom(self) -> bool`

Indicates whether the camera is a custom camera.

**Parameters:**
- None

**Returns:**
- bool: True if the camera is custom; otherwise, False.

### `name(self) -> str`

Returns the name of the camera.

**Parameters:**
- None

**Returns:**
- str: The camera name.

### `__annotations__`

Class attribute containing type annotations.

**Parameters:**
- None

**Returns:**
- dict: Mapping of attribute names to type annotations.

### `__module__`

Class attribute specifying the module path.

**Parameters:**
- None

**Returns:**
- str: The module name ('csc.view.camera_utils').

## Usage Example

```python
# Note: CameraData instances are typically provided by the Cascadeur API.

from csc.view.camera_utils import CameraData

def describe_camera(cam: CameraData):
    cam_id = cam.id()
    cam_name = cam.name()
    custom = cam.isCustom()
    print(f"Camera: {cam_name}, id={cam_id}, is_custom={custom}")
```

## Usage Notes

- CameraData provides read-access methods to identify and describe a camera.
- The id method returns a csc.model.ObjectId, which can be used with other API components that accept object identifiers.
- isCustom helps distinguish between built-in and user-defined cameras.

## See Also

- csc.view.Camera
- csc.view.Viewport
- csc.view.CameraType