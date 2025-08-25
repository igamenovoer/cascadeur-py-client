[CLEAN]

# csc.math.SizesInterval

## Overview
SizesInterval represents an integer interval with basic helper operations. It provides constructors to define a range and utilities to query emptiness, boundaries, and membership, as well as to combine or intersect intervals. Specific semantics (e.g., inclusivity and edge cases) are undocumented.

## Class Definition
```python
class csc.math.SizesInterval

__init__(self) -> None
__init__(self, start: int, end: int) -> None
```

## Constructor

### `__init__(self) -> None`
Default constructor (undocumented).

Returns:
- None

### `__init__(self, start: int, end: int) -> None`
Constructor with explicit bounds (undocumented).

Parameters:
- start: int – undocumented
- end: int – undocumented

Returns:
- None

## Methods

### `start(self) -> int`
Get the start of the interval (undocumented).

Returns:
- int – undocumented

### `end(self) -> int`
Get the end of the interval (undocumented).

Returns:
- int – undocumented

### `empty(self) -> bool`
Check whether the interval is empty (undocumented).

Returns:
- bool – undocumented

### `contains(self, i)`
Check whether a value is within the interval (undocumented).

Parameters:
- i: undocumented – undocumented

Returns:
- undocumented

### `inside_interval_inclusive(self, number)`
Check whether a value is inside the interval using inclusive bounds (undocumented).

Parameters:
- number: undocumented – undocumented

Returns:
- undocumented

### `construct_in_right_order(first, second)`
Construct an interval ensuring correct ordering of bounds (undocumented).

Parameters:
- first: undocumented – undocumented
- second: undocumented – undocumented

Returns:
- undocumented

### `safe_construct(first, second)`
Safely construct an interval from two values (undocumented).

Parameters:
- first: undocumented – undocumented
- second: undocumented – undocumented

Returns:
- undocumented

### `intersect_intervals(first, second)`
Compute the intersection of two intervals (undocumented).

Parameters:
- first: undocumented – undocumented
- second: undocumented – undocumented

Returns:
- undocumented

### `union_overlaping_intervals(first, second)`
Compute the union of two overlapping intervals (undocumented).

Parameters:
- first: undocumented – undocumented
- second: undocumented – undocumented

Returns:
- undocumented

## Usage Notes
- Method behaviors and edge-case semantics are undocumented in the source snippet.
- Names suggest typical interval operations; verify exact behavior in the original API before relying on specifics.

