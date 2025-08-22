[CLEAN]

# csc.domain.LocalInterpolator

**Module:** `csc.domain.LocalInterpolator`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.LocalInterpolator.html)

## Overview

The `LocalInterpolator` class provides functionality for performing local interpolation operations within the Cascadeur animation system. It handles the calculation and application of interpolated values for animation data.

## Class Definition

```python
class csc.domain.LocalInterpolator
```

The LocalInterpolator class manages local interpolation calculations and updates for animation curves and data.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new LocalInterpolator instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `interpolate(self) -> None`

Performs the interpolation calculation on the associated data.

**Returns:**
- None

### `reload(self) -> None`

Reloads the interpolator configuration and data.

**Returns:**
- None

## Usage Example

```python
import csc.domain

# Create a local interpolator instance
interpolator = csc.domain.LocalInterpolator()

# Reload the interpolator data if needed
interpolator.reload()

# Perform interpolation
interpolator.interpolate()

# The interpolation results are applied to the associated animation data
```

## Usage Notes

- LocalInterpolator works with animation curve data to provide smooth transitions
- The `reload()` method is typically called when the underlying data has changed
- The `interpolate()` method performs the actual calculation and applies results
- Local interpolation is used for fine-grained control over animation curve behavior
- This class is part of the domain layer and integrates with the broader animation system
- Interpolation results affect the visual representation of animation curves

## See Also

- Animation curve classes that use local interpolation
- `csc.layers` module for animation layer management
- Other interpolation and animation calculation classes in the domain