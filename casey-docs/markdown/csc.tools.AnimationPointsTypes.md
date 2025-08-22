[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:39 | Original: 2f1bf780 -->

# csc.tools.AnimationPointsTypes

**Module:** `csc.tools.AnimationPointsTypes`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html)

## Overview

Class of basic types of points which physics tools change through animation. Provides accessors for various categories of points and collision-related information:
- get_fulcrum_points – all fulcrum points with collision
- get_fixed_points – all points that need to be fixed with collision
- get_local_fixed_points – points that should keep local coordinates after apply
- get_collision_surface_points – collision points with normal type
- get_collision_pin_points – collision points with pin type
- get_collision_fixed_points – collision points with fulcrum groups
- get_fulcrum_floor_points – points that collide only with floor
- get_fixed_floor_points – points that collide only with floor and fulcrum groups
- get_frame_collision_info_points – collision info about points

## Class Definition

```python
class csc.tools.AnimationPointsTypes
```

Container for categorized animation points and per-frame collision information.

## Constructor

### `__init__(self, arg0, arg1, arg2, arg3) -> None`

Initializes the AnimationPointsTypes instance.

**Parameters:**
- `arg0` (unknown): Not documented
- `arg1` (unknown): Not documented
- `arg2` (unknown): Not documented
- `arg3` (unknown): Not documented

**Returns:**
- None

## Methods

### `get_collision_fixed_points(self) -> Dict[frame number, set of points]`

Returns collision points with fulcrum groups.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_collision_pin_points(self) -> Dict[frame number, set of points]`

Returns collision points with pin type.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_collision_surface_points(self) -> Dict[frame number, set of points]`

Returns collision points with normal type.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_fixed_floor_points(self) -> Dict[frame number, set of points]`

Returns points that collide only with the floor and fulcrum groups.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_fixed_points(self) -> Dict[frame number, set of points]`

Returns all points that need to be fixed with collision.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_frame_collision_info_points(self) -> Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]]`

Returns collision info about points.

**Parameters:**
- None

**Returns:**
- Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]]: Mapping of frame number to a mapping of object IDs to collision info.

### `get_fulcrum_floor_points(self) -> Dict[frame number, set of points]`

Returns points that collide only with the floor.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_fulcrum_points(self) -> Dict[frame number, set of points]`

Returns all fulcrum points with collision.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

### `get_local_fixed_points(self) -> Dict[frame number, set of points]`

Returns points that should keep local coordinates after apply.

**Parameters:**
- None

**Returns:**
- Dict[frame number, set of points]: Mapping of frame number to a set of points.

## Usage Example

```python
import csc.tools

# Instantiate with required parameters (placeholders shown)
apt = csc.tools.AnimationPointsTypes(arg0, arg1, arg2, arg3)

# Retrieve categorized points
fulcrum_points = apt.get_fulcrum_points()
fixed_points = apt.get_fixed_points()
collision_info = apt.get_frame_collision_info_points()
```

## Usage Notes

- All getters return per-frame mappings; handle frames explicitly when iterating or querying.
- The exact point type and collection types are not further specified; treat returned point sets as opaque collections unless documented elsewhere.
- Ensure consistency of frames across different getters if combining results.

## See Also

- Related collision and physics tools in the `csc.tools` module
- `csc.model.ObjectId`
- `CollisionInfoForPoint`