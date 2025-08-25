[CLEAN]

# csc.view.DialogButton

## Overview

DialogButton represents a button widget used in Cascadeur dialog/view interfaces. It can be constructed using plain text or a csc.view.StandardButton value, with an optional callable handler. Optional flags allow forcing active focus and applying an accent style. Additional behavior is undocumented in the provided source.

## Class Definition

```python
class csc.view.DialogButton
```

## Constructor

### `__init__(self) -> None`
Undocumented constructor overload.

- Parameters: none
- Returns: None

### `__init__(self, arg0: str) -> None`
Undocumented constructor overload.

- Parameters:
  - arg0: str – undocumented
- Returns: None

### `__init__(self, text: str, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None`
Undocumented constructor overload.

- Parameters:
  - text: str – undocumented
  - handler: Callable – undocumented
  - force_active_focus: bool – optional, default False (undocumented)
  - accent: bool – optional, default False (undocumented)
- Returns: None

### `__init__(self, arg0: csc.view.StandardButton) -> None`
Undocumented constructor overload.

- Parameters:
  - arg0: csc.view.StandardButton – undocumented
- Returns: None

### `__init__(self, button: csc.view.StandardButton, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None`
Undocumented constructor overload.

- Parameters:
  - button: csc.view.StandardButton – undocumented
  - handler: Callable – undocumented
  - force_active_focus: bool – optional, default False (undocumented)
  - accent: bool – optional, default False (undocumented)
- Returns: None

## Methods

### `text(self) -> str`
Undocumented accessor.

- Parameters: none
- Returns: str — undocumented

### `force_active_focus(self)`
Undocumented accessor.

- Parameters: none
- Returns: undocumented

## Usage Notes

- Overloaded constructors allow creation with either a text label or a StandardButton value, optionally with a handler and flags; specific behaviors are undocumented here.

