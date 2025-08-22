[CLEAN]

# csc.DirectionValue

**Module:** `csc.DirectionValue`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.DirectionValue.html)

## Overview

The `DirectionValue` enumeration represents directional values used throughout the Cascadeur animation system. It defines three possible direction states for various operations and calculations.

## Enumeration Definition

```python
class csc.DirectionValue(enum)
```

This enumeration provides standardized directional values for animation and transformation operations.

## Members

### `In`
Represents an inward direction.

### `Out`
Represents an outward direction.

### `Unknown`
Represents an unknown or undefined direction state.

## Constructor

### `__init__(self, value) -> None`

Creates a DirectionValue instance with the specified value.

**Parameters:**
- `value`: The directional value (In, Out, or Unknown)

**Returns:**
- None

## Attributes

### `name` (str)
The name of the enumeration member as a string.

### `value`
The value associated with the enumeration member.

## Usage Example

```python
import csc

# Access enumeration members
direction_in = csc.DirectionValue.In
direction_out = csc.DirectionValue.Out
direction_unknown = csc.DirectionValue.Unknown

# Create from value
direction = csc.DirectionValue(csc.DirectionValue.In)

# Get name and value
print(direction.name)   # "In"
print(direction.value)  # DirectionValue.In

# Compare values
if direction == csc.DirectionValue.In:
    print("Direction is inward")

# Use in conditional logic
def process_direction(direction_val):
    if direction_val == csc.DirectionValue.In:
        return "Processing inward direction"
    elif direction_val == csc.DirectionValue.Out:
        return "Processing outward direction"
    else:
        return "Direction is unknown"
```

## Usage Notes

- Used with `csc.Direction` class for directional operations
- Commonly used in animation and transformation calculations
- Provides standardized way to represent directional states
- Default value is typically `Unknown` when direction cannot be determined

## See Also

- `csc.Direction` - Direction class that uses these enumeration values
- Standard Python `enum` module documentation