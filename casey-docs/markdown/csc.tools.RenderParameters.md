[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:34 | Original: c48b0336 -->

# csc.tools.RenderParameters

**Module:** `csc.tools.RenderParameters`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.RenderParameters.html)

## Overview

Parameters for rendering.

## Class Definition

```python
class csc.tools.RenderParameters
```

A container for render configuration such as image size and sampling.

## Constructor

### `__init__(self) -> None`

Initializes a new RenderParameters instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__init__(self) -> None`

Initializes a new RenderParameters instance.

**Parameters:**
- None

**Returns:**
- None

## Attributes

- `height` (property): Render output height.
- `samples` (property): Number of samples used for rendering.
- `width` (property): Render output width.

## Usage Example

```python
from csc.tools import RenderParameters

# Practical usage example
params = RenderParameters()
# Assuming properties are settable in actual usage:
# params.width = 1920
# params.height = 1080
# params.samples = 64
```

## Usage Notes

- Ensure width and height match your target output resolution.
- Samples affect render quality and performance.

## See Also

- csc.tools.RenderToFile