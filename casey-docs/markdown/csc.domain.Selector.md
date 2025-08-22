[CLEAN]

# csc.domain.Selector

**Module:** `csc.domain.Selector`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.Selector.html)

## Overview

The `Selector` class provides basic methods and properties to operate on currently selected scene objects in Cascadeur. It serves as the primary interface for scene element selection, managing object IDs, pivot operations, and selection state changes with configurable filters and modes.

## Class Definition

```python
class csc.domain.Selector
```

The Selector class encapsulates scene object selection functionality with support for multiple selection modes, filtering, and pivot management.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new Selector instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Properties

### `ids` (Get)

Gets the currently selected object IDs.

**Type:** `Set[csc.model.ObjectId | csc.domain.Tool_object_id]`

## Methods

### `pivot(self) -> Pivot`

Gets the pivot object for the current selection.

**Returns:**
- Pivot: The pivot object associated with the current selection

### `select(*args, **kwargs)` (Overloaded)

Performs selection operations with multiple signature variants for different use cases.

#### Overload 1: `select(self, select: csc.domain.Select) -> None`

Applies a selection configuration to the selector.

**Parameters:**
- `select` (csc.domain.Select): The selection configuration to apply

**Returns:**
- None

#### Overload 2: `select(self, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = default, filter: csc.domain.SelectorFilter = SelectorFilter.Free, mode: csc.domain.SelectorMode = SelectorMode.NewSelection, type_filter: set[str] = set(), auto_pivot: bool = False) -> None`

Performs detailed selection with fine-grained control over selection parameters.

**Parameters:**
- `ids` (set): Set of object IDs to select
- `id` (Union[csc.model.ObjectId, csc.domain.Tool_object_id], optional): Primary object ID
- `filter` (csc.domain.SelectorFilter, optional): Selection filter mode (default: SelectorFilter.Free)
- `mode` (csc.domain.SelectorMode, optional): Selection mode (default: SelectorMode.NewSelection)
- `type_filter` (set[str], optional): Type-based filtering criteria (default: empty set)
- `auto_pivot` (bool, optional): Whether to automatically set pivot (default: False)

**Returns:**
- None

### `selected(self) -> Selection`

Gets the current selection state.

**Returns:**
- Selection: The current selection object containing selected elements

## Usage Example

```python
import csc.domain
import csc.model

# Create a selector instance
selector = csc.domain.Selector()

# Get currently selected object IDs
current_ids = selector.ids
print(f"Currently selected: {len(current_ids)} objects")

# Get the pivot for current selection
pivot = selector.pivot()

# Select specific objects with default settings
object_ids = {csc.model.ObjectId()}
selector.select(object_ids)

# Select with custom filter and mode
selector.select(
    ids=object_ids,
    filter=csc.domain.SelectorFilter.Free,
    mode=csc.domain.SelectorMode.NewSelection,
    type_filter={"mesh", "bone"},
    auto_pivot=True
)

# Get the current selection state
selection = selector.selected()

# Use a selection configuration
select_config = csc.domain.Select()
selector.select(select_config)
```

## Usage Notes

- The Selector class supports both model objects and tool objects for flexible scene interaction
- Selection operations can be filtered by object type using string-based type filters
- Multiple selection modes allow for different selection behaviors (new, additive, etc.)
- The pivot automatically updates based on selection changes when auto_pivot is enabled
- SelectorFilter provides control over what types of objects can be selected
- The class integrates with the broader Cascadeur selection and pivot system

## See Also

- `csc.domain.Select` - Selection configuration class
- `csc.domain.Selection` - Selection state representation
- `csc.domain.Pivot` - Pivot functionality for transformations
- `csc.domain.SelectorFilter` - Selection filtering options
- `csc.domain.SelectorMode` - Selection behavior modes
- `csc.model.ObjectId` - Model object identification
- `csc.domain.Tool_object_id` - Tool object identification