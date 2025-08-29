# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html

# csc.app.DataSourceManager [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html\#csc-app-datasourcemanager "Permalink to this heading")

_class_ csc.app.DataSourceManager [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager "Permalink to this definition")

DataSourceManager class

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.__init__ "csc.app.DataSourceManager.__init__")(\*args, \*\*kwargs) |  |
| [`close_scene`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.close_scene "csc.app.DataSourceManager.close_scene")(self, scene) |  |
| [`load_scene`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.load_scene "csc.app.DataSourceManager.load_scene")(self, file\_name) | Load scene and all additional datas (selection groups etc) Example: ds\_m = csc.app.get\_application().get\_data\_source\_manager() ds\_m.load\_scene(file\_path) |
| [`save_current_scene`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.save_current_scene "csc.app.DataSourceManager.save_current_scene")(\*args, \*\*kwargs) | Overloaded function. |
| [`save_scene`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.save_scene "csc.app.DataSourceManager.save_scene")(\*args, \*\*kwargs) | Overloaded function. |
| [`save_scene_as`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.save_scene_as "csc.app.DataSourceManager.save_scene_as")(self, scene\_view, full\_file\_name) |  |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.__module__ "Permalink to this definition")close\_scene( _self:[csc.app.DataSourceManager](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.close_scene "Permalink to this definition")load\_scene( _self:[csc.app.DataSourceManager](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.load_scene "Permalink to this definition")

Load scene and all additional datas (selection groups etc)
Example:
ds\_m = csc.app.get\_application().get\_data\_source\_manager()
ds\_m.load\_scene(file\_path)

save\_current\_scene( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.save_current_scene "Permalink to this definition")

Overloaded function.

1. save\_current\_scene(self: csc.app.DataSourceManager, handler: Callable\[\[bool\], None\]) -> None

2. save\_current\_scene(self: csc.app.DataSourceManager) -> None


save\_scene( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.save_scene "Permalink to this definition")

Overloaded function.

1. save\_scene(self: csc.app.DataSourceManager, scene\_view: csc.view.Scene, handler: Callable\[\[bool\], None\]) -> None

2. save\_scene(self: csc.app.DataSourceManager, scene\_view: csc.view.Scene) -> None


save\_scene\_as( _self:[csc.app.DataSourceManager](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")_, _scene\_view:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _full\_file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html#csc.app.DataSourceManager.save_scene_as "Permalink to this definition")