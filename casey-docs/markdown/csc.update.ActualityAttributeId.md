[CLEAN]

# csc.update.ActualityAttributeId

## Overview
Represents an identifier for an actuality attribute defined by a data id. This is an output-only attribute indicating whether a piece of data is actual or non-actual at the start of a graph update. The constructor is overloaded to accept a string, a csc.model.DataId, or no arguments. Further details are undocumented.

## Class Definition
```python
class csc.update.ActualityAttributeId
```

## Constructor

### `__init__() -> None`
Initializes a new ActualityAttributeId (undocumented).

Returns:
- None

### `__init__(arg0: str) -> None`
Initializes the attribute id from a string (undocumented).

Parameters:
- arg0: str - undocumented

Returns:
- None

### `__init__(arg0: csc.model.DataId) -> None`
Initializes the attribute id from a csc.model.DataId (undocumented).

Parameters:
- arg0: csc.model.DataId - undocumented

Returns:
- None

## Usage Notes
- This is an output-only attribute.
- The actual/non-actual state is determined at the start of a graph update.

