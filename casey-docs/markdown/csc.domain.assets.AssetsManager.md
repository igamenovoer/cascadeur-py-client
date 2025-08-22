---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html
html_file: 8033546f9134cb2952a62dd7fa00ff75.html
module: csc.domain.assets.AssetsManager
---

# csc.domain.assets.AssetsManager[??](#csc-domain-assets-assetsmanager "Permalink to this heading")

*class* csc.domain.assets.AssetsManager[??](#csc.domain.assets.AssetsManager "Permalink to this definition")
:   AssetsManager class

    This class implements basic methods to manage assets

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.assets.AssetsManager.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](#id0 "csc.domain.assets.AssetsManager.__init__")(\*args,??\*\*kwargs) |  |
    | [`add`](#csc.domain.assets.AssetsManager.add "csc.domain.assets.AssetsManager.add")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`at`](#csc.domain.assets.AssetsManager.at "csc.domain.assets.AssetsManager.at")(self,??arg0) | -> Asset |
    | [`erase`](#csc.domain.assets.AssetsManager.erase "csc.domain.assets.AssetsManager.erase")(self,??ids) |  |
    | [`get_cube_mesh`](#csc.domain.assets.AssetsManager.get_cube_mesh "csc.domain.assets.AssetsManager.get_cube_mesh")(arg0) | -> Mesh |
    | [`get_plane_mesh`](#csc.domain.assets.AssetsManager.get_plane_mesh "csc.domain.assets.AssetsManager.get_plane_mesh")(arg0) | -> Mesh |

    \_\_annotations\_\_ *= {}*[??](#csc.domain.assets.AssetsManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain.assets'*[??](#csc.domain.assets.AssetsManager.__module__ "Permalink to this definition")

    add(*\*args*, *\*\*kwargs*)[??](#csc.domain.assets.AssetsManager.add "Permalink to this definition")
    :   Overloaded function.

        1. add(self: csc.domain.assets.AssetsManager, asset: csc.domain.assets.MeshBlendshape) -> csc.domain.AssetId

           > -> csc.domain.AssetId
        2. add(self: csc.domain.assets.AssetsManager, asset: csc.domain.assets.Mesh) -> csc.domain.AssetId

           > -> csc.domain.AssetId
        3. add(self: csc.domain.assets.AssetsManager, asset: csc.domain.assets.MeshDependency) -> csc.domain.AssetId

           > -> csc.domain.AssetId

    at(*self: [csc.domain.assets.AssetsManager](#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*, *arg0: [csc.domain.AssetId](../csc.html#csc.domain.AssetId "csc.domain.AssetId")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.assets.AssetsManager.at "Permalink to this definition")
    :   -> Asset

    erase(*self: [csc.domain.assets.AssetsManager](#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*, *ids: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.domain.AssetId](../csc.html#csc.domain.AssetId "csc.domain.AssetId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.assets.AssetsManager.erase "Permalink to this definition")

    *static* get\_cube\_mesh(*arg0: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [csc.domain.assets.Mesh](csc.domain.assets.Mesh.html#csc.domain.assets.Mesh "csc.domain.assets.Mesh")[??](#csc.domain.assets.AssetsManager.get_cube_mesh "Permalink to this definition")
    :   -> Mesh

    *static* get\_plane\_mesh(*arg0: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [csc.domain.assets.Mesh](csc.domain.assets.Mesh.html#csc.domain.assets.Mesh "csc.domain.assets.Mesh")[??](#csc.domain.assets.AssetsManager.get_plane_mesh "Permalink to this definition")
    :   -> Mesh