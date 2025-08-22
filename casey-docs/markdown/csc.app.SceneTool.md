[CLEAN]

# csc.app.SceneTool

**Module:** `csc.app.SceneTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.SceneTool.html)

## Overview

The `SceneTool` class represents a scene-specific tool within the Cascadeur application. It provides the implementation for tools that operate on specific scenes, serving as the concrete implementation created by CascadeurTool's editor method.

## Class Definition

```python
class csc.app.SceneTool
```

The SceneTool class serves as a scene-specific tool implementation that can perform operations on a particular scene context.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a SceneTool instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Usage Example

```python
import csc.app

# Get the application and tools manager
app = csc.app.get_application()
tools_manager = app.get_tools_manager()

# Get a CascadeurTool instance (example workflow)
# cascadeur_tool = tools_manager.get_tool_by_name("SomeTool")

# Create a scene-specific tool editor
# scene = app.get_scene_manager().current_scene()
# scene_tool = cascadeur_tool.editor(scene)

# The scene_tool is now a SceneTool instance that can operate on the specific scene
# scene_tool.perform_operation()  # Example operation (method depends on tool type)

print("SceneTool instance created for scene-specific operations")
```

## Usage Notes

- SceneTool instances are typically created by calling the `editor()` method on a CascadeurTool
- Each SceneTool is bound to a specific scene context
- The exact methods and functionality available depend on the specific tool type
- SceneTool provides the concrete implementation for scene-specific operations
- Use SceneTool instances to perform tool operations on specific scenes
- Different tools will create different types of SceneTool instances with tool-specific methods

## See Also

- `csc.app.CascadeurTool` - Base tool class that creates SceneTool instances
- `csc.app.ToolsManager` - Manager for accessing and organizing tools
- `csc.app.SceneManager` - Scene management for providing scene context
- `csc.view.Scene` - Scene view class used with tools
- Tool system and scene operations in Cascadeur