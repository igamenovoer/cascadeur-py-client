---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.SceneUpdater.html
html_file: 1c422e2bb9950f6f7df8ee5934308db1.html
module: csc.domain.SceneUpdater
---

# csc.domain.SceneUpdater[??](#csc-domain-sceneupdater "Permalink to this heading")

*class* csc.domain.SceneUpdater[??](#csc.domain.SceneUpdater "Permalink to this definition")
:   SceneUpdater class

    The SceneUpdater serves to rule the scene modify.
    If we changed the update, we should regenerate it, also it has the possible to run the update with certain data.

    Variables:
    :   **run\_update** ??? overridden method by csc.model.DataId{} (localIds), int (frame) || csc.model.DataId{}, int{} (frames)

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.SceneUpdater.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.domain.SceneUpdater.__init__ "csc.domain.SceneUpdater.__init__")(\*args,??\*\*kwargs) |  |
    | [`generate_update`](../csc.html#csc.domain.SceneUpdater.generate_update "csc.domain.SceneUpdater.generate_update")(self) |  |
    | [`get_interpolator`](../csc.html#csc.domain.SceneUpdater.get_interpolator "csc.domain.SceneUpdater.get_interpolator")(self) |  |
    | [`run_update`](../csc.html#csc.domain.SceneUpdater.run_update "csc.domain.SceneUpdater.run_update")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`scene`](../csc.html#csc.domain.SceneUpdater.scene "csc.domain.SceneUpdater.scene")(self) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.domain.SceneUpdater.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.SceneUpdater.__module__ "Permalink to this definition")

    generate\_update(*self: [csc.domain.SceneUpdater](../csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SceneUpdater.generate_update "Permalink to this definition")

    get\_interpolator(*self: [csc.domain.SceneUpdater](../csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater")*)  [csc.domain.LocalInterpolator](../csc.html#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator")[??](#csc.domain.SceneUpdater.get_interpolator "Permalink to this definition")

    run\_update(*\*args*, *\*\*kwargs*)[??](#csc.domain.SceneUpdater.run_update "Permalink to this definition")
    :   Overloaded function.

        1. run\_update(self: csc.domain.SceneUpdater, local\_ids: set[csc.model.DataId], frame: int) -> None
        2. run\_update(self: csc.domain.SceneUpdater, local\_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None

    scene(*self: [csc.domain.SceneUpdater](../csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.SceneUpdater.scene "Permalink to this definition")