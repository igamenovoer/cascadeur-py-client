[CLEAN]

# csc.app.ToolsManager

**Module:** `csc.app.ToolsManager`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.ToolsManager.html)

## Overview

The `ToolsManager` class provides access to and management of tools within the Cascadeur application. It allows retrieval of specific tools by name and provides access to the complete list of available tools.

## Class Definition

```python
class csc.app.ToolsManager
```

The ToolsManager class serves as a registry and access point for all available tools in Cascadeur, enabling programmatic tool selection and usage.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new ToolsManager instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `get_tool(self, arg0: str) -> object`

Retrieves a specific tool by name.

**Parameters:**
- `arg0` (str): The name of the tool to retrieve

**Returns:**
- object: The tool object corresponding to the specified name, or None if not found

### `tools(self) -> list[object]`

Gets a list of all available tools.

**Returns:**
- list[object]: A list containing all available tool objects

## Usage Example

```python
import csc.app

# Get the tools manager from the application
app = csc.app.Application()
tools_manager = app.get_tools_manager()

# Get all available tools
all_tools = tools_manager.tools()
print(f"Available tools: {len(all_tools)}")

# Get a specific tool by name
physics_tool = tools_manager.get_tool("AutoPhysicTool")
if physics_tool:
    print("AutoPhysicTool found")
    # Use the tool for scene operations
    scene = app.current_scene()
    scene_tool = physics_tool.editor(scene)
else:
    print("AutoPhysicTool not found")

# List all tool names (assuming tools have a 'name' method)
for tool in all_tools:
    if hasattr(tool, 'name'):
        print(f"Tool: {tool.name()}")
```

## Usage Notes

- The ToolsManager provides access to all tools registered in Cascadeur
- Tools are retrieved as generic objects and may need to be cast to specific tool types
- Tool names are case-sensitive strings
- Each tool object can create scene-specific editors for actual operations
- The ToolsManager is accessed through the Application instance
- Tool availability may depend on the current Cascadeur configuration and loaded plugins

## See Also

- `csc.app.CascadeurTool` - Base class for Cascadeur tools
- `csc.app.SceneTool` - Scene-specific tool editor interface
- `csc.app.Application.get_tools_manager()` - Access to ToolsManager instance
- Individual tool classes in `csc.tools` module