[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:43 | Original: ea2527ae -->

# csc.tools.AutoPosingTool

**Module:** `csc.tools.AutoPosingTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.AutoPosingTool.html)

## Overview

AutoPosingTool class.

## Class Definition

```python
class csc.tools.AutoPosingTool
```

Tool for auto posing operations.

## Constructor

### `__init__(*args, **kwargs) -> None`

Initialize an AutoPosingTool instance.

**Parameters:**
- `*args` (tuple): Positional arguments.
- `**kwargs` (dict): Keyword arguments.

**Returns:**
- None

## Methods

### `add(self, arg0: csc.domain.Session) -> None`

Add the tool to the specified session.

**Parameters:**
- `arg0` (csc.domain.Session): Session object.

**Returns:**
- None

### `update(self, arg0: csc.domain.Session) -> None`

Update the tool state for the specified session.

**Parameters:**
- `arg0` (csc.domain.Session): Session object.

**Returns:**
- None

## Usage Example

```python
from csc.tools import AutoPosingTool
from csc.domain import Session

tool = AutoPosingTool()
session = Session()
tool.add(session)
tool.update(session)
```

## Usage Notes

- Ensure a valid csc.domain.Session is provided to add and update methods.
- Constructor accepts generic arguments; no specific parameters are documented.

## See Also

- csc.domain.Session
- csc.tools.AutoPhysicTool
- csc.tools.MirrorTool