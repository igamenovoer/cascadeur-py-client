# csc.layers.Cycle

**Module:** `csc.layers.Cycle`  
**Source:** [Original Documentation Link](https://cascadeur.com/python-api/_generate/csc.layers.Cycle.html)

## Overview

Represents an animation frame cycle with active and inactive frame ranges and utility methods to inspect frame indices and compare cycles.

## Class Definition

```python
class csc.layers.Cycle
```

## Constructor

### `__init__(*args, **kwargs)`

Description not available in source.

**Parameters:**
- `*args`: Variable length argument list.
- `**kwargs`: Arbitrary keyword arguments.

## Methods

### `get_no_pos()`

Description not available in source.

**Returns:**
- (unknown): Description not available in source.

### `is_the_same_frames_as(other_cycle) -> bool`

Returns whether this cycle covers the same frames as another cycle.

**Parameters:**
- `other_cycle` (Cycle): Cycle to compare.

**Returns:**
- bool: True if frames match.

### `left_frame_index() -> Pos`

Returns the left (starting) active frame index.

**Returns:**
- `Pos`: Left frame index.

### `right_frame_index() -> Pos`

Returns the right (ending) active frame index.

**Returns:**
- `Pos`: Right frame index.

## Attributes

- `first_active_frame_index` (`Pos`): First active frame index. (Inferred name; description not in source.)
- `following_interval` (unknown): Description not available in source.
- `last_active_frame_index` (`Pos`): Last active frame index. (Inferred.)
- `left_inactive_frame_index` (`Pos`): Left boundary of inactive interval preceding active frames. (Inferred.)
- `right_inactive_frame_index` (`Pos`): Right boundary of inactive interval following active frames. (Inferred.)

## Usage Notes

- Use `is_the_same_frames_as` to compare cycles efficiently.
- Frame index methods return `Pos` objects; ensure to access their numeric value as needed.
- Attributes may be read-only (not specified in source); modify through higher-level APIs if required.

```python
# Example usage
from csc.layers import Cycle

cycle_a = Cycle()
cycle_b = Cycle()

if cycle_a.is_the_same_frames_as(cycle_b):
	print("Cycles match")

start = cycle_a.left_frame_index()
end = cycle_a.right_frame_index()
print("Span:", start, end)
```