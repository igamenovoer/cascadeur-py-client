[CLEAN]

# csc.view.Scene

**Module:** `csc.view.Scene`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.view.Scene.html)

## Overview

The `Scene` class (SceneView) provides a comprehensive interface for managing the visual representation and interaction layer of Cascadeur scenes. It serves as the primary bridge between the domain scene data and the viewport system, offering viewport management, animation boundaries, scene persistence, and view-specific settings control.

## Class Definition

```python
class csc.view.Scene
```

The Scene class encapsulates view-layer functionality for scene management, viewport control, and visual representation operations.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Scene view instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `active_viewport(self) -> csc.view.Viewport`

Returns the currently active viewport for the scene.

**Returns:**
- csc.view.Viewport: The active viewport instance

### `animation_boundary(self) -> csc.view.AnimationBoundary`

Gets the animation boundary settings for the scene view.

**Returns:**
- csc.view.AnimationBoundary: Animation boundary configuration object

### `domain_scene(self) -> csc.domain.Scene`

Returns the underlying domain scene object that this view represents.

**Returns:**
- csc.domain.Scene: The domain scene instance

### `get_setting_handler(self) -> object`

Retrieves the settings handler for scene-specific configuration.

**Returns:**
- object: Settings handler for scene configuration

### `gravity_per_frame(self) -> float`

Gets the gravity value per frame for physics calculations.

**Returns:**
- float: Gravity acceleration value per frame

### `name(self) -> str`

Returns the name identifier of the scene.

**Returns:**
- str: Scene name

### `save(self, path_name: str) -> None`

Saves the scene to the specified file path.

**Parameters:**
- `path_name` (str): File path where the scene should be saved

**Returns:**
- None

### `viewports(self) -> List[csc.view.Viewport]`

Provides access to all viewport objects associated with the scene.

**Returns:**
- List[csc.view.Viewport]: Collection of all viewport instances

## Usage Example

```python
import csc.view
import csc.domain

# Access scene view functionality
scene_view = csc.view.Scene()

# Get scene information
scene_name = scene_view.name()
print(f"Current scene: {scene_name}")

# Access the underlying domain scene
domain_scene = scene_view.domain_scene()
print(f"Domain scene: {domain_scene}")

# Work with viewports
active_viewport = scene_view.active_viewport()
all_viewports = scene_view.viewports()

print(f"Active viewport: {active_viewport}")
print(f"Total viewports: {len(all_viewports)}")

# Animation settings
animation_boundary = scene_view.animation_boundary()
print(f"Animation boundary: {animation_boundary}")

# Physics settings
gravity = scene_view.gravity_per_frame()
print(f"Gravity per frame: {gravity}")

# Scene persistence
def save_scene_with_timestamp(scene_view, base_path):
    """Save scene with timestamp."""
    import datetime
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    scene_name = scene_view.name()
    save_path = f"{base_path}/{scene_name}_{timestamp}.csc"
    
    scene_view.save(save_path)
    print(f"Scene saved to: {save_path}")
    
    return save_path

# Multi-viewport management
def setup_viewport_layout(scene_view):
    """Configure multiple viewport layout."""
    viewports = scene_view.viewports()
    
    for i, viewport in enumerate(viewports):
        print(f"Viewport {i}: {viewport}")
        
        # Access viewport-specific functionality
        if hasattr(viewport, 'domain_viewport'):
            domain_vp = viewport.domain_viewport()
            # Configure viewport settings
    
    # Set active viewport
    if viewports:
        active = scene_view.active_viewport()
        print(f"Active viewport: {active}")

# Settings management
def configure_scene_settings(scene_view):
    """Configure scene-specific settings."""
    settings_handler = scene_view.get_setting_handler()
    
    if settings_handler:
        # Configure scene settings through handler
        print("Settings handler available for configuration")
    
    return settings_handler

# Integration with domain operations
def sync_view_with_domain(scene_view):
    """Synchronize view layer with domain changes."""
    domain_scene = scene_view.domain_scene()
    
    # Perform domain operations
    # The view will reflect these changes automatically
    
    return {
        'view_scene': scene_view,
        'domain_scene': domain_scene,
        'viewports': scene_view.viewports(),
        'animation_boundary': scene_view.animation_boundary()
    }
```

## Usage Notes

- The Scene class provides the view layer interface to Cascadeur scenes
- `domain_scene()` gives access to the underlying data model and operations
- Viewport management allows for multiple view perspectives of the same scene
- Animation boundaries control temporal aspects of scene visualization
- Scene saving supports project persistence and backup workflows
- Settings handler enables scene-specific configuration management
- Gravity settings affect physics simulation visualization
- The active viewport determines the primary interaction context

## See Also

- `csc.domain.Scene` - Underlying scene data and operations
- `csc.view.Viewport` - Individual viewport management
- `csc.view.Camera` - Camera control within viewports
- `csc.view.AnimationBoundary` - Animation range and boundary settings
- `csc.app.SceneManager` - Application-level scene management