[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:48 | Original: 301fc8f0 -->

# csc.view.DialogButton

**Module:** `csc.view.DialogButton`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/csc.html)

## Overview

DialogButton class.

## Class Definition

```python
class csc.view.DialogButton
```

Represents a dialog button in the Cascadeur GUI module.

## Constructor

### `__init__(self: csc.view.DialogButton) -> None`

Default constructor.

**Parameters:**
- None

**Returns:**
- None

### `__init__(self: csc.view.DialogButton, arg0: str) -> None`

Creates a dialog button with the specified text.

**Parameters:**
- `arg0` (str): Button text.

**Returns:**
- None

### `__init__(self: csc.view.DialogButton, text: str, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None`

Creates a dialog button with text and a handler.

**Parameters:**
- `text` (str): Button text.
- `handler` (Callable): Callback to handle button action.
- `force_active_focus` (bool, optional): Defaults to False.
- `accent` (bool, optional): Defaults to False.

**Returns:**
- None

### `__init__(self: csc.view.DialogButton, arg0: csc.view.StandardButton) -> None`

Creates a dialog button from a standard button type.

**Parameters:**
- `arg0` (csc.view.StandardButton): Standard button enum value.

**Returns:**
- None

### `__init__(self: csc.view.DialogButton, button: csc.view.StandardButton, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None`

Creates a dialog button from a standard button type with a handler.

**Parameters:**
- `button` (csc.view.StandardButton): Standard button enum value.
- `handler` (Callable): Callback to handle button action.
- `force_active_focus` (bool, optional): Defaults to False.
- `accent` (bool, optional): Defaults to False.

**Returns:**
- None

## Methods

No public methods documented for this class in the provided source.

## Usage Example

```python
import csc

# Define a handler function
def on_click():
    print("Button clicked")

# Different ways to create dialog buttons
btn_default = csc.view.DialogButton()
btn_text = csc.view.DialogButton("Apply")
btn_text_with_handler = csc.view.DialogButton("Apply", on_click, force_active_focus=True, accent=True)
btn_standard = csc.view.DialogButton(csc.view.StandardButton.Ok)
btn_standard_with_handler = csc.view.DialogButton(csc.view.StandardButton.Cancel, on_click)
```

## Usage Notes

- Supports both text-based and StandardButton-based constructors.
- Optional flags force_active_focus and accent default to False.

## See Also

- csc.view.StandardButton
- csc.view.DialogManager