[CLEAN]

# csc.domain.SelectorMode

**Module:** `csc.domain.SelectorMode`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.SelectorMode.html)

## Overview

The `SelectorMode` enumeration defines different selection behavior modes for scene object selection operations in Cascadeur. It controls how new selections interact with existing selections, supporting various selection patterns commonly used in 3D animation software.

## Enumeration Definition

```python
class csc.domain.SelectorMode(Enum)
```

The SelectorMode enumeration provides different strategies for handling object selection operations based on current selection state.

## Constructor

### `__init__(self, value: int)`

Initializes a SelectorMode with the specified value.

**Parameters:**
- `value` (int): The enumeration value for the selection mode

## Members

### `SingleSelection`

Single selection mode that manages individual object selection intelligently.

**Behavior:**
- Resets selection if new objects are selected
- No change if already selected objects are selected again
- Maintains single-object selection focus

### `MultiSelection`

Smart multiple selection mode with toggle behavior.

**Behavior:**  
- If not all target objects are currently selected, adds them to selection
- If all target objects are already selected, subtracts them from selection
- Provides intuitive toggle behavior for multiple objects

### `NewSelection`

Complete selection replacement mode.

**Behavior:**
- Resets the entire current selection
- Highlights only the newly specified selection
- Clears all previously selected objects

### `AdditionSelection`

Additive selection mode that expands current selection.

**Behavior:**
- Adds all specified objects to the current selection
- Preserves existing selection state
- Never removes objects from selection

### `SubtractionSelection`

Subtractive selection mode that reduces current selection.

**Behavior:**
- Removes specified objects from the current selection
- Preserves non-specified selected objects
- Only affects objects that are currently selected

## Properties

### `name` (Property)

Gets the name of the enumeration member.

**Type:** `str`

### `value` (Property)

Gets the integer value of the enumeration member.

**Type:** `int`

## Usage Example

```python
import csc.domain
import csc.model

# Create selector and object IDs
selector = csc.domain.Selector()
object_ids = {csc.model.ObjectId(), csc.model.ObjectId()}

# New selection - replaces current selection entirely
selector.select(
    ids=object_ids,
    mode=csc.domain.SelectorMode.NewSelection
)

# Addition selection - adds to current selection
additional_ids = {csc.model.ObjectId()}
selector.select(
    ids=additional_ids,
    mode=csc.domain.SelectorMode.AdditionSelection
)

# Multi selection - toggles objects in selection
selector.select(
    ids=object_ids,
    mode=csc.domain.SelectorMode.MultiSelection
)

# Subtraction selection - removes from current selection
selector.select(
    ids=additional_ids,
    mode=csc.domain.SelectorMode.SubtractionSelection
)

# Single selection - manages individual object focus
single_id = {csc.model.ObjectId()}
selector.select(
    ids=single_id,
    mode=csc.domain.SelectorMode.SingleSelection
)

# Access mode properties
mode = csc.domain.SelectorMode.NewSelection
print(f"Mode name: {mode.name}")
print(f"Mode value: {mode.value}")
```

## Usage Notes

- Selection modes determine how new selection operations interact with existing selections
- `NewSelection` is the most common mode for replacing the entire selection
- `AdditionSelection` and `SubtractionSelection` provide precise control over selection modification
- `MultiSelection` offers user-friendly toggle behavior for interactive selection
- `SingleSelection` is optimized for workflows focusing on individual object manipulation
- These modes integrate with `SelectorFilter` to provide comprehensive selection control
- Mode choice affects user experience and workflow efficiency in animation tasks

## See Also

- `csc.domain.Selector` - Main selector class that uses these modes
- `csc.domain.SelectorFilter` - Selection filtering options
- `csc.domain.Select` - Selection configuration class
- `csc.domain.Selection` - Selection state representation