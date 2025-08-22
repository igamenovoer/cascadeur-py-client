[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:40 | Original: c7186319 -->

# csc.tools.attractor.Args

**Module:** `csc.tools.attractor.Args`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.Args.html)

## Overview

Arguments container for the Attractor tool operations. Holds scene context, physics parameters, general settings, and behavior flags that control how attraction is applied.

## Class Definition

```python
class csc.tools.attractor.Args
```

Represents a structured set of parameters for configuring attractor operations.

## Constructor

### `__init__(self: csc.tools.attractor.Args, scene: csc.domain.Scene, gravity: float, general_settings: csc.tools.attractor.AttractorGeneralSettings, only_key_frames: bool, mode: csc.tools.attractor.ArgsMode, for_interval: bool = False, hard: bool = False, frame_action_on_change: csc.domain.FrameActionOnChange = <FrameActionOnChange.DoNothing: 2>, interval_action_on_change: csc.domain.IntervalActionOnChange = <IntervalActionOnChange.Fixing: 0>) -> None`

Initialize attractor arguments.

**Parameters:**
- `scene` (csc.domain.Scene): Scene context.
- `gravity` (float): Gravity value used for attraction computations.
- `general_settings` (csc.tools.attractor.AttractorGeneralSettings): General attractor settings.
- `only_key_frames` (bool): Whether to apply only to key frames.
- `mode` (csc.tools.attractor.ArgsMode): Attractor argument mode.
- `for_interval` (bool, default: False): Whether the operation targets an interval.
- `hard` (bool, default: False): Hard mode flag.
- `frame_action_on_change` (csc.domain.FrameActionOnChange, default: <FrameActionOnChange.DoNothing: 2>): Action to perform when a frame changes.
- `interval_action_on_change` (csc.domain.IntervalActionOnChange, default: <IntervalActionOnChange.Fixing: 0>): Action to perform when an interval changes.

**Returns:**
- None

## Methods

No additional methods are documented.

## Attributes

- `__annotations__` (dict): {}
- `__module__` (str): 'csc.tools.attractor'
- `for_interval` (property): Interval targeting flag.
- `frame_action_on_change` (property): Action on frame change.
- `general_settings` (property): General attractor settings.
- `interval_action_on_change` (property): Action on interval change.
- `mode` (property): Attractor argument mode.
- `only_key_frames` (property): Apply only to key frames.

## Usage Example

```python
import csc.tools.attractor
import csc.domain

# Prepare required objects
scene = csc.domain.Scene()
general = csc.tools.attractor.AttractorGeneralSettings()
mode = csc.tools.attractor.ArgsMode

# Create Args instance
args = csc.tools.attractor.Args(
    scene=scene,
    gravity=9.81,
    general_settings=general,
    only_key_frames=True,
    mode=mode,
    for_interval=False,
    hard=False
)
```

## Usage Notes

- Ensure the `scene` refers to a valid csc.domain.Scene instance before constructing Args.
- Configure `general_settings` and `mode` according to the desired attractor behavior.
- Use `only_key_frames` to limit operations to key frames when needed.
- `frame_action_on_change` and `interval_action_on_change` control how changes are handled during processing.

## See Also

- csc.tools.attractor.AttractorGeneralSettings
- csc.tools.attractor.ArgsMode
- csc.domain.FrameActionOnChange
- csc.domain.IntervalActionOnChange
- csc.tools.attractor.attract