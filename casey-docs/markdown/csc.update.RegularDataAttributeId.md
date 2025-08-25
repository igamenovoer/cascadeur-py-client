[CLEAN]

# csc.update.RegularDataAttributeId

## Overview
RegularDataAttributeId identifies a regular data attribute by its underlying data id. It is intended for data that exposes exactly one input and one output attribute. Construction is overloaded to accept either a string id, a DataId object, or no argument.

## Class Definition
```python
class csc.update.RegularDataAttributeId
```

## Constructor

### __init__(self: csc.update.RegularDataAttributeId, arg0: str) -> None
Initialize with a string identifier.
- Parameters:
  - arg0: str – undocumented
- Returns: None

### __init__(self: csc.update.RegularDataAttributeId, arg0: csc.model.DataId) -> None
Initialize with a DataId instance.
- Parameters:
  - arg0: csc.model.DataId – undocumented
- Returns: None

### __init__(self: csc.update.RegularDataAttributeId) -> None
Initialize without arguments.
- Parameters: undocumented
- Returns: None

## Usage Notes
- Designed for data with a single input and single output attribute.

