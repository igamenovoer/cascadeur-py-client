[CLEAN]

# csc.layers.ItemVariant

## Overview
ItemVariant represents an item in the layers system that can be either a Folder or a Layer and is associated with a Header. It provides methods to determine which kind of item it wraps and to access the underlying objects. Use it when traversing or manipulating layer hierarchies where items may differ in kind.

## Class Definition
```python
class csc.layers.ItemVariant
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a new ItemVariant instance; details are undocumented.

Parameters:
- args: undocumented
- kwargs: undocumented

Returns:
- None

## Methods

### `folder() -> Folder | None`
Returns the Folder if this variant represents a folder; otherwise None.

Parameters:
- none

Returns:
- Folder or None

### `header() -> Header`
Returns the associated Header.

Parameters:
- none

Returns:
- Header

### `is_folder() -> bool`
Indicates whether this variant represents a folder.

Parameters:
- none

Returns:
- bool

### `is_layer() -> bool`
Indicates whether this variant represents a layer.

Parameters:
- none

Returns:
- bool

### `layer() -> Layer | None`
Returns the Layer if this variant represents a layer; otherwise None.

Parameters:
- none

Returns:
- Layer or None

## Usage Notes
- This variant may correspond to either a folder or a layer; use is_folder() and is_layer() to check before accessing folder() or layer().

