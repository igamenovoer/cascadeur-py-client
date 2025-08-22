[CLEAN]

# csc.fbx.FbxLoader

**Module:** `csc.fbx.FbxLoader`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.fbx.FbxLoader.html)

## Overview

The `FbxLoader` class provides comprehensive functionality for importing and exporting FBX files in Cascadeur. It handles models, animations, joints, and complete scenes with various filtering and selection options.

## Class Definition

```python
class csc.fbx.FbxLoader
```

The FbxLoader class manages FBX file operations including import/export of models, animations, joints, and scenes with fine-grained control over what data is processed.

## Constructor

### `__init__(self, fps: float, handler, scene) -> None`

Initializes an FbxLoader instance with specified frame rate, handler, and scene context.

**Parameters:**
- `fps` (float): Frame rate for animation operations
- `handler`: Event handler for processing callbacks
- `scene`: The scene context for FBX operations

**Returns:**
- None

## Model Import/Export Methods

### `add_model(self, file_name: str) -> None`

Adds a model from an FBX file to the scene.

**Parameters:**
- `file_name` (str): Path to the FBX file containing the model

**Returns:**
- None

### `add_model_to_selected(self, file_name: str) -> None`

Adds a model from an FBX file to the currently selected objects.

**Parameters:**
- `file_name` (str): Path to the FBX file containing the model

**Returns:**
- None

### `import_model(self, file_name: str) -> None`

Imports a model from an FBX file.

**Parameters:**
- `file_name` (str): Path to the FBX file to import

**Returns:**
- None

### `export_model(self, file_name: str) -> None`

Exports the current model to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

## Animation Import/Export Methods

### `import_animation(self, file_name: str) -> None`

Imports animation data from an FBX file.

**Parameters:**
- `file_name` (str): Path to the FBX file containing animation data

**Returns:**
- None

### `import_animation_to_selected_frames(self, file_name: str, *args) -> None`

Imports animation data to selected frames from an FBX file.

**Parameters:**
- `file_name` (str): Path to the FBX file containing animation data
- `*args`: Additional arguments for frame selection

**Returns:**
- None

### `import_animation_to_selected_objects(self, file_name: str, *args) -> None`

Imports animation data to selected objects from an FBX file.

**Parameters:**
- `file_name` (str): Path to the FBX file containing animation data
- `*args`: Additional arguments for object selection

**Returns:**
- None

## Joints Export Methods

### `export_joints(self, file_name: str) -> None`

Exports joint data to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

### `export_joints_selected(self, file_name: str) -> None`

Exports selected joint data to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

### `export_joints_selected_frames(self, file_name: str) -> None`

Exports joint data from selected frames to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

### `export_joints_selected_objects(self, file_name: str) -> None`

Exports joint data from selected objects to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

## Scene Import/Export Methods

### `import_scene(self, file_name: str) -> None`

Imports a complete scene from an FBX file.

**Parameters:**
- `file_name` (str): Path to the FBX file to import

**Returns:**
- None

### `export_all_objects(self, file_name: str) -> None`

Exports all objects in the scene to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

### `export_scene_selected(self, file_name: str) -> None`

Exports selected scene elements to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

### `export_scene_selected_frames(self, file_name: str) -> None`

Exports scene data from selected frames to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

### `export_scene_selected_objects(self, file_name: str) -> None`

Exports selected objects from the scene to an FBX file.

**Parameters:**
- `file_name` (str): Path where the FBX file should be saved

**Returns:**
- None

## Configuration Methods

### `set_settings(self, settings: csc.fbx.FbxSettings) -> None`

Sets the FBX settings for import/export operations.

**Parameters:**
- `settings` (csc.fbx.FbxSettings): FBX settings configuration

**Returns:**
- None

## Usage Example

```python
import csc.fbx
import csc.app

# Get the application and scene
app = csc.app.get_application()
scene = app.get_scene_manager().current_scene()

# Create FBX loader with 30 FPS
fps = 30.0
handler = None  # Replace with actual handler if needed
fbx_loader = csc.fbx.FbxLoader(fps, handler, scene)

# Configure FBX settings
fbx_settings = csc.fbx.FbxSettings()
fbx_settings.mode = csc.fbx.FbxSettingsMode.Animation
fbx_settings.axis = csc.fbx.FbxSettingsAxis.YUp
fbx_loader.set_settings(fbx_settings)

# Import operations
fbx_loader.import_model("path/to/character.fbx")
fbx_loader.import_animation("path/to/animation.fbx")
fbx_loader.import_scene("path/to/complete_scene.fbx")

# Export operations
fbx_loader.export_model("path/to/exported_model.fbx")
fbx_loader.export_joints("path/to/joints.fbx")
fbx_loader.export_all_objects("path/to/full_scene.fbx")

# Selective export operations
fbx_loader.export_joints_selected("path/to/selected_joints.fbx")
fbx_loader.export_scene_selected_frames("path/to/frame_range.fbx")
fbx_loader.export_scene_selected_objects("path/to/selected_objects.fbx")

# Add models to existing scene
fbx_loader.add_model("path/to/additional_model.fbx")
fbx_loader.add_model_to_selected("path/to/model_for_selected.fbx")
```

## Usage Notes

- FbxLoader provides fine-grained control over FBX import/export operations
- Use appropriate FBX settings before performing operations for optimal results
- Frame rate affects animation import/export timing
- Selected frame/object operations allow for partial data transfer
- Joint export methods are useful for skeletal animation workflows
- Always configure settings before performing operations for consistent results
- The handler parameter can be used for progress callbacks and error handling

## See Also

- `csc.fbx.FbxSettings` - Configuration settings for FBX operations
- `csc.fbx.FbxSettingsMode` - Mode enumeration for FBX settings
- `csc.fbx.FbxSettingsAxis` - Axis system enumeration for FBX settings
- `csc.fbx.FbxSceneLoader` - Alternative scene loading functionality
- FBX file format and 3D model interchange standards