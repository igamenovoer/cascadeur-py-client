[CLEAN]

# csc.app.Analytics

**Module:** `csc.app.Analytics`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.Analytics.html)

## Overview

The `Analytics` class provides functionality for sending analytics events from within the Cascadeur application. This class is used to track user actions and behavior for analytics purposes.

## Class Definition

```python
class csc.app.Analytics
```

## Methods

### `send_action(type: str, key: str = '', label: str = '') -> None` (static)

Sends an analytics action event.

**Parameters:**
- `type` (str): The type of action being tracked
- `key` (str, optional): Optional key parameter for additional context. Defaults to empty string
- `label` (str, optional): Optional label for the action. Defaults to empty string

**Returns:**
- None

**Example:**
```python
import csc.app

# Send a basic analytics event
csc.app.Analytics.send_action("user_action")

# Send an analytics event with additional context
csc.app.Analytics.send_action(
    type="tool_usage", 
    key="animation_tool", 
    label="physics_simulation"
)
```

## Usage Notes

- This is a static method, so you don't need to instantiate the Analytics class
- Analytics events are used internally by Cascadeur to understand user behavior
- The `type` parameter is required, while `key` and `label` are optional
- All parameters should be strings