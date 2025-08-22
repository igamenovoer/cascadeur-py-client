[CLEAN]

# csc.domain.Session

**Module:** `csc.domain.Session`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Session.html)

## Overview

The `Session` class represents a session context within the Cascadeur animation system. It provides session-level access to scene operations, selectors, and frame management, serving as a context manager for coordinated scene modifications and interactions.

## Class Definition

```python
class csc.domain.Session
```

The Session class encapsulates session-specific functionality and provides access to scene manipulation tools within a controlled context.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Session instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `set_current_frame(self, frame: int) -> None`

Sets the current frame position within the session context.

**Parameters:**
- `frame` (int): The frame number to set as current

**Returns:**
- None

### `take_layers_selector(self) -> object`

Retrieves the layers selector for the session.

**Returns:**
- object: The layers selector instance for layer-specific operations

### `take_selector(self) -> object`

Retrieves the main scene selector for the session.

**Returns:**
- object: The scene selector instance for scene object operations

## Usage Example

```python
import csc.domain

# Create a session instance
session = csc.domain.Session()

# Set the current frame within the session
session.set_current_frame(30)

# Get the main scene selector
selector = session.take_selector()

# Get the layers selector
layers_selector = session.take_layers_selector()

# Use selectors for operations within the session context
# Example: select objects using the session's selector
if hasattr(selector, 'select'):
    object_ids = {csc.model.ObjectId()}
    selector.select(
        ids=object_ids,
        mode=csc.domain.SelectorMode.NewSelection
    )

# Work with layers using the layers selector
if hasattr(layers_selector, 'select_layer'):
    # Layer-specific operations would go here
    pass
```

## Usage Notes

- The Session class provides session-level context for scene operations
- Frame setting through `set_current_frame()` affects the session's temporal context
- The session maintains its own selectors for both scene objects and layers
- Sessions are useful for grouping related operations and maintaining consistent state
- Both `take_selector()` and `take_layers_selector()` return objects that provide selection functionality
- Session context helps ensure operations are performed in a coordinated manner
- This class integrates with the broader scene modification and session management system

## See Also

- `csc.domain.Selector` - Main scene selector functionality
- `csc.layers.Selector` - Layer-specific selector operations
- `csc.domain.Scene` - Scene management and modification
- Session management classes that work with scene contexts