---
source_url: https://cascadeur.com/python-api/_generate/csc.app.DataSourceManager.html
html_file: f30bb3206525268ab2b6b3883d32873c.html
module: csc.app.DataSourceManager
---

# csc.app.DataSourceManager[??](#csc-app-datasourcemanager "Permalink to this heading")

*class* csc.app.DataSourceManager[??](#csc.app.DataSourceManager "Permalink to this definition")
:   DataSourceManager class

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.DataSourceManager.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.app.DataSourceManager.__init__ "csc.app.DataSourceManager.__init__")(\*args,??\*\*kwargs) |  |
    | [`close_scene`](../csc.html#csc.app.DataSourceManager.close_scene "csc.app.DataSourceManager.close_scene")(self,??scene) |  |
    | [`load_scene`](../csc.html#csc.app.DataSourceManager.load_scene "csc.app.DataSourceManager.load_scene")(self,??file\_name) | Load scene and all additional datas (selection groups etc) Example: ds\_m = csc.app.get\_application().get\_data\_source\_manager() ds\_m.load\_scene(file\_path) |
    | [`save_current_scene`](../csc.html#csc.app.DataSourceManager.save_current_scene "csc.app.DataSourceManager.save_current_scene")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`save_scene`](../csc.html#csc.app.DataSourceManager.save_scene "csc.app.DataSourceManager.save_scene")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`save_scene_as`](../csc.html#csc.app.DataSourceManager.save_scene_as "csc.app.DataSourceManager.save_scene_as")(self,??scene\_view,??full\_file\_name) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.app.DataSourceManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.DataSourceManager.__module__ "Permalink to this definition")

    close\_scene(*self: [csc.app.DataSourceManager](../csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")*, *scene: [csc.view.Scene](../csc.html#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.DataSourceManager.close_scene "Permalink to this definition")

    load\_scene(*self: [csc.app.DataSourceManager](../csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.app.DataSourceManager.load_scene "Permalink to this definition")
    :   Load scene and all additional datas (selection groups etc)
        Example:
        ds\_m = csc.app.get\_application().get\_data\_source\_manager()
        ds\_m.load\_scene(file\_path)

    save\_current\_scene(*\*args*, *\*\*kwargs*)[??](#csc.app.DataSourceManager.save_current_scene "Permalink to this definition")
    :   Overloaded function.

        1. save\_current\_scene(self: csc.app.DataSourceManager, handler: Callable[[bool], None]) -> None
        2. save\_current\_scene(self: csc.app.DataSourceManager) -> None

    save\_scene(*\*args*, *\*\*kwargs*)[??](#csc.app.DataSourceManager.save_scene "Permalink to this definition")
    :   Overloaded function.

        1. save\_scene(self: csc.app.DataSourceManager, scene\_view: csc.view.Scene, handler: Callable[[bool], None]) -> None
        2. save\_scene(self: csc.app.DataSourceManager, scene\_view: csc.view.Scene) -> None

    save\_scene\_as(*self: [csc.app.DataSourceManager](../csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")*, *scene\_view: [csc.view.Scene](../csc.html#csc.view.Scene "csc.view.Scene")*, *full\_file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.DataSourceManager.save_scene_as "Permalink to this definition")