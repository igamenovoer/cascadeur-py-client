[CLEAN]

# csc.domain.SceneUpdater

**Module:** `csc.domain.SceneUpdater`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.SceneUpdater.html)

## Overview

The `SceneUpdater` class serves to control scene modifications in Cascadeur. It handles scene update generation, manages interpolators, and provides methods to run updates with specific data configurations. When the update system is modified, it should be regenerated through this class.

## Class Definition

```python
class csc.domain.SceneUpdater
```

The SceneUpdater class manages the scene modification process, including update generation and execution.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new SceneUpdater instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `generate_update(self)`

Generates the scene update. This should be called when the update system has been modified.

**Returns:**
- None (return type not specified in documentation)

### `get_interpolator(self)`

Gets the interpolator associated with this scene updater.

**Returns:**
- Interpolator instance (specific type not specified in documentation)

### `run_update(*args, **kwargs)` (Overloaded)

Runs the update with specific data configurations. This method is overloaded with multiple signatures.

#### Overload 1: `run_update(self, local_ids: set[csc.model.DataId], frame: int) -> None`

Runs the update for specified local IDs at a specific frame.

**Parameters:**
- `local_ids` (set[csc.model.DataId]): Set of local data IDs to update
- `frame` (int): The frame number at which to run the update

**Returns:**
- None

#### Overload 2: `run_update(self, local_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None`

Runs the update for specified local IDs across multiple frames.

**Parameters:**
- `local_ids` (set[csc.model.DataId]): Set of local data IDs to update  
- `frames` (csc.layers.index.FramesIndices): Frame indices specifying which frames to update

**Returns:**
- None

### `scene(self)` (Overloaded)

Gets the scene associated with this updater. This method has multiple overloads.

**Returns:**
- Scene instance (specific return type and overloads not fully specified in documentation)

## Usage Example

```python
import csc.domain
import csc.model
import csc.layers.index

# Create a scene updater instance
updater = csc.domain.SceneUpdater()

# Generate the update (call this after modifications)
updater.generate_update()

# Get the interpolator
interpolator = updater.get_interpolator()

# Prepare data for update
local_ids = {csc.model.DataId()}  # Set of data IDs
frame_number = 30

# Run update at specific frame
updater.run_update(local_ids, frame_number)

# Or run update across multiple frames
frames_indices = csc.layers.index.FramesIndices()
updater.run_update(local_ids, frames_indices)

# Access the associated scene
scene = updater.scene()
```

## Usage Notes

- SceneUpdater is responsible for managing scene modification workflows
- Always call `generate_update()` after making changes to the update system
- The `run_update()` method can operate on single frames or frame ranges
- Use appropriate data ID sets to specify which elements should be updated
- The interpolator provides additional control over update calculations
- This class integrates with the broader Cascadeur animation and scene management system

## See Also

- `csc.model.DataId` - Data identification for updates
- `csc.layers.index.FramesIndices` - Frame index management
- `csc.domain.Scene` - Scene representation and management
- `csc.domain.LocalInterpolator` - Interpolation functionality