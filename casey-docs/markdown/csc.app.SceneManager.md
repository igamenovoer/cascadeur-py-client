[CLEAN]

# csc.app.SceneManager

**Module:** `csc.app.SceneManager`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.SceneManager.html)

## Overview

The `SceneManager` class manages scenes within the Cascadeur application. It provides functionality for creating, accessing, and managing multiple scenes, including setting the current active scene and maintaining scene collections.

## Class Definition

```python
class csc.app.SceneManager
```

The SceneManager class serves as the central manager for scene operations and scene lifecycle management within the Cascadeur application.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a SceneManager instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Methods

### `create_application_scene(self) -> Scene`

Creates a new application scene.

**Returns:**
- Scene: The newly created scene object

### `current_scene(self) -> Scene`

Gets the currently active scene.

**Returns:**
- Scene: The current active scene object

### `remove_application_scene(self, scene) -> None`

Removes an application scene from the manager.

**Parameters:**
- `scene`: The scene object to remove

**Returns:**
- None

### `scenes(self) -> List[Scene]`

Gets a collection of all managed scenes.

**Returns:**
- List[Scene]: Collection of all scenes managed by this manager

### `set_current_scene(self, scene) -> None`

Sets the specified scene as the current active scene.

**Parameters:**
- `scene`: The scene object to set as current

**Returns:**
- None

## Usage Example

```python
import csc.app

# Get the application and scene manager
app = csc.app.get_application()
scene_manager = app.get_scene_manager()

# Get the current scene
current_scene = scene_manager.current_scene()
print(f"Current scene: {current_scene}")

# Create a new scene
new_scene = scene_manager.create_application_scene()

# Set the new scene as current
scene_manager.set_current_scene(new_scene)

# Get all scenes
all_scenes = scene_manager.scenes()
print(f"Total scenes: {len(all_scenes)}")

# Switch back to original scene
scene_manager.set_current_scene(current_scene)

# Remove a scene when no longer needed
scene_manager.remove_application_scene(new_scene)

# Working with scene operations
scene = scene_manager.current_scene()
if scene:
    # Access scene functionality
    data_viewer = scene.data_viewer()
    model_viewer = scene.model_viewer()
    assets_manager = scene.assets_manager()
    
    # Perform scene operations
    frame = scene.get_current_frame()
    scene.set_current_frame(30)
```

## Usage Notes

- The SceneManager maintains a collection of scenes and tracks the current active scene
- Use `current_scene()` to access the currently active scene for operations
- `create_application_scene()` creates new scenes that can be managed by the application
- Always set a scene as current before performing operations on it
- Remove scenes when they're no longer needed to free resources
- Scene switching affects which scene receives user interactions and operations
- The manager is typically accessed through the main Application instance

## See Also

- `csc.app.Application` - Main application class for accessing the scene manager
- `csc.domain.Scene` - Scene class with detailed scene operations
- `csc.app.DataSourceManager` - Scene loading and saving functionality
- `csc.view.Scene` - Scene view representation
- Scene lifecycle and management in Cascadeur