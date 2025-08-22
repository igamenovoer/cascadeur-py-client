[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:37 | Original: 6b395207 -->

# csc.parts.SceneClipboard

**Module:** `csc.parts.SceneClipboard`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.parts.SceneClipboard.html)

## Overview

SceneClipboard provides methods to operate on parts of the scene, including copying and pasting scene elements and copying images to the system clipboard.

## Class Definition

```python
class csc.parts.SceneClipboard
```

Provides clipboard operations for scene parts.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initializes a SceneClipboard instance.

**Parameters:**
- `*args` (tuple): Positional arguments (unspecified).
- `**kwargs` (dict): Keyword arguments (unspecified).

**Returns:**
- None

## Methods

### `copy(arg0) -> None`

Copies specified scene parts to the clipboard.

**Parameters:**
- `arg0` (unspecified): Target representing the scene parts to copy.

**Returns:**
- None

### `copy_image_to_clipboard(arg0) -> None`

Copies an image to the system clipboard.

**Parameters:**
- `arg0` (unspecified): Image or image source to copy.

**Returns:**
- None

### `paste(arg0) -> None`

Pastes scene parts from the clipboard into the specified target or context.

**Parameters:**
- `arg0` (unspecified): Target or context for the paste operation.

**Returns:**
- None

### `paste_with_session(arg0, arg1) -> None`

Pastes scene parts from the clipboard using a provided session.

**Parameters:**
- `arg0` (unspecified): Target or context for the paste operation.
- `arg1` (unspecified): Session object or session context.

**Returns:**
- None

## Usage Example

```python
import csc.parts

# Create a SceneClipboard instance
clipboard = csc.parts.SceneClipboard()

# Copy selected scene parts
clipboard.copy(selected_parts)

# Paste into a target context
clipboard.paste(target_context)

# Paste using an explicit session
clipboard.paste_with_session(target_context, session)

# Copy an image to the system clipboard
clipboard.copy_image_to_clipboard(image_data)
```

## Usage Notes

- Ensure the provided arguments match Cascadeur's expected scene or image objects.
- Pasting with a session can help maintain transactional integrity or undo/redo consistency.
- Operations may be context-dependent; verify target compatibility before pasting.

## See Also

- Other clipboard and scene manipulation utilities within `csc.parts`