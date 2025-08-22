[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:40 | Original: 13e90080 -->

# csc.tools.AnimationUnbakingTool

**Module:** `csc.tools.AnimationUnbakingTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.AnimationUnbakingTool.html)

## Overview

AnimationUnbakingTool class.

## Class Definition

```python
class csc.tools.AnimationUnbakingTool
```

Represents a tool related to animation unbaking operations.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a new instance of AnimationUnbakingTool.

**Parameters:**
- `*args` (tuple): Positional arguments (unspecified).
- `**kwargs` (dict): Keyword arguments (unspecified).

**Returns:**
- None

## Methods

### `get_interpolation_difference(self) -> float`

Returns the interpolation difference value.

**Parameters:**
- `self` (csc.tools.AnimationUnbakingTool): The instance of the tool.

**Returns:**
- float: Interpolation difference.

## Usage Example

```python
from csc.tools import AnimationUnbakingTool

# Practical usage example
tool = AnimationUnbakingTool()
diff = tool.get_interpolation_difference()
```

## Usage Notes

- The constructor accepts generic positional and keyword arguments; specific parameters are not detailed in the source documentation.
- Use get_interpolation_difference to obtain a numeric value representing interpolation differences in the context of animation unbaking.

## See Also

- csc.tools.AutoPosingTool
- csc.tools.MirrorTool
- csc.tools.AttractorTool