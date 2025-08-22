[CLEAN]

# csc.app.ProjectLoader

**Module:** `csc.app.ProjectLoader`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html)

## Overview

The `ProjectLoader` class provides methods to load domain scenes with minimal loading capabilities. This is a lower-level loader that loads basic scene data without additional features like selection groups or control pickers.

## Class Definition

```python
class csc.app.ProjectLoader
```

Provides methods to load domain scene with minimal functionality. For full scene loading with all features, use the DataSourceManager's load_scene method instead.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a ProjectLoader instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Methods

### `load_from(file_path: str, scene) -> None` (static)

Performs a minimal load of a scene from the specified file.

**Parameters:**
- `file_path` (str): Path to the scene file to load
- `scene`: The scene object to load into

**Returns:**
- None

## Usage Example

```python
import csc.app

# Get application and scene
app = csc.app.get_application()
scene_manager = app.get_scene_manager()
scene = scene_manager.get_current_scene()

# Minimal scene loading (basic data only)
file_path = "path/to/your/scene.cascadeur"
csc.app.ProjectLoader.load_from(file_path, scene)

# For full scene loading with all features, use DataSourceManager instead:
# data_source_manager = app.get_data_source_manager()
# data_source_manager.load_scene(file_path)
```

## Usage Notes

- **Minimal Load**: This method doesn't load selection groups, control pickers, and other advanced features
- **Recommended Alternative**: For complete scene loading, use `DataSourceManager.load_scene()` method instead
- **Use Cases**: Suitable for basic scene loading when you only need core scene data
- **Performance**: Faster loading compared to full scene loading due to reduced feature set
- **Static Method**: `load_from()` is a static method and can be called directly on the class

## See Also

- `csc.app.DataSourceManager` - Full-featured scene loading with all data
- `csc.app.DataSourceManager.load_scene()` - Recommended method for complete scene loading
- `csc.app.SceneManager` - Scene management functionality
- Scene persistence and loading in Cascadeur