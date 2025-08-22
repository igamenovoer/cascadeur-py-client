[CLEAN]

# csc.app.Application

**Module:** `csc.app.Application`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.Application.html)

## Overview

The `Application` class serves as the main entry point for interacting with the Cascadeur application. It provides access to various managers and components that control different aspects of the application functionality.

## Class Definition

```python
class csc.app.Application
```

The Application class acts as a central hub for accessing Cascadeur's core systems and managers.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Application instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `current_scene(self) -> Scene`

Gets the currently active scene in the application.

**Returns:**
- Scene: The current scene object

### `get_action_manager(self) -> ActionManager`

Retrieves the action manager for executing application actions.

**Returns:**
- ActionManager: The application's action manager instance

### `get_data_source_manager(self) -> DataSourceManager`

Gets the data source manager for handling data sources.

**Returns:**
- DataSourceManager: The data source manager instance

### `get_file_dialog_manager(self) -> FileDialogManager`

Retrieves the file dialog manager for file operations.

**Returns:**
- FileDialogManager: The file dialog manager instance

### `get_scene_clipboard(self) -> SceneClipboard`

Gets the scene clipboard for copy/paste operations.

**Returns:**
- SceneClipboard: The scene clipboard instance

### `get_scene_manager(self) -> SceneManager`

Retrieves the scene manager for scene operations.

**Returns:**
- SceneManager: The scene manager instance

### `get_setting_manager(self) -> SettingsManager`

Gets the settings manager for application configuration.

**Returns:**
- SettingsManager: The settings manager instance

### `get_status_manager(self) -> StatusManager`

Retrieves the status manager for application status and notifications.

**Returns:**
- StatusManager: The status manager instance

### `get_tools_manager(self) -> ToolsManager`

Gets the tools manager for accessing application tools.

**Returns:**
- ToolsManager: The tools manager instance

## Usage Example

```python
import csc.app

# Create an application instance
app = csc.app.Application()

# Get the current scene
scene = app.current_scene()

# Access various managers
action_manager = app.get_action_manager()
scene_manager = app.get_scene_manager()
tools_manager = app.get_tools_manager()

# Use the managers to perform operations
action_manager.call_action("some_action")
```

## Usage Notes

- The Application class is the primary interface for accessing Cascadeur's functionality
- All manager methods return specific manager instances that provide specialized functionality
- This class follows a manager pattern where different aspects of the application are handled by dedicated manager classes
- The Application instance serves as a factory for accessing these managers