[CLEAN]

# csc.Direction

**Module:** `csc.Direction`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.Direction.html)

## Overview

The `Direction` class represents a directional value within the Cascadeur animation system. This class implements direction functionality and provides methods for working with directional values.

## Class Definition

```python
class csc.Direction
```

The Direction class encapsulates directional information and provides utility methods for direction manipulation.

## Constructor

### `__init__(self, value: csc.DirectionValue = DirectionValue.Unknown) -> None`

Initializes a new Direction instance with the specified directional value.

**Parameters:**
- `value` (csc.DirectionValue, optional): The directional value. Defaults to DirectionValue.Unknown

**Returns:**
- None

## Methods

### `inverse(self) -> csc.DirectionValue`

Returns the inverse of the current direction.

**Returns:**
- csc.DirectionValue: The inverse directional value

### `to_string(self) -> str`

Converts the direction to its string representation.

**Returns:**
- str: String representation of the direction

### `value(self) -> csc.DirectionValue`

Gets the current directional value.

**Returns:**
- csc.DirectionValue: The current directional value

## Usage Example

```python
import csc

# Create a direction with default value
direction = csc.Direction()

# Create a direction with specific value
from csc import DirectionValue
direction = csc.Direction(DirectionValue.In)

# Get the current value
current_value = direction.value()

# Get inverse direction
inverse_value = direction.inverse()

# Convert to string
direction_str = direction.to_string()
```

## Usage Notes

- The Direction class works with DirectionValue enumeration values
- Default direction value is DirectionValue.Unknown if not specified
- The inverse() method returns the opposite directional value
- String representation provides human-readable direction information

## See Also

- `csc.DirectionValue` - Enumeration of direction values
- `csc.math` - Mathematical utilities for transformations