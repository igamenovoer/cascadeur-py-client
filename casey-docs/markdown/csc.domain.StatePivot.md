[CLEAN]

# csc.domain.StatePivot

**Module:** `csc.domain.StatePivot`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.StatePivot.html)

## Overview

The `StatePivot` enumeration defines the basic types of pivot states in Cascadeur animation system. It determines whether a pivot point remains stationary or moves during animation transformations, affecting how objects rotate and scale relative to their pivot point.

## Enumeration Definition

```python
class csc.domain.StatePivot(Enum)
```

The StatePivot enumeration provides two fundamental states for controlling pivot behavior during transformations.

## Constructor

### `__init__(self, value: int)`

Initializes a StatePivot with the specified value.

**Parameters:**
- `value` (int): The enumeration value for the pivot state

## Members

### `Fixed` = 0

Fixed pivot state where the pivot point remains stationary during transformations.

**Value:** `0`

**Behavior:**
- Pivot point does not move during object transformations
- Object rotates and scales around the fixed pivot location
- Provides stable transformation behavior for precise positioning

### `Moving` = 1

Moving pivot state where the pivot point can change position during transformations.

**Value:** `1`

**Behavior:**
- Pivot point can move along with object transformations
- Enables dynamic pivot positioning during animation
- Allows for more flexible transformation workflows

## Properties

### `name` (Property)

Gets the name of the enumeration member.

**Type:** `str`

### `value` (Property)

Gets the integer value of the enumeration member.

**Type:** `int`

## Usage Example

```python
import csc.domain

# Create pivot states
fixed_pivot = csc.domain.StatePivot.Fixed
moving_pivot = csc.domain.StatePivot.Moving

# Use with pivot operations
pivot = csc.domain.Pivot()

# Query pivot position with different states
frame_number = 30
position_fixed = pivot.position(frame_number, csc.domain.StatePivot.Fixed)
position_moving = pivot.position(frame_number, csc.domain.StatePivot.Moving)

# Query pivot rotation with different states
rotation_fixed = pivot.rotation(frame_number, csc.domain.StatePivot.Fixed)
rotation_moving = pivot.rotation(frame_number, csc.domain.StatePivot.Moving)

# Access pivot state properties
print(f"Fixed pivot value: {csc.domain.StatePivot.Fixed.value}")
print(f"Moving pivot name: {csc.domain.StatePivot.Moving.name}")

# Compare pivot states
current_state = csc.domain.StatePivot.Fixed
if current_state == csc.domain.StatePivot.Fixed:
    print("Pivot is in fixed state")
elif current_state == csc.domain.StatePivot.Moving:
    print("Pivot is in moving state")
```

## Usage Notes

- StatePivot determines the fundamental behavior of pivot points during transformations
- `Fixed` pivots provide stable, predictable transformation behavior
- `Moving` pivots enable dynamic transformation workflows with repositioning
- The choice between Fixed and Moving affects how objects behave during animation
- This enumeration integrates with the Pivot class to control transformation behavior
- Pivot state affects rotation, scaling, and positioning operations in the scene
- Understanding pivot states is crucial for precise animation control

## See Also

- `csc.domain.Pivot` - Pivot functionality that uses these states
- `csc.domain.Selector` - Selection system that works with pivots
- `csc.math.Quaternion` - Rotation representation used with pivots
- Animation transformation classes that depend on pivot behavior