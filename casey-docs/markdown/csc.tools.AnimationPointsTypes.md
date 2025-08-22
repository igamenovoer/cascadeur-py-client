---
source_url: https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html
html_file: b82f7f9b7684692252366af89009e4fe.html
module: csc.tools.AnimationPointsTypes
---

# csc.tools.AnimationPointsTypes[??](#csc-tools-animationpointstypes "Permalink to this heading")

*class* csc.tools.AnimationPointsTypes[??](#csc.tools.AnimationPointsTypes "Permalink to this definition")
:   Class of basic types of points which physics tools and change through animation
    for target center of mass it contains

    get\_fulcrum\_points ??? all fulcrum point with collision
    get\_fixed\_points ??? all points need to fix with collision
    get\_local\_fixed\_points ??? points that should keep local coordinates after apply
    get\_collision\_surface\_points ??? collision points with normal type
    get\_collision\_pin\_points ??? collision points with pin type
    get\_collision\_fixed\_points ??? collision points with fulcrum groups
    get\_fulcrum\_floor\_points ??? points collide with only floor
    get\_fixed\_floor\_points ??? points collide with only floor and fulcrum groups
    get\_frame\_collision\_info\_points ??? collision info about points

    \_\_init\_\_(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg2: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg3: [csc.tools.StaticPointsTypes](../csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.AnimationPointsTypes.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.tools.AnimationPointsTypes.__init__ "csc.tools.AnimationPointsTypes.__init__")(self,??arg0,??arg1,??arg2,??arg3) |  |
    | [`get_collision_fixed_points`](../csc.html#csc.tools.AnimationPointsTypes.get_collision_fixed_points "csc.tools.AnimationPointsTypes.get_collision_fixed_points")(self) | Dict[frame number, set of points] |
    | [`get_collision_pin_points`](../csc.html#csc.tools.AnimationPointsTypes.get_collision_pin_points "csc.tools.AnimationPointsTypes.get_collision_pin_points")(self) | Dict[frame number, set of points] |
    | [`get_collision_surface_points`](../csc.html#csc.tools.AnimationPointsTypes.get_collision_surface_points "csc.tools.AnimationPointsTypes.get_collision_surface_points")(self) | Dict[frame number, set of points] |
    | [`get_fixed_floor_points`](../csc.html#csc.tools.AnimationPointsTypes.get_fixed_floor_points "csc.tools.AnimationPointsTypes.get_fixed_floor_points")(self) | Dict[frame number, set of points] |
    | [`get_fixed_points`](../csc.html#csc.tools.AnimationPointsTypes.get_fixed_points "csc.tools.AnimationPointsTypes.get_fixed_points")(self) | Dict[frame number, set of points] |
    | [`get_frame_collision_info_points`](../csc.html#csc.tools.AnimationPointsTypes.get_frame_collision_info_points "csc.tools.AnimationPointsTypes.get_frame_collision_info_points")(self) | Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]] |
    | [`get_fulcrum_floor_points`](../csc.html#csc.tools.AnimationPointsTypes.get_fulcrum_floor_points "csc.tools.AnimationPointsTypes.get_fulcrum_floor_points")(self) | Dict[frame number, set of points] |
    | [`get_fulcrum_points`](../csc.html#csc.tools.AnimationPointsTypes.get_fulcrum_points "csc.tools.AnimationPointsTypes.get_fulcrum_points")(self) | Dict[frame number, set of points] |
    | [`get_local_fixed_points`](../csc.html#csc.tools.AnimationPointsTypes.get_local_fixed_points "csc.tools.AnimationPointsTypes.get_local_fixed_points")(self) | Dict[frame number, set of points] |

    \_\_annotations\_\_ *= {}*[??](#csc.tools.AnimationPointsTypes.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg2: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg3: [csc.tools.StaticPointsTypes](../csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.AnimationPointsTypes.__module__ "Permalink to this definition")

    get\_collision\_fixed\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_collision_fixed_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_collision\_pin\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_collision_pin_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_collision\_surface\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_collision_surface_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_fixed\_floor\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fixed_floor_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_fixed\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fixed_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_frame\_collision\_info\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  dict[int, dict[csc.model.ObjectId, domain::scene::collision::CollisionInfoForPoint]][??](#csc.tools.AnimationPointsTypes.get_frame_collision_info_points "Permalink to this definition")
    :   Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]]

    get\_fulcrum\_floor\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fulcrum_floor_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_fulcrum\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fulcrum_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_local\_fixed\_points(*self: [csc.tools.AnimationPointsTypes](../csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_local_fixed_points "Permalink to this definition")
    :   Dict[frame number, set of points]