---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.index.IndicesContainer.html
html_file: c27c8f3c4586c89070f42473d1002ed0.html
module: csc.layers.index.IndicesContainer
---

# csc.layers.index.IndicesContainer 

IndicesContainer class Contains of indices items in the structure std::map<ItemId, FramesIndices>
- all_frame_indices – overridden method by int (sizeLimit)
- frames_interval – overridden method by int (sizeLimit)

all_frame_indices – overridden method by int (sizeLimit) frames_interval – overridden method by int (sizeLimit) Overloaded function.
1. __init__(self: csc.layers.index.IndicesContainer) -> None
2. __init__(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None
3. __init__(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None

__init__(self: csc.layers.index.IndicesContainer) -> None __init__(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None __init__(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None Methods __init__ (*args, **kwargs) Overloaded function. add (self, other_container) otherContainer : IndicesContainer add_frame_indices (self, frame_indices) frame_indices: int{} add_item (self, item_indices) itemIndices : ItemIndices all_frame_indices (*args, **kwargs) Overloaded function. cell_indices (self) -> CellIndex[] delete_empty_items (self) direct_indices (*args, **kwargs) Overloaded function. frames_interval (*args, **kwargs) Overloaded function. is_empty (self) item_ids (self) -> Guid[] item_indices (self, id) -> FramesIndices items_indices (self) -> ItemIndices[] rect (self) -> RectIndicesContainer set_frame_indices (self, start, end) start, end : int Overloaded function.
1. __init__(self: csc.layers.index.IndicesContainer) -> None
2. __init__(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None
3. __init__(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None

__init__(self: csc.layers.index.IndicesContainer) -> None __init__(self: csc.layers.index.IndicesContainer, arg0: list[csc.layers.index.CellIndex]) -> None __init__(self: csc.layers.index.IndicesContainer, start: list[csc.Guid], end: csc.layers.index.FramesIndices) -> None otherContainer : IndicesContainer frame_indices: int{} itemIndices : ItemIndices Overloaded function.
1. all_frame_indices(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesIndices
2. all_frame_indices(self: csc.layers.index.IndicesContainer, size_limit: int) -> csc.layers.index.FramesIndices

all_frame_indices(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesIndices all_frame_indices(self: csc.layers.index.IndicesContainer, size_limit: int) -> csc.layers.index.FramesIndices -> CellIndex[] Overloaded function.
1. direct_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices]
2. direct_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices]

direct_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices] direct_indices(self: csc.layers.index.IndicesContainer) -> dict[csc.Guid, csc.layers.index.FramesIndices] Overloaded function.
1. frames_interval(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesInterval
2. frames_interval(self: csc.layers.index.IndicesContainer, size_limit: int) -> csc.layers.index.FramesInterval

frames_interval(self: csc.layers.index.IndicesContainer) -> csc.layers.index.FramesInterval frames_interval(self: csc.layers.index.IndicesContainer, size_limit: int) -> csc.layers.index.FramesInterval -> Guid[] -> FramesIndices -> ItemIndices[] -> RectIndicesContainer start, end : int