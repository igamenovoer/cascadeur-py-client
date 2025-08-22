[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:37 | Original: cf02ddb3 -->

# csc.physics.inertia_tensor

**Module:** `csc.physics.inertia_tensor`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.physics.inertia_tensor.html)

## Overview

Function for computing the inertia tensor (as a 3x3 matrix) for a system of point masses relative to a specified center.

## Class Definition

```python
class csc.physics.inertia_tensor
```

This entry represents a module-level function; no class is defined.

## Constructor

### `__init__(params) -> None`

Not applicable for this module-level function.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `inertia_tensor(mass_and_poses: list[csc.physics.PosMass], center: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 3]]`

Computes the inertia tensor for the given list of point masses and positions relative to the specified center.

**Parameters:**
- `mass_and_poses` (list[csc.physics.PosMass]): List of point-mass entries with associated positions.
- `center` (numpy.ndarray[numpy.float32[3, 1]]): Center point relative to which the inertia tensor is calculated.

**Returns:**
- numpy.ndarray[numpy.float32[3, 3]]: Matrix3f inertia tensor.

## Usage Example

```python
import csc.physics
import numpy as np

# Prepare inputs
mass_points = [csc.physics.PosMass(...), csc.physics.PosMass(...)]
center = np.zeros((3, 1), dtype=np.float32)

# Compute inertia tensor
I = csc.physics.inertia_tensor(mass_points, center)
```

## Usage Notes

- Ensure each PosMass instance contains valid mass and position data.
- The center must be a 3x1 NumPy array of dtype float32.
- The returned tensor is a 3x3 NumPy array of dtype float32.

## See Also

- csc.physics.PosMass