[CLEAN]

# csc.tools.RenderToFile

**Module:** `csc.tools.RenderToFile`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.RenderToFile.html)

## Overview

The `RenderToFile` class provides functionality for rendering animation sequences and individual frames to various file formats. It serves as a comprehensive rendering tool that supports both image sequence generation and video file output, enabling batch rendering operations for animation export and preview generation.

## Class Definition

```python
class csc.tools.RenderToFile
```

The RenderToFile class encapsulates rendering operations for exporting visual content from Cascadeur scenes to external file formats.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new RenderToFile instance with rendering capabilities.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `play_to_images_sequence(self, scene_view, ...) -> None`

Renders an animation sequence to a series of image files.

**Parameters:**
- `scene_view`: The scene view to render from
- `...`: Additional rendering parameters (format, resolution, frame range, output path, etc.)

**Returns:**
- None

### `play_to_video_file(self, scene_view, ...) -> None`

Renders an animation sequence to a single video file.

**Parameters:**
- `scene_view`: The scene view to render from
- `...`: Additional rendering parameters (video format, codec, resolution, frame range, output path, etc.)

**Returns:**
- None

### `take_image(self, scene_view, ...) -> None`

Captures a single frame image from the scene view.

**Parameters:**
- `scene_view`: The scene view to capture from
- `...`: Additional capture parameters (format, resolution, output path, etc.)

**Returns:**
- None

## Usage Example

```python
import csc.tools
import csc.view

# Create a render tool instance
render_tool = csc.tools.RenderToFile()

# Get the scene view for rendering
scene_view = csc.view.Scene()  # or appropriate scene view object

# Render single frame
render_tool.take_image(
    scene_view,
    output_path="frame_001.png",
    resolution=(1920, 1080),
    format="PNG"
)

# Render animation to image sequence
render_tool.play_to_images_sequence(
    scene_view,
    output_directory="./renders/",
    format="PNG",
    resolution=(1920, 1080),
    start_frame=1,
    end_frame=120,
    frame_step=1
)

# Render animation to video file
render_tool.play_to_video_file(
    scene_view,
    output_path="animation.mp4",
    format="MP4",
    codec="H.264",
    resolution=(1920, 1080),
    frame_rate=24,
    start_frame=1,
    end_frame=120
)

# Batch rendering workflow
def batch_render_animations(animations, output_dir):
    """Render multiple animations with consistent settings."""
    renderer = csc.tools.RenderToFile()
    
    for i, animation_view in enumerate(animations):
        # Render to image sequence
        renderer.play_to_images_sequence(
            animation_view,
            output_directory=f"{output_dir}/animation_{i:03d}/",
            format="PNG",
            resolution=(1920, 1080)
        )
        
        # Also render to video
        renderer.play_to_video_file(
            animation_view,
            output_path=f"{output_dir}/animation_{i:03d}.mp4",
            format="MP4",
            resolution=(1920, 1080),
            frame_rate=30
        )

# Preview generation
def generate_previews(scene_view, frames, output_dir):
    """Generate preview images at specific frames."""
    renderer = csc.tools.RenderToFile()
    
    for frame in frames:
        # Set scene to specific frame
        # (implementation depends on scene interface)
        
        renderer.take_image(
            scene_view,
            output_path=f"{output_dir}/preview_frame_{frame:04d}.jpg",
            format="JPEG",
            resolution=(800, 600)
        )
```

## Usage Notes

- The RenderToFile tool provides comprehensive rendering capabilities for various output formats
- Image sequence rendering is useful for compositing workflows and frame-by-frame analysis
- Video file rendering creates compressed output suitable for playback and distribution
- Single image capture enables keyframe previews and thumbnails
- Rendering parameters typically include resolution, format, frame range, and quality settings
- The scene view parameter determines the viewport and camera perspective for rendering
- Output paths should be properly configured to avoid file conflicts in batch operations
- Different formats may have specific parameter requirements (codec for video, compression for images)

## See Also

- `csc.tools.RenderParameters` - Rendering parameter configuration
- `csc.view.Scene` - Scene view for rendering
- `csc.view.Camera` - Camera control for render perspectives
- `csc.view.Viewport` - Viewport management for rendering
- Animation export and media generation workflows