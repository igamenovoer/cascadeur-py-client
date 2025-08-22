[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:37 | Original: 6cf6e980 -->

# csc.rig.AddElementData

**Module:** `csc.rig.AddElementData`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.rig.AddElementData.html)

## Overview

Represents data used when adding an element in the csc.rig module. Provides configuration flags and parameters controlling how the element is created and displayed.

## Class Definition

```python
class csc.rig.AddElementData
```

Container for parameters related to adding rig elements, including controller types, multiplicity, sizing, axes behavior, and point color.

## Constructor

### `__init__() -> None`

Default constructor.

**Parameters:**
- None

**Returns:**
- None

### `__init__(arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: float, arg8: numpy.ndarray[numpy.float32[3, 1]]) -> None`

Overloaded constructor accepting detailed configuration.

**Parameters:**
- `arg0` (bool): Unspecified boolean flag.
- `arg1` (bool): Unspecified boolean flag.
- `arg2` (int): Unspecified integer parameter.
- `arg3` (int): Unspecified integer parameter.
- `arg4` (bool): Unspecified boolean flag.
- `arg5` (bool): Unspecified boolean flag.
- `arg6` (int): Unspecified integer parameter.
- `arg7` (float): Unspecified floating-point parameter.
- `arg8` (numpy.ndarray[numpy.float32[3, 1]]): Unspecified 3D float32 vector/array parameter.

**Returns:**
- None

## Methods

- `__init__(*args, **kwargs) -> None`  
  Overloaded function. See Constructor for available signatures.

## Attributes

- `axis_point_controller`
- `box_multiplier`
- `is_multiple`
- `joint_size_without_child`
- `offset_point_controller`
- `only_box_controller`
- `orthogonal_with_parent`
- `point_color`
- `use_global_axis`

Note: The original documentation lists these attribute names without types or descriptions.

## Usage Example

```python
import csc.rig

# Create with default settings
data = csc.rig.AddElementData()

# Or using the detailed constructor (example placeholder values)
# Ensure arg8 is a numpy float32 3x1 array
import numpy as np
vec = np.array([[0.0], [1.0], [0.0]], dtype=np.float32)
data_detailed = csc.rig.AddElementData(
    True, False, 1, 2, True, False, 3, 1.0, vec
)
```

## Usage Notes

- This class provides multiple constructors; choose the default for basic usage or the detailed overload for explicit configuration.
- The attributes listed are part of the data structure; refer to the broader API or source for their specific semantics and types if needed.
- Ensure the numpy argument matches the required dtype and shape: numpy.float32[3, 1].

## See Also

- Other classes in the `csc.rig` module