[CLEAN]

# csc.view.Camera

**Module:** `csc.view.Camera`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.view.Camera.html)

## Overview

The `Camera` class represents a domain spherical camera within the Cascadeur view system. It provides functionality for camera control, target setting, and viewport navigation, enabling programmatic manipulation of the 3D viewport camera for animation and scene visualization.

## Class Definition

```python
class csc.view.Camera
```

The Camera class encapsulates spherical camera functionality with methods for positioning, targeting, and zoom operations within the 3D viewport.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Camera instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `set_target(self, arg0: numpy.ndarray[numpy.float32[3, 1]]) -> None`

Sets the target position for the camera to focus on.

**Parameters:**
- `arg0` (numpy.ndarray[numpy.float32[3, 1]]): 3D target position as a 32-bit float array

**Returns:**
- None

### `zoom_to_points(self, arg0: list[numpy.ndarray[numpy.float32[3, 1]]]) -> None`

Adjusts the camera zoom to frame a set of 3D points in the viewport.

**Parameters:**
- `arg0` (list[numpy.ndarray[numpy.float32[3, 1]]]): List of 3D points to frame in the camera view

**Returns:**
- None

## Usage Example

```python
import csc.view
import numpy as np

# Create a camera instance
camera = csc.view.Camera()

# Set camera target to a specific position
target_position = np.array([0.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
camera.set_target(target_position)

# Define points to zoom to
points_to_frame = [
    np.array([1.0, 1.0, 1.0], dtype=np.float32).reshape(3, 1),
    np.array([-1.0, -1.0, -1.0], dtype=np.float32).reshape(3, 1),
    np.array([2.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
]

# Zoom camera to frame all points
camera.zoom_to_points(points_to_frame)

# Example with animation object positions
# Assuming you have object positions from scene
object_positions = []
for obj_id in selected_objects:
    # Get object position (example)
    pos = np.array([x, y, z], dtype=np.float32).reshape(3, 1)
    object_positions.append(pos)

# Frame all selected objects
if object_positions:
    camera.zoom_to_points(object_positions)
```

## Usage Notes

- Camera uses spherical coordinate system for positioning and orientation
- Target setting affects the camera's look-at point in 3D space
- Zoom-to-points automatically calculates appropriate camera distance and position
- All position parameters use numpy arrays with 32-bit float precision
- The camera operates within Cascadeur's 3D viewport system
- Position arrays must be shaped as (3, 1) column vectors
- Zoom operations consider all provided points to determine optimal framing
- Camera changes are immediately reflected in the active viewport

## See Also

- `csc.view.Viewport` - Viewport management and control
- `csc.view.SphericalCameraStruct` - Camera structure and configuration
- `csc.view.CameraType` - Camera type enumeration
- `csc.view.ViewportDomain` - Viewport domain operations
- `csc.view.camera_utils.CameraData` - Camera utility data structures