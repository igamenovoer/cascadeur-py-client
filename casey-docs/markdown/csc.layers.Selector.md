[CLEAN]

# csc.layers.Selector

## Overview

Selector manages the selection state of layers and folders in Cascadeur. It provides methods to query which layers are included in the current selection, retrieve selection indices, set selections by indices or by item ranges, and control whether certain folders are uncheckable. This helps scripts observe and modify user selections programmatically.

## Class Definition

```python
class csc.layers.Selector:
    ...
```

## Constructor

### `__init__(*args, **kwargs)`

Initializes a Selector instance.

Parameters:
- `*args`: undocumented
- `**kwargs`: undocumented

Returns:
- None

## Methods

### `all_included_layer_ids(ignore_locked: bool = False) -> LayerId[]`

Returns identifiers of all layers included in the current selection.

Parameters:
- `ignore_locked: bool` – if true, locked layers are ignored (default: False)

Returns:
- `LayerId[]` – list of included layer identifiers

### `all_included_layer_indices(ignore_locked: bool = False) -> IndicesContainer`

Returns indices of all layers included in the current selection.

Parameters:
- `ignore_locked: bool` – if true, locked layers are ignored (default: False)

Returns:
- `IndicesContainer` – container of included layer indices

### `is_selected(id)`

Reports whether the given item is selected.

Parameters:
- `id: ItemId` – item identifier

Returns:
- undocumented

### `select_default()`

Selects the default selection.

Parameters:
- none

Returns:
- undocumented

### `selection() -> IndicesContainer`

Returns the current selection.

Parameters:
- none

Returns:
- `IndicesContainer` – container representing the current selection

### `set_full_selection_by_parts(inds: IndicesContainer) -> None`

Sets the full selection using an indices container.

Parameters:
- `inds: IndicesContainer` – indices to select

Returns:
- None

### `set_full_selection_by_parts(itms: list[csc.Guid], first: int, last: int) -> None`

Sets the full selection using a range within a list of item identifiers.

Parameters:
- `itms: list[csc.Guid]` – item identifiers
- `first: int` – start index (inclusive)
- `last: int` – end index (inclusive)

Returns:
- None

### `set_uncheckable_folder_id(id, uncheckable: bool)`

Marks or unmarks a folder as uncheckable.

Parameters:
- `id: ItemId` – folder identifier
- `uncheckable: bool` – whether the folder is uncheckable

Returns:
- undocumented

### `top_layer_id()`

Returns the top layer identifier.

Parameters:
- none

Returns:
- undocumented

## Usage Notes

- Types such as `LayerId`, `IndicesContainer`, `ItemId`, and `csc.Guid` are part of the Cascadeur API and not defined here.
- When choosing between `set_full_selection_by_parts` overloads, use `inds` for index-based selection or `itms` with `first`/`last` for range selection by item list.

