[CLEAN]

# csc.layers.Cycle

## Overview
Represents a frame cycle used in Cascadeur’s layer system. A cycle covers an active range of frames and may have surrounding inactive boundaries. It provides helpers to query boundary positions and to compare coverage with another cycle.

## Class Definition
```python
class csc.layers.Cycle
```

## Constructor

### `__init__(*args, **kwargs)`
Undocumented constructor.

**Parameters:**
- `*args`: undocumented – undocumented
- `**kwargs`: undocumented – undocumented

## Methods

### `get_no_pos()`
Undocumented.

**Returns:**
- undocumented – undocumented

### `is_the_same_frames_as(other_cycle) -> bool`
Returns whether this cycle covers the same frames as another cycle.

**Parameters:**
- `other_cycle`: Cycle – cycle to compare

**Returns:**
- bool – True if frames match

### `left_frame_index() -> Pos`
Returns the left (starting) active frame index.

**Returns:**
- `Pos` – undocumented

### `right_frame_index() -> Pos`
Returns the right (ending) active frame index.

**Returns:**
- `Pos` – undocumented

## Attributes

- `first_active_frame_index`: Pos – undocumented
- `following_interval`: undocumented – undocumented
- `last_active_frame_index`: Pos – undocumented
- `left_inactive_frame_index`: Pos – undocumented
- `right_inactive_frame_index`: Pos – undocumented

## Usage Notes

- Methods returning Pos yield position-like objects; specific structure is undocumented.
- Behavior details are not documented in the source; consult higher-level APIs or official references when available.

