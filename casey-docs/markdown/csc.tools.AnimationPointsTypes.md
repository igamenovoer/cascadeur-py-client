---
source_url: https://cascadeur.com/python-api/_generate/csc.tools.AnimationPointsTypes.html
html_file: b82f7f9b7684692252366af89009e4fe.html
module: csc.tools.AnimationPointsTypes
---

# csc.tools.AnimationPointsTypes 

Class of basic types of points which physics tools and change through animation
for target center of mass it contains get_fulcrum_points – all fulcrum point with collision
get_fixed_points – all points need to fix with collision
get_local_fixed_points – points that should keep local coordinates after apply
get_collision_surface_points – collision points with normal type
get_collision_pin_points – collision points with pin type
get_collision_fixed_points – collision points with fulcrum groups
get_fulcrum_floor_points – points collide with only floor
get_fixed_floor_points – points collide with only floor and fulcrum groups
get_frame_collision_info_points – collision info about points Methods __init__ (self, arg0, arg1, arg2, arg3) get_collision_fixed_points (self) Dict[frame number, set of points] get_collision_pin_points (self) Dict[frame number, set of points] get_collision_surface_points (self) Dict[frame number, set of points] get_fixed_floor_points (self) Dict[frame number, set of points] get_fixed_points (self) Dict[frame number, set of points] get_frame_collision_info_points (self) Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]] get_fulcrum_floor_points (self) Dict[frame number, set of points] get_fulcrum_points (self) Dict[frame number, set of points] get_local_fixed_points (self) Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points]