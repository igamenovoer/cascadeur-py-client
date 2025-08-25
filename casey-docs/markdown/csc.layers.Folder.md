[CLEAN]

# csc.layers.Folder

## Overview
Folder represents a parent container for layers and subfolders in the Cascadeur layer system. It provides operations to inspect and access child items by identifier or by position, and to query basic state such as child count and emptiness. Some parameter and return type details are not documented in the provided source.

## Class Definition
```python
class Folder
```

## Constructor

### `__init__(*args, **kwargs)`
Initialize a Folder instance; parameters are undocumented.

- Parameters:
  - `*args`: undocumented – variable positional arguments
  - `**kwargs`: undocumented – variable keyword arguments

- Returns: None

## Methods

### `child_by_id(self, id) -> ItemId`
Get a child by its identifier.

- Parameters:
  - `id`: undocumented – child identifier
- Returns: `ItemId` – undocumented

### `child_by_pos(self, pos: int) -> ItemId`
Get a child by its position index.

- Parameters:
  - `pos`: int – position index (undocumented)
- Returns: `ItemId` – undocumented

### `child_pos(self, id: ItemId) -> int`
Get the position index of a child by identifier.

- Parameters:
  - `id`: `ItemId` – child identifier (undocumented)
- Returns: `int` – position index (undocumented)

### `children_cnt(self) -> int`
Return the number of children.

- Returns: `int` – undocumented

### `children_ids(self) -> ItemId[]`
Return the list of child identifiers.

- Returns: `ItemId[]` – undocumented

### `children_ordered(self) -> ItemId[]`
Return the ordered list of child identifiers.

- Returns: `ItemId[]` – undocumented

### `has_child(self, id)`
Check whether a child with the given identifier exists.

- Parameters:
  - `id`: undocumented – child identifier
- Returns: undocumented

### `is_empty(self)`
Check whether the folder contains no children.

- Returns: undocumented

## Attributes

- `header`: `Header` – undocumented
- `id`: `ItemId` – undocumented
- `pos`: `int` – undocumented

## Usage Notes

- Types such as `ItemId` and `Header` are part of the Cascadeur API; their details are undocumented here.
- Indexing semantics (e.g., zero-based vs one-based) are not specified in the provided source.

