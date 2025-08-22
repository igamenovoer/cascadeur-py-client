[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:44 | Original: 3b70b25c -->

# csc.tools.CollisionInfoForPoint

**Module:** `csc.tools.CollisionInfoForPoint`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.CollisionInfoForPoint.html)

## Overview

Structure describing a collision between a point and another object. It is assumed that the normal vector points from the other object toward the point.

## Class Definition

```python
class csc.tools.CollisionInfoForPoint
```

Represents collision information for a specific point, including collision normal, the other object involved, penetration depth, and position.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a CollisionInfoForPoint instance.

**Parameters:**
- `*args` (tuple): Positional arguments (as provided by the API).
- `**kwargs` (dict): Keyword arguments (as provided by the API).

**Returns:**
- None

## Methods

### `__init__(*args, **kwargs) -> None`

Initializes a CollisionInfoForPoint instance.

**Parameters:**
- `*args` (tuple): Positional arguments.
- `**kwargs` (dict): Keyword arguments.

**Returns:**
- None

## Attributes

- `normal` (Vector3d): Collision normal pointing from the other object to the point.
- `other` (csc.model.ObjectId): Identifier of the other object involved in the collision.
- `penetration_depth` (double): Depth of penetration at the collision.
- `pos` (Vector3d): Position of the point involved in the collision.

## Usage Example

```python
import csc.tools

# Creating and using CollisionInfoForPoint (attributes availability depends on context)
info = csc.tools.CollisionInfoForPoint()
# Example attribute access (values typically provided by collision queries)
n = info.normal
other_id = info.other
depth = info.penetration_depth
position = info.pos
```

## Usage Notes

- The normal is defined to point from the other object toward the point.
- Instances are typically produced by collision detection routines; attribute values may be read-only and populated by the engine.
- Ensure types match the expected API types (Vector3d, csc.model.ObjectId, double).

## See Also

- csc.model.ObjectId
- Vector3d