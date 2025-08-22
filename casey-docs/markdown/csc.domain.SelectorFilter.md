[CLEAN]

# csc.domain.SelectorFilter

**Module:** `csc.domain.SelectorFilter`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.SelectorFilter.html)

## Overview

The `SelectorFilter` enumeration defines filtering options for scene object selection operations in Cascadeur. It provides various filtering criteria that can be combined using bitwise operations to control which types of objects can be selected during selection operations.

## Enumeration Definition

```python
class csc.domain.SelectorFilter(Enum)
```

The SelectorFilter enumeration uses bitwise flags to enable flexible combination of multiple filtering criteria.

## Constructor

### `__init__(self, value: int)`

Initializes a SelectorFilter with the specified value.

**Parameters:**
- `value` (int): The bitwise flag value for the filter

## Members

### `Free` = 0x00

No filtering applied - all objects can be selected regardless of their properties.

**Value:** `0x00` (0)

### `Selectable` = 0x01

Filter based on object selectability - only objects marked as selectable can be selected.

**Value:** `0x01` (1)

### `ObjectType` = 0x02

Filter based on object type - only objects of specific types can be selected.

**Value:** `0x02` (2)

### `Layer` = 0x04

Filter based on layer membership - only objects on specific layers can be selected.

**Value:** `0x04` (4)

### `CustomSelectionPolicy` = 0x08

Filter based on custom selection policy - objects must meet custom selection criteria.

**Value:** `0x08` (8)

### `Standard` = Selectable | ObjectType | Layer

Standard filtering combining selectability, object type, and layer filters.

**Value:** `0x07` (7) - Combination of Selectable, ObjectType, and Layer

### `Full` = 0xFF

Complete filtering - all available filter criteria are applied.

**Value:** `0xFF` (255)

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

# Use individual filter types
free_filter = csc.domain.SelectorFilter.Free
selectable_filter = csc.domain.SelectorFilter.Selectable
layer_filter = csc.domain.SelectorFilter.Layer

# Use predefined combinations
standard_filter = csc.domain.SelectorFilter.Standard
full_filter = csc.domain.SelectorFilter.Full

# Combine filters using bitwise operations
custom_filter = csc.domain.SelectorFilter.Selectable | csc.domain.SelectorFilter.ObjectType

# Use with selector operations
selector = csc.domain.Selector()
object_ids = {csc.model.ObjectId()}

# Apply filter during selection
selector.select(
    ids=object_ids,
    filter=csc.domain.SelectorFilter.Standard,
    mode=csc.domain.SelectorMode.NewSelection
)

# Check filter values
print(f"Free filter value: {csc.domain.SelectorFilter.Free.value}")
print(f"Standard filter value: {csc.domain.SelectorFilter.Standard.value}")
print(f"Filter name: {csc.domain.SelectorFilter.Standard.name}")
```

## Usage Notes

- SelectorFilter values are designed to be combined using bitwise OR operations
- The `Free` filter (0x00) disables all filtering, allowing selection of any object
- `Standard` is a common combination of `Selectable`, `ObjectType`, and `Layer` filters
- `Full` filter (0xFF) applies all available filtering criteria for maximum selectivity
- Filter combinations allow fine-grained control over what objects can be selected
- These filters integrate with the Selector class to control selection behavior
- Bitwise operations enable flexible creation of custom filter combinations

## See Also

- `csc.domain.Selector` - Main selector class that uses these filters
- `csc.domain.SelectorMode` - Selection behavior modes
- `csc.domain.Select` - Selection configuration class
- `csc.model.CustomSelectionPolicy` - Custom selection policy configuration