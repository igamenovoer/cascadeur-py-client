[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:43 | Original: 3a45e396 -->

# csc.tools.AttractorTool

**Module:** `csc.tools.AttractorTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.AttractorTool.html)

## Overview

Attractor tool class.

## Class Definition

```python
class csc.tools.AttractorTool
```

Represents the Attractor tool functionality.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes an instance of AttractorTool.

**Parameters:**
- `*args` (tuple): Positional arguments.
- `**kwargs` (dict): Keyword arguments.

**Returns:**
- None

## Methods

### `get_general_settings(self) -> csc.tools.attractor.AttractorGeneralSettings`

Returns general settings for the Attractor tool.

**Parameters:**
- None

**Returns:**
- csc.tools.attractor.AttractorGeneralSettings: General settings object.

### `is_only_key_frames(self) -> bool`

Checks if only key frames are used.

**Parameters:**
- None

**Returns:**
- bool: True if only key frames are used.

## Usage Example

```python
import csc.tools

tool = csc.tools.AttractorTool()
settings = tool.get_general_settings()
only_keys = tool.is_only_key_frames()
```

## Usage Notes

- Use get_general_settings to retrieve configurable options related to the Attractor tool.
- Use is_only_key_frames to determine whether operations are limited to key frames.

## See Also

- csc.tools.attractor.AttractorGeneralSettings
- csc.tools.attractor.attract
- csc.tools.MirrorTool
- csc.tools.AutoPhysicTool