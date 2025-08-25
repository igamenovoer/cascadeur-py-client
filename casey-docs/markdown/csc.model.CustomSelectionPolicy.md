[CLEAN]

# csc.model.CustomSelectionPolicy

## Overview
Enumeration defining how an entity participates in selection operations within the Cascadeur model. It controls whether an entity can be selected with others, only by itself, or only alongside entities of the same type. Use this to enforce consistent selection behavior in tools and scripts.

## Class Definition
```python
class csc.model.CustomSelectionPolicy
```

## Constructor
### `__init__(value)`
Constructs the enumeration member from a value.

**Parameters:**
- value: undocumented – underlying value used to identify the member.

**Returns:**
- None

## Attributes
- Default: the entity is selected with other entities.
- Single: the entity is selected only if the selection contains only this entity.
- SingleType: the entity is selected only if the selection contains only entities of the same type.

## Usage Notes
- Choose Default for standard multi-selection behavior.
- Use Single to restrict selection to a single entity at a time.
- Use SingleType when selection should be limited to entities of the same type.

