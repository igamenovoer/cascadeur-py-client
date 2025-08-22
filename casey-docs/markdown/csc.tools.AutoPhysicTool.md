[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:31 | Original: c533202d -->

# csc.tools.AutoPhysicTool

**Module:** `csc.tools.AutoPhysicTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.AutoPhysicTool.html)

## Overview

The `AutoPhysicTool` class is part of the Cascadeur toolset, designed to manage automatic physics-related functionalities within the application.

## Class Definition

```python
class csc.tools.AutoPhysicTool
```

This class provides methods to control physics settings, such as turning off specific physics features.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes an instance of the `AutoPhysicTool` class.

**Parameters:**
- `*args`: Variable length argument list.
- `**kwargs`: Arbitrary keyword arguments.

**Returns:**
- None

## Methods

### `turn_off(self) -> None`

Disables the auto physics feature.

**Parameters:**
- `self`: The instance of the `AutoPhysicTool`.

**Returns:**
- None

### `turn_off_all_fulcrum_points(self) -> None`

Disables all fulcrum points in the auto physics settings.

**Parameters:**
- `self`: The instance of the `AutoPhysicTool`.

**Returns:**
- None

## Usage Example

```python
import csc.tools

# Create an instance of AutoPhysicTool
auto_physic_tool = csc.tools.AutoPhysicTool()

# Turn off auto physics
auto_physic_tool.turn_off()

# Turn off all fulcrum points
auto_physic_tool.turn_off_all_fulcrum_points()
```

## Usage Notes

- The `AutoPhysicTool` is useful for managing physics settings in a streamlined manner.
- Ensure that the tool is properly initialized before invoking its methods.

## See Also

- Other related classes and modules within the `csc.tools` package.