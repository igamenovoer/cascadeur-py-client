---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.SceneUpdater.html
html_file: 1c422e2bb9950f6f7df8ee5934308db1.html
module: csc.domain.SceneUpdater
---

# csc.domain.SceneUpdater 

SceneUpdater class The SceneUpdater serves to rule the scene modify.
If we changed the update, we should regenerate it, also it has the possible to run the update with certain data. run_update – overridden method by csc.model.DataId{} (localIds), int (frame) || csc.model.DataId{}, int{} (frames) Methods __init__ (*args, **kwargs) generate_update (self) get_interpolator (self) run_update (*args, **kwargs) Overloaded function. scene (self) Overloaded function.
1. run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frame: int) -> None
2. run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None

run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frame: int) -> None run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None