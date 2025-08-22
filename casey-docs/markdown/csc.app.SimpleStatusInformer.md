[CLEAN]

# csc.app.SimpleStatusInformer

**Module:** `csc.app.SimpleStatusInformer`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.app.SimpleStatusInformer.html)

## Overview

The `SimpleStatusInformer` class provides a simple interface for displaying status information and progress updates to the user within Cascadeur. It allows control over status text, blocking behavior, and cancellation state.

## Class Definition

```python
class csc.app.SimpleStatusInformer
```

The SimpleStatusInformer class handles user feedback during long-running operations by providing status updates and cancellation capabilities.

## Constructor

### `__init__(self, arg0: str) -> None`

Creates a new SimpleStatusInformer instance with the specified initial status text.

**Parameters:**
- `arg0` (str): The initial status message to display

**Returns:**
- None

## Methods

### `is_canceled(self) -> bool`

Checks if the user has requested cancellation of the operation.

**Returns:**
- bool: True if the operation has been canceled by the user, False otherwise

### `set_blocking(self, arg0: bool) -> None`

Sets whether the status display should block user interaction.

**Parameters:**
- `arg0` (bool): True to block user interaction, False to allow interaction

**Returns:**
- None

### `set_cancelable(self, arg0: bool) -> None`

Sets whether the user can cancel the operation.

**Parameters:**
- `arg0` (bool): True to allow user cancellation, False to disable cancellation

**Returns:**
- None

### `set_text(self, arg0: str) -> None`

Updates the status text displayed to the user.

**Parameters:**
- `arg0` (str): The new status message to display

**Returns:**
- None

## Usage Example

```python
import csc.app

# Create a status informer with initial message
status = csc.app.SimpleStatusInformer("Processing animation...")

# Make it blocking and cancelable
status.set_blocking(True)
status.set_cancelable(True)

# Simulate long-running operation
for i in range(100):
    # Check if user canceled
    if status.is_canceled():
        print("Operation canceled by user")
        break
    
    # Update progress
    status.set_text(f"Processing frame {i+1}/100")
    
    # Simulate work
    time.sleep(0.1)

# Complete the operation
status.set_text("Processing complete")
status.set_blocking(False)
```

## Usage Notes

- Status informers are typically used for long-running operations that need user feedback
- Blocking status prevents user interaction with the interface while operation is running
- Cancelable status allows users to abort operations gracefully
- Always check `is_canceled()` periodically in loops to respect user cancellation
- Status text should be descriptive and informative about the current operation state

## See Also

- `csc.app.StatusManager` - Manages status informer instances
- `csc.app.Application.get_status_manager()` - Access to status management