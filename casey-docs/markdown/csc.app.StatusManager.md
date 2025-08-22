[CLEAN]

# csc.app.StatusManager

**Module:** `csc.app.StatusManager`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.StatusManager.html)

## Overview

The `StatusManager` class manages status informer instances within the Cascadeur application. It provides functionality for setting and removing status displays that communicate operation progress and status information to users.

## Class Definition

```python
class csc.app.StatusManager
```

The StatusManager class serves as a centralized controller for status informer objects, allowing applications to manage user feedback during operations.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new StatusManager instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `remove_status(self, arg0: cascadeur::StatusInformer) -> None`

Removes a status informer from the display.

**Parameters:**
- `arg0` (cascadeur::StatusInformer): The status informer instance to remove

**Returns:**
- None

### `set_status(self, arg0: cascadeur::StatusInformer) -> None`

Sets and displays a status informer.

**Parameters:**
- `arg0` (cascadeur::StatusInformer): The status informer instance to display

**Returns:**
- None

## Usage Example

```python
import csc.app

# Get the status manager from the application
app = csc.app.Application()
status_manager = app.get_status_manager()

# Create a status informer
status_informer = csc.app.SimpleStatusInformer("Loading scene...")

# Display the status
status_manager.set_status(status_informer)

# Perform some operation
# ... (operation code here)

# Remove the status when done
status_manager.remove_status(status_informer)
```

## Usage Notes

- The StatusManager works with status informer objects (like SimpleStatusInformer)
- Each status informer should be removed after use to prevent UI clutter
- Status informers provide feedback during long-running operations
- Multiple status informers can be managed, but typically only one is displayed at a time
- The StatusManager is accessed through the Application instance

## See Also

- `csc.app.SimpleStatusInformer` - Basic status informer implementation
- `csc.app.Application.get_status_manager()` - Access to StatusManager instance
- `cascadeur::StatusInformer` - Base status informer interface