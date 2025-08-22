---
source_url: https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html
html_file: f30bb3206525268ab2b6b3883d32873c.html
module: csc.app.DataSourceManager
---

# csc.app.DataSourceManager 

DataSourceManager class Methods __init__ (*args, **kwargs) close_scene (self, scene) load_scene (self, file_name) Load scene and all additional datas (selection groups etc) Example: ds_m = csc.app.get_application().get_data_source_manager() ds_m.load_scene(file_path) save_current_scene (*args, **kwargs) Overloaded function. save_scene (*args, **kwargs) Overloaded function. save_scene_as (self, scene_view, full_file_name) Load scene and all additional datas (selection groups etc)
Example:
ds_m = csc.app.get_application().get_data_source_manager()
ds_m.load_scene(file_path) Overloaded function.
1. save_current_scene(self: csc.app.DataSourceManager, handler: Callable[[bool], None]) -> None
2. save_current_scene(self: csc.app.DataSourceManager) -> None

save_current_scene(self: csc.app.DataSourceManager, handler: Callable[[bool], None]) -> None save_current_scene(self: csc.app.DataSourceManager) -> None Overloaded function.
1. save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene, handler: Callable[[bool], None]) -> None
2. save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene) -> None

save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene, handler: Callable[[bool], None]) -> None save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene) -> None