---
source_url: https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html
html_file: ea75dc1516040730ff89071670068ab6.html
module: csc.app.ProjectLoader
---

# csc.app.ProjectLoader[??](#csc-app-projectloader "Permalink to this heading")

*class* csc.app.ProjectLoader[??](#csc.app.ProjectLoader "Permalink to this definition")
:   ProjectLoader class

    Provides methods to load domain scene.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.ProjectLoader.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.app.ProjectLoader.__init__ "csc.app.ProjectLoader.__init__")(\*args,??\*\*kwargs) |  |
    | [`load_from`](../csc.html#csc.app.ProjectLoader.load_from "csc.app.ProjectLoader.load_from")(arg0,??arg1) | Minimal Load. |

    \_\_annotations\_\_ *= {}*[??](#csc.app.ProjectLoader.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.ProjectLoader.__module__ "Permalink to this definition")

    *static* load\_from(*arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.ProjectLoader.load_from "Permalink to this definition")
    :   Minimal Load. This method doesn???t load selection groups, control picker and etc.
        Better use data\_source\_manager???s load\_scene method.
        Example:
        csc.app.ProjectLoader.load\_from(file\_path, scene)