[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:44 | Original: 19287bbe -->

# csc.tools.mirror.Core

**Module:** `csc.tools.mirror.Core`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.mirror.Core.html)

## Overview

Mirror tool core class. Provides functionality to mirror objects across a defined plane for a single frame or an interval.

## Class Definition

```python
class csc.tools.mirror.Core
```

Core class for mirroring operations in Cascadeur.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a new Core instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

**Returns:**
- None

## Methods

### `mirror_frame(self, arg0: set[csc.model.ObjectId | csc.domain.Tool_object_id]) -> None`

Mirrors the specified objects on the current frame using the configured mirror plane.

**Parameters:**
- `arg0` (set[csc.model.ObjectId | csc.domain.Tool_object_id]): Set of object identifiers to mirror.

**Returns:**
- None: This method does not return a value.

### `mirror_interval(self, arg0: set[csc.model.ObjectId | csc.domain.Tool_object_id]) -> None`

Mirrors the specified objects over an interval using the configured mirror plane.

**Parameters:**
- `arg0` (set[csc.model.ObjectId | csc.domain.Tool_object_id]): Set of object identifiers to mirror across an interval.

**Returns:**
- None: This method does not return a value.

### `plane(self) -> csc.math.Plane`

Returns the current mirror plane.

**Parameters:**
- None

**Returns:**
- csc.math.Plane: The currently configured mirror plane.

### `set_plane(self, plane: csc.math.Plane) -> None`

Sets the mirror plane to use for mirroring operations.

**Parameters:**
- `plane` (csc.math.Plane): Plane to be used for mirroring.

**Returns:**
- None: This method does not return a value.

## Usage Example

```python
import csc.tools.mirror

# Create the core mirroring tool
core = csc.tools.mirror.Core()

# Get and (optionally) set the mirror plane
current_plane = core.plane()
# core.set_plane(current_plane)  # or set a different csc.math.Plane

# Prepare a set of object IDs (csc.model.ObjectId or csc.domain.Tool_object_id)
ids_to_mirror = set()  # populate with valid IDs from your scene

# Mirror on the current frame
core.mirror_frame(ids_to_mirror)

# Mirror across an interval
core.mirror_interval(ids_to_mirror)
```

## Usage Notes

- Ensure the mirror plane is correctly configured via set_plane before invoking mirroring operations.
- The arg0 parameter must be a set containing valid csc.model.ObjectId or csc.domain.Tool_object_id instances.
- Use plane to inspect the currently active mirror plane when debugging or configuring mirroring behavior.

## See Also

- csc.tools.MirrorTool
- csc.math.Plane
- csc.model.ObjectId
- csc.domain.Tool_object_id