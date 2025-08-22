[CLEAN]

# csc.domain.Pivot

**Module:** `csc.domain.Pivot`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Pivot.html)

## Overview

The `Pivot` class represents basic pivot functionality in Cascadeur, providing methods to access position and rotation data for animation objects. It supports frame-based queries and different pivot state configurations.

## Class Definition

```python
class csc.domain.Pivot
```

The Pivot class encapsulates basic pivot methods for accessing spatial transformation data in animation contexts.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Pivot instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `center_of_top_objects(self, arg0) -> numpy.ndarray`

Gets the center position of top-level objects.

**Parameters:**
- `arg0`: Object or frame identifier

**Returns:**
- numpy.ndarray: The center position as a numpy array

### `position(*args, **kwargs)` (Overloaded)

Gets the position of the pivot. This method is overloaded with multiple signatures.

#### Overload 1: `position(self) -> numpy.ndarray[numpy.float32[3, 1]]`

Gets the current position of the pivot.

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]]: 3D position vector as 32-bit floats

#### Overload 2: `position(self, frame: int) -> numpy.ndarray[numpy.float32[3, 1]]`

Gets the position of the pivot at a specific frame.

**Parameters:**
- `frame` (int): The frame number to query

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]]: 3D position vector at the specified frame

#### Overload 3: `position(self, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]]`

Gets the position of the pivot at a specific frame with a specific pivot state.

**Parameters:**
- `frame` (int): The frame number to query
- `pivot` (csc.domain.StatePivot): The pivot state to use

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]]: 3D position vector for the specified frame and pivot state

### `rotation(*args, **kwargs)` (Overloaded)

Gets the rotation of the pivot. This method is overloaded with multiple signatures.

#### Overload 1: `rotation(self) -> csc.math.Quaternion`

Gets the current rotation of the pivot.

**Returns:**
- csc.math.Quaternion: Current rotation as a quaternion

#### Overload 2: `rotation(self, frame: int) -> csc.math.Quaternion`

Gets the rotation of the pivot at a specific frame.

**Parameters:**
- `frame` (int): The frame number to query

**Returns:**
- csc.math.Quaternion: Rotation quaternion at the specified frame

#### Overload 3: `rotation(self, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion`

Gets the rotation of the pivot at a specific frame with a specific pivot state.

**Parameters:**
- `frame` (int): The frame number to query
- `pivot` (csc.domain.StatePivot): The pivot state to use

**Returns:**
- csc.math.Quaternion: Rotation quaternion for the specified frame and pivot state

### `select(self, entity_id)` (Overloaded)

Selects an entity by ID. This method has multiple overloads for different entity types.

**Parameters:**
- `entity_id`: The identifier of the entity to select

## Usage Example

```python
import csc.domain
import csc.math

# Create a pivot instance
pivot = csc.domain.Pivot()

# Get current position and rotation
current_pos = pivot.position()
current_rot = pivot.rotation()

print(f"Current position: {current_pos}")
print(f"Current rotation: {current_rot}")

# Get position and rotation at a specific frame
frame_10_pos = pivot.position(10)
frame_10_rot = pivot.rotation(10)

print(f"Frame 10 position: {frame_10_pos}")
print(f"Frame 10 rotation: {frame_10_rot}")

# Get center of top objects
center = pivot.center_of_top_objects(some_identifier)
print(f"Center of top objects: {center}")
```

## Usage Notes

- The Pivot class provides overloaded methods for flexible position and rotation queries
- Position data is returned as numpy arrays with 32-bit float precision
- Rotation data is returned as Quaternion objects for precise orientation representation
- Frame-based queries allow access to animation data at specific time points
- StatePivot parameter provides additional control over pivot state when querying data
- The class supports both current state queries and historical frame data access

## See Also

- `csc.domain.StatePivot` - Pivot state configuration class
- `csc.math.Quaternion` - Quaternion rotation representation
- Animation and transformation classes that work with pivot data