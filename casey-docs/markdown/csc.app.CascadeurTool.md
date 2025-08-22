[CLEAN]

# csc.app.CascadeurTool

**Module:** `csc.app.CascadeurTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.CascadeurTool.html)

## Overview

The `CascadeurTool` class represents a tool within the Cascadeur application. It provides functionality for accessing tool information and creating scene-specific tool editors.

## Class Definition

```python
class csc.app.CascadeurTool
```

The CascadeurTool class serves as a base class for tools that can be used within the Cascadeur environment.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new CascadeurTool instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `name(self) -> str`

Gets the name of the tool.

**Returns:**
- str: The name of the tool

### `editor(self, scene: csc.view.Scene) -> csc.app.SceneTool`

Creates a scene-specific editor for this tool.

**Parameters:**
- `scene` (csc.view.Scene): The scene for which to create the tool editor

**Returns:**
- csc.app.SceneTool: A scene tool editor instance for this tool

## Usage Example

```python
import csc.app
import csc.view

# Assuming you have a CascadeurTool instance
tool = csc.app.CascadeurTool()

# Get the tool's name
tool_name = tool.name()
print(f"Tool name: {tool_name}")

# Create a scene editor for this tool (assuming you have a scene)
scene = csc.view.Scene()
scene_tool = tool.editor(scene)
```

## Usage Notes

- The CascadeurTool class represents the abstract concept of a tool in Cascadeur
- Use the `name()` method to identify the tool
- The `editor()` method creates a scene-specific instance that can actually perform operations on a scene
- Each tool can have different editors depending on the scene context