[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:41 | Original: e8c8f13e -->

# csc.math.transforms_difference

**Module:** `csc.math.transforms_difference`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.math.transforms_difference.html)

## Overview

Computes the difference between two orthogonal transforms and returns the resulting orthogonal transform.

## Class Definition

```python
def csc.math.transforms_difference(first, second) -> csc.math.OrthogonalTransform
```

This is a module-level function in the csc.math namespace.

## Constructor

Not applicable (module-level function).

## Methods

### `transforms_difference(first, second) -> csc.math.OrthogonalTransform`

Computes the difference between two orthogonal transforms.

**Parameters:**
- `first` (csc.math.OrthogonalTransform): First orthogonal transform.
- `second` (csc.math.OrthogonalTransform): Second orthogonal transform.

**Returns:**
- csc.math.OrthogonalTransform: The resulting orthogonal transform.

## Usage Example

```python
import csc.math

# Suppose t1 and t2 are instances of csc.math.OrthogonalTransform
result = csc.math.transforms_difference(t1, t2)
```

## Usage Notes

- Inputs must be orthogonal transforms (rotation/translation without scaling or shearing).
- Ensure both inputs are valid csc.math.OrthogonalTransform instances.

## See Also

- csc.math.OrthogonalTransform
- csc.math.transform_point
- csc.math.inverse_transform_point