[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:46 | Original: 9a37cfb0 -->

# csc.tools.selection.Mode

**Module:** `csc.tools.selection.Mode`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.selection.Mode.html)

## Overview

Enumeration representing selection modes: SetGroup, SingleSelect, and MultiSelect.

## Class Definition

```python
class csc.tools.selection.Mode
```

Enumeration with members: SetGroup, SingleSelect, MultiSelect.

## Constructor

### `__init__(self, value) -> None`

Initializes the enumeration member with the specified value.

**Parameters:**
- `value` (Any): The value corresponding to an enumeration member.

**Returns:**
- None

## Methods

No additional methods documented.

## Attributes

- `SetGroup`: Enumeration member.
- `SingleSelect`: Enumeration member.
- `MultiSelect`: Enumeration member.
- `name`: The name of the enumeration member.
- `value`: The value of the enumeration member.

## Usage Example

```python
from csc.tools.selection import Mode

# Practical usage example
mode = Mode.SetGroup
print(mode.name)   # 'SetGroup'
print(mode.value)  # underlying value associated with the member
```

## Usage Notes

- Use Mode to specify how selections are handled within tools (e.g., single vs. multiple selection).
- Access the member name via the name attribute and its underlying value via the value attribute.
- Constructing Mode via Mode(value) will map the value to the corresponding member.

## See Also

- Other selection-related tools and enumerations within csc.tools.selection