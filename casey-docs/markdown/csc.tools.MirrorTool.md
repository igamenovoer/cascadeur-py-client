[CLEAN]

# csc.tools.MirrorTool

**Module:** `csc.tools.MirrorTool`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.MirrorTool.html)

## Overview

The `MirrorTool` class provides functionality for mirroring animation data and poses in Cascadeur. It enables symmetric animation workflows by allowing users to mirror selected objects and their animations across various axes, streamlining the creation of symmetric character movements and poses.

## Class Definition

```python
class csc.tools.MirrorTool
```

The MirrorTool class encapsulates mirroring operations for animation objects, providing access to core mirroring functionality through its core component.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new MirrorTool instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `core(self) -> object`

Retrieves the core mirror functionality object that handles the actual mirroring operations.

**Returns:**
- object: The core mirror implementation providing mirroring algorithms and operations

## Usage Example

```python
import csc.tools

# Create a mirror tool instance
mirror_tool = csc.tools.MirrorTool()

# Get the core mirror functionality
mirror_core = mirror_tool.core()

# Use core mirror functionality for mirroring operations
if mirror_core:
    # The core provides the actual mirroring implementation
    print("Mirror core available for operations")
    
    # Example: Access core mirroring methods (if available)
    # mirror_core.mirror_selection()
    # mirror_core.set_mirror_axis()

# Mirror tool integration example
def setup_mirror_workflow():
    tool = csc.tools.MirrorTool()
    core = tool.core()
    
    if core:
        # Configure mirroring parameters through core
        return core
    else:
        print("Mirror core not available")
        return None

# Use in animation workflow
mirror_core = setup_mirror_workflow()
if mirror_core:
    # Perform mirroring operations
    # This would typically involve:
    # 1. Selecting objects to mirror
    # 2. Setting mirror axis/plane
    # 3. Executing mirror operation
    pass
```

## Usage Notes

- The MirrorTool provides access to Cascadeur's mirroring functionality for animation workflows
- `core()` returns the actual implementation object that handles mirroring algorithms
- Mirror operations typically work with selected objects and can mirror poses, animation keys, and constraints
- The tool supports various mirroring modes and axis configurations
- Mirroring is essential for creating symmetric character animations efficiently
- The core object provides the detailed mirroring implementation and configuration options
- Mirror operations integrate with Cascadeur's selection system to determine what to mirror
- Always check if core is available before attempting to use mirroring functionality

## See Also

- `csc.tools.mirror.Core` - Core mirror implementation and algorithms
- `csc.domain.Selector` - Selection system for choosing objects to mirror
- `csc.tools.SelectionGroups` - Selection group management for mirroring workflows
- Animation tools that work with mirrored data and symmetric workflows