[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:41 | Original: d5321813 -->

# csc.tools.attractor.AttractorGeneralSettings

**Module:** `csc.tools.attractor.AttractorGeneralSettings`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.AttractorGeneralSettings.html)

## Overview

AttractorGeneralSettings represents general configuration settings for the Attractor tool, exposing properties that control behavior such as factors, modes, pivot, axes, and physics type.

## Class Definition

```python
class csc.tools.attractor.AttractorGeneralSettings
```

A settings holder class with properties for attractor behavior.

## Constructor

### `__init__(self) -> None`

Initializes a new instance of AttractorGeneralSettings.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `__init__(self) -> None`

Initializes the settings object.

**Parameters:**
- None

**Returns:**
- None

## Attributes

- `__annotations__`: {}
- `__module__`: 'csc.tools.attractor'
- `factor` (property)
- `mode` (property)
- `mode_relative_to_pivot` (property)
- `physic_type` (property)
- `pivot` (property)
- `position_axis` (property)
- `rotation_axis` (property)
- `scale_axis` (property)

## Usage Example

```python
import csc.tools.attractor as attractor

# Practical usage example
settings = attractor.AttractorGeneralSettings()

# Access or modify properties (example; actual property types depend on API)
# settings.factor = 1.0
# settings.mode = attractor.SpaceMode.World
```

## Usage Notes

- This class exposes properties used to configure the Attractor tool; refer to related enums and types in the csc.tools.attractor module for valid values.
- Properties are documented as attributes; specific getter/setter behavior is defined by the API implementation.

## See Also

- csc.tools.attractor.SpaceMode
- csc.tools.attractor.ArgsMode
- csc.tools.attractor.GSRotationAxis
- csc.tools.attractor.GSAxisFlag
- csc.tools.attractor.GSAxisIndex
- csc.tools.attractor.GSPhysicsType
- csc.tools.attractor.Args
- csc.tools.attractor.attract
- csc.tools.AttractorTool