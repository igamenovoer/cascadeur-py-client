# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html

# csc.app.ProjectLoader [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html\#csc-app-projectloader "Permalink to this heading")

_class_ csc.app.ProjectLoader [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html#csc.app.ProjectLoader "Permalink to this definition")

ProjectLoader class

Provides methods to load domain scene.

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html#csc.app.ProjectLoader.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader.__init__ "csc.app.ProjectLoader.__init__")(\*args, \*\*kwargs) |  |
| [`load_from`](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader.load_from "csc.app.ProjectLoader.load_from")(arg0, arg1) | Minimal Load. |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html#csc.app.ProjectLoader.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html#csc.app.ProjectLoader.__module__ "Permalink to this definition")_static_ load\_from( _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html#csc.app.ProjectLoader.load_from "Permalink to this definition")

Minimal Load. This method doesn’t load selection groups, control picker and etc.
Better use data\_source\_manager’s load\_scene method.
Example:
csc.app.ProjectLoader.load\_from(file\_path, scene)