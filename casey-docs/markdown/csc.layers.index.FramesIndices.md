[CLEAN]

# csc.layers.index.FramesIndices

## Overview

FramesIndices represents a collection of animation frame indices and utilities for working with frame-based intervals. It supports adding indices from various sources and performing set-like operations. Utility methods provide basic queries (first, last, size, empty) and conversions to interval representations. Specific parameter and return types are undocumented for several methods and should be verified against the original API.

## Class Definition

```python
class FramesIndices:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new FramesIndices instance.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- None

## Methods

### `add(self, index: int) -> None`

Adds a single frame index to the collection.

**Parameters:**
- `index: int` – frame index to add

**Returns:**
- None

### `add(self, other: csc.layers.index.FramesIndices) -> None`

Merges indices from another FramesIndices into this collection.

**Parameters:**
- `other: csc.layers.index.FramesIndices` – index collection to merge

**Returns:**
- None

### `add(self, indices: set[int]) -> None`

Adds multiple frame indices from a set.

**Parameters:**
- `indices: set[int]` – set of frame indices to add

**Returns:**
- None

### `add(self, indices: list[int]) -> None`

Adds multiple frame indices from a list.

**Parameters:**
- `indices: list[int]` – list of frame indices to add

**Returns:**
- None

### `clamp(self, min, max)`

Restricts indices to lie within the provided bounds.

**Parameters:**
- `min` – undocumented
- `max` – undocumented

**Returns:**
- undocumented

### `empty(self)`

Checks whether the collection contains no indices.

**Parameters:**
- None

**Returns:**
- undocumented

### `first(self)`

Retrieves the first (smallest) frame index in the collection.

**Parameters:**
- None

**Returns:**
- undocumented

### `from_range(min, max) -> FramesIndices`

Creates a FramesIndices instance from the given range bounds.

**Parameters:**
- `min` – undocumented
- `max` – undocumented

**Returns:**
- `FramesIndices`

### `intersect_indices(l, r)`

Computes the intersection of two index collections.

**Parameters:**
- `l` – undocumented
- `r` – undocumented

**Returns:**
- undocumented

### `last(self)`

Retrieves the last (largest) frame index in the collection.

**Parameters:**
- None

**Returns:**
- undocumented

### `size(self)`

Returns the number of indices in the collection.

**Parameters:**
- None

**Returns:**
- undocumented

### `to_intervals(indices) -> FramesInterval[]`

Converts a set of indices into contiguous frame intervals.

**Parameters:**
- `indices` – undocumented

**Returns:**
- `FramesInterval[]`

### `union_indices(l, r)`

Overloaded function that computes the union of two index collections.

**Parameters:**
- `l` – undocumented
- `r` – undocumented

**Returns:**
- undocumented

## Usage Notes

- Some methods are overloaded; behavior may depend on the argument types.
- Parameter and return types not explicitly shown here are undocumented in the source and should be confirmed with the original documentation.

