[CLEAN]

# csc.domain.Scene

**Module:** `csc.domain.Scene`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Scene.html)

## Overview

The `Scene` class is the root class that represents a scene in Cascadeur and provides methods for modifying and observing it. It serves as the central interface for scene operations, providing access to various managers, viewers, and scene modification functionality.

## Class Definition

```python
class csc.domain.Scene
```

The Scene class acts as the primary interface for scene manipulation and observation within the Cascadeur animation system.

## Constructor

### `__init__(self) -> None`

Initializes a new Scene instance.

**Returns:**
- None

## Manager and Viewer Access Methods

### `assets_manager(self) -> AssetsManager`

Gets the assets manager for the scene.

**Returns:**
- AssetsManager: The scene's assets manager instance

### `behaviour_viewer(self) -> csc.model.BehaviourViewer`

Gets the behaviour viewer for observing scene behaviours.

**Returns:**
- csc.model.BehaviourViewer: The behaviour viewer instance

### `data_viewer(self) -> csc.model.DataViewer`

Gets the data viewer for observing scene data.

**Returns:**
- csc.model.DataViewer: The data viewer instance

### `layers_viewer(self) -> csc.layers.Viewer`

Gets the layers viewer for observing animation layers.

**Returns:**
- csc.layers.Viewer: The layers viewer instance

### `model_viewer(self) -> csc.model.ModelViewer`

Gets the model viewer for observing scene models.

**Returns:**
- csc.model.ModelViewer: The model viewer instance

### `selector(self) -> Selector`

Gets the scene selector for element selection operations.

**Returns:**
- Selector: The scene selector instance

### `get_layers_selector(self) -> csc.layers.Selector`

Gets the layers-specific selector.

**Returns:**
- csc.layers.Selector: The layers selector instance

## Frame Operations

### `get_current_frame(self, clamp_animation: bool = True) -> int`

Gets the current frame number in the scene.

**Parameters:**
- `clamp_animation` (bool, optional): Whether to clamp to animation bounds

**Returns:**
- int: The current frame number

### `set_current_frame(self, frame: int) -> None`

Sets the current frame in the scene.

**Parameters:**
- `frame` (int): The frame number to set as current

**Returns:**
- None

## Event and Logging Methods

### `error(self, message: str) -> None`

Logs an error message.

**Parameters:**
- `message` (str): The error message to log

**Returns:**
- None

### `info(self, message: str) -> None`

Logs an informational message.

**Parameters:**
- `message` (str): The info message to log

**Returns:**
- None

### `success(self, message: str) -> None`

Logs a success message.

**Parameters:**
- `message` (str): The success message to log

**Returns:**
- None

### `warning(self, message: str) -> None`

Logs a warning message.

**Parameters:**
- `message` (str): The warning message to log

**Returns:**
- None

### `get_event_log_or_null(self) -> Optional[EventLog]`

Gets the event log if available.

**Returns:**
- Optional[EventLog]: The event log instance or None

### `set_event_log(self, message_handler) -> None`

Sets the event log message handler.

**Parameters:**
- `message_handler`: The message handler for event logging

**Returns:**
- None

## Scene Modification Methods

### `modify(self, name: str, func) -> bool`

Modifies the scene using a modifier function.

**Parameters:**
- `name` (str): Name of the modifier
- `func`: Modify functor with signature void(modelEditor, updateEditor, scene)

**Returns:**
- bool: True if modification was successful

### `modify_update(self, name: str, func) -> bool`

Modifies the scene update system using a modifier function.

**Parameters:**
- `name` (str): Name of the modifier
- `func`: Modify functor with signature void(modelEditor, updateEditor, sceneUpdater)

**Returns:**
- bool: True if modification was successful

### `modify_with_session(self, name: str, func) -> bool`

Modifies the scene with session context.

**Parameters:**
- `name` (str): Name of the modifier
- `func`: Modify functor with session support

**Returns:**
- bool: True if modification was successful

### `modify_update_with_session(self, name: str, func) -> bool`

Modifies the scene update system with session context.

**Parameters:**
- `name` (str): Name of the modifier
- `func`: Modify functor with session support for update system

**Returns:**
- bool: True if modification was successful

## Usage Example

```python
import csc.domain

# Get or create a scene instance
scene = csc.domain.Scene()

# Access various managers and viewers
assets = scene.assets_manager()
data_viewer = scene.data_viewer()
model_viewer = scene.model_viewer()

# Frame operations
current_frame = scene.get_current_frame()
scene.set_current_frame(30)

# Logging
scene.info("Scene operation started")
scene.success("Operation completed successfully")

# Scene modification
def my_modifier(model_editor, update_editor, scene):
    # Perform scene modifications
    pass

success = scene.modify("MyModification", my_modifier)
```

## Usage Notes

- The Scene class is the central hub for all scene operations in Cascadeur
- Use the various viewer methods to access different aspects of the scene data
- Modification methods support custom functors for complex scene changes
- Frame operations allow for timeline navigation and control
- Event logging provides feedback and debugging capabilities
- Session-aware modification methods provide additional context and safety

## See Also

- `csc.model.ModelViewer` - Model viewing functionality
- `csc.layers.Viewer` - Animation layers management
- `csc.domain.Selector` - Element selection operations
- `csc.model.DataViewer` - Scene data observation