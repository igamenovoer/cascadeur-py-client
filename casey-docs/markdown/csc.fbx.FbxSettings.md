[CLEAN]

# csc.fbx.FbxSettings

**Module:** `csc.fbx.FbxSettings`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.fbx.FbxSettings.html)

## Overview

The `FbxSettings` class provides configuration options for FBX file import and export operations within the Cascadeur system. It encapsulates various settings that control how FBX data is processed, including animation baking, coordinate system handling, and filtering options, enabling customized FBX workflows for different project requirements.

## Class Definition

```python
class csc.fbx.FbxSettings
```

The FbxSettings class serves as a configuration container for FBX import/export operations with adjustable parameters for animation and coordinate system handling.

## Constructor

### `__init__(self) -> None`

Initializes a new FbxSettings instance with default configuration values.

**Returns:**
- None

## Attributes

### `apply_euler_filter` (Property)

Controls whether Euler angle filtering is applied during FBX processing to reduce gimbal lock artifacts.

**Type:** bool  
**Access:** Read/Write

### `bake_animation` (Property)

Determines whether animation data should be baked into keyframes during FBX export.

**Type:** bool  
**Access:** Read/Write

### `mode` (Property)

Specifies the FBX processing mode, controlling the overall behavior of import/export operations.

**Type:** csc.fbx.FbxSettingsMode  
**Access:** Read/Write

### `up_axis` (Property)

Defines the up-axis convention for coordinate system conversion during FBX operations.

**Type:** csc.fbx.FbxSettingsAxis  
**Access:** Read/Write

## Usage Example

```python
import csc.fbx

# Create FBX settings with default values
fbx_settings = csc.fbx.FbxSettings()

# Configure animation baking
fbx_settings.bake_animation = True
print(f"Animation baking enabled: {fbx_settings.bake_animation}")

# Configure Euler filtering
fbx_settings.apply_euler_filter = True
print(f"Euler filtering enabled: {fbx_settings.apply_euler_filter}")

# Set coordinate system up-axis
fbx_settings.up_axis = csc.fbx.FbxSettingsAxis.Y_UP  # Assuming enum value
print(f"Up axis: {fbx_settings.up_axis}")

# Set processing mode
fbx_settings.mode = csc.fbx.FbxSettingsMode.IMPORT  # Assuming enum value
print(f"FBX mode: {fbx_settings.mode}")

# Use settings with FBX loader
fbx_loader = csc.fbx.FbxLoader()

# Apply settings for import operation
def import_fbx_with_settings(file_path, settings):
    """Import FBX file with specific settings."""
    try:
        # Configure loader with settings
        result = fbx_loader.load_with_settings(file_path, settings)
        print(f"FBX imported successfully: {file_path}")
        return result
    except Exception as e:
        print(f"FBX import failed: {e}")
        return None

# Animation-specific export settings
def create_animation_export_settings():
    """Create settings optimized for animation export."""
    settings = csc.fbx.FbxSettings()
    
    # Enable animation baking for compatibility
    settings.bake_animation = True
    
    # Apply Euler filtering to reduce rotation artifacts
    settings.apply_euler_filter = True
    
    # Set appropriate coordinate system
    settings.up_axis = csc.fbx.FbxSettingsAxis.Y_UP
    
    # Set export mode
    settings.mode = csc.fbx.FbxSettingsMode.EXPORT
    
    return settings

# Character rig export settings
def create_rig_export_settings():
    """Create settings optimized for character rig export."""
    settings = csc.fbx.FbxSettings()
    
    # Preserve original animation curves (don't bake)
    settings.bake_animation = False
    
    # Enable filtering for smooth rotations
    settings.apply_euler_filter = True
    
    # Configure coordinate system
    settings.up_axis = csc.fbx.FbxSettingsAxis.Z_UP
    
    # Set mode
    settings.mode = csc.fbx.FbxSettingsMode.EXPORT
    
    return settings

# Batch processing with different settings
def process_fbx_files(file_paths, settings_config):
    """Process multiple FBX files with specified settings."""
    settings = csc.fbx.FbxSettings()
    
    # Apply configuration
    for key, value in settings_config.items():
        setattr(settings, key, value)
    
    results = []
    for file_path in file_paths:
        result = import_fbx_with_settings(file_path, settings)
        results.append({
            'file': file_path,
            'success': result is not None,
            'data': result
        })
    
    return results

# Example batch processing
animation_files = ["walk.fbx", "run.fbx", "jump.fbx"]
animation_settings = {
    'bake_animation': True,
    'apply_euler_filter': True,
    'up_axis': 'Y_UP'  # String representation
}

batch_results = process_fbx_files(animation_files, animation_settings)
```

## Usage Notes

- FbxSettings provides fine-grained control over FBX import/export behavior
- Animation baking converts curves to keyframes, useful for compatibility but increases file size
- Euler filtering helps prevent rotation artifacts and gimbal lock issues
- Up-axis setting ensures proper coordinate system conversion between different 3D applications
- Mode setting determines whether the configuration applies to import or export operations
- Settings should be configured before passing to FBX loader/exporter operations
- Different settings profiles can be created for various workflow scenarios (animation vs. static meshes)
- Proper coordinate system handling is crucial when exchanging data with other 3D software

## See Also

- `csc.fbx.FbxLoader` - FBX file loading functionality that uses these settings
- `csc.fbx.FbxSceneLoader` - Scene-level FBX loading operations
- `csc.fbx.FbxSettingsMode` - Enumeration of FBX processing modes
- `csc.fbx.FbxSettingsAxis` - Coordinate system axis configuration options
- FBX import/export workflows and file format considerations