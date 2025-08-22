---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Selector.html
html_file: 92ff7297ba42f99dd901779ce81f2a57.html
module: csc.layers.Selector
---

# csc.layers.Selector 

Selector class 
This class contains methods to observe and to set selected layers and folders set_full_selection_by_parts – overridden method by ItemId[] (itms), int (first), int (last) || IndicesContainer (inds) Methods __init__ (*args, **kwargs) all_included_layer_ids (self[, ignore_locked]) ignoreLocked : bool (false) | -> LayerId[] all_included_layer_indices (self, ignore_locked) ignoreLocked : bool (false) | -> IndicesContainer is_selected (self, id) select_default (self) selection (self) -> IndicesContainer set_full_selection_by_parts (*args, **kwargs) Overloaded function. set_uncheckable_folder_id (self, id, uncheckable) id : ItemId | uncheckable : bool top_layer_id (self) ignoreLocked : bool (false) | -> LayerId[] ignoreLocked : bool (false) | -> IndicesContainer -> IndicesContainer Overloaded function.
1. set_full_selection_by_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None inds : IndicesContainer
2. set_full_selection_by_parts(self: csc.layers.Selector, itms: list[csc.Guid], first: int, last: int) -> None

set_full_selection_by_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None
> inds : IndicesContainer

inds : IndicesContainer set_full_selection_by_parts(self: csc.layers.Selector, itms: list[csc.Guid], first: int, last: int) -> None id : ItemId | uncheckable : bool