[CLEAN]

# csc.update.ExternalPropertiesId

## Overview

ExternalPropertiesId is a GUID-based identifier used for external properties in the csc.update module. It is defined to always match the GroupId of the group where the external property is used. This type serves as an ID wrapper to reference external properties.

## Class Definition

```python
class csc.update.ExternalPropertiesId
```

## Constructor

### `__init__(arg0: csc.update.GroupId) -> None`

Constructor overload that creates an ExternalPropertiesId from a GroupId.

- Parameters:
  - arg0: csc.update.GroupId – undocumented
- Returns: None
- Notes: The resulting ID is equal to the provided GroupId.

### `__init__(arg0: str) -> None`

Constructor overload that creates an ExternalPropertiesId from a string.

- Parameters:
  - arg0: str – undocumented
- Returns: None

### `__init__() -> None`

Constructor overload with no arguments.

- Returns: None

## Usage Notes

- This ID always equals the GroupId of the group where the external property is used.
- Specific formatting requirements for the string overload are undocumented.

