[CLEAN]

# csc.app.SettingsManager

**Module:** `csc.app.SettingsManager`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.SettingsManager.html)

## Overview

The `SettingsManager` class provides functionality for managing and retrieving application settings within Cascadeur. It allows access to configuration values of various types including boolean, float, and color values.

## Class Definition

```python
class csc.app.SettingsManager
```

The SettingsManager class is responsible for handling application settings and providing typed access to configuration parameters.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new SettingsManager instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `get_bool_value(self, arg0: str) -> bool`

Retrieves a boolean setting value by key.

**Parameters:**
- `arg0` (str): The setting key to retrieve

**Returns:**
- bool: The boolean value of the setting

### `get_color_value(self, arg0: str) -> numpy.ndarray[numpy.float32[3, 1]]`

Retrieves a color setting value as a numpy array.

**Parameters:**
- `arg0` (str): The setting key to retrieve

**Returns:**
- numpy.ndarray[numpy.float32[3, 1]]: A 3D numpy array containing RGB color values as 32-bit floats

### `get_float_value(self, arg0: str) -> float`

Retrieves a float setting value by key.

**Parameters:**
- `arg0` (str): The setting key to retrieve

**Returns:**
- float: The float value of the setting

## Usage Example

```python
import csc.app

# Create a settings manager instance
settings = csc.app.SettingsManager()

# Get boolean setting
show_grid = settings.get_bool_value("ui.show_grid")

# Get float setting
animation_speed = settings.get_float_value("animation.playback_speed")

# Get color setting
background_color = settings.get_color_value("viewport.background_color")
print(f"Background RGB: {background_color}")
```

## Usage Notes

- All getter methods require a string key to identify the specific setting
- Boolean settings return standard Python bool values
- Float settings return Python float values
- Color settings return numpy arrays with RGB values as 32-bit floats
- Setting keys follow dot notation convention (e.g., "category.setting_name")
- Invalid keys may raise exceptions or return default values depending on implementation

## See Also

- `csc.app.Application` - Main application interface that provides access to SettingsManager
- `numpy` - Required for color value array handling