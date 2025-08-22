[CLEAN]

# csc.app.DataSourceManager

**Module:** `csc.app.DataSourceManager`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html)

## Overview

The `DataSourceManager` class manages scene data loading and saving operations in Cascadeur. It handles scene files and additional data such as selection groups, providing a centralized interface for scene data persistence.

## Class Definition

```python
class csc.app.DataSourceManager
```

This class serves as the primary interface for scene file operations and data source management within the Cascadeur application.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a DataSourceManager instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Methods

### `close_scene(self, scene) -> None`

Closes the specified scene.

**Parameters:**
- `scene`: The scene to close

**Returns:**
- None

### `load_scene(self, file_name: str) -> None`

Loads a scene and all additional data (selection groups, etc.) from the specified file.

**Parameters:**
- `file_name` (str): Path to the scene file to load

**Returns:**
- None

### `save_current_scene(*args, **kwargs) -> None`

Saves the current active scene. This method has multiple overloaded signatures:

**Overloaded signatures:**
1. `save_current_scene(self, handler: Callable[[bool], None]) -> None`
2. `save_current_scene(self) -> None`

**Parameters:**
- `handler` (Callable[[bool], None], optional): Callback function that receives success status

**Returns:**
- None

### `save_scene(*args, **kwargs) -> None`

Saves the specified scene. This method has multiple overloaded signatures:

**Overloaded signatures:**
1. `save_scene(self, scene_view: csc.view.Scene, handler: Callable[[bool], None]) -> None`
2. `save_scene(self, scene_view: csc.view.Scene) -> None`

**Parameters:**
- `scene_view` (csc.view.Scene): The scene view to save
- `handler` (Callable[[bool], None], optional): Callback function that receives success status

**Returns:**
- None

### `save_scene_as(self, scene_view: csc.view.Scene, full_file_name: str) -> None`

Saves the specified scene to a new file location.

**Parameters:**
- `scene_view` (csc.view.Scene): The scene view to save
- `full_file_name` (str): Full path for the new scene file

**Returns:**
- None

## Usage Example

```python
import csc.app

# Get the data source manager from the application
app = csc.app.get_application()
ds_manager = app.get_data_source_manager()

# Load a scene file
scene_file_path = "path/to/your/scene.cascadeur"
ds_manager.load_scene(scene_file_path)

# Save the current scene
ds_manager.save_current_scene()

# Save current scene with callback
def on_save_complete(success):
    if success:
        print("Scene saved successfully")
    else:
        print("Failed to save scene")

ds_manager.save_current_scene(on_save_complete)

# Save a specific scene view
scene_view = app.get_scene_manager().get_current_scene()
ds_manager.save_scene(scene_view)

# Save scene as new file
new_file_path = "path/to/new/scene.cascadeur"
ds_manager.save_scene_as(scene_view, new_file_path)

# Close a scene
ds_manager.close_scene(scene_view)
```

## Usage Notes

- The DataSourceManager handles both scene data and additional metadata (selection groups, etc.)
- Loading a scene includes all associated data, not just the basic scene geometry
- Save operations can be performed synchronously or with callback handlers
- Use `save_scene_as()` for "Save As" functionality with a new file name
- The manager is typically obtained through the main Application instance

## See Also

- `csc.app.Application` - Main application class for accessing managers
- `csc.view.Scene` - Scene view class used in save operations
- `csc.app.SceneManager` - Scene management functionality
- File I/O and scene persistence in Cascadeur