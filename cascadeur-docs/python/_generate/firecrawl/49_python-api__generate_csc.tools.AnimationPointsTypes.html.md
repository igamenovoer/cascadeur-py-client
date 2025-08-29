# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html

# csc.tools.AnimationPointsTypes [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html\#csc-tools-animationpointstypes "Permalink to this heading")

_class_ csc.tools.AnimationPointsTypes [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes "Permalink to this definition")

Class of basic types of points which physics tools and change through animation
for target center of mass it contains

get\_fulcrum\_points – all fulcrum point with collision
get\_fixed\_points – all points need to fix with collision
get\_local\_fixed\_points – points that should keep local coordinates after apply
get\_collision\_surface\_points – collision points with normal type
get\_collision\_pin\_points – collision points with pin type
get\_collision\_fixed\_points – collision points with fulcrum groups
get\_fulcrum\_floor\_points – points collide with only floor
get\_fixed\_floor\_points – points collide with only floor and fulcrum groups
get\_frame\_collision\_info\_points – collision info about points

\_\_init\_\_( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg2:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg3:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.__init__ "csc.tools.AnimationPointsTypes.__init__")(self, arg0, arg1, arg2, arg3) |  |
| [`get_collision_fixed_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_collision_fixed_points "csc.tools.AnimationPointsTypes.get_collision_fixed_points")(self) | Dict\[frame number, set of points\] |
| [`get_collision_pin_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_collision_pin_points "csc.tools.AnimationPointsTypes.get_collision_pin_points")(self) | Dict\[frame number, set of points\] |
| [`get_collision_surface_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_collision_surface_points "csc.tools.AnimationPointsTypes.get_collision_surface_points")(self) | Dict\[frame number, set of points\] |
| [`get_fixed_floor_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fixed_floor_points "csc.tools.AnimationPointsTypes.get_fixed_floor_points")(self) | Dict\[frame number, set of points\] |
| [`get_fixed_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fixed_points "csc.tools.AnimationPointsTypes.get_fixed_points")(self) | Dict\[frame number, set of points\] |
| [`get_frame_collision_info_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_frame_collision_info_points "csc.tools.AnimationPointsTypes.get_frame_collision_info_points")(self) | Dict\[frame number, Dict\[csc.model.ObjectId, CollisionInfoForPoint\]\] |
| [`get_fulcrum_floor_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fulcrum_floor_points "csc.tools.AnimationPointsTypes.get_fulcrum_floor_points")(self) | Dict\[frame number, set of points\] |
| [`get_fulcrum_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fulcrum_points "csc.tools.AnimationPointsTypes.get_fulcrum_points")(self) | Dict\[frame number, set of points\] |
| [`get_local_fixed_points`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_local_fixed_points "csc.tools.AnimationPointsTypes.get_local_fixed_points")(self) | Dict\[frame number, set of points\] |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg2:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg3:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.__module__ "Permalink to this definition")get\_collision\_fixed\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_collision_fixed_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_collision\_pin\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_collision_pin_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_collision\_surface\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_collision_surface_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_fixed\_floor\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_fixed_floor_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_fixed\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_fixed_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_frame\_collision\_info\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→dict\[int,dict\[csc.model.ObjectId,domain::scene::collision::CollisionInfoForPoint\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_frame_collision_info_points "Permalink to this definition")

Dict\[frame number, Dict\[csc.model.ObjectId, CollisionInfoForPoint\]\]

get\_fulcrum\_floor\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_fulcrum_floor_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_fulcrum\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_fulcrum_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_local\_fixed\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html#csc.tools.AnimationPointsTypes.get_local_fixed_points "Permalink to this definition")

Dict\[frame number, set of points\]