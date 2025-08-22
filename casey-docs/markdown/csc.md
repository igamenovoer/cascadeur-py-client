---
source_url: https://cascadeur.com/python-api/csc.html
html_file: 60c8cf5e3e5950beaef8ff0a113d9830.html
module: csc
---

# CSC[??](#module-csc "Permalink to this heading")

## csc The main Cascadeur python module.[??](#csc-the-main-cascadeur-python-module "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.Guid`](#csc.Guid "csc.Guid") |  |
| [`csc.math.Quaternion`](#csc.math.Quaternion "csc.math.Quaternion") | Quaternion class |
| [`csc.math.Rotation`](#csc.math.Rotation "csc.math.Rotation") | Rotation class |
| [`csc.math.transform_point`](#csc.math.transform_point "csc.math.transform_point")(\*args,??\*\*kwargs) | Overloaded function. |
| [`csc.math.inverse_transform_point`](#csc.math.inverse_transform_point "csc.math.inverse_transform_point")(transform,??...) | -> Vector3f |
| [`csc.math.basic_transform_from_triangle`](#csc.math.basic_transform_from_triangle "csc.math.basic_transform_from_triangle")(triangle) | -> csc.math.OrthogonalTransform |
| [`csc.math.project_point_on_basic_line`](#csc.math.project_point_on_basic_line "csc.math.project_point_on_basic_line")(...) | -> Vector3f |
| [`csc.math.euler_angles_to_quaternion_x_y_z`](#csc.math.euler_angles_to_quaternion_x_y_z "csc.math.euler_angles_to_quaternion_x_y_z")(...) | -> Quaternionf |
| [`csc.math.modify_position_by_matrix`](#csc.math.modify_position_by_matrix "csc.math.modify_position_by_matrix")(matrix,??...) | -> Vector3f |
| [`csc.math.transforms_difference`](#csc.math.transforms_difference "csc.math.transforms_difference")(...) | -> csc.math.OrthogonalTransform |
| [`csc.math.transform_point`](#csc.math.transform_point "csc.math.transform_point")(\*args,??\*\*kwargs) | Overloaded function. |
| [`csc.math.get_m3f_diag`](#csc.math.get_m3f_diag "csc.math.get_m3f_diag")(matrix) | -> Vector3f |
| [`csc.physics.PosMass`](#csc.physics.PosMass "csc.physics.PosMass") | PosMass class |
| [`csc.physics.inertia_tensor`](#csc.physics.inertia_tensor "csc.physics.inertia_tensor")(mass\_and\_poses,??...) | -> Matrix3f |
| [`csc.DirectionValue`](#csc.DirectionValue "csc.DirectionValue") | DirectionValue enumeration |
| [`csc.Direction`](#csc.Direction "csc.Direction") | Direction class Implements direction. |
| [`csc.Version`](#csc.Version "csc.Version") | Version class |
| [`csc.SystemVariables`](#csc.SystemVariables "csc.SystemVariables") |  |
| [`csc.math.ScaledTransform`](#csc.math.ScaledTransform "csc.math.ScaledTransform") | ScaledTransform class |
| [`csc.math.OrthogonalTransform`](#csc.math.OrthogonalTransform "csc.math.OrthogonalTransform") | OrthogonalTransform class |
| [`csc.math.Triangle`](#csc.math.Triangle "csc.math.Triangle") | Triangle class |
| [`csc.math.SizesInterval`](#csc.math.SizesInterval "csc.math.SizesInterval") | SizesInterval class |
| [`csc.parts.Type`](#csc.parts.Type "csc.parts.Type") | Type of the parts, enum |
| [`csc.parts.Info`](#csc.parts.Info "csc.parts.Info") | Info class |
| [`csc.parts.GroupInfo`](#csc.parts.GroupInfo "csc.parts.GroupInfo") | GroupInfo class |
| [`csc.parts.Buffer`](#csc.parts.Buffer "csc.parts.Buffer") | Buffer class |

*class* csc.Direction[??](#csc.Direction "Permalink to this definition")
:   Direction class
    Implements direction.

    Parameters:
    :   **value** ([*csc.DirectionValue*](#csc.DirectionValue "csc.DirectionValue")) ???

    \_\_annotations\_\_ *= {}*[??](#csc.Direction.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: csc.Direction*, *value: csc.DirectionValue = <DirectionValue.Unknown: 2>*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.Direction.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc'*[??](#csc.Direction.__module__ "Permalink to this definition")

    inverse(*self: [csc.Direction](#csc.Direction "csc.Direction")*)  [csc.DirectionValue](#csc.DirectionValue "csc.DirectionValue")[??](#csc.Direction.inverse "Permalink to this definition")

    to\_string(*self: [csc.Direction](#csc.Direction "csc.Direction")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.Direction.to_string "Permalink to this definition")

    value(*self: [csc.Direction](#csc.Direction "csc.Direction")*)  [csc.DirectionValue](#csc.DirectionValue "csc.DirectionValue")[??](#csc.Direction.value "Permalink to this definition")

*class* csc.DirectionValue[??](#csc.DirectionValue "Permalink to this definition")
:   > DirectionValue enumeration
    > In, Out, Unknown

    Members:

    > In
    >
    > Out
    >
    > Unknown

    In *= <DirectionValue.In: 0>*[??](#csc.DirectionValue.In "Permalink to this definition")

    Out *= <DirectionValue.Out: 1>*[??](#csc.DirectionValue.Out "Permalink to this definition")

    Unknown *= <DirectionValue.Unknown: 2>*[??](#csc.DirectionValue.Unknown "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.DirectionValue.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.DirectionValue.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.DirectionValue.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.DirectionValue.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.DirectionValue](#csc.DirectionValue "csc.DirectionValue")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.DirectionValue.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.DirectionValue](#csc.DirectionValue "csc.DirectionValue")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.DirectionValue.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.DirectionValue](#csc.DirectionValue "csc.DirectionValue")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.DirectionValue.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'In': <DirectionValue.In: 0>, 'Out': <DirectionValue.Out: 1>, 'Unknown': <DirectionValue.Unknown: 2>}*[??](#csc.DirectionValue.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc'*[??](#csc.DirectionValue.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.DirectionValue.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.DirectionValue.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.DirectionValue](#csc.DirectionValue "csc.DirectionValue")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.DirectionValue.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.DirectionValue.__str__ "Permalink to this definition")

    *property* name[??](#csc.DirectionValue.name "Permalink to this definition")

    *property* value[??](#csc.DirectionValue.value "Permalink to this definition")

*class* csc.Guid[??](#csc.Guid "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.Guid.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.Guid](#csc.Guid "csc.Guid")*, *arg0: [csc.Guid](#csc.Guid "csc.Guid")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.Guid.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.Guid](#csc.Guid "csc.Guid")*, *arg0: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.Guid.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.Guid](#csc.Guid "csc.Guid")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.Guid.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.Guid.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.Guid, arg0: str) -> None
        2. \_\_init\_\_(self: csc.Guid) -> None

    \_\_module\_\_ *= 'csc'*[??](#csc.Guid.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.Guid](#csc.Guid "csc.Guid")*, *arg0: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.Guid.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.Guid](#csc.Guid "csc.Guid")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.Guid.__str__ "Permalink to this definition")

    is\_null(*self: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.Guid.is_null "Permalink to this definition")

    *static* null()  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.Guid.null "Permalink to this definition")

    to\_string(*self: [csc.Guid](#csc.Guid "csc.Guid")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.Guid.to_string "Permalink to this definition")

*class* csc.SystemVariables[??](#csc.SystemVariables "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.SystemVariables.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.SystemVariables.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc'*[??](#csc.SystemVariables.__module__ "Permalink to this definition")

    *static* git\_count()  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.SystemVariables.git_count "Permalink to this definition")

    *static* git\_date()  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.SystemVariables.git_date "Permalink to this definition")

    *static* git\_sha()  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.SystemVariables.git_sha "Permalink to this definition")

    *static* git\_version()  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.SystemVariables.git_version "Permalink to this definition")

*class* csc.Version[??](#csc.Version "Permalink to this definition")
:   Version class

    Implements Version.

    Variables:
    :   * **major** ??? Get set int
        * **minor** ??? Get set int
        * **patch** ??? Get set int

    \_\_annotations\_\_ *= {}*[??](#csc.Version.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.Version](#csc.Version "csc.Version")*, *arg0: [csc.Version](#csc.Version "csc.Version")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.Version.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.Version](#csc.Version "csc.Version")*, *arg0: [csc.Version](#csc.Version "csc.Version")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.Version.__eq__ "Permalink to this definition")

    \_\_hash\_\_ *= None*[??](#csc.Version.__hash__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.Version](#csc.Version "csc.Version")*, *major: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *minor: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *patch: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.Version.__init__ "Permalink to this definition")

    \_\_lt\_\_(*self: [csc.Version](#csc.Version "csc.Version")*, *arg0: [csc.Version](#csc.Version "csc.Version")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.Version.__lt__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc'*[??](#csc.Version.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.Version](#csc.Version "csc.Version")*, *arg0: [csc.Version](#csc.Version "csc.Version")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.Version.__ne__ "Permalink to this definition")

    *static* from\_string(*arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.Version](#csc.Version "csc.Version")[??](#csc.Version.from_string "Permalink to this definition")

    *property* major[??](#csc.Version.major "Permalink to this definition")

    *property* minor[??](#csc.Version.minor "Permalink to this definition")

    *property* patch[??](#csc.Version.patch "Permalink to this definition")

    to\_string(*self: [csc.Version](#csc.Version "csc.Version")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.Version.to_string "Permalink to this definition")

csc.get\_meaningful\_list()  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]][??](#csc.get_meaningful_list "Permalink to this definition")

## csc.tools The Cascadeur python module provides tools.[??](#module-csc.tools "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.tools.ActivateDeactivate`](#csc.tools.ActivateDeactivate "csc.tools.ActivateDeactivate") | ActivateDeactivate class |
| [`csc.tools.selection.Mode`](#csc.tools.selection.Mode "csc.tools.selection.Mode") | Mode enumeration |
| [`csc.tools.selection.Group`](#csc.tools.selection.Group "csc.tools.selection.Group") | Group class |
| [`csc.tools.selection.Core`](#csc.tools.selection.Core "csc.tools.selection.Core") | Core class |
| [`csc.tools.SelectionGroups`](#csc.tools.SelectionGroups "csc.tools.SelectionGroups") | SelectionGroups class |
| [`csc.tools.mirror.Core`](#csc.tools.mirror.Core "csc.tools.mirror.Core") | Mirror tool core class |
| [`csc.tools.MirrorTool`](#csc.tools.MirrorTool "csc.tools.MirrorTool") | Mirror tool class |
| [`csc.tools.JointData`](#csc.tools.JointData "csc.tools.JointData") |  |
| [`csc.tools.ObjectKey`](#csc.tools.ObjectKey "csc.tools.ObjectKey") |  |
| [`csc.tools.DataKey`](#csc.tools.DataKey "csc.tools.DataKey") |  |
| [`csc.tools.RiggingModeTool`](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool") | Rigging mode tool class |
| [`csc.tools.attractor.SpaceMode`](#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode") | attractor::Mode enum |
| [`csc.tools.attractor.ArgsMode`](#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode") | attractor::Mode enum |
| [`csc.tools.attractor.GSRotationAxis`](#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.GSAxisFlag`](#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.GSAxisIndex`](#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.GSPhysicsType`](#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.AttractorGeneralSettings`](#csc.tools.attractor.AttractorGeneralSettings "csc.tools.attractor.AttractorGeneralSettings") |  |
| [`csc.tools.attractor.Args`](#csc.tools.attractor.Args "csc.tools.attractor.Args") |  |
| [`csc.tools.attractor.attract`](#csc.tools.attractor.attract "csc.tools.attractor.attract")(args) |  |
| [`csc.tools.AttractorTool`](#csc.tools.AttractorTool "csc.tools.AttractorTool") | Attractor tool class |
| [`csc.tools.AutoPhysicTool`](#csc.tools.AutoPhysicTool "csc.tools.AutoPhysicTool") | Auto physics tool class |
| [`csc.tools.AnimationPointsTypes`](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes") | Class of basic types of points which physics tools and change through animation for target center of mass it contains |
| [`csc.tools.CollisionInfoForPoint`](#csc.tools.CollisionInfoForPoint "csc.tools.CollisionInfoForPoint") | Structure with which the point collides. |
| [`csc.tools.BallisticTrajectory`](#csc.tools.BallisticTrajectory "csc.tools.BallisticTrajectory") | BallisticTrajectory class |
| [`csc.tools.Trajectory`](#csc.tools.Trajectory "csc.tools.Trajectory") | Trajectory class |
| [`csc.tools.AutoPosingTool`](#csc.tools.AutoPosingTool "csc.tools.AutoPosingTool") | AutoPosingTool class |
| [`csc.tools.AnimationUnbakingTool`](#csc.tools.AnimationUnbakingTool "csc.tools.AnimationUnbakingTool") | AnimationUnbakingTool class |
| [`csc.tools.RenderParameters`](#csc.tools.RenderParameters "csc.tools.RenderParameters") | Parameters for rendering |
| [`csc.tools.RenderToFile`](#csc.tools.RenderToFile "csc.tools.RenderToFile") | Render to file tool class |

*class* csc.tools.ActivateDeactivate[??](#csc.tools.ActivateDeactivate "Permalink to this definition")
:   ActivateDeactivate class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.ActivateDeactivate.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.ActivateDeactivate.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.ActivateDeactivate.__module__ "Permalink to this definition")

    activate(*self: [csc.tools.ActivateDeactivate](#csc.tools.ActivateDeactivate "csc.tools.ActivateDeactivate")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId"), [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.ActivateDeactivate.activate "Permalink to this definition")

    deactivate(*self: [csc.tools.ActivateDeactivate](#csc.tools.ActivateDeactivate "csc.tools.ActivateDeactivate")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.ActivateDeactivate.deactivate "Permalink to this definition")

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

    \_\_annotations\_\_ *= {}*[??](#csc.tools.AnimationPointsTypes.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg2: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg3: [csc.tools.StaticPointsTypes](#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.AnimationPointsTypes.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.AnimationPointsTypes.__module__ "Permalink to this definition")

    get\_collision\_fixed\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_collision_fixed_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_collision\_pin\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_collision_pin_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_collision\_surface\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_collision_surface_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_fixed\_floor\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fixed_floor_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_fixed\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fixed_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_frame\_collision\_info\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  dict[int, dict[csc.model.ObjectId, domain::scene::collision::CollisionInfoForPoint]][??](#csc.tools.AnimationPointsTypes.get_frame_collision_info_points "Permalink to this definition")
    :   Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]]

    get\_fulcrum\_floor\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fulcrum_floor_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_fulcrum\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_fulcrum_points "Permalink to this definition")
    :   Dict[frame number, set of points]

    get\_local\_fixed\_points(*self: [csc.tools.AnimationPointsTypes](#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.AnimationPointsTypes.get_local_fixed_points "Permalink to this definition")
    :   Dict[frame number, set of points]

*class* csc.tools.AnimationUnbakingTool[??](#csc.tools.AnimationUnbakingTool "Permalink to this definition")
:   AnimationUnbakingTool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.AnimationUnbakingTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.AnimationUnbakingTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.AnimationUnbakingTool.__module__ "Permalink to this definition")

    get\_interpolation\_difference(*self: [csc.tools.AnimationUnbakingTool](#csc.tools.AnimationUnbakingTool "csc.tools.AnimationUnbakingTool")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.tools.AnimationUnbakingTool.get_interpolation_difference "Permalink to this definition")

*class* csc.tools.AttractorTool[??](#csc.tools.AttractorTool "Permalink to this definition")
:   Attractor tool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.AttractorTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.AttractorTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.AttractorTool.__module__ "Permalink to this definition")

    get\_general\_settings(*self: [csc.tools.AttractorTool](#csc.tools.AttractorTool "csc.tools.AttractorTool")*)  [csc.tools.attractor.AttractorGeneralSettings](#csc.tools.attractor.AttractorGeneralSettings "csc.tools.attractor.AttractorGeneralSettings")[??](#csc.tools.AttractorTool.get_general_settings "Permalink to this definition")

    is\_only\_key\_frames(*self: [csc.tools.AttractorTool](#csc.tools.AttractorTool "csc.tools.AttractorTool")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.AttractorTool.is_only_key_frames "Permalink to this definition")

*class* csc.tools.AutoPhysicTool[??](#csc.tools.AutoPhysicTool "Permalink to this definition")
:   Auto physics tool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.AutoPhysicTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.AutoPhysicTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.AutoPhysicTool.__module__ "Permalink to this definition")

    turn\_off(*self: [csc.tools.AutoPhysicTool](#csc.tools.AutoPhysicTool "csc.tools.AutoPhysicTool")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.AutoPhysicTool.turn_off "Permalink to this definition")

    turn\_off\_all\_fulcrum\_points(*self: [csc.tools.AutoPhysicTool](#csc.tools.AutoPhysicTool "csc.tools.AutoPhysicTool")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.AutoPhysicTool.turn_off_all_fulcrum_points "Permalink to this definition")

*class* csc.tools.AutoPosingTool[??](#csc.tools.AutoPosingTool "Permalink to this definition")
:   AutoPosingTool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.AutoPosingTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.AutoPosingTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.AutoPosingTool.__module__ "Permalink to this definition")

    add(*self: [csc.tools.AutoPosingTool](#csc.tools.AutoPosingTool "csc.tools.AutoPosingTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.AutoPosingTool.add "Permalink to this definition")

    update(*self: [csc.tools.AutoPosingTool](#csc.tools.AutoPosingTool "csc.tools.AutoPosingTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.AutoPosingTool.update "Permalink to this definition")

*class* csc.tools.BallisticTrajectory[??](#csc.tools.BallisticTrajectory "Permalink to this definition")
:   BallisticTrajectory class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.BallisticTrajectory.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.BallisticTrajectory.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.BallisticTrajectory.__module__ "Permalink to this definition")

*class* csc.tools.CollisionInfoForPoint[??](#csc.tools.CollisionInfoForPoint "Permalink to this definition")
:   Structure with which the point collides.
    When used, it is assumed that the normal goes from other to point.

    \_\_annotations\_\_ *= {}*[??](#csc.tools.CollisionInfoForPoint.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.CollisionInfoForPoint.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.CollisionInfoForPoint.__module__ "Permalink to this definition")

    *property* normal[??](#csc.tools.CollisionInfoForPoint.normal "Permalink to this definition")
    :   Vector3d

    *property* other[??](#csc.tools.CollisionInfoForPoint.other "Permalink to this definition")
    :   csc.model.ObjectId

    *property* penetration\_depth[??](#csc.tools.CollisionInfoForPoint.penetration_depth "Permalink to this definition")
    :   double

    *property* pos[??](#csc.tools.CollisionInfoForPoint.pos "Permalink to this definition")
    :   Vector3d

*class* csc.tools.DataKey[??](#csc.tools.DataKey "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.tools.DataKey.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey")*, *arg0: [csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.DataKey.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.DataKey.__hash__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.DataKey.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.DataKey.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey")*, *arg0: [csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.DataKey.__ne__ "Permalink to this definition")

    *property* data\_name[??](#csc.tools.DataKey.data_name "Permalink to this definition")

    *property* object\_key[??](#csc.tools.DataKey.object_key "Permalink to this definition")

*class* csc.tools.JointData[??](#csc.tools.JointData "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.tools.JointData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.JointData](#csc.tools.JointData "csc.tools.JointData")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.JointData.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.JointData.__module__ "Permalink to this definition")

    *property* local\_position[??](#csc.tools.JointData.local_position "Permalink to this definition")

    *property* local\_rotation[??](#csc.tools.JointData.local_rotation "Permalink to this definition")

    *property* local\_scale[??](#csc.tools.JointData.local_scale "Permalink to this definition")

    *property* visibility[??](#csc.tools.JointData.visibility "Permalink to this definition")

*class* csc.tools.MirrorTool[??](#csc.tools.MirrorTool "Permalink to this definition")
:   Mirror tool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.MirrorTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.MirrorTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.MirrorTool.__module__ "Permalink to this definition")

    core(*self: [csc.tools.MirrorTool](#csc.tools.MirrorTool "csc.tools.MirrorTool")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.tools.MirrorTool.core "Permalink to this definition")

*class* csc.tools.ObjectKey[??](#csc.tools.ObjectKey "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.tools.ObjectKey.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.tools.ObjectKey](#csc.tools.ObjectKey "csc.tools.ObjectKey")*, *arg0: [csc.tools.ObjectKey](#csc.tools.ObjectKey "csc.tools.ObjectKey")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.ObjectKey.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.tools.ObjectKey](#csc.tools.ObjectKey "csc.tools.ObjectKey")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.ObjectKey.__hash__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.ObjectKey](#csc.tools.ObjectKey "csc.tools.ObjectKey")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.ObjectKey.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.ObjectKey.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.tools.ObjectKey](#csc.tools.ObjectKey "csc.tools.ObjectKey")*, *arg0: [csc.tools.ObjectKey](#csc.tools.ObjectKey "csc.tools.ObjectKey")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.ObjectKey.__ne__ "Permalink to this definition")

    *property* behaviour\_name[??](#csc.tools.ObjectKey.behaviour_name "Permalink to this definition")

    *property* path\_name[??](#csc.tools.ObjectKey.path_name "Permalink to this definition")

*class* csc.tools.RenderParameters[??](#csc.tools.RenderParameters "Permalink to this definition")
:   Parameters for rendering

    \_\_annotations\_\_ *= {}*[??](#csc.tools.RenderParameters.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.RenderParameters](#csc.tools.RenderParameters "csc.tools.RenderParameters")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RenderParameters.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.RenderParameters.__module__ "Permalink to this definition")

    *property* height[??](#csc.tools.RenderParameters.height "Permalink to this definition")

    *property* samples[??](#csc.tools.RenderParameters.samples "Permalink to this definition")

    *property* width[??](#csc.tools.RenderParameters.width "Permalink to this definition")

*class* csc.tools.RenderToFile[??](#csc.tools.RenderToFile "Permalink to this definition")
:   Render to file tool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.RenderToFile.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.RenderToFile.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.RenderToFile.__module__ "Permalink to this definition")

    play\_to\_images\_sequence(*self: [csc.tools.RenderToFile](#csc.tools.RenderToFile "csc.tools.RenderToFile")*, *scene\_view: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *render\_parameters: [csc.tools.RenderParameters](#csc.tools.RenderParameters "csc.tools.RenderParameters")*, *folder\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RenderToFile.play_to_images_sequence "Permalink to this definition")

    play\_to\_video\_file(*self: [csc.tools.RenderToFile](#csc.tools.RenderToFile "csc.tools.RenderToFile")*, *scene\_view: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *render\_parameters: [csc.tools.RenderParameters](#csc.tools.RenderParameters "csc.tools.RenderParameters")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RenderToFile.play_to_video_file "Permalink to this definition")

    take\_image(*self: [csc.tools.RenderToFile](#csc.tools.RenderToFile "csc.tools.RenderToFile")*, *scene\_view: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *render\_parameters: [csc.tools.RenderParameters](#csc.tools.RenderParameters "csc.tools.RenderParameters")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RenderToFile.take_image "Permalink to this definition")

*class* csc.tools.RiggingModeTool[??](#csc.tools.RiggingModeTool "Permalink to this definition")
:   Rigging mode tool class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.RiggingModeTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.RiggingModeTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.RiggingModeTool.__module__ "Permalink to this definition")

    erase\_joints\_data(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.erase_joints_data "Permalink to this definition")

    erase\_layer\_id\_by\_object\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.erase_layer_id_by_object_ids "Permalink to this definition")

    erase\_layers\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.erase_layers_ids "Permalink to this definition")

    erase\_preserved\_data(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.erase_preserved_data "Permalink to this definition")

    erase\_preserved\_object\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.erase_preserved_object_ids "Permalink to this definition")

    erase\_preserved\_setting(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.erase_preserved_setting "Permalink to this definition")

    get\_joints\_data(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.tools.JointData](#csc.tools.JointData "csc.tools.JointData")]][??](#csc.tools.RiggingModeTool.get_joints_data "Permalink to this definition")

    get\_layer\_id\_by\_object\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]][??](#csc.tools.RiggingModeTool.get_layer_id_by_object_ids "Permalink to this definition")

    get\_layers\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.tools.RiggingModeTool.get_layers_ids "Permalink to this definition")

    get\_preserved\_data(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]]]][??](#csc.tools.RiggingModeTool.get_preserved_data "Permalink to this definition")

    get\_preserved\_object\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.PathName](#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.tools.RiggingModeTool.get_preserved_object_ids "Permalink to this definition")

    get\_preserved\_setting(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")]][??](#csc.tools.RiggingModeTool.get_preserved_setting "Permalink to this definition")

    set\_joints\_data(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.tools.JointData](#csc.tools.JointData "csc.tools.JointData")]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.set_joints_data "Permalink to this definition")

    set\_layers\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.set_layers_ids "Permalink to this definition")

    set\_preserved\_data(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]]]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.set_preserved_data "Permalink to this definition")

    set\_preserved\_object\_ids(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.PathName](#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.set_preserved_object_ids "Permalink to this definition")

    set\_preserved\_setting(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.tools.DataKey](#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.set_preserved_setting "Permalink to this definition")

    set\_undo\_redo\_context(*self: [csc.tools.RiggingModeTool](#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")*, *arg0: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *arg1: Callable*, *arg2: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *arg3: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingModeTool.set_undo_redo_context "Permalink to this definition")

*class* csc.tools.RiggingWindow[??](#csc.tools.RiggingWindow "Permalink to this definition")
:   SelectionGroups class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.RiggingWindow.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.RiggingWindow.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.RiggingWindow.__module__ "Permalink to this definition")

    create\_from\_qrt\_by\_content(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.create_from_qrt_by_content "Permalink to this definition")

    create\_from\_qrt\_by\_fileName(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.create_from_qrt_by_fileName "Permalink to this definition")

    generate\_rig\_elements(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.generate_rig_elements "Permalink to this definition")

    get\_character\_mirror\_plane(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.RiggingWindow.get_character_mirror_plane "Permalink to this definition")

    get\_is\_create\_autoposing(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.RiggingWindow.get_is_create_autoposing "Permalink to this definition")

    get\_template\_from\_qrt(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.RiggingWindow.get_template_from_qrt "Permalink to this definition")

    is\_create\_qrt(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.RiggingWindow.is_create_qrt "Permalink to this definition")

    load\_template\_by\_content(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.load_template_by_content "Permalink to this definition")

    load\_template\_by\_fileName(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.load_template_by_fileName "Permalink to this definition")

    open\_quick\_rigging\_tool(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.open_quick_rigging_tool "Permalink to this definition")

    set\_axis\_after\_qrt(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *axis: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.set_axis_after_qrt "Permalink to this definition")

    set\_character\_mirror\_plane(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *plane: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.set_character_mirror_plane "Permalink to this definition")

    set\_is\_create\_autoposing(*self: [csc.tools.RiggingWindow](#csc.tools.RiggingWindow "csc.tools.RiggingWindow")*, *on: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.RiggingWindow.set_is_create_autoposing "Permalink to this definition")

*class* csc.tools.SelectionGroups[??](#csc.tools.SelectionGroups "Permalink to this definition")
:   SelectionGroups class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.SelectionGroups.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.SelectionGroups.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.SelectionGroups.__module__ "Permalink to this definition")

    core(*self: [csc.tools.SelectionGroups](#csc.tools.SelectionGroups "csc.tools.SelectionGroups")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.tools.SelectionGroups.core "Permalink to this definition")

    import\_file(*self: [csc.tools.SelectionGroups](#csc.tools.SelectionGroups "csc.tools.SelectionGroups")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.SelectionGroups.import_file "Permalink to this definition")

*class* csc.tools.StaticPointsTypes[??](#csc.tools.StaticPointsTypes "Permalink to this definition")
:   Class of basic types of points which physics tools use and dont change through animation
    for target center of mass it contains

    get\_main\_points ??? all points that can be associated with center of mass
    get\_direction\_controllers ??? all direction controller associated with center of mass
    get\_interpolation\_group ??? all points that should be interpolated and use instead direction controller in apply

    \_\_annotations\_\_ *= {}*[??](#csc.tools.StaticPointsTypes.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.StaticPointsTypes](#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*, *arg0: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg1: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.StaticPointsTypes.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.StaticPointsTypes.__module__ "Permalink to this definition")

    get\_direction\_controllers(*self: [csc.tools.StaticPointsTypes](#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.tools.StaticPointsTypes.get_direction_controllers "Permalink to this definition")
    :   set[ModelId]

    get\_interpolation\_group(*self: [csc.tools.StaticPointsTypes](#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.tools.StaticPointsTypes.get_interpolation_group "Permalink to this definition")
    :   set[ModelId]

    get\_main\_points(*self: [csc.tools.StaticPointsTypes](#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.tools.StaticPointsTypes.get_main_points "Permalink to this definition")
    :   set[ModelId]

*class* csc.tools.Trajectory[??](#csc.tools.Trajectory "Permalink to this definition")
:   Trajectory class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.Trajectory.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.Trajectory.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools'*[??](#csc.tools.Trajectory.__module__ "Permalink to this definition")

*class* csc.tools.selection.Core[??](#csc.tools.selection.Core "Permalink to this definition")
:   Core class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.selection.Core.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.selection.Core.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.selection'*[??](#csc.tools.selection.Core.__module__ "Permalink to this definition")

    get\_group(*self: [csc.tools.selection.Core](#csc.tools.selection.Core "csc.tools.selection.Core")*, *idx: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.tools.selection.Group](#csc.tools.selection.Group "csc.tools.selection.Group")[??](#csc.tools.selection.Core.get_group "Permalink to this definition")
    :   pbdoc( -> Group )pbdoc

    get\_groups(*self: [csc.tools.selection.Core](#csc.tools.selection.Core "csc.tools.selection.Core")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [csc.tools.selection.Group](#csc.tools.selection.Group "csc.tools.selection.Group")][??](#csc.tools.selection.Core.get_groups "Permalink to this definition")
    :   pbdoc( -> std::map<GroupIndex, Group> )pbdoc

    process(*self: [csc.tools.selection.Core](#csc.tools.selection.Core "csc.tools.selection.Core")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *mode: [csc.tools.selection.Mode](#csc.tools.selection.Mode "csc.tools.selection.Mode")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.selection.Core.process "Permalink to this definition")

    set\_group(*self: [csc.tools.selection.Core](#csc.tools.selection.Core "csc.tools.selection.Core")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *group: [csc.tools.selection.Group](#csc.tools.selection.Group "csc.tools.selection.Group")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.selection.Core.set_group "Permalink to this definition")

    set\_groups(*self: [csc.tools.selection.Core](#csc.tools.selection.Core "csc.tools.selection.Core")*, *groups: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [csc.tools.selection.Group](#csc.tools.selection.Group "csc.tools.selection.Group")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.selection.Core.set_groups "Permalink to this definition")

*class* csc.tools.selection.Group[??](#csc.tools.selection.Group "Permalink to this definition")
:   Group class

    Variables:
    :   * **objects** ??? std::set<ModelObjectId>
        * **pivot** ??? ModelObjectId

    \_\_annotations\_\_ *= {}*[??](#csc.tools.selection.Group.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.selection.Group.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.tools.selection.Group) -> None
        2. \_\_init\_\_(self: csc.tools.selection.Group, arg0: set[Union[csc.model.ObjectId, csc.domain.Tool\_object\_id]], arg1: Union[csc.model.ObjectId, csc.domain.Tool\_object\_id]) -> None

    \_\_module\_\_ *= 'csc.tools.selection'*[??](#csc.tools.selection.Group.__module__ "Permalink to this definition")

    *property* objects[??](#csc.tools.selection.Group.objects "Permalink to this definition")

    *property* pivot[??](#csc.tools.selection.Group.pivot "Permalink to this definition")

*class* csc.tools.selection.Mode[??](#csc.tools.selection.Mode "Permalink to this definition")
:   > Mode enumeration
    >
    > SetGroup, SingleSelect, MultiSelect

    Members:

    > SetGroup
    >
    > SingleSelect
    >
    > MultiSelect

    MultiSelect *= <Mode.MultiSelect: 2>*[??](#csc.tools.selection.Mode.MultiSelect "Permalink to this definition")

    SetGroup *= <Mode.SetGroup: 0>*[??](#csc.tools.selection.Mode.SetGroup "Permalink to this definition")

    SingleSelect *= <Mode.SingleSelect: 1>*[??](#csc.tools.selection.Mode.SingleSelect "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.selection.Mode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.selection.Mode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.selection.Mode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.selection.Mode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.selection.Mode](#csc.tools.selection.Mode "csc.tools.selection.Mode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.selection.Mode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.selection.Mode](#csc.tools.selection.Mode "csc.tools.selection.Mode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.selection.Mode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.selection.Mode](#csc.tools.selection.Mode "csc.tools.selection.Mode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.selection.Mode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'MultiSelect': <Mode.MultiSelect: 2>, 'SetGroup': <Mode.SetGroup: 0>, 'SingleSelect': <Mode.SingleSelect: 1>}*[??](#csc.tools.selection.Mode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.selection'*[??](#csc.tools.selection.Mode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.selection.Mode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.selection.Mode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.selection.Mode](#csc.tools.selection.Mode "csc.tools.selection.Mode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.selection.Mode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.selection.Mode.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.selection.Mode.name "Permalink to this definition")

    *property* value[??](#csc.tools.selection.Mode.value "Permalink to this definition")

*class* csc.tools.mirror.Core[??](#csc.tools.mirror.Core "Permalink to this definition")
:   Mirror tool core class

    \_\_annotations\_\_ *= {}*[??](#csc.tools.mirror.Core.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.tools.mirror.Core.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.mirror'*[??](#csc.tools.mirror.Core.__module__ "Permalink to this definition")

    mirror\_frame(*self: [csc.tools.mirror.Core](#csc.tools.mirror.Core "csc.tools.mirror.Core")*, *arg0: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.mirror.Core.mirror_frame "Permalink to this definition")

    mirror\_interval(*self: [csc.tools.mirror.Core](#csc.tools.mirror.Core "csc.tools.mirror.Core")*, *arg0: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.mirror.Core.mirror_interval "Permalink to this definition")

    plane(*self: [csc.tools.mirror.Core](#csc.tools.mirror.Core "csc.tools.mirror.Core")*)  [csc.math.Plane](#csc.math.Plane "csc.math.Plane")[??](#csc.tools.mirror.Core.plane "Permalink to this definition")

    set\_plane(*self: [csc.tools.mirror.Core](#csc.tools.mirror.Core "csc.tools.mirror.Core")*, *plane: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.mirror.Core.set_plane "Permalink to this definition")

*class* csc.tools.attractor.Args[??](#csc.tools.attractor.Args "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.Args.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: csc.tools.attractor.Args*, *scene: csc.domain.Scene*, *gravity: float*, *general\_settings: csc.tools.attractor.AttractorGeneralSettings*, *only\_key\_frames: bool*, *mode: csc.tools.attractor.ArgsMode*, *for\_interval: bool = False*, *hard: bool = False*, *frame\_action\_on\_change: csc.domain.FrameActionOnChange = <FrameActionOnChange.DoNothing: 2>*, *interval\_action\_on\_change: csc.domain.IntervalActionOnChange = <IntervalActionOnChange.Fixing: 0>*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.Args.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.Args.__module__ "Permalink to this definition")

    *property* for\_interval[??](#csc.tools.attractor.Args.for_interval "Permalink to this definition")

    *property* frame\_action\_on\_change[??](#csc.tools.attractor.Args.frame_action_on_change "Permalink to this definition")

    *property* general\_settings[??](#csc.tools.attractor.Args.general_settings "Permalink to this definition")

    *property* interval\_action\_on\_change[??](#csc.tools.attractor.Args.interval_action_on_change "Permalink to this definition")

    *property* mode[??](#csc.tools.attractor.Args.mode "Permalink to this definition")

    *property* only\_key\_frames[??](#csc.tools.attractor.Args.only_key_frames "Permalink to this definition")

*class* csc.tools.attractor.ArgsMode[??](#csc.tools.attractor.ArgsMode "Permalink to this definition")
:   > attractor::Mode enum
    >
    > Previous, Next, Inertial, InverseInertial, Average, Interpolation

    Members:

    > Previous
    >
    > Next
    >
    > Inertial
    >
    > InverseInertial
    >
    > Average
    >
    > Interpolation

    Average *= <ArgsMode.Average: 4>*[??](#csc.tools.attractor.ArgsMode.Average "Permalink to this definition")

    Inertial *= <ArgsMode.Inertial: 2>*[??](#csc.tools.attractor.ArgsMode.Inertial "Permalink to this definition")

    Interpolation *= <ArgsMode.Interpolation: 5>*[??](#csc.tools.attractor.ArgsMode.Interpolation "Permalink to this definition")

    InverseInertial *= <ArgsMode.InverseInertial: 3>*[??](#csc.tools.attractor.ArgsMode.InverseInertial "Permalink to this definition")

    Next *= <ArgsMode.Next: 1>*[??](#csc.tools.attractor.ArgsMode.Next "Permalink to this definition")

    Previous *= <ArgsMode.Previous: 0>*[??](#csc.tools.attractor.ArgsMode.Previous "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.ArgsMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.attractor.ArgsMode](#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.ArgsMode](#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.attractor.ArgsMode](#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Average': <ArgsMode.Average: 4>, 'Inertial': <ArgsMode.Inertial: 2>, 'Interpolation': <ArgsMode.Interpolation: 5>, 'InverseInertial': <ArgsMode.InverseInertial: 3>, 'Next': <ArgsMode.Next: 1>, 'Previous': <ArgsMode.Previous: 0>}*[??](#csc.tools.attractor.ArgsMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.ArgsMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.attractor.ArgsMode](#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.ArgsMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.attractor.ArgsMode.name "Permalink to this definition")

    *property* value[??](#csc.tools.attractor.ArgsMode.value "Permalink to this definition")

*class* csc.tools.attractor.AttractorGeneralSettings[??](#csc.tools.attractor.AttractorGeneralSettings "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.AttractorGeneralSettings.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.AttractorGeneralSettings](#csc.tools.attractor.AttractorGeneralSettings "csc.tools.attractor.AttractorGeneralSettings")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.AttractorGeneralSettings.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.AttractorGeneralSettings.__module__ "Permalink to this definition")

    *property* factor[??](#csc.tools.attractor.AttractorGeneralSettings.factor "Permalink to this definition")

    *property* mode[??](#csc.tools.attractor.AttractorGeneralSettings.mode "Permalink to this definition")

    *property* mode\_relative\_to\_pivot[??](#csc.tools.attractor.AttractorGeneralSettings.mode_relative_to_pivot "Permalink to this definition")

    *property* physic\_type[??](#csc.tools.attractor.AttractorGeneralSettings.physic_type "Permalink to this definition")

    *property* pivot[??](#csc.tools.attractor.AttractorGeneralSettings.pivot "Permalink to this definition")

    *property* position\_axis[??](#csc.tools.attractor.AttractorGeneralSettings.position_axis "Permalink to this definition")

    *property* rotation\_axis[??](#csc.tools.attractor.AttractorGeneralSettings.rotation_axis "Permalink to this definition")

    *property* scale\_axis[??](#csc.tools.attractor.AttractorGeneralSettings.scale_axis "Permalink to this definition")

*class* csc.tools.attractor.GSAxisFlag[??](#csc.tools.attractor.GSAxisFlag "Permalink to this definition")
:   > GeneralSettings::RotationAxis enum
    >
    > X, Y, Z, XYZ, Empty

    Members:

    > X
    >
    > Y
    >
    > Z
    >
    > XYZ
    >
    > Empty

    Empty *= <GSAxisFlag.Empty: 0>*[??](#csc.tools.attractor.GSAxisFlag.Empty "Permalink to this definition")

    X *= <GSAxisFlag.X: 1>*[??](#csc.tools.attractor.GSAxisFlag.X "Permalink to this definition")

    XYZ *= <GSAxisFlag.XYZ: 7>*[??](#csc.tools.attractor.GSAxisFlag.XYZ "Permalink to this definition")

    Y *= <GSAxisFlag.Y: 2>*[??](#csc.tools.attractor.GSAxisFlag.Y "Permalink to this definition")

    Z *= <GSAxisFlag.Z: 4>*[??](#csc.tools.attractor.GSAxisFlag.Z "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.GSAxisFlag.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.attractor.GSAxisFlag](#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.GSAxisFlag](#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.attractor.GSAxisFlag](#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Empty': <GSAxisFlag.Empty: 0>, 'X': <GSAxisFlag.X: 1>, 'XYZ': <GSAxisFlag.XYZ: 7>, 'Y': <GSAxisFlag.Y: 2>, 'Z': <GSAxisFlag.Z: 4>}*[??](#csc.tools.attractor.GSAxisFlag.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.GSAxisFlag.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.attractor.GSAxisFlag](#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisFlag.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.attractor.GSAxisFlag.name "Permalink to this definition")

    *property* value[??](#csc.tools.attractor.GSAxisFlag.value "Permalink to this definition")

*class* csc.tools.attractor.GSAxisIndex[??](#csc.tools.attractor.GSAxisIndex "Permalink to this definition")
:   > GeneralSettings::RotationAxis enum
    >
    > X, Y, Z

    Members:

    > X
    >
    > Y
    >
    > Z

    X *= <GSAxisIndex.X: 0>*[??](#csc.tools.attractor.GSAxisIndex.X "Permalink to this definition")

    Y *= <GSAxisIndex.Y: 1>*[??](#csc.tools.attractor.GSAxisIndex.Y "Permalink to this definition")

    Z *= <GSAxisIndex.Z: 2>*[??](#csc.tools.attractor.GSAxisIndex.Z "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.GSAxisIndex.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.attractor.GSAxisIndex](#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.GSAxisIndex](#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.attractor.GSAxisIndex](#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'X': <GSAxisIndex.X: 0>, 'Y': <GSAxisIndex.Y: 1>, 'Z': <GSAxisIndex.Z: 2>}*[??](#csc.tools.attractor.GSAxisIndex.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.GSAxisIndex.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.attractor.GSAxisIndex](#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSAxisIndex.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.attractor.GSAxisIndex.name "Permalink to this definition")

    *property* value[??](#csc.tools.attractor.GSAxisIndex.value "Permalink to this definition")

*class* csc.tools.attractor.GSPhysicsType[??](#csc.tools.attractor.GSPhysicsType "Permalink to this definition")
:   > GeneralSettings::RotationAxis enum
    >
    > FrameRelax, InterpolationRelax

    Members:

    > FrameRelax
    >
    > InterpolationRelax

    FrameRelax *= <GSPhysicsType.FrameRelax: 0>*[??](#csc.tools.attractor.GSPhysicsType.FrameRelax "Permalink to this definition")

    InterpolationRelax *= <GSPhysicsType.InterpolationRelax: 1>*[??](#csc.tools.attractor.GSPhysicsType.InterpolationRelax "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.GSPhysicsType.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.attractor.GSPhysicsType](#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.GSPhysicsType](#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.attractor.GSPhysicsType](#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'FrameRelax': <GSPhysicsType.FrameRelax: 0>, 'InterpolationRelax': <GSPhysicsType.InterpolationRelax: 1>}*[??](#csc.tools.attractor.GSPhysicsType.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.GSPhysicsType.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.attractor.GSPhysicsType](#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSPhysicsType.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.attractor.GSPhysicsType.name "Permalink to this definition")

    *property* value[??](#csc.tools.attractor.GSPhysicsType.value "Permalink to this definition")

*class* csc.tools.attractor.GSRotationAxis[??](#csc.tools.attractor.GSRotationAxis "Permalink to this definition")
:   > GeneralSettings::RotationAxis enum
    >
    > X, Y, Z, Whole, Empty

    Members:

    > X
    >
    > Y
    >
    > Z
    >
    > Whole
    >
    > Empty

    Empty *= <GSRotationAxis.Empty: 4>*[??](#csc.tools.attractor.GSRotationAxis.Empty "Permalink to this definition")

    Whole *= <GSRotationAxis.Whole: 3>*[??](#csc.tools.attractor.GSRotationAxis.Whole "Permalink to this definition")

    X *= <GSRotationAxis.X: 0>*[??](#csc.tools.attractor.GSRotationAxis.X "Permalink to this definition")

    Y *= <GSRotationAxis.Y: 1>*[??](#csc.tools.attractor.GSRotationAxis.Y "Permalink to this definition")

    Z *= <GSRotationAxis.Z: 2>*[??](#csc.tools.attractor.GSRotationAxis.Z "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.GSRotationAxis.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.attractor.GSRotationAxis](#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.GSRotationAxis](#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.attractor.GSRotationAxis](#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Empty': <GSRotationAxis.Empty: 4>, 'Whole': <GSRotationAxis.Whole: 3>, 'X': <GSRotationAxis.X: 0>, 'Y': <GSRotationAxis.Y: 1>, 'Z': <GSRotationAxis.Z: 2>}*[??](#csc.tools.attractor.GSRotationAxis.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.GSRotationAxis.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.attractor.GSRotationAxis](#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.GSRotationAxis.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.attractor.GSRotationAxis.name "Permalink to this definition")

    *property* value[??](#csc.tools.attractor.GSRotationAxis.value "Permalink to this definition")

*class* csc.tools.attractor.SpaceMode[??](#csc.tools.attractor.SpaceMode "Permalink to this definition")
:   > attractor::Mode enum
    >
    > Global, Local

    Members:

    > Global
    >
    > Local

    Global *= <SpaceMode.Global: 0>*[??](#csc.tools.attractor.SpaceMode.Global "Permalink to this definition")

    Local *= <SpaceMode.Local: 1>*[??](#csc.tools.attractor.SpaceMode.Local "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.tools.attractor.SpaceMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.tools.attractor.SpaceMode](#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.tools.attractor.SpaceMode](#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.tools.attractor.SpaceMode](#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Global': <SpaceMode.Global: 0>, 'Local': <SpaceMode.Local: 1>}*[??](#csc.tools.attractor.SpaceMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.tools.attractor'*[??](#csc.tools.attractor.SpaceMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.tools.attractor.SpaceMode](#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.tools.attractor.SpaceMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.tools.attractor.SpaceMode.name "Permalink to this definition")

    *property* value[??](#csc.tools.attractor.SpaceMode.value "Permalink to this definition")

csc.tools.attractor.attract(*args: [csc.tools.attractor.Args](#csc.tools.attractor.Args "csc.tools.attractor.Args")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.tools.attractor.attract "Permalink to this definition")

## csc.view The Cascadeur python module provides basic methods to operate GUI.[??](#module-csc.view "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.view.StandardButton`](#csc.view.StandardButton "csc.view.StandardButton") | StandardButton enum |
| [`csc.view.DialogButton`](#csc.view.DialogButton "csc.view.DialogButton") | DialogButton class |
| [`csc.view.DialogManager`](#csc.view.DialogManager "csc.view.DialogManager") | DialogManager class |
| [`csc.view.FileDialogManager`](#csc.view.FileDialogManager "csc.view.FileDialogManager") | FileDialogManager class |
| [`csc.view.Scene`](#csc.view.Scene "csc.view.Scene") | SceneView class |
| [`csc.view.AnimationBoundary`](#csc.view.AnimationBoundary "csc.view.AnimationBoundary") | AnimationBoundary class |
| [`csc.view.CameraType`](#csc.view.CameraType "csc.view.CameraType") | CameraType enumerable |
| [`csc.view.SphericalCameraStruct`](#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct") | SphericalCameraStruct class |
| [`csc.view.Camera`](#csc.view.Camera "csc.view.Camera") | Domain Spherical camera class |
| [`csc.view.ViewportDomain`](#csc.view.ViewportDomain "csc.view.ViewportDomain") | Domain Viewport class |
| [`csc.view.Viewport`](#csc.view.Viewport "csc.view.Viewport") | Viewport class |

*class* csc.view.AnimationBoundary[??](#csc.view.AnimationBoundary "Permalink to this definition")
:   AnimationBoundary class

    \_\_annotations\_\_ *= {}*[??](#csc.view.AnimationBoundary.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.AnimationBoundary.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.AnimationBoundary.__module__ "Permalink to this definition")

    *property* first\_frame[??](#csc.view.AnimationBoundary.first_frame "Permalink to this definition")
    :   Set first frame of animation

    *property* first\_visible\_frame[??](#csc.view.AnimationBoundary.first_visible_frame "Permalink to this definition")
    :   Set first visible frame of animation

    *property* last\_frame[??](#csc.view.AnimationBoundary.last_frame "Permalink to this definition")
    :   Set last frame of animation

    *property* last\_visible\_frame[??](#csc.view.AnimationBoundary.last_visible_frame "Permalink to this definition")
    :   Set last visible frame of animation

*class* csc.view.Camera[??](#csc.view.Camera "Permalink to this definition")
:   Domain Spherical camera class

    \_\_annotations\_\_ *= {}*[??](#csc.view.Camera.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.Camera.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.Camera.__module__ "Permalink to this definition")

    set\_target(*self: [csc.view.Camera](#csc.view.Camera "csc.view.Camera")*, *arg0: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.Camera.set_target "Permalink to this definition")

    zoom\_to\_points(*self: [csc.view.Camera](#csc.view.Camera "csc.view.Camera")*, *arg0: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.Camera.zoom_to_points "Permalink to this definition")

*class* csc.view.CameraType[??](#csc.view.CameraType "Permalink to this definition")
:   > CameraType enumerable

    Members:

    > ISOMETRIC
    >
    > PERSPECTIVE

    ISOMETRIC *= <CameraType.ISOMETRIC: 0>*[??](#csc.view.CameraType.ISOMETRIC "Permalink to this definition")

    PERSPECTIVE *= <CameraType.PERSPECTIVE: 1>*[??](#csc.view.CameraType.PERSPECTIVE "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.view.CameraType.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.CameraType.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.CameraType.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.CameraType.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.view.CameraType](#csc.view.CameraType "csc.view.CameraType")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.CameraType.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.view.CameraType](#csc.view.CameraType "csc.view.CameraType")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.CameraType.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.view.CameraType](#csc.view.CameraType "csc.view.CameraType")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.CameraType.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'ISOMETRIC': <CameraType.ISOMETRIC: 0>, 'PERSPECTIVE': <CameraType.PERSPECTIVE: 1>}*[??](#csc.view.CameraType.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.CameraType.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.CameraType.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.CameraType.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.view.CameraType](#csc.view.CameraType "csc.view.CameraType")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.CameraType.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.CameraType.__str__ "Permalink to this definition")

    *property* name[??](#csc.view.CameraType.name "Permalink to this definition")

    *property* value[??](#csc.view.CameraType.value "Permalink to this definition")

*class* csc.view.DialogButton[??](#csc.view.DialogButton "Permalink to this definition")
:   DialogButton class

    \_\_annotations\_\_ *= {}*[??](#csc.view.DialogButton.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.DialogButton.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.view.DialogButton) -> None
        2. \_\_init\_\_(self: csc.view.DialogButton, arg0: str) -> None
        3. \_\_init\_\_(self: csc.view.DialogButton, text: str, handler: Callable, force\_active\_focus: bool = False, accent: bool = False) -> None
        4. \_\_init\_\_(self: csc.view.DialogButton, arg0: csc.view.StandardButton) -> None
        5. \_\_init\_\_(self: csc.view.DialogButton, button: csc.view.StandardButton, handler: Callable, force\_active\_focus: bool = False, accent: bool = False) -> None

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.DialogButton.__module__ "Permalink to this definition")

    force\_active\_focus(*self: [csc.view.DialogButton](#csc.view.DialogButton "csc.view.DialogButton")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.DialogButton.force_active_focus "Permalink to this definition")

    text(*self: [csc.view.DialogButton](#csc.view.DialogButton "csc.view.DialogButton")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.DialogButton.text "Permalink to this definition")
    :   -> string

*class* csc.view.DialogManager[??](#csc.view.DialogManager "Permalink to this definition")
:   DialogManager class

    \_\_annotations\_\_ *= {}*[??](#csc.view.DialogManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.DialogManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.DialogManager.__module__ "Permalink to this definition")

    *static* instance()  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.DialogManager.instance "Permalink to this definition")

    show\_buttons\_dialog(*self: [csc.view.DialogManager](#csc.view.DialogManager "csc.view.DialogManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg2: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.view.DialogButton](#csc.view.DialogButton "csc.view.DialogButton")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.DialogManager.show_buttons_dialog "Permalink to this definition")

    show\_info(*self: [csc.view.DialogManager](#csc.view.DialogManager "csc.view.DialogManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.DialogManager.show_info "Permalink to this definition")

    show\_input\_dialog(*\*args*, *\*\*kwargs*)[??](#csc.view.DialogManager.show_input_dialog "Permalink to this definition")
    :   Overloaded function.

        1. show\_input\_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable) -> None
        2. show\_input\_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable, arg4: Callable) -> None

    show\_inputs\_dialog(*self: [csc.view.DialogManager](#csc.view.DialogManager "csc.view.DialogManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*, *arg2: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*, *arg3: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg4: Callable*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.DialogManager.show_inputs_dialog "Permalink to this definition")

    show\_styled\_buttons\_dialog(*self: [csc.view.DialogManager](#csc.view.DialogManager "csc.view.DialogManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg2: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.view.DialogButton](#csc.view.DialogButton "csc.view.DialogButton")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.DialogManager.show_styled_buttons_dialog "Permalink to this definition")

*class* csc.view.FileDialogManager[??](#csc.view.FileDialogManager "Permalink to this definition")
:   FileDialogManager class

    \_\_annotations\_\_ *= {}*[??](#csc.view.FileDialogManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.FileDialogManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.FileDialogManager.__module__ "Permalink to this definition")

    show\_folder\_dialog(*self: [csc.view.FileDialogManager](#csc.view.FileDialogManager "csc.view.FileDialogManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.FileDialogManager.show_folder_dialog "Permalink to this definition")

    show\_open\_file\_dialog(*self: [csc.view.FileDialogManager](#csc.view.FileDialogManager "csc.view.FileDialogManager")*, *title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *filters: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*, *handler: Callable*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.FileDialogManager.show_open_file_dialog "Permalink to this definition")

    show\_save\_file\_dialog(*self: [csc.view.FileDialogManager](#csc.view.FileDialogManager "csc.view.FileDialogManager")*, *title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *filters: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*, *handler: Callable*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.FileDialogManager.show_save_file_dialog "Permalink to this definition")

*class* csc.view.Scene[??](#csc.view.Scene "Permalink to this definition")
:   SceneView class

    \_\_annotations\_\_ *= {}*[??](#csc.view.Scene.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.Scene.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.Scene.__module__ "Permalink to this definition")

    active\_viewport(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.Scene.active_viewport "Permalink to this definition")
    :   Returns active csc.view.Viewport

    animation\_boundary(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.Scene.animation_boundary "Permalink to this definition")
    :   -> csc.view.AnimationBoundary

    domain\_scene(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.Scene.domain_scene "Permalink to this definition")
    :   Return current csc.domain.Scene

    get\_setting\_handler(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.Scene.get_setting_handler "Permalink to this definition")

    gravity\_per\_frame(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.view.Scene.gravity_per_frame "Permalink to this definition")

    name(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.Scene.name "Permalink to this definition")

    save(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *path\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.Scene.save "Permalink to this definition")

    viewports(*self: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")][??](#csc.view.Scene.viewports "Permalink to this definition")
    :   Provides all of csc.view.Viewport objects

*class* csc.view.SphericalCameraStruct[??](#csc.view.SphericalCameraStruct "Permalink to this definition")
:   SphericalCameraStruct class

    Variables:
    :   * **target** ??? Get set Vector3f
        * **position** ??? Get set Vector3f
        * **type** ??? Get set CameraType

    \_\_annotations\_\_ *= {}*[??](#csc.view.SphericalCameraStruct.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.view.SphericalCameraStruct](#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.SphericalCameraStruct.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.SphericalCameraStruct.__module__ "Permalink to this definition")

    *property* position[??](#csc.view.SphericalCameraStruct.position "Permalink to this definition")

    *property* target[??](#csc.view.SphericalCameraStruct.target "Permalink to this definition")

    *property* type[??](#csc.view.SphericalCameraStruct.type "Permalink to this definition")

*class* csc.view.StandardButton[??](#csc.view.StandardButton "Permalink to this definition")
:   > StandardButton enum
    >
    > This enumerates the basic types of standard buttons.
    > Ok, Cancel, Yes, No

    Members:

    > Ok
    >
    > Cancel
    >
    > No
    >
    > Yes

    Cancel *= <StandardButton.Cancel: 1>*[??](#csc.view.StandardButton.Cancel "Permalink to this definition")

    No *= <StandardButton.No: 3>*[??](#csc.view.StandardButton.No "Permalink to this definition")

    Ok *= <StandardButton.Ok: 0>*[??](#csc.view.StandardButton.Ok "Permalink to this definition")

    Yes *= <StandardButton.Yes: 2>*[??](#csc.view.StandardButton.Yes "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.view.StandardButton.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.StandardButton.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.StandardButton.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.StandardButton.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.view.StandardButton](#csc.view.StandardButton "csc.view.StandardButton")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.StandardButton.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.view.StandardButton](#csc.view.StandardButton "csc.view.StandardButton")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.StandardButton.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.view.StandardButton](#csc.view.StandardButton "csc.view.StandardButton")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.StandardButton.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Cancel': <StandardButton.Cancel: 1>, 'No': <StandardButton.No: 3>, 'Ok': <StandardButton.Ok: 0>, 'Yes': <StandardButton.Yes: 2>}*[??](#csc.view.StandardButton.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.StandardButton.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.StandardButton.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.StandardButton.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.view.StandardButton](#csc.view.StandardButton "csc.view.StandardButton")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.StandardButton.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.StandardButton.__str__ "Permalink to this definition")

    *property* name[??](#csc.view.StandardButton.name "Permalink to this definition")

    *property* value[??](#csc.view.StandardButton.value "Permalink to this definition")

*class* csc.view.Viewport[??](#csc.view.Viewport "Permalink to this definition")
:   Viewport class

    \_\_annotations\_\_ *= {}*[??](#csc.view.Viewport.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.Viewport.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.Viewport.__module__ "Permalink to this definition")

    domain\_viewport(*self: [csc.view.Viewport](#csc.view.Viewport "csc.view.Viewport")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.Viewport.domain_viewport "Permalink to this definition")

*class* csc.view.ViewportDomain[??](#csc.view.ViewportDomain "Permalink to this definition")
:   Domain Viewport class

    \_\_annotations\_\_ *= {}*[??](#csc.view.ViewportDomain.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.ViewportDomain.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.ViewportDomain.__module__ "Permalink to this definition")

    camera(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.view.ViewportDomain.camera "Permalink to this definition")

    camera\_struct(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*)  [csc.view.SphericalCameraStruct](#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct")[??](#csc.view.ViewportDomain.camera_struct "Permalink to this definition")

    id(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.view.ViewportDomain.id "Permalink to this definition")

    is\_main(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.ViewportDomain.is_main "Permalink to this definition")

    mode\_visualizers(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*)  [csc.view.ViewportMode](#csc.view.ViewportMode "csc.view.ViewportMode")[??](#csc.view.ViewportDomain.mode_visualizers "Permalink to this definition")

    set\_camera\_struct(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*, *camera\_struct: [csc.view.SphericalCameraStruct](#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.ViewportDomain.set_camera_struct "Permalink to this definition")

    set\_mode\_visualizers(*self: [csc.view.ViewportDomain](#csc.view.ViewportDomain "csc.view.ViewportDomain")*, *mode: [csc.view.ViewportMode](#csc.view.ViewportMode "csc.view.ViewportMode")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.ViewportDomain.set_mode_visualizers "Permalink to this definition")

*class* csc.view.ViewportMode[??](#csc.view.ViewportMode "Permalink to this definition")
:   > ViewportMode enumerable

    Members:

    > View
    >
    > AutoPosing
    >
    > PointController
    >
    > Controller
    >
    > Joint
    >
    > Mesh
    >
    > Rigging
    >
    > ModeCount

    AutoPosing *= <ViewportMode.AutoPosing: 1>*[??](#csc.view.ViewportMode.AutoPosing "Permalink to this definition")

    Controller *= <ViewportMode.Controller: 3>*[??](#csc.view.ViewportMode.Controller "Permalink to this definition")

    Joint *= <ViewportMode.Joint: 4>*[??](#csc.view.ViewportMode.Joint "Permalink to this definition")

    Mesh *= <ViewportMode.Mesh: 5>*[??](#csc.view.ViewportMode.Mesh "Permalink to this definition")

    ModeCount *= <ViewportMode.ModeCount: 7>*[??](#csc.view.ViewportMode.ModeCount "Permalink to this definition")

    PointController *= <ViewportMode.PointController: 2>*[??](#csc.view.ViewportMode.PointController "Permalink to this definition")

    Rigging *= <ViewportMode.Rigging: 6>*[??](#csc.view.ViewportMode.Rigging "Permalink to this definition")

    View *= <ViewportMode.View: 0>*[??](#csc.view.ViewportMode.View "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.view.ViewportMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.ViewportMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.ViewportMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.ViewportMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.view.ViewportMode](#csc.view.ViewportMode "csc.view.ViewportMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.ViewportMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.view.ViewportMode](#csc.view.ViewportMode "csc.view.ViewportMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.ViewportMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.view.ViewportMode](#csc.view.ViewportMode "csc.view.ViewportMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.view.ViewportMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'AutoPosing': <ViewportMode.AutoPosing: 1>, 'Controller': <ViewportMode.Controller: 3>, 'Joint': <ViewportMode.Joint: 4>, 'Mesh': <ViewportMode.Mesh: 5>, 'ModeCount': <ViewportMode.ModeCount: 7>, 'PointController': <ViewportMode.PointController: 2>, 'Rigging': <ViewportMode.Rigging: 6>, 'View': <ViewportMode.View: 0>}*[??](#csc.view.ViewportMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view'*[??](#csc.view.ViewportMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.ViewportMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.ViewportMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.view.ViewportMode](#csc.view.ViewportMode "csc.view.ViewportMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.ViewportMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.ViewportMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.view.ViewportMode.name "Permalink to this definition")

    *property* value[??](#csc.view.ViewportMode.value "Permalink to this definition")

## csc.view.camera\_utils The Cascadeur python module provides utulity methods to manage viewport cameras.[??](#csc-view-camera-utils-the-cascadeur-python-module-provides-utulity-methods-to-manage-viewport-cameras "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.view.camera_utils.CameraData`](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData") | CameraData class |

*class* csc.view.camera\_utils.CameraData[??](#csc.view.camera_utils.CameraData "Permalink to this definition")
:   CameraData class

    \_\_annotations\_\_ *= {}*[??](#csc.view.camera_utils.CameraData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.view.camera_utils.CameraData.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.view.camera\_utils'*[??](#csc.view.camera_utils.CameraData.__module__ "Permalink to this definition")

    id(*self: [csc.view.camera\_utils.CameraData](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")*)  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.view.camera_utils.CameraData.id "Permalink to this definition")

    isCustom(*self: [csc.view.camera\_utils.CameraData](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.camera_utils.CameraData.isCustom "Permalink to this definition")

    name(*self: [csc.view.camera\_utils.CameraData](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.view.camera_utils.CameraData.name "Permalink to this definition")

csc.view.camera\_utils.get\_cameras(*scene: cascadeur::Scene*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.view.camera\_utils.CameraData](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")][??](#csc.view.camera_utils.get_cameras "Permalink to this definition")

csc.view.camera\_utils.is\_camera\_active(*viewport: [csc.view.Viewport](#csc.view.Viewport "csc.view.Viewport")*, *camera: [csc.view.camera\_utils.CameraData](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.view.camera_utils.is_camera_active "Permalink to this definition")

csc.view.camera\_utils.reset\_camera(*scene: [csc.view.Viewport](#csc.view.Viewport "csc.view.Viewport")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.camera_utils.reset_camera "Permalink to this definition")

csc.view.camera\_utils.set\_camera\_active(*viewport: [csc.view.Viewport](#csc.view.Viewport "csc.view.Viewport")*, *camera: [csc.view.camera\_utils.CameraData](#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.view.camera_utils.set_camera_active "Permalink to this definition")

## csc.app The Cascadeur python module provides basic methods to operate GUI.[??](#module-csc.app "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.app.Analytics`](#csc.app.Analytics "csc.app.Analytics") | Analytics class |
| [`csc.app.ActionManager`](#csc.app.ActionManager "csc.app.ActionManager") | ActionManager class |
| [`csc.app.DataSourceManager`](#csc.app.DataSourceManager "csc.app.DataSourceManager") | DataSourceManager class |
| [`csc.app.SettingsManager`](#csc.app.SettingsManager "csc.app.SettingsManager") | SettingsManager class |
| [`csc.app.SceneManager`](#csc.app.SceneManager "csc.app.SceneManager") | SceneManager class |
| [`csc.app.SceneTool`](#csc.app.SceneTool "csc.app.SceneTool") | SceneTool class |
| [`csc.app.CascadeurTool`](#csc.app.CascadeurTool "csc.app.CascadeurTool") | CascadeurTool class |
| [`csc.app.ToolsManager`](#csc.app.ToolsManager "csc.app.ToolsManager") | ToolsManager class |
| [`csc.app.Application`](#csc.app.Application "csc.app.Application") | Application class |
| [`csc.app.ProjectLoader`](#csc.app.ProjectLoader "csc.app.ProjectLoader") | ProjectLoader class |
| [`csc.app.StatusManager`](#csc.app.StatusManager "csc.app.StatusManager") | StatusManager class |
| [`csc.app.SimpleStatusInformer`](#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer") | SimpleStatusInformer class |

*class* csc.app.ActionManager[??](#csc.app.ActionManager "Permalink to this definition")
:   ActionManager class

    \_\_annotations\_\_ *= {}*[??](#csc.app.ActionManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.ActionManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.ActionManager.__module__ "Permalink to this definition")

    call\_action(*self: [csc.app.ActionManager](#csc.app.ActionManager "csc.app.ActionManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.ActionManager.call_action "Permalink to this definition")

*class* csc.app.Analytics[??](#csc.app.Analytics "Permalink to this definition")
:   Analytics class

    \_\_annotations\_\_ *= {}*[??](#csc.app.Analytics.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.Analytics.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.Analytics.__module__ "Permalink to this definition")

    *static* send\_action(*type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = ''*, *label: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = ''*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.Analytics.send_action "Permalink to this definition")

*class* csc.app.Application[??](#csc.app.Application "Permalink to this definition")
:   Application class

    \_\_annotations\_\_ *= {}*[??](#csc.app.Application.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.Application.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.Application.__module__ "Permalink to this definition")

    current\_scene(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.current_scene "Permalink to this definition")

    get\_action\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_action_manager "Permalink to this definition")

    get\_data\_source\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_data_source_manager "Permalink to this definition")

    get\_file\_dialog\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_file_dialog_manager "Permalink to this definition")

    get\_scene\_clipboard(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_scene_clipboard "Permalink to this definition")

    get\_scene\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_scene_manager "Permalink to this definition")

    get\_setting\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_setting_manager "Permalink to this definition")

    get\_status\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_status_manager "Permalink to this definition")

    get\_tools\_manager(*self: [csc.app.Application](#csc.app.Application "csc.app.Application")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.Application.get_tools_manager "Permalink to this definition")

*class* csc.app.CascadeurTool[??](#csc.app.CascadeurTool "Permalink to this definition")
:   CascadeurTool class

    \_\_annotations\_\_ *= {}*[??](#csc.app.CascadeurTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.CascadeurTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.CascadeurTool.__module__ "Permalink to this definition")

    editor(*self: [csc.app.CascadeurTool](#csc.app.CascadeurTool "csc.app.CascadeurTool")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [csc.app.SceneTool](#csc.app.SceneTool "csc.app.SceneTool")[??](#csc.app.CascadeurTool.editor "Permalink to this definition")

    name(*self: [csc.app.CascadeurTool](#csc.app.CascadeurTool "csc.app.CascadeurTool")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.app.CascadeurTool.name "Permalink to this definition")

*class* csc.app.DataSourceManager[??](#csc.app.DataSourceManager "Permalink to this definition")
:   DataSourceManager class

    \_\_annotations\_\_ *= {}*[??](#csc.app.DataSourceManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.DataSourceManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.DataSourceManager.__module__ "Permalink to this definition")

    close\_scene(*self: [csc.app.DataSourceManager](#csc.app.DataSourceManager "csc.app.DataSourceManager")*, *scene: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.DataSourceManager.close_scene "Permalink to this definition")

    load\_scene(*self: [csc.app.DataSourceManager](#csc.app.DataSourceManager "csc.app.DataSourceManager")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.app.DataSourceManager.load_scene "Permalink to this definition")
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

    save\_scene\_as(*self: [csc.app.DataSourceManager](#csc.app.DataSourceManager "csc.app.DataSourceManager")*, *scene\_view: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *full\_file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.DataSourceManager.save_scene_as "Permalink to this definition")

*class* csc.app.ProjectLoader[??](#csc.app.ProjectLoader "Permalink to this definition")
:   ProjectLoader class

    Provides methods to load domain scene.

    \_\_annotations\_\_ *= {}*[??](#csc.app.ProjectLoader.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.ProjectLoader.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.ProjectLoader.__module__ "Permalink to this definition")

    *static* load\_from(*arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.ProjectLoader.load_from "Permalink to this definition")
    :   Minimal Load. This method doesn???t load selection groups, control picker and etc.
        Better use data\_source\_manager???s load\_scene method.
        Example:
        csc.app.ProjectLoader.load\_from(file\_path, scene)

*class* csc.app.SceneManager[??](#csc.app.SceneManager "Permalink to this definition")
:   SceneManager class

    \_\_annotations\_\_ *= {}*[??](#csc.app.SceneManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.SceneManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.SceneManager.__module__ "Permalink to this definition")

    create\_application\_scene(*self: [csc.app.SceneManager](#csc.app.SceneManager "csc.app.SceneManager")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.SceneManager.create_application_scene "Permalink to this definition")

    current\_scene(*self: [csc.app.SceneManager](#csc.app.SceneManager "csc.app.SceneManager")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.SceneManager.current_scene "Permalink to this definition")

    remove\_application\_scene(*self: [csc.app.SceneManager](#csc.app.SceneManager "csc.app.SceneManager")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.SceneManager.remove_application_scene "Permalink to this definition")

    scenes(*self: [csc.app.SceneManager](#csc.app.SceneManager "csc.app.SceneManager")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")][??](#csc.app.SceneManager.scenes "Permalink to this definition")

    set\_current\_scene(*self: [csc.app.SceneManager](#csc.app.SceneManager "csc.app.SceneManager")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.SceneManager.set_current_scene "Permalink to this definition")

*class* csc.app.SceneTool[??](#csc.app.SceneTool "Permalink to this definition")
:   SceneTool class

    \_\_annotations\_\_ *= {}*[??](#csc.app.SceneTool.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.SceneTool.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.SceneTool.__module__ "Permalink to this definition")

*class* csc.app.SettingsHandler[??](#csc.app.SettingsHandler "Permalink to this definition")
:   SettingsHandler class

    \_\_annotations\_\_ *= {}*[??](#csc.app.SettingsHandler.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.SettingsHandler.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.SettingsHandler.__module__ "Permalink to this definition")

    get\_bool\_value(*self: [csc.app.SettingsHandler](#csc.app.SettingsHandler "csc.app.SettingsHandler")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.app.SettingsHandler.get_bool_value "Permalink to this definition")

    get\_float\_value(*self: [csc.app.SettingsHandler](#csc.app.SettingsHandler "csc.app.SettingsHandler")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.app.SettingsHandler.get_float_value "Permalink to this definition")

    get\_int\_value(*self: [csc.app.SettingsHandler](#csc.app.SettingsHandler "csc.app.SettingsHandler")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.app.SettingsHandler.get_int_value "Permalink to this definition")

    get\_string\_value(*self: [csc.app.SettingsHandler](#csc.app.SettingsHandler "csc.app.SettingsHandler")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.app.SettingsHandler.get_string_value "Permalink to this definition")

*class* csc.app.SettingsManager[??](#csc.app.SettingsManager "Permalink to this definition")
:   SettingsManager class

    \_\_annotations\_\_ *= {}*[??](#csc.app.SettingsManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.SettingsManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.SettingsManager.__module__ "Permalink to this definition")

    get\_bool\_value(*self: [csc.app.SettingsManager](#csc.app.SettingsManager "csc.app.SettingsManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.app.SettingsManager.get_bool_value "Permalink to this definition")

    get\_color\_value(*self: [csc.app.SettingsManager](#csc.app.SettingsManager "csc.app.SettingsManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.app.SettingsManager.get_color_value "Permalink to this definition")

    get\_float\_value(*self: [csc.app.SettingsManager](#csc.app.SettingsManager "csc.app.SettingsManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.app.SettingsManager.get_float_value "Permalink to this definition")

*class* csc.app.SimpleStatusInformer[??](#csc.app.SimpleStatusInformer "Permalink to this definition")
:   SimpleStatusInformer class

    \_\_annotations\_\_ *= {}*[??](#csc.app.SimpleStatusInformer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.app.SimpleStatusInformer](#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.SimpleStatusInformer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.SimpleStatusInformer.__module__ "Permalink to this definition")

    is\_canceled(*self: [csc.app.SimpleStatusInformer](#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.app.SimpleStatusInformer.is_canceled "Permalink to this definition")

    set\_blocking(*self: [csc.app.SimpleStatusInformer](#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")*, *arg0: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.SimpleStatusInformer.set_blocking "Permalink to this definition")

    set\_cancelable(*self: [csc.app.SimpleStatusInformer](#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")*, *arg0: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.SimpleStatusInformer.set_cancelable "Permalink to this definition")

    set\_text(*self: [csc.app.SimpleStatusInformer](#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.SimpleStatusInformer.set_text "Permalink to this definition")

*class* csc.app.StatusInformer[??](#csc.app.StatusInformer "Permalink to this definition")
:   StatusInformer class

    \_\_annotations\_\_ *= {}*[??](#csc.app.StatusInformer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.StatusInformer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.StatusInformer.__module__ "Permalink to this definition")

*class* csc.app.StatusManager[??](#csc.app.StatusManager "Permalink to this definition")
:   StatusManager class

    \_\_annotations\_\_ *= {}*[??](#csc.app.StatusManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.StatusManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.StatusManager.__module__ "Permalink to this definition")

    remove\_status(*self: csc.app.StatusManager*, *arg0: cascadeur::StatusInformer*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.StatusManager.remove_status "Permalink to this definition")

    set\_status(*self: csc.app.StatusManager*, *arg0: cascadeur::StatusInformer*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.app.StatusManager.set_status "Permalink to this definition")

*class* csc.app.ToolsManager[??](#csc.app.ToolsManager "Permalink to this definition")
:   ToolsManager class

    \_\_annotations\_\_ *= {}*[??](#csc.app.ToolsManager.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.app.ToolsManager.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.app'*[??](#csc.app.ToolsManager.__module__ "Permalink to this definition")

    get\_tool(*self: [csc.app.ToolsManager](#csc.app.ToolsManager "csc.app.ToolsManager")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.ToolsManager.get_tool "Permalink to this definition")

    tools(*self: [csc.app.ToolsManager](#csc.app.ToolsManager "csc.app.ToolsManager")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")][??](#csc.app.ToolsManager.tools "Permalink to this definition")

csc.app.get\_application()  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.app.get_application "Permalink to this definition")

## csc.parts The Cascadeur python module provides basic methods to operate scene parts.[??](#module-csc.parts "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.parts.Type`](#csc.parts.Type "csc.parts.Type") | Type of the parts, enum |
| [`csc.parts.Info`](#csc.parts.Info "csc.parts.Info") | Info class |
| [`csc.parts.GroupInfo`](#csc.parts.GroupInfo "csc.parts.GroupInfo") | GroupInfo class |
| [`csc.parts.SceneClipboard`](#csc.parts.SceneClipboard "csc.parts.SceneClipboard") | SceneClipboard class |
| [`csc.parts.Buffer`](#csc.parts.Buffer "csc.parts.Buffer") | Buffer class |

*class* csc.parts.Buffer[??](#csc.parts.Buffer "Permalink to this definition")
:   Buffer class

    Provides methods to operate parts of the scene.

    \_\_annotations\_\_ *= {}*[??](#csc.parts.Buffer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.parts.Buffer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.parts'*[??](#csc.parts.Buffer.__module__ "Permalink to this definition")

    *static* get(*source\_dir: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = ''*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.parts.Buffer.get "Permalink to this definition")

    get\_parts\_info\_by\_id(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.parts.Info](#csc.parts.Info "csc.parts.Info")][??](#csc.parts.Buffer.get_parts_info_by_id "Permalink to this definition")

    get\_src\_dir(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.parts.Buffer.get_src_dir "Permalink to this definition")

    insert\_elementary\_by\_id(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo")[??](#csc.parts.Buffer.insert_elementary_by_id "Permalink to this definition")

    insert\_elementary\_by\_path(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo")[??](#csc.parts.Buffer.insert_elementary_by_path "Permalink to this definition")

    insert\_object\_by\_id(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.parts.Buffer.insert_object_by_id "Permalink to this definition")

    insert\_object\_by\_path(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.parts.Buffer.insert_object_by_path "Permalink to this definition")

    insert\_objects\_by\_id(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")], [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")]][??](#csc.parts.Buffer.insert_objects_by_id "Permalink to this definition")

    insert\_objects\_by\_path(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")], [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")]][??](#csc.parts.Buffer.insert_objects_by_path "Permalink to this definition")

    insert\_selected\_objects\_by\_path(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.parts.Buffer.insert_selected_objects_by_path "Permalink to this definition")

    insert\_update\_group\_by\_id(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId"), [csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo")]][??](#csc.parts.Buffer.insert_update_group_by_id "Permalink to this definition")

    insert\_update\_group\_by\_path(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId"), [csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo")]][??](#csc.parts.Buffer.insert_update_group_by_path "Permalink to this definition")

    refresh(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.Buffer.refresh "Permalink to this definition")

    reset\_cache(*self: [csc.parts.Buffer](#csc.parts.Buffer "csc.parts.Buffer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.Buffer.reset_cache "Permalink to this definition")

    take\_elementary\_to\_parts(*self: csc.parts.Buffer*, *part\_name: str*, *from: csc.domain.Scene*, *object\_id: csc.model.ObjectId*, *parent\_group: csc.update.GroupId*, *elementary: csc.parts.GroupInfo*, *path\_to\_scene\_parts: str*)  [csc.parts.Info](#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_elementary_to_parts "Permalink to this definition")

    take\_object\_to\_parts(*self: csc.parts.Buffer*, *part\_name: str*, *from: csc.domain.Scene*, *object\_id: csc.model.ObjectId*, *path\_to\_scene\_parts: str*)  [csc.parts.Info](#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_object_to_parts "Permalink to this definition")

    take\_objects\_to\_parts(*self: csc.parts.Buffer, part\_name: str, from: csc.domain.Scene, objects: list[csc.model.ObjectId], objects\_grs: list[csc.update.GroupId], path\_to\_scene\_parts: str*)  [csc.parts.Info](#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_objects_to_parts "Permalink to this definition")

    take\_selected\_objects\_to\_parts(*self: csc.parts.Buffer, part\_name: str, from: csc.domain.Scene, selected\_objects: list[csc.model.ObjectId], path\_to\_scene\_parts: str*)  [csc.parts.Info](#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_selected_objects_to_parts "Permalink to this definition")

    take\_update\_group\_to\_parts(*self: csc.parts.Buffer, part\_name: str, from: csc.domain.Scene, object\_id: csc.model.ObjectId, parent\_group: csc.update.GroupId, elementary: csc.parts.GroupInfo, sub\_groups: list[csc.update.GroupId], path\_to\_scene\_parts: str*)  [csc.parts.Info](#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_update_group_to_parts "Permalink to this definition")

*class* csc.parts.GroupInfo[??](#csc.parts.GroupInfo "Permalink to this definition")
:   GroupInfo class

    Variables:
    :   * **type** ??? Get set Data::Id{}
        * **name** ??? Get set Setting::Id{}
        * **path** ??? Get set HyperedgeId{}
        * **object\_id** ??? Get set SettingFunctionId{}

    \_\_annotations\_\_ *= {}*[??](#csc.parts.GroupInfo.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.parts.GroupInfo](#csc.parts.GroupInfo "csc.parts.GroupInfo")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.GroupInfo.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.parts'*[??](#csc.parts.GroupInfo.__module__ "Permalink to this definition")

    *property* datas[??](#csc.parts.GroupInfo.datas "Permalink to this definition")

    *property* regular\_funcs[??](#csc.parts.GroupInfo.regular_funcs "Permalink to this definition")

    *property* settings[??](#csc.parts.GroupInfo.settings "Permalink to this definition")

    *property* settings\_funcs[??](#csc.parts.GroupInfo.settings_funcs "Permalink to this definition")

*class* csc.parts.Info[??](#csc.parts.Info "Permalink to this definition")
:   Info class

    Variables:
    :   * **type** ??? Get csc.parts.Type
        * **name** ??? Get string
        * **path** ??? Get string
        * **object\_id** ??? Get csc.model.ObjectId

    \_\_annotations\_\_ *= {}*[??](#csc.parts.Info.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.parts.Info.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.parts'*[??](#csc.parts.Info.__module__ "Permalink to this definition")

    *property* name[??](#csc.parts.Info.name "Permalink to this definition")

    *property* object\_id[??](#csc.parts.Info.object_id "Permalink to this definition")

    *property* path[??](#csc.parts.Info.path "Permalink to this definition")

    *property* type[??](#csc.parts.Info.type "Permalink to this definition")

*class* csc.parts.SceneClipboard[??](#csc.parts.SceneClipboard "Permalink to this definition")
:   SceneClipboard class

    Provides methods to operate parts of the scene.

    \_\_annotations\_\_ *= {}*[??](#csc.parts.SceneClipboard.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.parts.SceneClipboard.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.parts'*[??](#csc.parts.SceneClipboard.__module__ "Permalink to this definition")

    copy(*self: [csc.parts.SceneClipboard](#csc.parts.SceneClipboard "csc.parts.SceneClipboard")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.SceneClipboard.copy "Permalink to this definition")

    copy\_image\_to\_clipboard(*self: [csc.parts.SceneClipboard](#csc.parts.SceneClipboard "csc.parts.SceneClipboard")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.SceneClipboard.copy_image_to_clipboard "Permalink to this definition")

    paste(*self: [csc.parts.SceneClipboard](#csc.parts.SceneClipboard "csc.parts.SceneClipboard")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.SceneClipboard.paste "Permalink to this definition")

    paste\_with\_session(*self: [csc.parts.SceneClipboard](#csc.parts.SceneClipboard "csc.parts.SceneClipboard")*, *arg0: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *arg1: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.SceneClipboard.paste_with_session "Permalink to this definition")

*class* csc.parts.Type[??](#csc.parts.Type "Permalink to this definition")
:   > Type of the parts, enum
    >
    > Elementary: includes only regular and setting functions + regular and setting data + connections that link them
    > UpdateGroup: sub update groups and their elementary entities + connections that link them
    > Object: includes all related entities of some object
    > ObjectGroup: includes all objects and sub object groups and all related entities
    > SelectedObjects: selected objects from different groups

    Members:

    > Elementary
    >
    > UpdateGroup
    >
    > Object
    >
    > ObjectGroup
    >
    > SelectedObjects

    Elementary *= <Type.Elementary: 0>*[??](#csc.parts.Type.Elementary "Permalink to this definition")

    Object *= <Type.Object: 2>*[??](#csc.parts.Type.Object "Permalink to this definition")

    ObjectGroup *= <Type.ObjectGroup: 3>*[??](#csc.parts.Type.ObjectGroup "Permalink to this definition")

    SelectedObjects *= <Type.SelectedObjects: 4>*[??](#csc.parts.Type.SelectedObjects "Permalink to this definition")

    UpdateGroup *= <Type.UpdateGroup: 1>*[??](#csc.parts.Type.UpdateGroup "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.parts.Type.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.parts.Type.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.parts.Type.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.parts.Type.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.parts.Type](#csc.parts.Type "csc.parts.Type")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.parts.Type.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.parts.Type](#csc.parts.Type "csc.parts.Type")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.Type.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.parts.Type](#csc.parts.Type "csc.parts.Type")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.parts.Type.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Elementary': <Type.Elementary: 0>, 'Object': <Type.Object: 2>, 'ObjectGroup': <Type.ObjectGroup: 3>, 'SelectedObjects': <Type.SelectedObjects: 4>, 'UpdateGroup': <Type.UpdateGroup: 1>}*[??](#csc.parts.Type.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.parts'*[??](#csc.parts.Type.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.parts.Type.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.parts.Type.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.parts.Type](#csc.parts.Type "csc.parts.Type")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.Type.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.parts.Type.__str__ "Permalink to this definition")

    *property* name[??](#csc.parts.Type.name "Permalink to this definition")

    *property* value[??](#csc.parts.Type.value "Permalink to this definition")

## csc.external The Cascadeur python module provides basic api to external data formats.[??](#module-csc.external.fbx "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.external.fbx.ExtraDatas`](#csc.external.fbx.ExtraDatas "csc.external.fbx.ExtraDatas") | ExtraDatas class |
| [`csc.external.fbx.FbxDatas`](#csc.external.fbx.FbxDatas "csc.external.fbx.FbxDatas") | FbxDatas class |

*class* csc.external.fbx.ExtraDatas[??](#csc.external.fbx.ExtraDatas "Permalink to this definition")
:   ExtraDatas class

    \_\_annotations\_\_ *= {}*[??](#csc.external.fbx.ExtraDatas.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.external.fbx.ExtraDatas](#csc.external.fbx.ExtraDatas "csc.external.fbx.ExtraDatas")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.external.fbx.ExtraDatas.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.external.fbx'*[??](#csc.external.fbx.ExtraDatas.__module__ "Permalink to this definition")

    *property* look[??](#csc.external.fbx.ExtraDatas.look "Permalink to this definition")

    *property* node\_index[??](#csc.external.fbx.ExtraDatas.node_index "Permalink to this definition")

    *property* post\_rotation[??](#csc.external.fbx.ExtraDatas.post_rotation "Permalink to this definition")

    *property* pre\_rotation[??](#csc.external.fbx.ExtraDatas.pre_rotation "Permalink to this definition")

    *property* size[??](#csc.external.fbx.ExtraDatas.size "Permalink to this definition")

*class* csc.external.fbx.FbxDatas[??](#csc.external.fbx.FbxDatas "Permalink to this definition")
:   FbxDatas class

    \_\_annotations\_\_ *= {}*[??](#csc.external.fbx.FbxDatas.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.external.fbx.FbxDatas](#csc.external.fbx.FbxDatas "csc.external.fbx.FbxDatas")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.external.fbx.FbxDatas.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.external.fbx'*[??](#csc.external.fbx.FbxDatas.__module__ "Permalink to this definition")

    *property* ignore\_namespace[??](#csc.external.fbx.FbxDatas.ignore_namespace "Permalink to this definition")

    *property* order[??](#csc.external.fbx.FbxDatas.order "Permalink to this definition")

    *property* rotation[??](#csc.external.fbx.FbxDatas.rotation "Permalink to this definition")

    *property* scale[??](#csc.external.fbx.FbxDatas.scale "Permalink to this definition")

    *property* translation[??](#csc.external.fbx.FbxDatas.translation "Permalink to this definition")

## csc.fbx The Cascadeur python module provides basic methods to operate fbx.[??](#module-csc.fbx "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.fbx.FbxSettingsMode`](#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode") | FbxSettingsMode enumeration |
| [`csc.fbx.FbxSettingsAxis`](#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis") | FbxSettingsAxis enumeration |
| [`csc.fbx.FbxSettings`](#csc.fbx.FbxSettings "csc.fbx.FbxSettings") | FbxSettings class |
| [`csc.fbx.FbxLoader`](#csc.fbx.FbxLoader "csc.fbx.FbxLoader") | FbxLoader class |
| [`csc.fbx.FbxSceneLoader`](#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader") | FbxSceneLoader class |

*class* csc.fbx.FbxLoader[??](#csc.fbx.FbxLoader "Permalink to this definition")
:   FbxLoader class

    \_\_annotations\_\_ *= {}*[??](#csc.fbx.FbxLoader.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *fps: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *handler: [csc.domain.IMessageHandler](#csc.domain.IMessageHandler "csc.domain.IMessageHandler")*, *scene: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.fbx'*[??](#csc.fbx.FbxLoader.__module__ "Permalink to this definition")

    add\_model(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.add_model "Permalink to this definition")

    add\_model\_to\_selected(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.add_model_to_selected "Permalink to this definition")

    export\_all\_objects(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_all_objects "Permalink to this definition")

    export\_joints(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_joints "Permalink to this definition")

    export\_joints\_selected(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_joints_selected "Permalink to this definition")

    export\_joints\_selected\_frames(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_joints_selected_frames "Permalink to this definition")

    export\_joints\_selected\_objects(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_joints_selected_objects "Permalink to this definition")

    export\_model(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_model "Permalink to this definition")

    export\_scene\_selected(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_scene_selected "Permalink to this definition")

    export\_scene\_selected\_frames(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_scene_selected_frames "Permalink to this definition")

    export\_scene\_selected\_objects(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.export_scene_selected_objects "Permalink to this definition")

    import\_animation(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.import_animation "Permalink to this definition")

    import\_animation\_to\_selected\_frames(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.import_animation_to_selected_frames "Permalink to this definition")

    import\_animation\_to\_selected\_objects(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.import_animation_to_selected_objects "Permalink to this definition")

    import\_model(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.import_model "Permalink to this definition")

    import\_scene(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.import_scene "Permalink to this definition")

    set\_settings(*self: [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")*, *settings: [csc.fbx.FbxSettings](#csc.fbx.FbxSettings "csc.fbx.FbxSettings")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxLoader.set_settings "Permalink to this definition")

*class* csc.fbx.FbxSceneLoader[??](#csc.fbx.FbxSceneLoader "Permalink to this definition")
:   FbxSceneLoader class

    \_\_annotations\_\_ *= {}*[??](#csc.fbx.FbxSceneLoader.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.fbx.FbxSceneLoader.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.fbx'*[??](#csc.fbx.FbxSceneLoader.__module__ "Permalink to this definition")

    export\_fbx\_scene(*self: [csc.fbx.FbxSceneLoader](#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")*, *scene: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSceneLoader.export_fbx_scene "Permalink to this definition")

    get\_fbx\_loader(*self: [csc.fbx.FbxSceneLoader](#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")*, *scene: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*)  [csc.fbx.FbxLoader](#csc.fbx.FbxLoader "csc.fbx.FbxLoader")[??](#csc.fbx.FbxSceneLoader.get_fbx_loader "Permalink to this definition")

    import\_fbx\_animation(*self: [csc.fbx.FbxSceneLoader](#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")*, *scene: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSceneLoader.import_fbx_animation "Permalink to this definition")

    import\_fbx\_scene(*self: [csc.fbx.FbxSceneLoader](#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")*, *scene: [csc.view.Scene](#csc.view.Scene "csc.view.Scene")*, *file\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSceneLoader.import_fbx_scene "Permalink to this definition")

*class* csc.fbx.FbxSettings[??](#csc.fbx.FbxSettings "Permalink to this definition")
:   FbxSettings class

    \_\_annotations\_\_ *= {}*[??](#csc.fbx.FbxSettings.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.fbx.FbxSettings](#csc.fbx.FbxSettings "csc.fbx.FbxSettings")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSettings.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.fbx'*[??](#csc.fbx.FbxSettings.__module__ "Permalink to this definition")

    *property* apply\_euler\_filter[??](#csc.fbx.FbxSettings.apply_euler_filter "Permalink to this definition")

    *property* bake\_animation[??](#csc.fbx.FbxSettings.bake_animation "Permalink to this definition")

    *property* mode[??](#csc.fbx.FbxSettings.mode "Permalink to this definition")

    *property* up\_axis[??](#csc.fbx.FbxSettings.up_axis "Permalink to this definition")

*class* csc.fbx.FbxSettingsAxis[??](#csc.fbx.FbxSettingsAxis "Permalink to this definition")
:   > FbxSettingsAxis enumeration
    >
    > Binary, Ascii

    Members:

    > X
    >
    > Y
    >
    > Z

    X *= <FbxSettingsAxis.X: 0>*[??](#csc.fbx.FbxSettingsAxis.X "Permalink to this definition")

    Y *= <FbxSettingsAxis.Y: 1>*[??](#csc.fbx.FbxSettingsAxis.Y "Permalink to this definition")

    Z *= <FbxSettingsAxis.Z: 2>*[??](#csc.fbx.FbxSettingsAxis.Z "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.fbx.FbxSettingsAxis.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.fbx.FbxSettingsAxis](#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.fbx.FbxSettingsAxis](#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.fbx.FbxSettingsAxis](#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'X': <FbxSettingsAxis.X: 0>, 'Y': <FbxSettingsAxis.Y: 1>, 'Z': <FbxSettingsAxis.Z: 2>}*[??](#csc.fbx.FbxSettingsAxis.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.fbx'*[??](#csc.fbx.FbxSettingsAxis.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.fbx.FbxSettingsAxis](#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.fbx.FbxSettingsAxis.__str__ "Permalink to this definition")

    *property* name[??](#csc.fbx.FbxSettingsAxis.name "Permalink to this definition")

    *property* value[??](#csc.fbx.FbxSettingsAxis.value "Permalink to this definition")

*class* csc.fbx.FbxSettingsMode[??](#csc.fbx.FbxSettingsMode "Permalink to this definition")
:   > FbxSettingsMode enumeration
    >
    > Binary, Ascii

    Members:

    > Binary
    >
    > Ascii

    Ascii *= <FbxSettingsMode.Ascii: 1>*[??](#csc.fbx.FbxSettingsMode.Ascii "Permalink to this definition")

    Binary *= <FbxSettingsMode.Binary: 0>*[??](#csc.fbx.FbxSettingsMode.Binary "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.fbx.FbxSettingsMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.fbx.FbxSettingsMode](#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.fbx.FbxSettingsMode](#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.fbx.FbxSettingsMode](#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Ascii': <FbxSettingsMode.Ascii: 1>, 'Binary': <FbxSettingsMode.Binary: 0>}*[??](#csc.fbx.FbxSettingsMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.fbx'*[??](#csc.fbx.FbxSettingsMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.fbx.FbxSettingsMode](#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.fbx.FbxSettingsMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.fbx.FbxSettingsMode.name "Permalink to this definition")

    *property* value[??](#csc.fbx.FbxSettingsMode.value "Permalink to this definition")

## csc.rig The Cascadeur python module that implements the basic functions for operating a rig.[??](#module-csc.rig "Permalink to this heading")

|  |  |
| --- | --- |
| [`csc.rig.AddElementData`](#csc.rig.AddElementData "csc.rig.AddElementData") |  |
| [`csc.rig.BoneProperty`](#csc.rig.BoneProperty "csc.rig.BoneProperty") |  |
| [`csc.rig.TwistProperty`](#csc.rig.TwistProperty "csc.rig.TwistProperty") |  |
| [`csc.rig.TwistBoneProperty`](#csc.rig.TwistBoneProperty "csc.rig.TwistBoneProperty") |  |
| [`csc.rig.QrtData`](#csc.rig.QrtData "csc.rig.QrtData") |  |

*class* csc.rig.AddElementData[??](#csc.rig.AddElementData "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.rig.AddElementData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.rig.AddElementData.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.rig.AddElementData) -> None
        2. \_\_init\_\_(self: csc.rig.AddElementData, arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: float, arg8: numpy.ndarray[numpy.float32[3, 1]]) -> None

    \_\_module\_\_ *= 'csc.rig'*[??](#csc.rig.AddElementData.__module__ "Permalink to this definition")

    *property* axis\_point\_controller[??](#csc.rig.AddElementData.axis_point_controller "Permalink to this definition")

    *property* box\_multiplier[??](#csc.rig.AddElementData.box_multiplier "Permalink to this definition")

    *property* is\_multiple[??](#csc.rig.AddElementData.is_multiple "Permalink to this definition")

    *property* joint\_size\_without\_child[??](#csc.rig.AddElementData.joint_size_without_child "Permalink to this definition")

    *property* offset\_point\_controller[??](#csc.rig.AddElementData.offset_point_controller "Permalink to this definition")

    *property* only\_box\_controller[??](#csc.rig.AddElementData.only_box_controller "Permalink to this definition")

    *property* orthogonal\_with\_parent[??](#csc.rig.AddElementData.orthogonal_with_parent "Permalink to this definition")

    *property* point\_color[??](#csc.rig.AddElementData.point_color "Permalink to this definition")

    *property* use\_global\_axis[??](#csc.rig.AddElementData.use_global_axis "Permalink to this definition")

*class* csc.rig.BoneProperty[??](#csc.rig.BoneProperty "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.rig.BoneProperty.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.rig.BoneProperty](#csc.rig.BoneProperty "csc.rig.BoneProperty")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.rig.BoneProperty.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.rig'*[??](#csc.rig.BoneProperty.__module__ "Permalink to this definition")

    *property* bone\_name[??](#csc.rig.BoneProperty.bone_name "Permalink to this definition")

    *property* joint\_path\_name[??](#csc.rig.BoneProperty.joint_path_name "Permalink to this definition")

    *property* object\_id[??](#csc.rig.BoneProperty.object_id "Permalink to this definition")

    *property* required\_field[??](#csc.rig.BoneProperty.required_field "Permalink to this definition")

*class* csc.rig.QrtData[??](#csc.rig.QrtData "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.rig.QrtData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.rig.QrtData](#csc.rig.QrtData "csc.rig.QrtData")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.rig.QrtData.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.rig'*[??](#csc.rig.QrtData.__module__ "Permalink to this definition")

    *property* body[??](#csc.rig.QrtData.body "Permalink to this definition")

    *property* hinge\_arm\_direction[??](#csc.rig.QrtData.hinge_arm_direction "Permalink to this definition")

    *property* hinge\_leg\_direction[??](#csc.rig.QrtData.hinge_leg_direction "Permalink to this definition")

    *property* is\_align\_pelvis[??](#csc.rig.QrtData.is_align_pelvis "Permalink to this definition")

    *property* is\_create\_layers[??](#csc.rig.QrtData.is_create_layers "Permalink to this definition")

    *property* is\_replace\_existing[??](#csc.rig.QrtData.is_replace_existing "Permalink to this definition")

    *property* is\_spline\_ik[??](#csc.rig.QrtData.is_spline_ik "Permalink to this definition")

    *property* left\_hand[??](#csc.rig.QrtData.left_hand "Permalink to this definition")

    *property* right\_hand[??](#csc.rig.QrtData.right_hand "Permalink to this definition")

    *property* twists[??](#csc.rig.QrtData.twists "Permalink to this definition")

*class* csc.rig.TwistBoneProperty[??](#csc.rig.TwistBoneProperty "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.rig.TwistBoneProperty.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.rig.TwistBoneProperty](#csc.rig.TwistBoneProperty "csc.rig.TwistBoneProperty")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.rig.TwistBoneProperty.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.rig'*[??](#csc.rig.TwistBoneProperty.__module__ "Permalink to this definition")

    *property* bone\_name[??](#csc.rig.TwistBoneProperty.bone_name "Permalink to this definition")

    *property* twist\_properties[??](#csc.rig.TwistBoneProperty.twist_properties "Permalink to this definition")

*class* csc.rig.TwistProperty[??](#csc.rig.TwistProperty "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.rig.TwistProperty.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.rig.TwistProperty](#csc.rig.TwistProperty "csc.rig.TwistProperty")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.rig.TwistProperty.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.rig'*[??](#csc.rig.TwistProperty.__module__ "Permalink to this definition")

    *property* joint\_path\_name[??](#csc.rig.TwistProperty.joint_path_name "Permalink to this definition")

    *property* object\_id[??](#csc.rig.TwistProperty.object_id "Permalink to this definition")

    *property* twist\_axis[??](#csc.rig.TwistProperty.twist_axis "Permalink to this definition")

    *property* twist\_strength[??](#csc.rig.TwistProperty.twist_strength "Permalink to this definition")

## csc.layers The Cascadeur python module that implements scene layers functionality.[??](#csc-layers-the-cascadeur-python-module-that-implements-scene-layers-functionality "Permalink to this heading")

LayerId == FolderId == ItemId == Guid

|  |  |
| --- | --- |
| [`csc.layers.Header`](#csc.layers.Header "csc.layers.Header") | Header class |
| [`csc.layers.ItemVariant`](#csc.layers.ItemVariant "csc.layers.ItemVariant") | ItemVariant class |
| [`csc.layers.Folder`](#csc.layers.Folder "csc.layers.Folder") | Folder class |
| [`csc.layers.Layer`](#csc.layers.Layer "csc.layers.Layer") | Layer class |
| [`csc.layers.Viewer`](#csc.layers.Viewer "csc.layers.Viewer") | Viewer class |
| [`csc.layers.Editor`](#csc.layers.Editor "csc.layers.Editor") | Editor class |
| [`csc.layers.Selector`](#csc.layers.Selector "csc.layers.Selector") | Selector class |
| [`csc.layers.LayersContainer`](#csc.layers.LayersContainer "csc.layers.LayersContainer") | LayersContainer class |
| [`csc.layers.UserLabelData`](#csc.layers.UserLabelData "csc.layers.UserLabelData") | UserLabelData class |
| [`csc.layers.Layers`](#csc.layers.Layers "csc.layers.Layers") | Layers class |
| [`csc.layers.Cycle`](#csc.layers.Cycle "csc.layers.Cycle") | Cycle class |
| [`csc.layers.CyclesViewer`](#csc.layers.CyclesViewer "csc.layers.CyclesViewer") | Cycle viewer class |
| [`csc.layers.CyclesEditor`](#csc.layers.CyclesEditor "csc.layers.CyclesEditor") | Cycle editor class |
| [`csc.layers.LayersSelectionChanger`](#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger") | Layer SelectionChanger class |
| [`csc.layers.layer.Interpolation`](_generate/csc.layers.layer.Interpolation.html#csc.layers.layer.Interpolation "csc.layers.layer.Interpolation") | Interpolation enumerable |
| [`csc.layers.layer.Tangents`](_generate/csc.layers.layer.Tangents.html#csc.layers.layer.Tangents "csc.layers.layer.Tangents") | Layer Frame Tangents enumerable |
| [`csc.layers.layer.IkFk`](_generate/csc.layers.layer.IkFk.html#csc.layers.layer.IkFk "csc.layers.layer.IkFk") | Layer Frame IkFk enumerable |
| [`csc.layers.layer.Fixation`](_generate/csc.layers.layer.Fixation.html#csc.layers.layer.Fixation "csc.layers.layer.Fixation") | Layer Frame Fixation enumerable |
| [`csc.layers.layer.Common`](_generate/csc.layers.layer.Common.html#csc.layers.layer.Common "csc.layers.layer.Common") | Common class |
| [`csc.layers.layer.Key`](_generate/csc.layers.layer.Key.html#csc.layers.layer.Key "csc.layers.layer.Key") | Key class |
| [`csc.layers.layer.Interval`](_generate/csc.layers.layer.Interval.html#csc.layers.layer.Interval "csc.layers.layer.Interval") | Interval class |
| [`csc.layers.layer.Section`](_generate/csc.layers.layer.Section.html#csc.layers.layer.Section "csc.layers.layer.Section") | Section class |
| [`csc.layers.layer.Cell`](_generate/csc.layers.layer.Cell.html#csc.layers.layer.Cell "csc.layers.layer.Cell") | Cell class |
| [`csc.layers.index.FramesInterval`](_generate/csc.layers.index.FramesInterval.html#csc.layers.index.FramesInterval "csc.layers.index.FramesInterval") | FramesInterval class |
| [`csc.layers.index.FramesIndices`](_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices") | FramesIndices class |
| [`csc.layers.index.CellIndex`](_generate/csc.layers.index.CellIndex.html#csc.layers.index.CellIndex "csc.layers.index.CellIndex") | CellIndex class |
| [`csc.layers.index.RectIndicesContainer`](_generate/csc.layers.index.RectIndicesContainer.html#csc.layers.index.RectIndicesContainer "csc.layers.index.RectIndicesContainer") | RectIndicesContainer class |
| [`csc.layers.index.IndicesContainer`](_generate/csc.layers.index.IndicesContainer.html#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer") | IndicesContainer class |

*class* csc.layers.Cycle[??](#csc.layers.Cycle "Permalink to this definition")
:   Cycle class

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Cycle.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Cycle.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Cycle.__module__ "Permalink to this definition")

    *property* first\_active\_frame\_index[??](#csc.layers.Cycle.first_active_frame_index "Permalink to this definition")

    *property* following\_interval[??](#csc.layers.Cycle.following_interval "Permalink to this definition")

    *static* get\_no\_pos()  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Cycle.get_no_pos "Permalink to this definition")

    is\_the\_same\_frames\_as(*self: [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")*, *other\_cycle: [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Cycle.is_the_same_frames_as "Permalink to this definition")
    :   -> bool

    *property* last\_active\_frame\_index[??](#csc.layers.Cycle.last_active_frame_index "Permalink to this definition")

    left\_frame\_index(*self: [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Cycle.left_frame_index "Permalink to this definition")
    :   -> Pos

    *property* left\_inactive\_frame\_index[??](#csc.layers.Cycle.left_inactive_frame_index "Permalink to this definition")

    right\_frame\_index(*self: [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Cycle.right_frame_index "Permalink to this definition")
    :   -> Pos

    *property* right\_inactive\_frame\_index[??](#csc.layers.Cycle.right_inactive_frame_index "Permalink to this definition")

*class* csc.layers.CyclesEditor[??](#csc.layers.CyclesEditor "Permalink to this definition")
:   Cycle editor class

    \_\_annotations\_\_ *= {}*[??](#csc.layers.CyclesEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.layers.CyclesEditor](#csc.layers.CyclesEditor "csc.layers.CyclesEditor")*, *layer: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.CyclesEditor.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.CyclesEditor.__module__ "Permalink to this definition")

    change\_inactive\_parts(*self: [csc.layers.CyclesEditor](#csc.layers.CyclesEditor "csc.layers.CyclesEditor")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg2: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.CyclesEditor.change_inactive_parts "Permalink to this definition")

    create\_cycle(*self: [csc.layers.CyclesEditor](#csc.layers.CyclesEditor "csc.layers.CyclesEditor")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg2: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")[??](#csc.layers.CyclesEditor.create_cycle "Permalink to this definition")

    delete\_cycle(*self: [csc.layers.CyclesEditor](#csc.layers.CyclesEditor "csc.layers.CyclesEditor")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.CyclesEditor.delete_cycle "Permalink to this definition")

    find\_cycle(*self: [csc.layers.CyclesEditor](#csc.layers.CyclesEditor "csc.layers.CyclesEditor")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.CyclesEditor.find_cycle "Permalink to this definition")

    normalize(*self: [csc.layers.CyclesEditor](#csc.layers.CyclesEditor "csc.layers.CyclesEditor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.CyclesEditor.normalize "Permalink to this definition")

*class* csc.layers.CyclesViewer[??](#csc.layers.CyclesViewer "Permalink to this definition")
:   Cycle viewer class

    \_\_annotations\_\_ *= {}*[??](#csc.layers.CyclesViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *layer: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.CyclesViewer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.CyclesViewer.__module__ "Permalink to this definition")

    any\_cycles\_exist\_in\_frames(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.any_cycles_exist_in_frames "Permalink to this definition")

    cycle\_contains\_frame\_index(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.cycle_contains_frame_index "Permalink to this definition")

    find\_cycle(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.CyclesViewer.find_cycle "Permalink to this definition")

    get\_active\_pos(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.CyclesViewer.get_active_pos "Permalink to this definition")

    get\_active\_section\_pos(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.CyclesViewer.get_active_section_pos "Permalink to this definition")

    get\_cycles\_in\_frames(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")][??](#csc.layers.CyclesViewer.get_cycles_in_frames "Permalink to this definition")

    get\_most\_left\_and\_right\_frame\_indices\_of\_cycle(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [csc.layers.Cycle](#csc.layers.Cycle "csc.layers.Cycle")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][??](#csc.layers.CyclesViewer.get_most_left_and_right_frame_indices_of_cycle "Permalink to this definition")

    is\_pos\_in\_active\_cycle\_zone(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.is_pos_in_active_cycle_zone "Permalink to this definition")

    is\_pos\_in\_inactive\_cycle\_zone(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.is_pos_in_inactive_cycle_zone "Permalink to this definition")

    last\_pos(*self: [csc.layers.CyclesViewer](#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.CyclesViewer.last_pos "Permalink to this definition")

*class* csc.layers.Editor[??](#csc.layers.Editor "Permalink to this definition")
:   Editor class

    This class contains all methods and properties that need to edit the structure of scene objects??? interpolation properties.
    The structure is represented in the hierarchy of layers divided by folders.

    Variables:
    :   * **create\_folder** ??? name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId
        * **create\_layer** ??? name : string, parent : FolderId, pos : int or None, -> FolderId
        * **set\_fixed\_interpolation\_if\_need** ??? overridden method by ItemId, int, int || LayerId, int (frame)
        * **set\_fixed\_interpolation\_or\_key\_if\_need** ??? overridden method by LayerId, int, bool

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Editor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Editor.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Editor.__module__ "Permalink to this definition")

    change\_section(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [csc.Guid](#csc.Guid "csc.Guid")*, *arg2: Callable*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.change_section "Permalink to this definition")

    clear(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.clear "Permalink to this definition")

    create\_folder(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *parent: [csc.Guid](#csc.Guid "csc.Guid")*, *with\_default\_layer: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = None*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Editor.create_folder "Permalink to this definition")
    :   name : string | parent : FolderId | withDefaultLayer : bool (true) | pos : int or None | -> FolderId

    create\_layer(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *parent: [csc.Guid](#csc.Guid "csc.Guid")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = None*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Editor.create_layer "Permalink to this definition")
    :   name : string | parent : FolderId | pos : int or None | -> FolderId

    delete\_empty\_folders(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_empty_folders "Permalink to this definition")

    delete\_empty\_layers(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_empty_layers "Permalink to this definition")

    delete\_folder(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_folder "Permalink to this definition")

    delete\_layer(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.delete_layer "Permalink to this definition")

    find\_header(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *arg0: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Editor.find_header "Permalink to this definition")
    :   -> Header

    insert\_layer(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *layer: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.insert_layer "Permalink to this definition")
    :   layer : Layer | pos : int or None

    move\_item(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *item\_id: [csc.Guid](#csc.Guid "csc.Guid")*, *folder\_id: [csc.Guid](#csc.Guid "csc.Guid")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = None*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.move_item "Permalink to this definition")
    :   pos : int or None

    normalize\_sections(*self: csc.layers.Editor*, *scene: domain::scene::Scene*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.normalize_sections "Permalink to this definition")

    set\_default(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_default "Permalink to this definition")

    set\_fixed\_interpolation\_if\_need(*\*args*, *\*\*kwargs*)[??](#csc.layers.Editor.set_fixed_interpolation_if_need "Permalink to this definition")
    :   Overloaded function.

        1. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool
        2. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool

    set\_fixed\_interpolation\_or\_key\_if\_need(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *set\_key: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Editor.set_fixed_interpolation_or_key_if_need "Permalink to this definition")

    set\_locked\_for\_item(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *is\_l: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_locked_for_item "Permalink to this definition")
    :   isL : bool | id : ItemId

    set\_locked\_for\_layer(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *is\_l: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_locked_for_layer "Permalink to this definition")
    :   isL : bool | id : LayerId

    set\_name(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_name "Permalink to this definition")

    set\_section(*self: csc.layers.Editor*, *section: domain::scene::layers::layer::Section*, *pos: int*, *id: csc.Guid*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_section "Permalink to this definition")
    :   section : Section | pos : int | id : ItemId

    set\_sections(*self: csc.layers.Editor, arg0: dict[int, domain::scene::layers::layer::Section], arg1: csc.Guid*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_sections "Permalink to this definition")
    :   section : <Pos, Section>{} | id : LayerId

    set\_visible\_for\_item(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *is\_v: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_visible_for_item "Permalink to this definition")
    :   isV : bool | id : ItemId

    set\_visible\_for\_layer(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *is\_v: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.set_visible_for_layer "Permalink to this definition")
    :   isV : bool | id : LayerId

    unset\_section(*self: [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Editor.unset_section "Permalink to this definition")
    :   pos : int | id : ItemId

*class* csc.layers.Folder[??](#csc.layers.Folder "Permalink to this definition")
:   Folder class

    Implements the parent folder properties of children layers and sub folders items

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Folder.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Folder.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Folder.__module__ "Permalink to this definition")

    child\_by\_id(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Folder.child_by_id "Permalink to this definition")
    :   -> ItemId

    child\_by\_pos(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Folder.child_by_pos "Permalink to this definition")
    :   pos : int
        -> ItemId

    child\_pos(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Folder.child_pos "Permalink to this definition")
    :   id : ItemId | -> int

    children\_cnt(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Folder.children_cnt "Permalink to this definition")
    :   -> int

    children\_ids(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Folder.children_ids "Permalink to this definition")
    :   -> ItemId[]

    children\_ordered(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Folder.children_ordered "Permalink to this definition")
    :   -> ItemId[]

    has\_child(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Folder.has_child "Permalink to this definition")

    *property* header[??](#csc.layers.Folder.header "Permalink to this definition")
    :   -> Header

    is\_empty(*self: [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Folder.is_empty "Permalink to this definition")

*class* csc.layers.Header[??](#csc.layers.Header "Permalink to this definition")
:   Header class

    Describes the header properties for a folder

    Variables:
    :   * **parent** ??? Get set csc.Guid
        * **id** ??? Get set csc.Guid
        * **name** ??? Get set string

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Header.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Header.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Header.__module__ "Permalink to this definition")

    *property* id[??](#csc.layers.Header.id "Permalink to this definition")

    *property* name[??](#csc.layers.Header.name "Permalink to this definition")

    *property* parent[??](#csc.layers.Header.parent "Permalink to this definition")

*class* csc.layers.ItemVariant[??](#csc.layers.ItemVariant "Permalink to this definition")
:   ItemVariant class

    Can implement a folder or layer for a header

    \_\_annotations\_\_ *= {}*[??](#csc.layers.ItemVariant.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.ItemVariant.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.ItemVariant.__module__ "Permalink to this definition")

    folder(*self: [csc.layers.ItemVariant](#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  domain::scene::layers::Folder[??](#csc.layers.ItemVariant.folder "Permalink to this definition")
    :   -> Folder (if it has folder otherwise none)

    header(*self: [csc.layers.ItemVariant](#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  [csc.layers.Header](#csc.layers.Header "csc.layers.Header")[??](#csc.layers.ItemVariant.header "Permalink to this definition")
    :   -> Header

    is\_folder(*self: [csc.layers.ItemVariant](#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.ItemVariant.is_folder "Permalink to this definition")

    is\_layer(*self: [csc.layers.ItemVariant](#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.ItemVariant.is_layer "Permalink to this definition")

    layer(*self: [csc.layers.ItemVariant](#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  domain::scene::layers::Layer[??](#csc.layers.ItemVariant.layer "Permalink to this definition")
    :   -> Layer (if it has layer otherwise none)

*class* csc.layers.Layer[??](#csc.layers.Layer "Permalink to this definition")
:   Layer class

    The Layer is the basic element that implements intervals and sections to set
    interpolation properties of scene objects

    Variables:
    :   * **header** ??? Get Header
        * **is\_locked** ??? Get bool
        * **is\_visible** ??? Get bool
        * **obj\_ids** ??? Get csc.Guid{}
        * **sections** ??? Get std::map<Pos, Section>

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Layer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Layer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Layer.__module__ "Permalink to this definition")

    actual\_key(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Key[??](#csc.layers.Layer.actual_key "Permalink to this definition")
    :   -> Key

    actual\_key\_pos(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Layer.actual_key_pos "Permalink to this definition")
    :   -> int

    actual\_section(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Section[??](#csc.layers.Layer.actual_section "Permalink to this definition")
    :   -> Section

    actual\_section\_pos(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Layer.actual_section_pos "Permalink to this definition")
    :   -> int

    find\_section(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Layer.find_section "Permalink to this definition")
    :   pos : int | -> Section

    *property* header[??](#csc.layers.Layer.header "Permalink to this definition")

    interval(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Interval[??](#csc.layers.Layer.interval "Permalink to this definition")
    :   -> Interval

    is\_key(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Layer.is_key "Permalink to this definition")

    is\_key\_or\_fixed(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Layer.is_key_or_fixed "Permalink to this definition")

    *property* is\_locked[??](#csc.layers.Layer.is_locked "Permalink to this definition")

    *property* is\_visible[??](#csc.layers.Layer.is_visible "Permalink to this definition")

    key(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Key[??](#csc.layers.Layer.key "Permalink to this definition")
    :   -> Key

    key\_frame\_indices(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*)  domain::scene::layers::index::FramesIndices[??](#csc.layers.Layer.key_frame_indices "Permalink to this definition")
    :   -> FramesIndices

    last\_key\_pos(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Layer.last_key_pos "Permalink to this definition")
    :   -> int

    *property* obj\_ids[??](#csc.layers.Layer.obj_ids "Permalink to this definition")
    :   -> csc.model.ObjectId{}

    section(*self: [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Section[??](#csc.layers.Layer.section "Permalink to this definition")
    :   -> Section

    *property* sections[??](#csc.layers.Layer.sections "Permalink to this definition")
    :   -> std::map<Pos, Section>

*class* csc.layers.Layers[??](#csc.layers.Layers "Permalink to this definition")
:   Layers class

    The root class describes the layers??? hierarchy of the scene.
    Each scene object can be placed on any layer to define its personal interpolation properties.

    Variables:
    :   **root\_id** ??? Get csc.Guid

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Layers.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Layers.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Layers.__module__ "Permalink to this definition")

    folders(*self: [csc.layers.Layers](#csc.layers.Layers "csc.layers.Layers")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Layers.folders "Permalink to this definition")
    :   -> <FolderId, Folder>{}

    layers(*self: [csc.layers.Layers](#csc.layers.Layers "csc.layers.Layers")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Layers.layers "Permalink to this definition")
    :   -> LayersContainer

    *property* root\_id[??](#csc.layers.Layers.root_id "Permalink to this definition")

    userLabels(*self: [csc.layers.Layers](#csc.layers.Layers "csc.layers.Layers")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Layers.userLabels "Permalink to this definition")
    :   -> UserLabels

*class* csc.layers.LayersContainer[??](#csc.layers.LayersContainer "Permalink to this definition")
:   LayersContainer class

    It is the container of layers.

    \_\_annotations\_\_ *= {}*[??](#csc.layers.LayersContainer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.LayersContainer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.LayersContainer.__module__ "Permalink to this definition")

    at(*self: [csc.layers.LayersContainer](#csc.layers.LayersContainer "csc.layers.LayersContainer")*, *arg0: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.LayersContainer.at "Permalink to this definition")
    :   -> Layer

    has\_any\_obj\_ids(*self: [csc.layers.LayersContainer](#csc.layers.LayersContainer "csc.layers.LayersContainer")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersContainer.has_any_obj_ids "Permalink to this definition")

    has\_obj\_id(*self: csc.layers.LayersContainer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersContainer.has_obj_id "Permalink to this definition")

    layer\_id\_by\_obj\_id(*self: csc.layers.LayersContainer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.LayersContainer.layer_id_by_obj_id "Permalink to this definition")
    :   -> LayerId

    layer\_id\_by\_obj\_id\_or\_null(*self: csc.layers.LayersContainer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.LayersContainer.layer_id_by_obj_id_or_null "Permalink to this definition")
    :   -> LayerId

    map(*self: [csc.layers.LayersContainer](#csc.layers.LayersContainer "csc.layers.LayersContainer")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.LayersContainer.map "Permalink to this definition")
    :   -> <LayerId, Layer>{}

    obj\_ids(*self: [csc.layers.LayersContainer](#csc.layers.LayersContainer "csc.layers.LayersContainer")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.LayersContainer.obj_ids "Permalink to this definition")
    :   -> <csc.model.ObjectId, LayerId>{}

*class* csc.layers.LayersSelectionChanger[??](#csc.layers.LayersSelectionChanger "Permalink to this definition")
:   Layer SelectionChanger class

    \_\_annotations\_\_ *= {}*[??](#csc.layers.LayersSelectionChanger.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.LayersSelectionChanger.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.LayersSelectionChanger.__module__ "Permalink to this definition")

    refresh(*self: [csc.layers.LayersSelectionChanger](#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersSelectionChanger.refresh "Permalink to this definition")

    selectDefault(*self: [csc.layers.LayersSelectionChanger](#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersSelectionChanger.selectDefault "Permalink to this definition")

    set\_full\_selection\_by\_parts(*\*args*, *\*\*kwargs*)[??](#csc.layers.LayersSelectionChanger.set_full_selection_by_parts "Permalink to this definition")
    :   Overloaded function.

        1. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None

           > inds : IndicesContainer
        2. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, itms: list[csc.Guid], first: int, last: int) -> bool

*class* csc.layers.Selector[??](#csc.layers.Selector "Permalink to this definition")
:   Selector class

    This class contains methods to observe and to set selected layers and folders

    Variables:
    :   **set\_full\_selection\_by\_parts** ??? overridden method by ItemId[] (itms), int (first), int (last) || IndicesContainer (inds)

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Selector.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Selector.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Selector.__module__ "Permalink to this definition")

    all\_included\_layer\_ids(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Selector.all_included_layer_ids "Permalink to this definition")
    :   ignoreLocked : bool (false) | -> LayerId[]

    all\_included\_layer\_indices(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  domain::scene::layers::index::IndicesContainer[??](#csc.layers.Selector.all_included_layer_indices "Permalink to this definition")
    :   ignoreLocked : bool (false) | -> IndicesContainer

    is\_selected(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Selector.is_selected "Permalink to this definition")

    select\_default(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Selector.select_default "Permalink to this definition")

    selection(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*)  domain::scene::layers::index::IndicesContainer[??](#csc.layers.Selector.selection "Permalink to this definition")
    :   -> IndicesContainer

    set\_full\_selection\_by\_parts(*\*args*, *\*\*kwargs*)[??](#csc.layers.Selector.set_full_selection_by_parts "Permalink to this definition")
    :   Overloaded function.

        1. set\_full\_selection\_by\_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None

           > inds : IndicesContainer
        2. set\_full\_selection\_by\_parts(self: csc.layers.Selector, itms: list[csc.Guid], first: int, last: int) -> None

    set\_uncheckable\_folder\_id(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*, *uncheckable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Selector.set_uncheckable_folder_id "Permalink to this definition")
    :   id : ItemId | uncheckable : bool

    top\_layer\_id(*self: [csc.layers.Selector](#csc.layers.Selector "csc.layers.Selector")*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Selector.top_layer_id "Permalink to this definition")

*class* csc.layers.UserLabelData[??](#csc.layers.UserLabelData "Permalink to this definition")
:   UserLabelData class

    The data of user defined label.

    \_\_annotations\_\_ *= {}*[??](#csc.layers.UserLabelData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.UserLabelData.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.UserLabelData.__module__ "Permalink to this definition")

    *property* color[??](#csc.layers.UserLabelData.color "Permalink to this definition")

    *property* id[??](#csc.layers.UserLabelData.id "Permalink to this definition")

    *property* name[??](#csc.layers.UserLabelData.name "Permalink to this definition")

*class* csc.layers.UserLabels[??](#csc.layers.UserLabels "Permalink to this definition")
:   UserLabels class

    It is the storage of user defined labels.

    \_\_annotations\_\_ *= {}*[??](#csc.layers.UserLabels.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.UserLabels.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.UserLabels.__module__ "Permalink to this definition")

    add(*self: [csc.layers.UserLabels](#csc.layers.UserLabels "csc.layers.UserLabels")*, *label: [csc.layers.UserLabelData](#csc.layers.UserLabelData "csc.layers.UserLabelData")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.UserLabels.add "Permalink to this definition")

    find(*self: [csc.layers.UserLabels](#csc.layers.UserLabels "csc.layers.UserLabels")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.UserLabels.find "Permalink to this definition")
    :   -> index

    remove(*\*args*, *\*\*kwargs*)[??](#csc.layers.UserLabels.remove "Permalink to this definition")
    :   Overloaded function.

        1. remove(self: csc.layers.UserLabels, index: int) -> None
        2. remove(self: csc.layers.UserLabels, arg0: int) -> object

           > -> UserLabelData

    storage(*self: [csc.layers.UserLabels](#csc.layers.UserLabels "csc.layers.UserLabels")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.UserLabels.storage "Permalink to this definition")
    :   -> UserLabelData[]

*class* csc.layers.Viewer[??](#csc.layers.Viewer "Permalink to this definition")
:   Viewer class

    This class contains all methods and properties that describe the structure of scene objects??? interpolation properties.
    The structure is represented in the hierarchy of layers divided by folders.

    Variables:
    :   * **top\_layer\_id** ??? overridden method by ItemId || ItemId[]
        * **merged\_layer** ??? overridden method like static and member LayerId[]
        * **last\_key\_pos** ??? overridden method by LayerId[], -> Layer
        * **frames\_count** ??? overridden method by LayerId[], -> int
        * **significant\_frames** ??? overridden method by LayerId{}, -> int{}

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Viewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Viewer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Viewer.__module__ "Permalink to this definition")

    actual\_key\_pos(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Viewer.actual_key_pos "Permalink to this definition")

    all\_child\_ids(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Viewer.all_child_ids "Permalink to this definition")
    :   -> ItemId[]

    all\_included\_layer\_ids(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *items: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")]*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Viewer.all_included_layer_ids "Permalink to this definition")
    :   items : ItemId[] | ignoreLocked : bool (false) | -> LayerId[]

    all\_layer\_ids(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Viewer.all_layer_ids "Permalink to this definition")
    :   -> LayerId[]

    all\_parent\_ids(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Viewer.all_parent_ids "Permalink to this definition")
    :   -> FolderId[]

    default\_layer\_id(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Viewer.default_layer_id "Permalink to this definition")
    :   -> LayerId

    find\_folder(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Viewer.find_folder "Permalink to this definition")
    :   id : FolderId | -> Folder

    find\_layer(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Viewer.find_layer "Permalink to this definition")
    :   id : LayerId | -> Layer

    folder(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Viewer.folder "Permalink to this definition")
    :   id : FolderId | -> Folder

    folders\_map(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid"), [csc.layers.Folder](#csc.layers.Folder "csc.layers.Folder")][??](#csc.layers.Viewer.folders_map "Permalink to this definition")
    :   -> <FolderId, Folder>{}

    for\_all\_ordered\_items(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *arg0: Callable[[[csc.Guid](#csc.Guid "csc.Guid")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.Viewer.for_all_ordered_items "Permalink to this definition")

    frames\_count(*\*args*, *\*\*kwargs*)[??](#csc.layers.Viewer.frames_count "Permalink to this definition")
    :   Overloaded function.

        1. frames\_count(self: csc.layers.Viewer) -> int
        2. frames\_count(self: csc.layers.Viewer, id\_arr: list[csc.Guid]) -> int

    has\_item(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Viewer.has_item "Permalink to this definition")
    :   -> bool

    header(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Viewer.header "Permalink to this definition")
    :   id : ItemId | -> Header

    is\_deep\_child(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *item\_id: [csc.Guid](#csc.Guid "csc.Guid")*, *folder\_id: [csc.Guid](#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Viewer.is_deep_child "Permalink to this definition")
    :   -> bool

    item(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [csc.layers.ItemVariant](#csc.layers.ItemVariant "csc.layers.ItemVariant")[??](#csc.layers.Viewer.item "Permalink to this definition")
    :   id : ItemId | -> ItemVariant

    last\_key\_pos(*\*args*, *\*\*kwargs*)[??](#csc.layers.Viewer.last_key_pos "Permalink to this definition")
    :   Overloaded function.

        1. last\_key\_pos(self: csc.layers.Viewer) -> int
        2. last\_key\_pos(self: csc.layers.Viewer, id\_arr: list[csc.Guid]) -> int

    layer(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Viewer.layer "Permalink to this definition")
    :   id : LayerId | -> Layer

    layer\_id\_by\_obj\_id(*self: csc.layers.Viewer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Viewer.layer_id_by_obj_id "Permalink to this definition")
    :   id : csc.model.ObjectId | -> LayerId

    layer\_id\_by\_obj\_id\_or\_null(*self: csc.layers.Viewer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Viewer.layer_id_by_obj_id_or_null "Permalink to this definition")
    :   id : csc.model.ObjectId | -> LayerId

    layer\_ids\_by\_obj\_ids(*self: csc.layers.Viewer, ids: list[common::GenericId<domain::scene::model::ModelObject>]*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Viewer.layer_ids_by_obj_ids "Permalink to this definition")
    :   ids : csc.model.ObjectId[] | -> LayerId{}

    layers\_indices(*self: csc.layers.Viewer*, *id\_arr: domain::scene::layers::index::IndicesContainer*, *ignore\_locked: bool = False*)  domain::scene::layers::index::IndicesContainer[??](#csc.layers.Viewer.layers_indices "Permalink to this definition")
    :   -> IndicesContainer

    layers\_map(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid"), [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")][??](#csc.layers.Viewer.layers_map "Permalink to this definition")
    :   -> <LayerId, Layer>{}

    merged\_layer(*self: csc.layers.Viewer, scene: domain::scene::Scene, ids: list[csc.Guid], normalize: bool = True*)  [csc.layers.Layer](#csc.layers.Layer "csc.layers.Layer")[??](#csc.layers.Viewer.merged_layer "Permalink to this definition")

    obj\_ids\_by\_layer\_ids(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id\_arr: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")]*)  list[common::GenericId<domain::scene::model::ModelObject>][??](#csc.layers.Viewer.obj_ids_by_layer_ids "Permalink to this definition")
    :   -> LayerId[]

    pos\_in\_parent(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id: [csc.Guid](#csc.Guid "csc.Guid")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Viewer.pos_in_parent "Permalink to this definition")
    :   -> int

    root\_id(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*)  [csc.Guid](#csc.Guid "csc.Guid")[??](#csc.layers.Viewer.root_id "Permalink to this definition")
    :   -> FolderId

    significant\_frames(*\*args*, *\*\*kwargs*)[??](#csc.layers.Viewer.significant_frames "Permalink to this definition")
    :   Overloaded function.

        1. significant\_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices
        2. significant\_frames(self: csc.layers.Viewer, id\_arr: set[csc.Guid]) -> domain::scene::layers::index::FramesIndices

    top\_layer\_id(*\*args*, *\*\*kwargs*)[??](#csc.layers.Viewer.top_layer_id "Permalink to this definition")
    :   Overloaded function.

        1. top\_layer\_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid
        2. top\_layer\_id(self: csc.layers.Viewer, id\_arr: list[csc.Guid]) -> csc.Guid

    unlocked\_layer\_ids(*self: [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")*, *id\_arr: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")]*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](#csc.Guid "csc.Guid")][??](#csc.layers.Viewer.unlocked_layer_ids "Permalink to this definition")
    :   -> LayerId[]

## csc.model The Cascadeur python module that implements model and behaviors scene editors methods.[??](#csc-model-the-cascadeur-python-module-that-implements-model-and-behaviors-scene-editors-methods "Permalink to this heading")

Data.Value = std::variant<bool, int, float, Eigen::Vector3f, math::Rotation,
:   Eigen::Matrix3f, Eigen::Matrix4f, Eigen::Quaternionf,
    std::string, common::Vector3b>;

Setting.Value = std::variant<bool, int>;

ClusterId = int

|  |  |
| --- | --- |
| [`csc.model.Data`](#csc.model.Data "csc.model.Data") | Data class |
| [`csc.model.Setting`](#csc.model.Setting "csc.model.Setting") | Setting class |
| [`csc.model.ClusterViewer`](#csc.model.ClusterViewer "csc.model.ClusterViewer") | ClusterViewer class |
| [`csc.model.ClusterEditor`](#csc.model.ClusterEditor "csc.model.ClusterEditor") | ClusterEditor class |
| [`csc.model.DataViewer`](#csc.model.DataViewer "csc.model.DataViewer") | DataViewer class |
| [`csc.model.DataEditor`](#csc.model.DataEditor "csc.model.DataEditor") | DataEditor class |
| [`csc.model.BehaviourViewer`](#csc.model.BehaviourViewer "csc.model.BehaviourViewer") | BehaviourViewer class |
| [`csc.model.BehaviourEditor`](#csc.model.BehaviourEditor "csc.model.BehaviourEditor") | BehaviourEditor class |
| [`csc.model.ModelViewer`](#csc.model.ModelViewer "csc.model.ModelViewer") | ModelViewer class |
| [`csc.model.ModelEditor`](#csc.model.ModelEditor "csc.model.ModelEditor") | ModelEditor class |
| [`csc.model.DataMode`](#csc.model.DataMode "csc.model.DataMode") | Data::Mode enum |
| [`csc.model.SettingMode`](#csc.model.SettingMode "csc.model.SettingMode") | Setting::Mode enum |
| [`csc.model.ObjectId`](#csc.model.ObjectId "csc.model.ObjectId") |  |
| [`csc.model.DataId`](#csc.model.DataId "csc.model.DataId") |  |
| [`csc.model.BehaviourId`](#csc.model.BehaviourId "csc.model.BehaviourId") |  |
| [`csc.model.SettingId`](#csc.model.SettingId "csc.model.SettingId") |  |
| [`csc.model.HyperedgeId`](#csc.model.HyperedgeId "csc.model.HyperedgeId") |  |
| [`csc.model.SettingFunctionId`](#csc.model.SettingFunctionId "csc.model.SettingFunctionId") |  |
| [`csc.model.LerpMode`](#csc.model.LerpMode "csc.model.LerpMode") | LerpMode enumerable |
| [`csc.model.DescriptionTerm`](#csc.model.DescriptionTerm "csc.model.DescriptionTerm") |  |
| [`csc.model.CustomSelectionPolicy`](#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy") | CustomSelectionPolicy enumerable |
| [`csc.model.PropertyType`](#csc.model.PropertyType "csc.model.PropertyType") | PropertyType enumerable |
| [`csc.model.PathName`](#csc.model.PathName "csc.model.PathName") |  |
| [`csc.model.ClustersEdge`](#csc.model.ClustersEdge "csc.model.ClustersEdge") | ClustersEdge class |

*class* csc.model.BehaviourEditor[??](#csc.model.BehaviourEditor "Permalink to this definition")
:   BehaviourEditor class

    This class allows editing of scene behaviours and their properties.

    \_\_annotations\_\_ *= {}*[??](#csc.model.BehaviourEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourEditor.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.BehaviourEditor.__module__ "Permalink to this definition")

    add\_behaviour(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourEditor.add_behaviour "Permalink to this definition")
    :   Overloaded function.

        1. add\_behaviour(self: csc.model.BehaviourEditor, arg0: csc.model.ObjectId, arg1: str) -> csc.model.BehaviourId

           > object\_id : csc.model.ObjectId | behaviour\_type : string | -> csc.model.BehaviourId
        2. add\_behaviour(self: csc.model.BehaviourEditor, object\_id: csc.model.ObjectId, behaviour\_type: str, behaviour\_id: csc.model.BehaviourId) -> csc.model.BehaviourId

           > object\_id : csc.model.ObjectId | behaviour\_type : string | behaviour\_id : csc.model.BehaviourId | -> csc.model.BehaviourId

    add\_behaviour\_asset\_to\_range(*self: csc.model.BehaviourEditor*, *behaviour\_id: csc.model.BehaviourId*, *name: str*, *asset\_id: common::GenericId<domain::scene::assets::Asset>*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_asset_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | asset\_id : csc.domain.AssetId

    add\_behaviour\_data\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *data\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_data_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | data\_id : csc.model.DataId

    add\_behaviour\_model\_object\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *mo\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_model_object_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId

    add\_behaviour\_reference\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *beh\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_reference_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId

    add\_behaviour\_setting\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *setting\_id: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_setting_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId

    delete\_behaviour(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.BehaviourEditor.delete_behaviour "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId

    delete\_behaviours(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *objects\_id: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.BehaviourEditor.delete_behaviours "Permalink to this definition")
    :   objectsId : {csc.model.ObjectId}

    erase\_behaviour\_data\_from\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *data\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_data_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | data\_id : csc.model.DataId

    erase\_behaviour\_model\_object\_from\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *mo\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_model_object_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId

    erase\_behaviour\_reference\_from\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *beh\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_reference_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId

    erase\_behaviour\_setting\_from\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *setting\_id: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_setting_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId

    get\_viewer(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*)  [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")[??](#csc.model.BehaviourEditor.get_viewer "Permalink to this definition")

    hide\_behaviour(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *hidden: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.hide_behaviour "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | hidden : bool(true) -> bool

    set\_behaviour\_asset(*self: csc.model.BehaviourEditor*, *behaviour\_id: csc.model.BehaviourId*, *name: str*, *asset\_id: common::GenericId<domain::scene::assets::Asset>*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_asset "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | asset\_id : csc.domain.AssetId

    set\_behaviour\_data(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *data\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_data "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | dataId : csc.model.DataId

    set\_behaviour\_data\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_data_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.DataId

    set\_behaviour\_field\_value(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *name\_value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_field_value "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | name\_value : string

    set\_behaviour\_model\_object(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *mo\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_model_object "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId

    set\_behaviour\_model\_objects\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_model_objects_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.ObjectId[]

    set\_behaviour\_reference(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *beh\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_reference "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId

    set\_behaviour\_references\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_references_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.BehaviourId[]

    set\_behaviour\_setting(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *setting\_id: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_setting "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId

    set\_behaviour\_settings\_to\_range(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_settings_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.SettingId[]

    set\_behaviour\_string(*self: [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *str: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_string "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | str : string

*class* csc.model.BehaviourId[??](#csc.model.BehaviourId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.BehaviourId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *arg0: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.BehaviourId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *arg0: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.BehaviourId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.BehaviourId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.model.BehaviourId) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.BehaviourId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *arg0: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.BehaviourId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourId.is_null "Permalink to this definition")

    *static* null()  [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourId.null "Permalink to this definition")

    to\_string(*self: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.BehaviourId.to_string "Permalink to this definition")

*class* csc.model.BehaviourViewer[??](#csc.model.BehaviourViewer "Permalink to this definition")
:   BehaviourViewer class

    This class allows viewing of scene behaviours and their properties.

    \_\_annotations\_\_ *= {}*[??](#csc.model.BehaviourViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourViewer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.BehaviourViewer.__module__ "Permalink to this definition")

    behaviour\_id(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *object\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *behaviour\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourViewer.behaviour_id "Permalink to this definition")
    :   objectId : csc.model.ObjectId | behaviour\_name : string | -> csc.model.BehaviourId

    get\_behaviour\_asset(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  common::GenericId<domain::scene::assets::Asset>[??](#csc.model.BehaviourViewer.get_behaviour_asset "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId

    get\_behaviour\_asset\_range(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  list[common::GenericId<domain::scene::assets::Asset>][??](#csc.model.BehaviourViewer.get_behaviour_asset_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[]

    get\_behaviour\_by\_name(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *object\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *behaviour\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourViewer.get_behaviour_by_name "Permalink to this definition")
    :   objectId : csc.model.ObjectId | behaviour\_name : string | -> csc.model.BehaviourId

    get\_behaviour\_data(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.DataId](#csc.model.DataId "csc.model.DataId")[??](#csc.model.BehaviourViewer.get_behaviour_data "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.DataId

    get\_behaviour\_data\_range(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")][??](#csc.model.BehaviourViewer.get_behaviour_data_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.DataId[]

    get\_behaviour\_name(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.BehaviourViewer.get_behaviour_name "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | -> string

    get\_behaviour\_object(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.model.BehaviourViewer.get_behaviour_object "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId

    get\_behaviour\_objects\_range(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.model.BehaviourViewer.get_behaviour_objects_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId[]

    get\_behaviour\_owner(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.model.BehaviourViewer.get_behaviour_owner "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | -> csc.model.ObjectId

    get\_behaviour\_property\_names(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][??](#csc.model.BehaviourViewer.get_behaviour_property_names "Permalink to this definition")
    :   -> string[]

    get\_behaviour\_reference(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourViewer.get_behaviour_reference "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId

    get\_behaviour\_reference\_range(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")][??](#csc.model.BehaviourViewer.get_behaviour_reference_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[]

    get\_behaviour\_setting(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")[??](#csc.model.BehaviourViewer.get_behaviour_setting "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId

    get\_behaviour\_settings\_range(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")][??](#csc.model.BehaviourViewer.get_behaviour_settings_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId[]

    get\_behaviour\_string(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.BehaviourViewer.get_behaviour_string "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> string

    get\_behaviours(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourViewer.get_behaviours "Permalink to this definition")
    :   Overloaded function.

        1. get\_behaviours(self: csc.model.BehaviourViewer, type\_name: str) -> list[csc.model.BehaviourId]

           > typeName : string | -> csc.model.BehaviourId[]
        2. get\_behaviours(self: csc.model.BehaviourViewer, object\_id: csc.model.ObjectId) -> list[csc.model.BehaviourId]

           > objectId : csc.model.ObjectId | -> csc.model.BehaviourId[]

    get\_children(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *object\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")][??](#csc.model.BehaviourViewer.get_children "Permalink to this definition")
    :   -> Children behs ids

    get\_property\_type(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.PropertyType](#csc.model.PropertyType "csc.model.PropertyType")[??](#csc.model.BehaviourViewer.get_property_type "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> Type[]

    is\_hidden(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourViewer.is_hidden "Permalink to this definition")
    :   -> bool

    is\_valid\_behaviour\_type(*self: [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourViewer.is_valid_behaviour_type "Permalink to this definition")
    :   behaviour\_name : string | -> bool

*class* csc.model.ClusterEditor[??](#csc.model.ClusterEditor "Permalink to this definition")
:   ClusterEditor class

    This class lets edit scene data clusters.

    \_\_annotations\_\_ *= {}*[??](#csc.model.ClusterEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ClusterEditor.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ClusterEditor.__module__ "Permalink to this definition")

    add\_cluster(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.ClusterEditor.add_cluster "Permalink to this definition")
    :   insertedIds : csc.model.DataId[] | name : string (??????) | -> ClusterId

    add\_data\_to\_cluster(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.add_data_to_cluster "Permalink to this definition")
    :   cluster\_index : ClusterId | insertedIds : csc.model.DataId[]

    bind\_clusters(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id\_first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *cluster\_id\_second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.bind_clusters "Permalink to this definition")
    :   cluster\_id\_first : ClusterId | cluster\_id\_second : ClusterId

    remove\_cluster(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.remove_cluster "Permalink to this definition")
    :   cluster\_id : ClusterId

    remove\_data\_from\_cluster(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *data\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.remove_data_from_cluster "Permalink to this definition")
    :   data\_id : csc.model.DataId

    set\_cluster\_name(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.set_cluster_name "Permalink to this definition")
    :   cluster\_id : ClusterId | name : string

    unbind\_cluster(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.unbind_cluster "Permalink to this definition")
    :   cluster\_id : ClusterId

    unbind\_clusters(*self: [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id\_first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *cluster\_id\_second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.unbind_clusters "Permalink to this definition")
    :   cluster\_id\_first : ClusterId | cluster\_id\_second : ClusterId

*class* csc.model.ClusterViewer[??](#csc.model.ClusterViewer "Permalink to this definition")
:   ClusterViewer class

    This class lets read scene data clusters.

    \_\_annotations\_\_ *= {}*[??](#csc.model.ClusterViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ClusterViewer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ClusterViewer.__module__ "Permalink to this definition")

    cluster\_by\_data(*self: [csc.model.ClusterViewer](#csc.model.ClusterViewer "csc.model.ClusterViewer")*, *data\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.ClusterViewer.cluster_by_data "Permalink to this definition")
    :   data\_id : csc.model.DataId | -> ClusterId

    cluster\_datas(*self: [csc.model.ClusterViewer](#csc.model.ClusterViewer "csc.model.ClusterViewer")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")][??](#csc.model.ClusterViewer.cluster_datas "Permalink to this definition")
    :   cluster\_id : ClusterId | -> csc.model.DataId[]

    cluster\_name(*self: [csc.model.ClusterViewer](#csc.model.ClusterViewer "csc.model.ClusterViewer")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ClusterViewer.cluster_name "Permalink to this definition")
    :   cluster\_id : ClusterId | -> string

    clusters(*self: [csc.model.ClusterViewer](#csc.model.ClusterViewer "csc.model.ClusterViewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][??](#csc.model.ClusterViewer.clusters "Permalink to this definition")
    :   -> ClusterId[]

    clusters\_bindings(*self: [csc.model.ClusterViewer](#csc.model.ClusterViewer "csc.model.ClusterViewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ClustersEdge](#csc.model.ClustersEdge "csc.model.ClustersEdge")][??](#csc.model.ClusterViewer.clusters_bindings "Permalink to this definition")
    :   -> (ClusterId,ClusterId)[]

*class* csc.model.ClustersEdge[??](#csc.model.ClustersEdge "Permalink to this definition")
:   ClustersEdge class

    This class contains link between clusters

    \_\_annotations\_\_ *= {}*[??](#csc.model.ClustersEdge.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ClustersEdge.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ClustersEdge.__module__ "Permalink to this definition")

    *property* a[??](#csc.model.ClustersEdge.a "Permalink to this definition")

    *property* b[??](#csc.model.ClustersEdge.b "Permalink to this definition")

*class* csc.model.CustomSelectionPolicy[??](#csc.model.CustomSelectionPolicy "Permalink to this definition")
:   > CustomSelectionPolicy enumerable
    >
    > Default, // the entity is selected with other entities
    >
    > Single, // the entity is selected only if the selection contains only from this entity
    >
    > SingleType // the entity is selected only if the selection contains only entities of the same type

    Members:

    > Default
    >
    > Single
    >
    > SingleType

    Default *= <CustomSelectionPolicy.Default: 0>*[??](#csc.model.CustomSelectionPolicy.Default "Permalink to this definition")

    Single *= <CustomSelectionPolicy.Single: 1>*[??](#csc.model.CustomSelectionPolicy.Single "Permalink to this definition")

    SingleType *= <CustomSelectionPolicy.SingleType: 2>*[??](#csc.model.CustomSelectionPolicy.SingleType "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.model.CustomSelectionPolicy.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.model.CustomSelectionPolicy](#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.model.CustomSelectionPolicy](#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.model.CustomSelectionPolicy](#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Default': <CustomSelectionPolicy.Default: 0>, 'Single': <CustomSelectionPolicy.Single: 1>, 'SingleType': <CustomSelectionPolicy.SingleType: 2>}*[??](#csc.model.CustomSelectionPolicy.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.CustomSelectionPolicy.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.model.CustomSelectionPolicy](#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.CustomSelectionPolicy.__str__ "Permalink to this definition")

    *property* name[??](#csc.model.CustomSelectionPolicy.name "Permalink to this definition")

    *property* value[??](#csc.model.CustomSelectionPolicy.value "Permalink to this definition")

*class* csc.model.Data[??](#csc.model.Data "Permalink to this definition")
:   Data class

    This class serves to represent any special type of data.
    These data can be used in the update calculation or as behaviors??? properties.

    Variables:
    :   * **id** ??? Get Set csc.model.DataId
        * **object\_id** ??? Get Set csc.model.ObjectId
        * **name** ??? Get Set string
        * **mode** ??? Get Set csc.model.DataMode

    \_\_annotations\_\_ *= {}*[??](#csc.model.Data.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.Data.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.Data.__module__ "Permalink to this definition")

    *property* id[??](#csc.model.Data.id "Permalink to this definition")

    *property* mode[??](#csc.model.Data.mode "Permalink to this definition")

    *property* name[??](#csc.model.Data.name "Permalink to this definition")

    *property* object\_id[??](#csc.model.Data.object_id "Permalink to this definition")

*class* csc.model.DataEditor[??](#csc.model.DataEditor "Permalink to this definition")
:   DataEditor class

    This class has the possibility to edit scene data and their properties.

    Variables:
    :   * **add\_data** ??? overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data
        * **add\_setting** ??? overridden method by string, Setting.Value || csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting
        * **add\_constant\_data** ??? overridden method by string, Data.Value || string, Data.Value, csc.model.DataId -> Data
        * **add\_constant\_setting** ??? overridden method by string, Setting.Value || string, Setting.Value, csc.model.SettingId -> Setting
        * **set\_data\_value** ??? overridden method by csc.model.DataId&, Data.Value || csc.model.DataId, int{}, Data.Value || csc.model.DataId, int, Data.Value

    \_\_annotations\_\_ *= {}*[??](#csc.model.DataEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DataEditor.__module__ "Permalink to this definition")

    add\_constant\_data(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_constant_data "Permalink to this definition")
    :   Overloaded function.

        1. add\_constant\_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data
        2. add\_constant\_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data

    add\_constant\_setting(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_constant_setting "Permalink to this definition")
    :   Overloaded function.

        1. add\_constant\_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) -> csc.model.Setting
        2. add\_constant\_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting

    add\_data(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_data "Permalink to this definition")
    :   Overloaded function.

        1. add\_data(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data

           > -> Data
        2. add\_data(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data

           > -> Data

    add\_description(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.add_description "Permalink to this definition")

    add\_setting(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.add_setting "Permalink to this definition")
    :   Overloaded function.

        1. add\_setting(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting

           > -> Setting
        2. add\_setting(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting

           > -> Setting

    change\_description(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.change_description "Permalink to this definition")

    cluster\_editor(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*)  [csc.model.ClusterEditor](#csc.model.ClusterEditor "csc.model.ClusterEditor")[??](#csc.model.DataEditor.cluster_editor "Permalink to this definition")
    :   -> ClusterEditor

    copy\_data(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*, *from\_to: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId"), [csc.model.DataId](#csc.model.DataId "csc.model.DataId")]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.copy_data "Permalink to this definition")

    delete\_data(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*, *id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.delete_data "Permalink to this definition")

    delete\_setting(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*, *id: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.delete_setting "Permalink to this definition")

    remove\_description(*self: [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataEditor.remove_description "Permalink to this definition")

    reset\_description\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.reset_description_value "Permalink to this definition")
    :   Overloaded function.

        1. reset\_description\_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None
        2. reset\_description\_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None

    set\_data\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.set_data_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
        2. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
        3. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None

    set\_description\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.set_description_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_description\_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None
        2. set\_description\_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None

    set\_setting\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataEditor.set_setting_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_setting\_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) -> None
        2. set\_setting\_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None

*class* csc.model.DataId[??](#csc.model.DataId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.DataId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*, *arg0: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*, *arg0: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.DataId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.DataId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.DataId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.model.DataId) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DataId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*, *arg0: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.DataId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.DataId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.DataId.is_null "Permalink to this definition")

    *static* null()  [csc.model.DataId](#csc.model.DataId "csc.model.DataId")[??](#csc.model.DataId.null "Permalink to this definition")

    to\_string(*self: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.DataId.to_string "Permalink to this definition")

*class* csc.model.DataMode[??](#csc.model.DataMode "Permalink to this definition")
:   > Data::Mode enum
    >
    > This enumerates the basic types of data.
    > Static, Animation

    Members:

    > Static
    >
    > Animation

    Animation *= <DataMode.Animation: 1>*[??](#csc.model.DataMode.Animation "Permalink to this definition")

    Static *= <DataMode.Static: 0>*[??](#csc.model.DataMode.Static "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.model.DataMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.DataMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.model.DataMode](#csc.model.DataMode "csc.model.DataMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.model.DataMode](#csc.model.DataMode "csc.model.DataMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.model.DataMode](#csc.model.DataMode "csc.model.DataMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Animation': <DataMode.Animation: 1>, 'Static': <DataMode.Static: 0>}*[??](#csc.model.DataMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DataMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.DataMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.DataMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.model.DataMode](#csc.model.DataMode "csc.model.DataMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.DataMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.model.DataMode.name "Permalink to this definition")

    *property* value[??](#csc.model.DataMode.value "Permalink to this definition")

*class* csc.model.DataViewer[??](#csc.model.DataViewer "Permalink to this definition")
:   DataViewer class

    This class allows to view scene data and their properties.

    Variables:
    :   * **get\_data\_value** ??? overridden method by id : csc.model.DataId || csc.model.DataId, int (frame) -> Data.Value
        * **get\_behaviour\_property** ??? overridden method by : csc.model.BehaviourId, string -> Data.Value || csc.model.BehaviourId, string, int (frame) -> Setiing.Value

    \_\_annotations\_\_ *= {}*[??](#csc.model.DataViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DataViewer.__module__ "Permalink to this definition")

    cluster\_viewer(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*)  [csc.model.ClusterViewer](#csc.model.ClusterViewer "csc.model.ClusterViewer")[??](#csc.model.DataViewer.cluster_viewer "Permalink to this definition")
    :   -> ClusterViewer

    get\_all\_data\_id(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *object\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")][??](#csc.model.DataViewer.get_all_data_id "Permalink to this definition")
    :   -> csc.model.DataId[]

    get\_all\_settings\_id(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *object\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")][??](#csc.model.DataViewer.get_all_settings_id "Permalink to this definition")
    :   -> csc.model.SettingId[]

    get\_animation\_size(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.DataViewer.get_animation_size "Permalink to this definition")
    :   -> int

    get\_behaviour\_default\_data\_value(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.BehaviourId](#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DataViewer.get_behaviour_default_data_value "Permalink to this definition")
    :   id : csc.model.Beh id | name : string | -> csc.model.DataValue

    get\_behaviour\_property(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_behaviour_property "Permalink to this definition")
    :   Overloaded function.

        1. get\_behaviour\_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
        2. get\_behaviour\_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union[bool, int]

    get\_data(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [csc.model.Data](#csc.model.Data "csc.model.Data")[??](#csc.model.DataViewer.get_data "Permalink to this definition")
    :   id : csc.model.DataId | -> Data

    get\_data\_id(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.DataId](#csc.model.DataId "csc.model.DataId")[??](#csc.model.DataViewer.get_data_id "Permalink to this definition")
    :   id : csc.model.ObjectId | name : string | -> csc.model.DataId

    get\_data\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_data_value "Permalink to this definition")
    :   Overloaded function.

        1. get\_data\_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
        2. get\_data\_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

    get\_description\_by\_name(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.DataViewer.get_description_by_name "Permalink to this definition")
    :   -> string

    get\_description\_names(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][??](#csc.model.DataViewer.get_description_names "Permalink to this definition")
    :   -> string[]

    get\_description\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_description_value "Permalink to this definition")
    :   Overloaded function.

        1. get\_description\_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str

           > id : csc.model.DataId -> string
        2. get\_description\_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str

           > id : csc.model.SettingId -> string

    get\_setting(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [csc.model.Setting](#csc.model.Setting "csc.model.Setting")[??](#csc.model.DataViewer.get_setting "Permalink to this definition")
    :   id : csc.model.SettingId | -> Setting

    get\_setting\_id(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")[??](#csc.model.DataViewer.get_setting_id "Permalink to this definition")
    :   id : csc.model.ObjectId | name : string | -> csc.model.DataId

    get\_setting\_value(*\*args*, *\*\*kwargs*)[??](#csc.model.DataViewer.get_setting_value "Permalink to this definition")
    :   Overloaded function.

        1. get\_setting\_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union[bool, int]

           > id : csc.model.SettingId | -> Setting.Value
        2. get\_setting\_value(self: csc.model.DataViewer, setting\_id: csc.model.SettingId, position: int) -> Union[bool, int]

           > id : csc.model.SettingId, position : int | -> Setting.Value

    union\_get\_data\_value(*self: [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")*, *data\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = 0*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]][??](#csc.model.DataViewer.union_get_data_value "Permalink to this definition")
    :   id : csc.model.DataId | -> Data.Value

*class* csc.model.DescriptionTerm[??](#csc.model.DescriptionTerm "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.DescriptionTerm.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.model.DescriptionTerm](#csc.model.DescriptionTerm "csc.model.DescriptionTerm")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.DescriptionTerm.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.DescriptionTerm.__module__ "Permalink to this definition")

*class* csc.model.HyperedgeId[??](#csc.model.HyperedgeId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.HyperedgeId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*, *arg0: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.HyperedgeId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*, *arg0: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.HyperedgeId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.HyperedgeId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.HyperedgeId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.HyperedgeId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.model.HyperedgeId) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.HyperedgeId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*, *arg0: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.HyperedgeId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.HyperedgeId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.HyperedgeId.is_null "Permalink to this definition")

    *static* null()  [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")[??](#csc.model.HyperedgeId.null "Permalink to this definition")

    to\_string(*self: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.HyperedgeId.to_string "Permalink to this definition")

*class* csc.model.LerpMode[??](#csc.model.LerpMode "Permalink to this definition")
:   > LerpMode enumerable
    >
    > Empty, Linear, Spherical

    Members:

    > Empty
    >
    > Linear
    >
    > Spherical

    Empty *= <LerpMode.Empty: 0>*[??](#csc.model.LerpMode.Empty "Permalink to this definition")

    Linear *= <LerpMode.Linear: 1>*[??](#csc.model.LerpMode.Linear "Permalink to this definition")

    Spherical *= <LerpMode.Spherical: 2>*[??](#csc.model.LerpMode.Spherical "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.model.LerpMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.LerpMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.LerpMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.LerpMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.model.LerpMode](#csc.model.LerpMode "csc.model.LerpMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.LerpMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.model.LerpMode](#csc.model.LerpMode "csc.model.LerpMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.LerpMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.model.LerpMode](#csc.model.LerpMode "csc.model.LerpMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.LerpMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Empty': <LerpMode.Empty: 0>, 'Linear': <LerpMode.Linear: 1>, 'Spherical': <LerpMode.Spherical: 2>}*[??](#csc.model.LerpMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.LerpMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.LerpMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.LerpMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.model.LerpMode](#csc.model.LerpMode "csc.model.LerpMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.LerpMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.LerpMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.model.LerpMode.name "Permalink to this definition")

    *property* value[??](#csc.model.LerpMode.value "Permalink to this definition")

*class* csc.model.ModelEditor[??](#csc.model.ModelEditor "Permalink to this definition")
:   ModelEditor class

    Represents basic methods to edit the scene model

    Variables:
    :   **add\_object** ??? overridden method by GroupId -> csc.model.ObjectId

    \_\_annotations\_\_ *= {}*[??](#csc.model.ModelEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelEditor.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ModelEditor.__module__ "Permalink to this definition")

    add\_object(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelEditor.add_object "Permalink to this definition")
    :   Overloaded function.

        1. add\_object(self: csc.model.ModelEditor) -> csc.model.ObjectId
        2. add\_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId

    behaviour\_editor(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.model.BehaviourEditor](#csc.model.BehaviourEditor "csc.model.BehaviourEditor")[??](#csc.model.ModelEditor.behaviour_editor "Permalink to this definition")
    :   -> BehaviourEditor

    data\_editor(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.model.DataEditor](#csc.model.DataEditor "csc.model.DataEditor")[??](#csc.model.ModelEditor.data_editor "Permalink to this definition")
    :   -> DataEditor

    delete\_objects(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *ids: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*, *close\_connections: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.delete_objects "Permalink to this definition")

    fit\_animation\_size\_by\_layers(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.fit_animation_size_by_layers "Permalink to this definition")

    get\_viewer(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.model.ModelViewer](#csc.model.ModelViewer "csc.model.ModelViewer")[??](#csc.model.ModelEditor.get_viewer "Permalink to this definition")

    init\_default\_constants(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.init_default_constants "Permalink to this definition")

    layers(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.model.ModelEditor.layers "Permalink to this definition")
    :   -> csc.layers.Layers

    layers\_editor(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.layers.Editor](#csc.layers.Editor "csc.layers.Editor")[??](#csc.model.ModelEditor.layers_editor "Permalink to this definition")
    :   -> csc.layers.Editor

    layers\_selector(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.model.ModelEditor.layers_selector "Permalink to this definition")
    :   -> csc.layers.Selector

    move\_obj\_ids\_in\_layers(*self: csc.model.ModelEditor, objIds = csc.model.ObjectId[]: list[csc.model.ObjectId], layer\_id: csc.Guid*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.move_obj_ids_in_layers "Permalink to this definition")

    move\_objects\_to\_layer(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")]*, *target\_layer\_id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.move_objects_to_layer "Permalink to this definition")

    set\_fixed\_interpolation\_if\_need(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *actuals: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.DataId](#csc.model.DataId "csc.model.DataId")]*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.set_fixed_interpolation_if_need "Permalink to this definition")

    set\_object\_name(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.set_object_name "Permalink to this definition")

    set\_object\_type\_name(*self: [csc.model.ModelEditor](#csc.model.ModelEditor "csc.model.ModelEditor")*, *id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.set_object_type_name "Permalink to this definition")

*class* csc.model.ModelViewer[??](#csc.model.ModelViewer "Permalink to this definition")
:   ModelViewer class

    Represents basic methods to view the scene model

    Variables:
    :   **get\_objects** ??? overridden method by string -> csc.model.ObjectId[]

    \_\_annotations\_\_ *= {}*[??](#csc.model.ModelViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelViewer.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ModelViewer.__module__ "Permalink to this definition")

    behaviour\_viewer(*self: [csc.model.ModelViewer](#csc.model.ModelViewer "csc.model.ModelViewer")*)  [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")[??](#csc.model.ModelViewer.behaviour_viewer "Permalink to this definition")
    :   -> BehaviourViewer

    data\_viewer(*self: [csc.model.ModelViewer](#csc.model.ModelViewer "csc.model.ModelViewer")*)  [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")[??](#csc.model.ModelViewer.data_viewer "Permalink to this definition")
    :   -> DataViewer

    get\_object\_name(*self: [csc.model.ModelViewer](#csc.model.ModelViewer "csc.model.ModelViewer")*, *id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ModelViewer.get_object_name "Permalink to this definition")

    get\_object\_type\_name(*self: [csc.model.ModelViewer](#csc.model.ModelViewer "csc.model.ModelViewer")*, *id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ModelViewer.get_object_type_name "Permalink to this definition")

    get\_objects(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelViewer.get_objects "Permalink to this definition")
    :   Overloaded function.

        1. get\_objects(self: csc.model.ModelViewer) -> list[csc.model.ObjectId]
        2. get\_objects(self: csc.model.ModelViewer, name: str) -> list[csc.model.ObjectId]

*class* csc.model.ObjectId[??](#csc.model.ObjectId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.ObjectId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.ObjectId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.ObjectId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.ObjectId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ObjectId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.ObjectId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.model.ObjectId) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ObjectId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.ObjectId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ObjectId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.ObjectId.is_null "Permalink to this definition")

    *static* null()  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.model.ObjectId.null "Permalink to this definition")

    to\_string(*self: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ObjectId.to_string "Permalink to this definition")

*class* csc.model.PathName[??](#csc.model.PathName "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.PathName.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*, *arg0: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.PathName.__cmp__ "Permalink to this definition")

    \_\_copy\_\_(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [csc.model.PathName](#csc.model.PathName "csc.model.PathName")[??](#csc.model.PathName.__copy__ "Permalink to this definition")

    \_\_deepcopy\_\_(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*, *arg0: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")*)  [csc.model.PathName](#csc.model.PathName "csc.model.PathName")[??](#csc.model.PathName.__deepcopy__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*, *arg0: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.PathName.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.PathName.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.PathName.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.PathName) -> None

           > PathName class
           >
           > Implements a hierarchical name
        2. \_\_init\_\_(self: csc.model.PathName, arg0: str, arg1: list[str]) -> None

           > PathName class
           >
           > Implements a hierarchical name
           >
           > ivar name:
           > :   Get Set string
           >
           > ivar path:
           > :   Get Set string[]

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.PathName.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*, *arg0: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.PathName.__ne__ "Permalink to this definition")

    clear(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.PathName.clear "Permalink to this definition")

    empty(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.PathName.empty "Permalink to this definition")

    full\_path(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][??](#csc.model.PathName.full_path "Permalink to this definition")

    get\_namespace(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.PathName.get_namespace "Permalink to this definition")

    *static* get\_path\_name(*obj\_id: csc.model.ObjectId*, *mv: domain::scene::model::ModelViewer*, *beh\_name: str = 'Joint'*)  [csc.model.PathName](#csc.model.PathName "csc.model.PathName")[??](#csc.model.PathName.get_path_name "Permalink to this definition")

    *static* get\_path\_names(*arg0: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [csc.model.PathName](#csc.model.PathName "csc.model.PathName")][??](#csc.model.PathName.get_path_names "Permalink to this definition")

    *static* get\_path\_names\_by\_behavior(*arg0: str*, *arg1: domain::scene::model::ModelViewer*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.PathName](#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.model.PathName.get_path_names_by_behavior "Permalink to this definition")

    *static* get\_path\_names\_for\_objects(*arg0: set[csc.model.ObjectId], arg1: domain::scene::model::ModelViewer*)  [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.model.PathName](#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.model.PathName.get_path_names_for_objects "Permalink to this definition")

    *property* name[??](#csc.model.PathName.name "Permalink to this definition")

    *property* path[??](#csc.model.PathName.path "Permalink to this definition")

    set\_namespace(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*, *namespace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.PathName.set_namespace "Permalink to this definition")

    to\_string(*self: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.PathName.to_string "Permalink to this definition")

*class* csc.model.PropertyType[??](#csc.model.PropertyType "Permalink to this definition")
:   > PropertyType enumerable
    >
    > Undefined,
    > DataType,
    > DataRangeType,
    > SettingType,
    > SettingRangeType,
    > ObjectType,
    > ObjectRangeType,
    > BehaviourType,
    > BehaviourRangeType,
    > AssetType,
    > AssetRangeType,
    > StringType

    Members:

    > Undefined
    >
    > DataType
    >
    > DataRangeType
    >
    > SettingType
    >
    > SettingRangeType
    >
    > ObjectType
    >
    > ObjectRangeType
    >
    > BehaviourType
    >
    > BehaviourRangeType
    >
    > AssetType
    >
    > AssetRangeType
    >
    > StringType

    AssetRangeType *= <PropertyType.AssetRangeType: 10>*[??](#csc.model.PropertyType.AssetRangeType "Permalink to this definition")

    AssetType *= <PropertyType.AssetType: 9>*[??](#csc.model.PropertyType.AssetType "Permalink to this definition")

    BehaviourRangeType *= <PropertyType.BehaviourRangeType: 8>*[??](#csc.model.PropertyType.BehaviourRangeType "Permalink to this definition")

    BehaviourType *= <PropertyType.BehaviourType: 7>*[??](#csc.model.PropertyType.BehaviourType "Permalink to this definition")

    DataRangeType *= <PropertyType.DataRangeType: 2>*[??](#csc.model.PropertyType.DataRangeType "Permalink to this definition")

    DataType *= <PropertyType.DataType: 1>*[??](#csc.model.PropertyType.DataType "Permalink to this definition")

    ObjectRangeType *= <PropertyType.ObjectRangeType: 6>*[??](#csc.model.PropertyType.ObjectRangeType "Permalink to this definition")

    ObjectType *= <PropertyType.ObjectType: 5>*[??](#csc.model.PropertyType.ObjectType "Permalink to this definition")

    SettingRangeType *= <PropertyType.SettingRangeType: 4>*[??](#csc.model.PropertyType.SettingRangeType "Permalink to this definition")

    SettingType *= <PropertyType.SettingType: 3>*[??](#csc.model.PropertyType.SettingType "Permalink to this definition")

    StringType *= <PropertyType.StringType: 11>*[??](#csc.model.PropertyType.StringType "Permalink to this definition")

    Undefined *= <PropertyType.Undefined: 0>*[??](#csc.model.PropertyType.Undefined "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.model.PropertyType.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.PropertyType.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.PropertyType.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.PropertyType.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.model.PropertyType](#csc.model.PropertyType "csc.model.PropertyType")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.PropertyType.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.model.PropertyType](#csc.model.PropertyType "csc.model.PropertyType")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.PropertyType.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.model.PropertyType](#csc.model.PropertyType "csc.model.PropertyType")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.PropertyType.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'AssetRangeType': <PropertyType.AssetRangeType: 10>, 'AssetType': <PropertyType.AssetType: 9>, 'BehaviourRangeType': <PropertyType.BehaviourRangeType: 8>, 'BehaviourType': <PropertyType.BehaviourType: 7>, 'DataRangeType': <PropertyType.DataRangeType: 2>, 'DataType': <PropertyType.DataType: 1>, 'ObjectRangeType': <PropertyType.ObjectRangeType: 6>, 'ObjectType': <PropertyType.ObjectType: 5>, 'SettingRangeType': <PropertyType.SettingRangeType: 4>, 'SettingType': <PropertyType.SettingType: 3>, 'StringType': <PropertyType.StringType: 11>, 'Undefined': <PropertyType.Undefined: 0>}*[??](#csc.model.PropertyType.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.PropertyType.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.PropertyType.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.PropertyType.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.model.PropertyType](#csc.model.PropertyType "csc.model.PropertyType")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.PropertyType.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.PropertyType.__str__ "Permalink to this definition")

    *property* name[??](#csc.model.PropertyType.name "Permalink to this definition")

    *property* value[??](#csc.model.PropertyType.value "Permalink to this definition")

*class* csc.model.Setting[??](#csc.model.Setting "Permalink to this definition")
:   Setting class

    This class serves to represent int or bool value that using in the update calculation.

    Variables:
    :   * **id** ??? Get csc.model.DataId
        * **object\_id** ??? Get csc.model.ObjectId
        * **name** ??? Get string
        * **type** ??? Get int
        * **mode** ??? Get csc.model.SettingMode

    Parameters:
    :   **object\_id** ([*csc.model.ObjectId*](#csc.model.ObjectId "csc.model.ObjectId")) ??? object\_id

    \_\_annotations\_\_ *= {}*[??](#csc.model.Setting.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.Setting.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.Setting, id: csc.model.SettingId, object\_id: csc.model.ObjectId, name: str, type: int) -> None
        2. \_\_init\_\_(self: csc.model.Setting, object\_id: csc.model.ObjectId, name: str, type: int) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.Setting.__module__ "Permalink to this definition")

    *property* id[??](#csc.model.Setting.id "Permalink to this definition")

    *property* mode[??](#csc.model.Setting.mode "Permalink to this definition")

    *property* name[??](#csc.model.Setting.name "Permalink to this definition")

    *property* object\_id[??](#csc.model.Setting.object_id "Permalink to this definition")

    *property* type[??](#csc.model.Setting.type "Permalink to this definition")

*class* csc.model.SettingFunctionId[??](#csc.model.SettingFunctionId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.SettingFunctionId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*, *arg0: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingFunctionId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*, *arg0: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingFunctionId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingFunctionId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.SettingFunctionId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.SettingFunctionId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.model.SettingFunctionId) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.SettingFunctionId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*, *arg0: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingFunctionId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.SettingFunctionId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingFunctionId.is_null "Permalink to this definition")

    *static* null()  [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")[??](#csc.model.SettingFunctionId.null "Permalink to this definition")

    to\_string(*self: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.SettingFunctionId.to_string "Permalink to this definition")

*class* csc.model.SettingId[??](#csc.model.SettingId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.model.SettingId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*, *arg0: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*, *arg0: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.SettingId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.model.SettingId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.model.SettingId) -> None

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.SettingId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*, *arg0: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.SettingId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingId.is_null "Permalink to this definition")

    *static* null()  [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")[??](#csc.model.SettingId.null "Permalink to this definition")

    to\_string(*self: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.SettingId.to_string "Permalink to this definition")

*class* csc.model.SettingMode[??](#csc.model.SettingMode "Permalink to this definition")
:   > Setting::Mode enum
    >
    > This enumerates the basic types of data.
    > Static, Animation

    Members:

    > Static
    >
    > Animation

    Animation *= <SettingMode.Animation: 1>*[??](#csc.model.SettingMode.Animation "Permalink to this definition")

    Static *= <SettingMode.Static: 0>*[??](#csc.model.SettingMode.Static "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.model.SettingMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.model.SettingMode](#csc.model.SettingMode "csc.model.SettingMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.model.SettingMode](#csc.model.SettingMode "csc.model.SettingMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.SettingMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.model.SettingMode](#csc.model.SettingMode "csc.model.SettingMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.SettingMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Animation': <SettingMode.Animation: 1>, 'Static': <SettingMode.Static: 0>}*[??](#csc.model.SettingMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.SettingMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.SettingMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.SettingMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.model.SettingMode](#csc.model.SettingMode "csc.model.SettingMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.SettingMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.SettingMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.model.SettingMode.name "Permalink to this definition")

    *property* value[??](#csc.model.SettingMode.value "Permalink to this definition")

csc.model.get\_path\_without\_namespace(*path\_name: [csc.model.PathName](#csc.model.PathName "csc.model.PathName")*)  [csc.model.PathName](#csc.model.PathName "csc.model.PathName")[??](#csc.model.get_path_without_namespace "Permalink to this definition")
:   -> PathName

## csc.domain The Cascadeur python module that implements basic scene properties and infrastructure.[??](#csc-domain-the-cascadeur-python-module-that-implements-basic-scene-properties-and-infrastructure "Permalink to this heading")

Entity3d\_id = std::variant<model::ModelObject::Id, Tool\_object\_id>

|  |  |
| --- | --- |
| [`csc.domain.Pivot`](#csc.domain.Pivot "csc.domain.Pivot") | Pivot class |
| [`csc.domain.Selection`](#csc.domain.Selection "csc.domain.Selection") | Selection class |
| [`csc.domain.Selector`](#csc.domain.Selector "csc.domain.Selector") | Selector class |
| [`csc.domain.AssetId`](#csc.domain.AssetId "csc.domain.AssetId") |  |
| [`csc.domain.Asset`](#csc.domain.Asset "csc.domain.Asset") | Asset class |
| [`csc.domain.LocalInterpolator`](#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator") | LocalInterpolator class |
| [`csc.domain.SceneUpdater`](#csc.domain.SceneUpdater "csc.domain.SceneUpdater") | SceneUpdater class |
| [`csc.domain.ProcessorsStorage`](#csc.domain.ProcessorsStorage "csc.domain.ProcessorsStorage") | ProcessorsStorage class |
| [`csc.domain.IMessageHandler`](#csc.domain.IMessageHandler "csc.domain.IMessageHandler") | IMessageHandler interface |
| [`csc.domain.Scene`](#csc.domain.Scene "csc.domain.Scene") | Scene class |
| [`csc.domain.Session`](#csc.domain.Session "csc.domain.Session") | Session class |
| [`csc.domain.Tool_object_id`](#csc.domain.Tool_object_id "csc.domain.Tool_object_id") |  |
| [`csc.domain.StatePivot`](#csc.domain.StatePivot "csc.domain.StatePivot") | StatePivot enum |
| [`csc.domain.FrameActionOnChange`](#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange") | FrameActionOnChange enum |
| [`csc.domain.IntervalActionOnChange`](#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange") | IntervalActionOnChange enum |
| [`csc.domain.SelectorMode`](#csc.domain.SelectorMode "csc.domain.SelectorMode") | SelectorMode enumerable |
| [`csc.domain.SelectorFilter`](#csc.domain.SelectorFilter "csc.domain.SelectorFilter") | SelectorFilter enumerable |
| [`csc.domain.Select`](#csc.domain.Select "csc.domain.Select") | Select class |
| [`csc.domain.assets.FigureVertex`](_generate/csc.domain.assets.FigureVertex.html#csc.domain.assets.FigureVertex "csc.domain.assets.FigureVertex") | FigureVertex class |
| [`csc.domain.assets.Triangle`](_generate/csc.domain.assets.Triangle.html#csc.domain.assets.Triangle "csc.domain.assets.Triangle") | Triangle class |
| [`csc.domain.assets.Mesh`](_generate/csc.domain.assets.Mesh.html#csc.domain.assets.Mesh "csc.domain.assets.Mesh") | Mesh class |
| [`csc.domain.assets.MeshDependency`](_generate/csc.domain.assets.MeshDependency.html#csc.domain.assets.MeshDependency "csc.domain.assets.MeshDependency") | MeshDependency class |
| [`csc.domain.assets.AssetsManager`](_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager") | AssetsManager class |

*class* csc.domain.Asset[??](#csc.domain.Asset "Permalink to this definition")
:   Asset class

    Assets are objects resources that have content like meshes or textures.

    Variables:
    :   **id** ??? Get csc.Guid

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Asset.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Asset.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Asset.__module__ "Permalink to this definition")

    *property* id[??](#csc.domain.Asset.id "Permalink to this definition")

*class* csc.domain.AssetId[??](#csc.domain.AssetId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.domain.AssetId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*, *arg0: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.AssetId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*, *arg0: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.AssetId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.AssetId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.AssetId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.domain.AssetId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.domain.AssetId) -> None

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.AssetId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*, *arg0: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.AssetId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.AssetId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.AssetId.is_null "Permalink to this definition")

    *static* null()  [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")[??](#csc.domain.AssetId.null "Permalink to this definition")

    to\_string(*self: [csc.domain.AssetId](#csc.domain.AssetId "csc.domain.AssetId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.AssetId.to_string "Permalink to this definition")

*class* csc.domain.FrameActionOnChange[??](#csc.domain.FrameActionOnChange "Permalink to this definition")
:   > FrameActionOnChange enum
    >
    > AutoKey = 0, Fixing = 1, DoNothing = 2

    Members:

    > AutoKey
    >
    > Fixing
    >
    > DoNothing

    AutoKey *= <FrameActionOnChange.AutoKey: 0>*[??](#csc.domain.FrameActionOnChange.AutoKey "Permalink to this definition")

    DoNothing *= <FrameActionOnChange.DoNothing: 2>*[??](#csc.domain.FrameActionOnChange.DoNothing "Permalink to this definition")

    Fixing *= <FrameActionOnChange.Fixing: 1>*[??](#csc.domain.FrameActionOnChange.Fixing "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.domain.FrameActionOnChange.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.domain.FrameActionOnChange](#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.FrameActionOnChange](#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.domain.FrameActionOnChange](#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'AutoKey': <FrameActionOnChange.AutoKey: 0>, 'DoNothing': <FrameActionOnChange.DoNothing: 2>, 'Fixing': <FrameActionOnChange.Fixing: 1>}*[??](#csc.domain.FrameActionOnChange.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.FrameActionOnChange.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.domain.FrameActionOnChange](#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.FrameActionOnChange.__str__ "Permalink to this definition")

    *property* name[??](#csc.domain.FrameActionOnChange.name "Permalink to this definition")

    *property* value[??](#csc.domain.FrameActionOnChange.value "Permalink to this definition")

*class* csc.domain.IMessageHandler[??](#csc.domain.IMessageHandler "Permalink to this definition")
:   IMessageHandler interface

    \_\_annotations\_\_ *= {}*[??](#csc.domain.IMessageHandler.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.IMessageHandler.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.IMessageHandler.__module__ "Permalink to this definition")

*class* csc.domain.IntervalActionOnChange[??](#csc.domain.IntervalActionOnChange "Permalink to this definition")
:   > IntervalActionOnChange enum
    >
    > Fixing = 0, DoNothing = 1

    Members:

    > Fixing
    >
    > DoNothing

    DoNothing *= <IntervalActionOnChange.DoNothing: 1>*[??](#csc.domain.IntervalActionOnChange.DoNothing "Permalink to this definition")

    Fixing *= <IntervalActionOnChange.Fixing: 0>*[??](#csc.domain.IntervalActionOnChange.Fixing "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.domain.IntervalActionOnChange.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.domain.IntervalActionOnChange](#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.IntervalActionOnChange](#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.domain.IntervalActionOnChange](#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'DoNothing': <IntervalActionOnChange.DoNothing: 1>, 'Fixing': <IntervalActionOnChange.Fixing: 0>}*[??](#csc.domain.IntervalActionOnChange.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.IntervalActionOnChange.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.domain.IntervalActionOnChange](#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.IntervalActionOnChange.__str__ "Permalink to this definition")

    *property* name[??](#csc.domain.IntervalActionOnChange.name "Permalink to this definition")

    *property* value[??](#csc.domain.IntervalActionOnChange.value "Permalink to this definition")

*class* csc.domain.LocalInterpolator[??](#csc.domain.LocalInterpolator "Permalink to this definition")
:   LocalInterpolator class

    \_\_annotations\_\_ *= {}*[??](#csc.domain.LocalInterpolator.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.LocalInterpolator.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.LocalInterpolator.__module__ "Permalink to this definition")

    interpolate(*self: [csc.domain.LocalInterpolator](#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.LocalInterpolator.interpolate "Permalink to this definition")

    reload(*self: [csc.domain.LocalInterpolator](#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.LocalInterpolator.reload "Permalink to this definition")

*class* csc.domain.Pivot[??](#csc.domain.Pivot "Permalink to this definition")
:   Pivot class

    Represents basic Pivot methods.

    Variables:
    :   * **position** ??? overridden method by ??? || int (frame) || int, StatePivot (pivot)
        * **rotation** ??? overridden method by ??? || int (frame) || int, StatePivot (pivot)

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Pivot.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Pivot.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Pivot.__module__ "Permalink to this definition")

    center\_of\_top\_objects(*self: [csc.domain.Pivot](#csc.domain.Pivot "csc.domain.Pivot")*, *arg0: Callable[[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")], numpy.ndarray[numpy.float32[3, 1]]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.domain.Pivot.center_of_top_objects "Permalink to this definition")

    position(*\*args*, *\*\*kwargs*)[??](#csc.domain.Pivot.position "Permalink to this definition")
    :   Overloaded function.

        1. position(self: csc.domain.Pivot) -> numpy.ndarray[numpy.float32[3, 1]]
        2. position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray[numpy.float32[3, 1]]
        3. position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]]

    rotation(*\*args*, *\*\*kwargs*)[??](#csc.domain.Pivot.rotation "Permalink to this definition")
    :   Overloaded function.

        1. rotation(self: csc.domain.Pivot) -> csc.math.Quaternion
        2. rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion
        3. rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion

    select(*self: [csc.domain.Pivot](#csc.domain.Pivot "csc.domain.Pivot")*, *entity\_id: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Pivot.select "Permalink to this definition")

*class* csc.domain.ProcessorsStorage[??](#csc.domain.ProcessorsStorage "Permalink to this definition")
:   ProcessorsStorage class

    The class serves to contain entity 3d processors

    \_\_annotations\_\_ *= {}*[??](#csc.domain.ProcessorsStorage.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.ProcessorsStorage.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.ProcessorsStorage.__module__ "Permalink to this definition")

*class* csc.domain.Scene[??](#csc.domain.Scene "Permalink to this definition")
:   Scene class

    Root class that represents a scene and its methods for modifying or observing it.

    Modify scene by func modify:

    Parameters:
    :   * **name** ??? Name of the modifier
        * **func** ??? Modify functor void(modelEditor, updateEditor, scene)

    Modify scene by func modify\_update:

    Parameters:
    :   * **name** ??? Name of the modifier
        * **func** ??? Modify functor void(modelEditor, updateEditor, sceneUpdater)

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Scene.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Scene.__module__ "Permalink to this definition")

    assets\_manager(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  domain::scene::AssetsManager[??](#csc.domain.Scene.assets_manager "Permalink to this definition")
    :   -> AssetsManager

    behaviour\_viewer(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [csc.model.BehaviourViewer](#csc.model.BehaviourViewer "csc.model.BehaviourViewer")[??](#csc.domain.Scene.behaviour_viewer "Permalink to this definition")
    :   -> csc.model.BehaviourViewer

    data\_viewer(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [csc.model.DataViewer](#csc.model.DataViewer "csc.model.DataViewer")[??](#csc.domain.Scene.data_viewer "Permalink to this definition")
    :   -> csc.model.DataViewer

    error(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.error "Permalink to this definition")

    get\_current\_frame(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *clamp\_animation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.Scene.get_current_frame "Permalink to this definition")
    :   -> int

    get\_event\_log\_or\_null(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Scene.get_event_log_or_null "Permalink to this definition")

    get\_layers\_selector(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Scene.get_layers_selector "Permalink to this definition")
    :   -> csc.layers.Selector

    info(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.info "Permalink to this definition")

    layers\_viewer(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [csc.layers.Viewer](#csc.layers.Viewer "csc.layers.Viewer")[??](#csc.domain.Scene.layers_viewer "Permalink to this definition")
    :   -> csc.layers.Viewer

    model\_viewer(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [csc.model.ModelViewer](#csc.model.ModelViewer "csc.model.ModelViewer")[??](#csc.domain.Scene.model_viewer "Permalink to this definition")
    :   -> csc.model.ModelViewer

    modify(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify "Permalink to this definition")
    :   -> bool

    modify\_update(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify_update "Permalink to this definition")
    :   -> bool

    modify\_update\_with\_session(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify_update_with_session "Permalink to this definition")
    :   -> bool

    modify\_with\_session(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify_with_session "Permalink to this definition")
    :   -> bool

    selector(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Scene.selector "Permalink to this definition")
    :   -> Selector

    set\_current\_frame(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.set_current_frame "Permalink to this definition")

    set\_event\_log(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *message\_handler: [csc.domain.IMessageHandler](#csc.domain.IMessageHandler "csc.domain.IMessageHandler")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.set_event_log "Permalink to this definition")

    success(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.success "Permalink to this definition")

    warning(*self: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.warning "Permalink to this definition")

*class* csc.domain.SceneUpdater[??](#csc.domain.SceneUpdater "Permalink to this definition")
:   SceneUpdater class

    The SceneUpdater serves to rule the scene modify.
    If we changed the update, we should regenerate it, also it has the possible to run the update with certain data.

    Variables:
    :   **run\_update** ??? overridden method by csc.model.DataId{} (localIds), int (frame) || csc.model.DataId{}, int{} (frames)

    \_\_annotations\_\_ *= {}*[??](#csc.domain.SceneUpdater.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.SceneUpdater.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.SceneUpdater.__module__ "Permalink to this definition")

    generate\_update(*self: [csc.domain.SceneUpdater](#csc.domain.SceneUpdater "csc.domain.SceneUpdater")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SceneUpdater.generate_update "Permalink to this definition")

    get\_interpolator(*self: [csc.domain.SceneUpdater](#csc.domain.SceneUpdater "csc.domain.SceneUpdater")*)  [csc.domain.LocalInterpolator](#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator")[??](#csc.domain.SceneUpdater.get_interpolator "Permalink to this definition")

    run\_update(*\*args*, *\*\*kwargs*)[??](#csc.domain.SceneUpdater.run_update "Permalink to this definition")
    :   Overloaded function.

        1. run\_update(self: csc.domain.SceneUpdater, local\_ids: set[csc.model.DataId], frame: int) -> None
        2. run\_update(self: csc.domain.SceneUpdater, local\_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None

    scene(*self: [csc.domain.SceneUpdater](#csc.domain.SceneUpdater "csc.domain.SceneUpdater")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.SceneUpdater.scene "Permalink to this definition")

*class* csc.domain.Select[??](#csc.domain.Select "Permalink to this definition")
:   Select class

    Represents properties of the current selection state of the scene

    Variables:
    :   * **object\_ids** ??? Get Set (csc.model.ObjectId or csc.scene.Tool\_object\_id){}
        * **pivot\_id** ??? Get Set (csc.model.ObjectId or csc.scene.Tool\_object\_id)
        * **filter** ??? Get Set csc.scene.SelectorFilter
        * **mode** ??? Get Set csc.scene.SelectorMode
        * **types\_filter** ??? Get Set string{}

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Select.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.Select](#csc.domain.Select "csc.domain.Select")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Select.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Select.__module__ "Permalink to this definition")

    *property* filter[??](#csc.domain.Select.filter "Permalink to this definition")

    *property* mode[??](#csc.domain.Select.mode "Permalink to this definition")

    *property* object\_ids[??](#csc.domain.Select.object_ids "Permalink to this definition")

    *property* pivot\_id[??](#csc.domain.Select.pivot_id "Permalink to this definition")

    *property* types\_filter[??](#csc.domain.Select.types_filter "Permalink to this definition")

*class* csc.domain.Selection[??](#csc.domain.Selection "Permalink to this definition")
:   Selection class

    Contains selected objects

    Variables:
    :   **ids** ??? Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Selection.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Selection.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Selection.__module__ "Permalink to this definition")

    *property* ids[??](#csc.domain.Selection.ids "Permalink to this definition")

    *property* ordered\_ids[??](#csc.domain.Selection.ordered_ids "Permalink to this definition")

*class* csc.domain.SelectionChanger[??](#csc.domain.SelectionChanger "Permalink to this definition")
:   SelectionChanger class

    Contains basic methods and properties to operate current selected scene objects

    Variables:
    :   * **ids** ??? Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}
        * **select** ??? overridden method by Select || Entity3d\_id{}, Entity3d\_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)

    \_\_annotations\_\_ *= {}*[??](#csc.domain.SelectionChanger.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.SelectionChanger.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.SelectionChanger.__module__ "Permalink to this definition")

    clear\_selection(*self: [csc.domain.SelectionChanger](#csc.domain.SelectionChanger "csc.domain.SelectionChanger")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectionChanger.clear_selection "Permalink to this definition")

    refresh\_selection(*self: [csc.domain.SelectionChanger](#csc.domain.SelectionChanger "csc.domain.SelectionChanger")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectionChanger.refresh_selection "Permalink to this definition")

    select(*\*args*, *\*\*kwargs*)[??](#csc.domain.SelectionChanger.select "Permalink to this definition")
    :   Overloaded function.

        1. select(self: csc.domain.SelectionChanger, select: csc.domain.Select) -> None
        2. select(self: csc.domain.SelectionChanger, ids: set[Union[csc.model.ObjectId, csc.domain.Tool\_object\_id]], id: Union[csc.model.ObjectId, csc.domain.Tool\_object\_id] = <csc.model.ObjectId object at 0x7f3d3ffa9b30>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, types\_filter: set[str] = set(), auto\_pivot: bool = False) -> None

*class* csc.domain.Selector[??](#csc.domain.Selector "Permalink to this definition")
:   Selector class

    Contains basic methods and properties to operate current selected scene objects

    Variables:
    :   * **ids** ??? Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}
        * **select** ??? overridden method by Select || Entity3d\_id{}, Entity3d\_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Selector.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Selector.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Selector.__module__ "Permalink to this definition")

    pivot(*self: [csc.domain.Selector](#csc.domain.Selector "csc.domain.Selector")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Selector.pivot "Permalink to this definition")
    :   -> Pivot

    select(*\*args*, *\*\*kwargs*)[??](#csc.domain.Selector.select "Permalink to this definition")
    :   Overloaded function.

        1. select(self: csc.domain.Selector, select: csc.domain.Select) -> None
        2. select(self: csc.domain.Selector, ids: set[Union[csc.model.ObjectId, csc.domain.Tool\_object\_id]], id: Union[csc.model.ObjectId, csc.domain.Tool\_object\_id] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type\_filter: set[str] = set(), auto\_pivot: bool = False) -> None

    selected(*self: [csc.domain.Selector](#csc.domain.Selector "csc.domain.Selector")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Selector.selected "Permalink to this definition")
    :   -> Selection

*class* csc.domain.SelectorFilter[??](#csc.domain.SelectorFilter "Permalink to this definition")
:   > SelectorFilter enumerable
    >
    > Free = 0x00,
    > Selectable = 0x01,
    > ObjectType = 0x02,
    > Layer = 0x04,
    > CustomSelectionPolicy = 0x08,
    > Standart = Selectable | ObjectType | Layer,
    > Full = 0xFF,

    Members:

    > Free
    >
    > Selectable
    >
    > ObjectType
    >
    > Layer
    >
    > CustomSelectionPolicy
    >
    > Standart
    >
    > Full

    CustomSelectionPolicy *= <SelectorFilter.CustomSelectionPolicy: 8>*[??](#csc.domain.SelectorFilter.CustomSelectionPolicy "Permalink to this definition")

    Free *= <SelectorFilter.Free: 0>*[??](#csc.domain.SelectorFilter.Free "Permalink to this definition")

    Full *= <SelectorFilter.Full: 255>*[??](#csc.domain.SelectorFilter.Full "Permalink to this definition")

    Layer *= <SelectorFilter.Layer: 4>*[??](#csc.domain.SelectorFilter.Layer "Permalink to this definition")

    ObjectType *= <SelectorFilter.ObjectType: 2>*[??](#csc.domain.SelectorFilter.ObjectType "Permalink to this definition")

    Selectable *= <SelectorFilter.Selectable: 1>*[??](#csc.domain.SelectorFilter.Selectable "Permalink to this definition")

    Standart *= <SelectorFilter.Standart: 7>*[??](#csc.domain.SelectorFilter.Standart "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.domain.SelectorFilter.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.domain.SelectorFilter](#csc.domain.SelectorFilter "csc.domain.SelectorFilter")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.SelectorFilter](#csc.domain.SelectorFilter "csc.domain.SelectorFilter")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.domain.SelectorFilter](#csc.domain.SelectorFilter "csc.domain.SelectorFilter")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'CustomSelectionPolicy': <SelectorFilter.CustomSelectionPolicy: 8>, 'Free': <SelectorFilter.Free: 0>, 'Full': <SelectorFilter.Full: 255>, 'Layer': <SelectorFilter.Layer: 4>, 'ObjectType': <SelectorFilter.ObjectType: 2>, 'Selectable': <SelectorFilter.Selectable: 1>, 'Standart': <SelectorFilter.Standart: 7>}*[??](#csc.domain.SelectorFilter.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.SelectorFilter.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.domain.SelectorFilter](#csc.domain.SelectorFilter "csc.domain.SelectorFilter")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.SelectorFilter.__str__ "Permalink to this definition")

    *property* name[??](#csc.domain.SelectorFilter.name "Permalink to this definition")

    *property* value[??](#csc.domain.SelectorFilter.value "Permalink to this definition")

*class* csc.domain.SelectorMode[??](#csc.domain.SelectorMode "Permalink to this definition")
:   > SelectorMode enumerable
    >
    > SingleSelection, // Resets if new objects were selected, and nothing changes if already selected ones were selected
    >
    > MultiSelection, // Multiple selections. If not all objects were selected, adds, otherwise subtracts
    >
    > NewSelection, // Resets everything and highlights the selection
    >
    > AdditionSelection, // Adds all selections to selections
    >
    > SubtractionSelection // Subtracts highlighted entities from selections

    Members:

    > SingleSelection
    >
    > MultiSelection
    >
    > NewSelection
    >
    > AdditionSelection
    >
    > SubtractionSelection

    AdditionSelection *= <SelectorMode.AdditionSelection: 3>*[??](#csc.domain.SelectorMode.AdditionSelection "Permalink to this definition")

    MultiSelection *= <SelectorMode.MultiSelection: 1>*[??](#csc.domain.SelectorMode.MultiSelection "Permalink to this definition")

    NewSelection *= <SelectorMode.NewSelection: 2>*[??](#csc.domain.SelectorMode.NewSelection "Permalink to this definition")

    SingleSelection *= <SelectorMode.SingleSelection: 0>*[??](#csc.domain.SelectorMode.SingleSelection "Permalink to this definition")

    SubtractionSelection *= <SelectorMode.SubtractionSelection: 4>*[??](#csc.domain.SelectorMode.SubtractionSelection "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.domain.SelectorMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.SelectorMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.domain.SelectorMode](#csc.domain.SelectorMode "csc.domain.SelectorMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.SelectorMode](#csc.domain.SelectorMode "csc.domain.SelectorMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectorMode.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.domain.SelectorMode](#csc.domain.SelectorMode "csc.domain.SelectorMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'AdditionSelection': <SelectorMode.AdditionSelection: 3>, 'MultiSelection': <SelectorMode.MultiSelection: 1>, 'NewSelection': <SelectorMode.NewSelection: 2>, 'SingleSelection': <SelectorMode.SingleSelection: 0>, 'SubtractionSelection': <SelectorMode.SubtractionSelection: 4>}*[??](#csc.domain.SelectorMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.SelectorMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.SelectorMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.SelectorMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.domain.SelectorMode](#csc.domain.SelectorMode "csc.domain.SelectorMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectorMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.SelectorMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.domain.SelectorMode.name "Permalink to this definition")

    *property* value[??](#csc.domain.SelectorMode.value "Permalink to this definition")

*class* csc.domain.Session[??](#csc.domain.Session "Permalink to this definition")
:   Session class

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Session.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Session.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Session.__module__ "Permalink to this definition")

    set\_current\_frame(*self: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Session.set_current_frame "Permalink to this definition")

    take\_layers\_selector(*self: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Session.take_layers_selector "Permalink to this definition")

    take\_selector(*self: [csc.domain.Session](#csc.domain.Session "csc.domain.Session")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Session.take_selector "Permalink to this definition")

*class* csc.domain.StatePivot[??](#csc.domain.StatePivot "Permalink to this definition")
:   > StatePivot enum
    >
    > This enumerates the basic types of pivot states.
    > Fixed = 0, Moving = 1

    Members:

    > Fixed
    >
    > Moving

    Fixed *= <StatePivot.Fixed: 0>*[??](#csc.domain.StatePivot.Fixed "Permalink to this definition")

    Moving *= <StatePivot.Moving: 1>*[??](#csc.domain.StatePivot.Moving "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.domain.StatePivot.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.StatePivot.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.StatePivot.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.StatePivot.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.domain.StatePivot](#csc.domain.StatePivot "csc.domain.StatePivot")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.StatePivot.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.StatePivot](#csc.domain.StatePivot "csc.domain.StatePivot")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.StatePivot.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.domain.StatePivot](#csc.domain.StatePivot "csc.domain.StatePivot")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.StatePivot.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'Fixed': <StatePivot.Fixed: 0>, 'Moving': <StatePivot.Moving: 1>}*[??](#csc.domain.StatePivot.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.StatePivot.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.StatePivot.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.StatePivot.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.domain.StatePivot](#csc.domain.StatePivot "csc.domain.StatePivot")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.StatePivot.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.StatePivot.__str__ "Permalink to this definition")

    *property* name[??](#csc.domain.StatePivot.name "Permalink to this definition")

    *property* value[??](#csc.domain.StatePivot.value "Permalink to this definition")

*class* csc.domain.Tool\_object\_id[??](#csc.domain.Tool_object_id "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.domain.Tool_object_id.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*, *arg0: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.Tool_object_id.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*, *arg0: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Tool_object_id.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.Tool_object_id.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Tool_object_id.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.domain.Tool\_object\_id, arg0: str) -> None
        2. \_\_init\_\_(self: csc.domain.Tool\_object\_id) -> None

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Tool_object_id.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*, *arg0: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Tool_object_id.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.Tool_object_id.__str__ "Permalink to this definition")

    is\_null(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Tool_object_id.is_null "Permalink to this definition")

    *static* null()  [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")[??](#csc.domain.Tool_object_id.null "Permalink to this definition")

    to\_string(*self: [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.Tool_object_id.to_string "Permalink to this definition")

csc.domain.delete\_entity\_3d\_processor(*scene: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *ids: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.delete_entity_3d_processor "Permalink to this definition")

csc.domain.get\_tool\_name(*scene: [csc.domain.Scene](#csc.domain.Scene "csc.domain.Scene")*, *ids: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.domain.Tool\_object\_id](#csc.domain.Tool_object_id "csc.domain.Tool_object_id")]*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.get_tool_name "Permalink to this definition")

*class* csc.math.Affine[??](#csc.math.Affine "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.math.Affine.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Affine](#csc.math.Affine "csc.math.Affine")*, *angle\_axisf: [csc.math.AngleAxis](#csc.math.AngleAxis "csc.math.AngleAxis")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Affine.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Affine.__module__ "Permalink to this definition")

    linear(*self: [csc.math.Affine](#csc.math.Affine "csc.math.Affine")*)  numpy.ndarray[numpy.float32[3, 3], flags.f\_contiguous][??](#csc.math.Affine.linear "Permalink to this definition")

*class* csc.math.AngleAxis[??](#csc.math.AngleAxis "Permalink to this definition")
:   AngleAxis class

    \_\_annotations\_\_ *= {}*[??](#csc.math.AngleAxis.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.AngleAxis](#csc.math.AngleAxis "csc.math.AngleAxis")*, *angle: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *axis: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.AngleAxis.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.AngleAxis.__module__ "Permalink to this definition")

    affine\_linear(*self: [csc.math.AngleAxis](#csc.math.AngleAxis "csc.math.AngleAxis")*)  numpy.ndarray[numpy.float32[3, 3], flags.writeable, flags.f\_contiguous][??](#csc.math.AngleAxis.affine_linear "Permalink to this definition")

    angle(*self: [csc.math.AngleAxis](#csc.math.AngleAxis "csc.math.AngleAxis")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.AngleAxis.angle "Permalink to this definition")

    axis(*self: [csc.math.AngleAxis](#csc.math.AngleAxis "csc.math.AngleAxis")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.AngleAxis.axis "Permalink to this definition")

*class* csc.math.Circle[??](#csc.math.Circle "Permalink to this definition")
:   Circle3d class

    \_\_annotations\_\_ *= {}*[??](#csc.math.Circle.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Circle](#csc.math.Circle "csc.math.Circle")*, *radius: numpy.ndarray[numpy.float32[3, 1]]*, *center: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *normal: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Circle.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Circle.__module__ "Permalink to this definition")

    center(*self: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Circle.center "Permalink to this definition")

    normal(*self: [csc.math.Circle](#csc.math.Circle "csc.math.Circle")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Circle.normal "Permalink to this definition")

    radius(*self: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Circle.radius "Permalink to this definition")

*class* csc.math.OrthogonalTransform[??](#csc.math.OrthogonalTransform "Permalink to this definition")
:   OrthogonalTransform class

    Implements orthogonal transform

    Variables:
    :   * **position** ??? Get set Vector3f
        * **rotation** ??? Get set Rotation

    \_\_annotations\_\_ *= {}*[??](#csc.math.OrthogonalTransform.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.math.OrthogonalTransform.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.math.OrthogonalTransform, position: numpy.ndarray[numpy.float32[3, 1]], rotate: csc.math.Quaternion) -> None
        2. \_\_init\_\_(self: csc.math.OrthogonalTransform) -> None

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.OrthogonalTransform.__module__ "Permalink to this definition")

    *property* position[??](#csc.math.OrthogonalTransform.position "Permalink to this definition")

    *property* rotation[??](#csc.math.OrthogonalTransform.rotation "Permalink to this definition")

*class* csc.math.ParametrizedLine[??](#csc.math.ParametrizedLine "Permalink to this definition")
:   ParametrizedLine class

    \_\_annotations\_\_ *= {}*[??](#csc.math.ParametrizedLine.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.ParametrizedLine](#csc.math.ParametrizedLine "csc.math.ParametrizedLine")*, *origin: numpy.ndarray[numpy.float32[3, 1]]*, *direction: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.ParametrizedLine.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.ParametrizedLine.__module__ "Permalink to this definition")

    projection(*self: [csc.math.ParametrizedLine](#csc.math.ParametrizedLine "csc.math.ParametrizedLine")*, *arg0: numpy.ndarray[numpy.float32[3, 1]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.ParametrizedLine.projection "Permalink to this definition")

*class* csc.math.Plane[??](#csc.math.Plane "Permalink to this definition")
:   Hyperplane class

    \_\_annotations\_\_ *= {}*[??](#csc.math.Plane.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*, *normal: numpy.ndarray[numpy.float32[3, 1]]*, *point: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Plane.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Plane.__module__ "Permalink to this definition")

    projection(*self: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*, *arg0: numpy.ndarray[numpy.float32[3, 1]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Plane.projection "Permalink to this definition")

*class* csc.math.Quaternion[??](#csc.math.Quaternion "Permalink to this definition")
:   Quaternion class

    This class is useful to calculate rotation operations.

    \_\_annotations\_\_ *= {}*[??](#csc.math.Quaternion.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*, *w: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *z: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Quaternion.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Quaternion.__module__ "Permalink to this definition")

    \_\_mul\_\_(*\*args*, *\*\*kwargs*)[??](#csc.math.Quaternion.__mul__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_mul\_\_(self: csc.math.Quaternion, arg0: csc.math.Quaternion) -> csc.math.Quaternion
        2. \_\_mul\_\_(self: csc.math.Quaternion, arg0: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]

    *static* from\_two\_vectors(*arg0: numpy.ndarray[numpy.float32[3, 1]]*, *arg1: numpy.ndarray[numpy.float32[3, 1]]*)  [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Quaternion.from_two_vectors "Permalink to this definition")

    *static* identity()  [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Quaternion.identity "Permalink to this definition")

    inverse(*self: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*)  [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Quaternion.inverse "Permalink to this definition")

    w(*self: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.w "Permalink to this definition")

    x(*self: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.x "Permalink to this definition")

    y(*self: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.y "Permalink to this definition")

    z(*self: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Quaternion.z "Permalink to this definition")

*class* csc.math.Rotation[??](#csc.math.Rotation "Permalink to this definition")
:   Rotation class

    The Euler angles implementation.

    \_\_annotations\_\_ *= {}*[??](#csc.math.Rotation.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Rotation.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Rotation.__module__ "Permalink to this definition")

    *static* from\_angle\_axis(*\*args*, *\*\*kwargs*)[??](#csc.math.Rotation.from_angle_axis "Permalink to this definition")
    :   Overloaded function.

        1. from\_angle\_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation
        2. from\_angle\_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation

    *static* from\_euler(*\*args*, *\*\*kwargs*)[??](#csc.math.Rotation.from_euler "Permalink to this definition")
    :   Overloaded function.

        1. from\_euler(x: float, y: float, z: float) -> csc.math.Rotation
        2. from\_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation

    *static* from\_quaternion(*\*args*, *\*\*kwargs*)[??](#csc.math.Rotation.from_quaternion "Permalink to this definition")
    :   Overloaded function.

        1. from\_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation
        2. from\_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation

    *static* from\_rotation\_matrix(*arg0: numpy.ndarray[numpy.float32[3, 3]]*)  [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")[??](#csc.math.Rotation.from_rotation_matrix "Permalink to this definition")

    to\_angle\_axis(*self: [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")*)  [csc.math.AngleAxis](#csc.math.AngleAxis "csc.math.AngleAxis")[??](#csc.math.Rotation.to_angle_axis "Permalink to this definition")

    to\_euler\_angles(*self: [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Rotation.to_euler_angles "Permalink to this definition")

    to\_euler\_angles\_x\_y\_z(*self: [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Rotation.to_euler_angles_x_y_z "Permalink to this definition")

    to\_quaternion(*self: [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")*)  [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.Rotation.to_quaternion "Permalink to this definition")

    to\_rotation\_matrix(*self: [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")*)  numpy.ndarray[numpy.float32[3, 3]][??](#csc.math.Rotation.to_rotation_matrix "Permalink to this definition")

*class* csc.math.ScaledTransform[??](#csc.math.ScaledTransform "Permalink to this definition")
:   ScaledTransform class

    Implements transform with the scale possibility.

    Variables:
    :   * **position** ??? Get set Vector3f
        * **rotation** ??? Get set Rotation
        * **scale** ??? Get set Vector3f

    \_\_annotations\_\_ *= {}*[??](#csc.math.ScaledTransform.__annotations__ "Permalink to this definition")

    \_\_copy\_\_(*self: [csc.math.ScaledTransform](#csc.math.ScaledTransform "csc.math.ScaledTransform")*)  [csc.math.ScaledTransform](#csc.math.ScaledTransform "csc.math.ScaledTransform")[??](#csc.math.ScaledTransform.__copy__ "Permalink to this definition")

    \_\_deepcopy\_\_(*self: [csc.math.ScaledTransform](#csc.math.ScaledTransform "csc.math.ScaledTransform")*, *arg0: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")*)  [csc.math.ScaledTransform](#csc.math.ScaledTransform "csc.math.ScaledTransform")[??](#csc.math.ScaledTransform.__deepcopy__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.ScaledTransform](#csc.math.ScaledTransform "csc.math.ScaledTransform")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.ScaledTransform.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.ScaledTransform.__module__ "Permalink to this definition")

    *property* position[??](#csc.math.ScaledTransform.position "Permalink to this definition")

    *property* rotation[??](#csc.math.ScaledTransform.rotation "Permalink to this definition")

    *property* scale[??](#csc.math.ScaledTransform.scale "Permalink to this definition")

*class* csc.math.SizesInterval[??](#csc.math.SizesInterval "Permalink to this definition")
:   SizesInterval class

    Implements the sizes interval basic methods

    \_\_annotations\_\_ *= {}*[??](#csc.math.SizesInterval.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*, *arg0: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.__eq__ "Permalink to this definition")

    \_\_hash\_\_ *= None*[??](#csc.math.SizesInterval.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.math.SizesInterval.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.math.SizesInterval) -> None
        2. \_\_init\_\_(self: csc.math.SizesInterval, start: int, end: int) -> None

    \_\_lt\_\_(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*, *arg0: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.__lt__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.SizesInterval.__module__ "Permalink to this definition")

    *static* construct\_in\_right\_order(*first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.construct_in_right_order "Permalink to this definition")

    contains(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*, *i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.contains "Permalink to this definition")

    empty(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.empty "Permalink to this definition")
    :   -> bool

    end(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.math.SizesInterval.end "Permalink to this definition")
    :   -> int

    inside\_interval\_inclusive(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.math.SizesInterval.inside_interval_inclusive "Permalink to this definition")

    *static* intersect\_intervals(*first: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*, *second: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.intersect_intervals "Permalink to this definition")

    *static* safe\_construct(*first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.safe_construct "Permalink to this definition")

    start(*self: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.math.SizesInterval.start "Permalink to this definition")
    :   -> int

    *static* union\_overlaping\_intervals(*first: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*, *second: [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")*)  [csc.math.SizesInterval](#csc.math.SizesInterval "csc.math.SizesInterval")[??](#csc.math.SizesInterval.union_overlaping_intervals "Permalink to this definition")

*class* csc.math.Sphere[??](#csc.math.Sphere "Permalink to this definition")
:   Sphere class

    \_\_annotations\_\_ *= {}*[??](#csc.math.Sphere.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*, *radius: numpy.ndarray[numpy.float32[3, 1]]*, *center: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Sphere.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Sphere.__module__ "Permalink to this definition")

    center(*self: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.Sphere.center "Permalink to this definition")

    radius(*self: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.Sphere.radius "Permalink to this definition")

*class* csc.math.Triangle[??](#csc.math.Triangle "Permalink to this definition")
:   Triangle class

    Structure from three points

    Variables:
    :   * **point1** ??? Get set Vector3f
        * **point2** ??? Get set Vector3f
        * **point3** ??? Get set Vector3f

    \_\_annotations\_\_ *= {}*[??](#csc.math.Triangle.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.math.Triangle](#csc.math.Triangle "csc.math.Triangle")*, *point1: numpy.ndarray[numpy.float32[3, 1]]*, *point2: numpy.ndarray[numpy.float32[3, 1]]*, *point3: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.Triangle.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.math'*[??](#csc.math.Triangle.__module__ "Permalink to this definition")

    *property* point1[??](#csc.math.Triangle.point1 "Permalink to this definition")

    *property* point2[??](#csc.math.Triangle.point2 "Permalink to this definition")

    *property* point3[??](#csc.math.Triangle.point3 "Permalink to this definition")

csc.math.basic\_transform\_from\_triangle(*triangle: math::Triangle*)  math::OrthogonalTransform[??](#csc.math.basic_transform_from_triangle "Permalink to this definition")
:   -> csc.math.OrthogonalTransform

csc.math.combine\_transforms(*first orthogonal transform: math::OrthogonalTransform*, *second orthogonal transform: math::OrthogonalTransform*)  math::OrthogonalTransform[??](#csc.math.combine_transforms "Permalink to this definition")
:   -> csc.math.OrthogonalTransform

csc.math.decompose\_matrix(*arg0: numpy.ndarray[numpy.float32[4, 4]]*)  domain::scene::model::data\_struct::ScaledTransform[??](#csc.math.decompose_matrix "Permalink to this definition")

csc.math.euler\_angles\_to\_quaternion\_x\_y\_z(*euler\_angles: numpy.ndarray[numpy.float32[3, 1]]*)  [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")[??](#csc.math.euler_angles_to_quaternion_x_y_z "Permalink to this definition")
:   -> Quaternionf

csc.math.euler\_flip(*arg0: numpy.ndarray[numpy.float32[3, 1]]*, *arg1: numpy.ndarray[numpy.float32[3, 1]]*)  [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation")[??](#csc.math.euler_flip "Permalink to this definition")

csc.math.get\_m3f\_diag(*matrix: numpy.ndarray[numpy.float32[3, 3]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.get_m3f_diag "Permalink to this definition")
:   -> Vector3f

csc.math.ik\_spline(*arg0: numpy.ndarray[numpy.float32[3, 1]]*, *arg1: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]]*, *arg2: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")]*, *arg3: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")]*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")]][??](#csc.math.ik_spline "Permalink to this definition")
:   -> Tuple<vector<Vector3f>, vector<Quaternion>>

csc.math.ik\_spline\_2(*arg0: numpy.ndarray[numpy.float32[3, 1]]*, *arg1: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]]*, *arg2: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")]*, *arg3: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")]*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")]][??](#csc.math.ik_spline_2 "Permalink to this definition")
:   -> Tuple<vector<Vector3f>, vector<Quaternion>>

csc.math.ik\_spline\_3(*arg0: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]]*, *arg1: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")]*, *arg2: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")]*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[numpy.ndarray[numpy.float32[3, 1]]], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")]][??](#csc.math.ik_spline_3 "Permalink to this definition")
:   -> Tuple<vector<Vector3f>, vector<Quaternion>>

csc.math.inverse\_transform\_point(*transform: math::OrthogonalTransform, point: numpy.ndarray[numpy.float32[3, 1]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.inverse_transform_point "Permalink to this definition")
:   -> Vector3f

csc.math.line\_on\_intersection\_planes(*arg0: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*, *arg1: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*)  [csc.math.ParametrizedLine](#csc.math.ParametrizedLine "csc.math.ParametrizedLine") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.line_on_intersection_planes "Permalink to this definition")

csc.math.modify\_position\_by\_matrix(*matrix: numpy.ndarray[numpy.float32[3, 3]]*, *position: numpy.ndarray[numpy.float32[3, 1]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.modify_position_by_matrix "Permalink to this definition")
:   -> Vector3f

csc.math.point\_on\_intersection\_planes(*arg0: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*, *arg1: [csc.math.Plane](#csc.math.Plane "csc.math.Plane")*)  numpy.ndarray[numpy.float32[3, 1]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.point_on_intersection_planes "Permalink to this definition")

csc.math.project\_point\_on\_basic\_line(*line\_direction: numpy.ndarray[numpy.float32[3, 1]]*, *point: numpy.ndarray[numpy.float32[3, 1]]*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.project_point_on_basic_line "Permalink to this definition")
:   -> Vector3f

csc.math.quaternion\_to\_euler\_angles\_x\_y\_z(*quaternion: [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion")*)  numpy.ndarray[numpy.float32[3, 1]][??](#csc.math.quaternion_to_euler_angles_x_y_z "Permalink to this definition")
:   -> Vector3f

csc.math.spheres\_intersection(*arg0: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*, *arg1: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*)  [csc.math.Circle](#csc.math.Circle "csc.math.Circle") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.spheres_intersection "Permalink to this definition")

csc.math.spheres\_intersection\_extended(*arg0: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*, *arg1: [csc.math.Sphere](#csc.math.Sphere "csc.math.Sphere")*)  [csc.math.Circle](#csc.math.Circle "csc.math.Circle") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.math.spheres_intersection_extended "Permalink to this definition")

csc.math.step\_linear\_func(*arg0: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *arg1: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *arg2: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[??](#csc.math.step_linear_func "Permalink to this definition")

csc.math.transform\_point(*\*args*, *\*\*kwargs*)[??](#csc.math.transform_point "Permalink to this definition")
:   Overloaded function.

    1. transform\_point(transform: math::OrthogonalTransform, point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]

       > -> Vector3f
    2. transform\_point(matrix: numpy.ndarray[numpy.float32[4, 4]], point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]

       > -> Vector3f

csc.math.transforms\_difference(*first orthogonal transform: math::OrthogonalTransform*, *second orthogonal transform: math::OrthogonalTransform*)  math::OrthogonalTransform[??](#csc.math.transforms_difference "Permalink to this definition")
:   -> csc.math.OrthogonalTransform

csc.math.untwist(*arg0: numpy.ndarray[numpy.float32[4, 4]]*, *arg1: numpy.ndarray[numpy.float32[4, 4]]*, *arg2: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *arg3: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *arg4: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg5: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  numpy.ndarray[numpy.float32[4, 4]][??](#csc.math.untwist "Permalink to this definition")
:   (weight:float,roll:float,axis:int,negate:bool,
    parentMatrix:Matrix4f,objectMatrix:Matrix4f) -> Matrix4f

*class* csc.physics.PosMass[??](#csc.physics.PosMass "Permalink to this definition")
:   PosMass class

    This structure contains the mass and the position

    Variables:
    :   * **mass** ??? Get Set float.
        * **position** ??? Get Set Vector3f.

    \_\_annotations\_\_ *= {}*[??](#csc.physics.PosMass.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.physics.PosMass](#csc.physics.PosMass "csc.physics.PosMass")*, *mass: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *position: numpy.ndarray[numpy.float32[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.physics.PosMass.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.physics'*[??](#csc.physics.PosMass.__module__ "Permalink to this definition")

    *property* mass[??](#csc.physics.PosMass.mass "Permalink to this definition")

    *property* position[??](#csc.physics.PosMass.position "Permalink to this definition")

csc.physics.inertia\_tensor(*mass\_and\_poses: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.physics.PosMass](#csc.physics.PosMass "csc.physics.PosMass")]*, *center: numpy.ndarray[numpy.float32[3, 1]]*)  numpy.ndarray[numpy.float32[3, 3]][??](#csc.physics.inertia_tensor "Permalink to this definition")
:   -> Matrix3f

## csc.update The Cascadeur python module that implements basic update editor methods and its infrastructure.[??](#csc-update-the-cascadeur-python-module-that-implements-basic-update-editor-methods-and-its-infrastructure "Permalink to this heading")

Update editor provides a node-like interface to edit data and setting graphs.
Naming conventions: regular means the same as data. It differs stuff from settings.

Additional functionality.
Update editor can be used to check what data functions will be active if you set some datas as actual.

AttributeId = std::variant<RegularFunctionAttributeId, ActivityAttributeId,
:   RegularDataAttributeId, ActualityAttributeId,
    SettingFunctionAttributeId, SettingDataAttributeId,
    GroupAttributeId, ExternalPropertyAttributeId,
    ConstantDataAttributeId, ConstantSettingAttributeId>;

|  |  |
| --- | --- |
| [`csc.update.NodeAttribute`](#csc.update.NodeAttribute "csc.update.NodeAttribute") | NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute. |
| [`csc.update.RegularDataAttribute`](#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute") | RegularDataAttribute represents an attribute of a regular data. |
| [`csc.update.ActualityAttribute`](#csc.update.ActualityAttribute "csc.update.ActualityAttribute") | ActualityAttribute shows whether data is actual at the start of the graphs update. |
| [`csc.update.ConstantDataAttribute`](#csc.update.ConstantDataAttribute "csc.update.ConstantDataAttribute") | ConstantDataAttribute represents an attribute of a constant regular data. |
| [`csc.update.ConstantSettingAttribute`](#csc.update.ConstantSettingAttribute "csc.update.ConstantSettingAttribute") | ConstantSettingAttribute represents an attribute of a constant setting. |
| [`csc.update.ExternalPropertyAttribute`](#csc.update.ExternalPropertyAttribute "csc.update.ExternalPropertyAttribute") | ExternalPropertyAttribute represents an attribute of the external properties of the update. |
| [`csc.update.SettingFunctionAttribute`](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute") | SettingFunctionAttribute represents an attribute of a setting function. |
| [`csc.update.InterfaceAttributeSide`](#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide") | InterfaceAttributeSide enumerable |
| [`csc.update.InterfaceAttribute`](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") | InterfaceAttribute represents a group attribute. |
| [`csc.update.RegularFunctionAttribute`](#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute") | RegularFunctionAttribute represents an attribute of a data function. |
| [`csc.update.ActivityAttribute`](#csc.update.ActivityAttribute "csc.update.ActivityAttribute") | ActivityAttribute represents the activity of the data function. |
| [`csc.update.SettingDataAttribute`](#csc.update.SettingDataAttribute "csc.update.SettingDataAttribute") | SettingDataAttribute represents an attribute of a setting. |
| [`csc.update.Node`](#csc.update.Node "csc.update.Node") | Node class represents a generic Node and implements methods that are common for all nodes |
| [`csc.update.InterfaceNode`](#csc.update.InterfaceNode "csc.update.InterfaceNode") | InterfaceNode is a node inside the group that represents its connections with the ouside nodes. |
| [`csc.update.ConstantDatas`](#csc.update.ConstantDatas "csc.update.ConstantDatas") | ConstantDatas represents a node of constant datas. |
| [`csc.update.ConstantSettings`](#csc.update.ConstantSettings "csc.update.ConstantSettings") | ConstantSettings represents a node of constant settings. |
| [`csc.update.External
**Properties:**
- ``](#csc.update.ExternalProperties "csc.update.ExternalProperties") | ExternalProperties represents a node of external properties. |
| [`csc.update.RegularFunction`](#csc.update.RegularFunction "csc.update.RegularFunction") | RegularFunction class represents a node that calculates same operation, done with datas. |
| [`csc.update.SettingData`](#csc.update.SettingData "csc.update.SettingData") | SettingData class represents a node that calculates same operation, done with settings. |
| [`csc.update.SettingFunction`](#csc.update.SettingFunction "csc.update.SettingFunction") | SettingFunction class |
| [`csc.update.Object`](#csc.update.Object "csc.update.Object") | Object class represents an object node. |
| [`csc.update.RegularData`](#csc.update.RegularData "csc.update.RegularData") | RegularData class represents a node of a data. |
| [`csc.update.Group`](#csc.update.Group "csc.update.Group") | Group class |
| [`csc.update.ObjectGroup`](#csc.update.ObjectGroup "csc.update.ObjectGroup") | ObjectGroup class represents object group node |
| [`csc.update.UpdateGroup`](#csc.update.UpdateGroup "csc.update.UpdateGroup") | UpdateGroup class represents update group node |
| [`csc.update.HierarchyUpdate`](#csc.update.HierarchyUpdate "csc.update.HierarchyUpdate") | HierarchyUpdate class provides concrete operations with connections |
| [`csc.update.Update`](#csc.update.Update "csc.update.Update") | Update class represents the whole update editor |
| [`csc.update.RegularFunctionAttributeId`](#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute |
| [`csc.update.RegularDataAttributeId`](#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | RegularDataAttributeId is defined by the data id. |
| [`csc.update.ActualityAttributeId`](#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | ActualityAttributeId is defined by the data id. |
| [`csc.update.SettingFunctionAttributeId`](#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | SettingFunctionAttributeId is defined by the SettingFunctionId and the index of the attribute |
| [`csc.update.GroupId`](#csc.update.GroupId "csc.update.GroupId") |  |
| [`csc.update.GroupAttributeId`](#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | GroupAttributeId is defined by the GroupId and the guid-based id of the attribute. |
| [`csc.update.ExternalPropertiesId`](#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") | ExternalPropertiesId is a guid based id. |
| [`csc.update.ExternalProperty`](#csc.update.ExternalProperty "csc.update.ExternalProperty") | ExternalProperty enum |
| [`csc.update.ExternalPropertyAttributeId`](#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | ExternalPropertyAttributeId is defined by the ExternalPropertiesId and the value of the ExternalProperty enum |
| [`csc.update.ConstantDatasId`](#csc.update.ConstantDatasId "csc.update.ConstantDatasId") | ConstantDatasId is a guid based id. |
| [`csc.update.ConstantDataAttributeId`](#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant |
| [`csc.update.ConstantSettingsId`](#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") | ConstantSettingsId is a guid based id. |
| [`csc.update.ConstantSettingAttributeId`](#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId") | ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant |
| [`csc.update.Connection`](#csc.update.Connection "csc.update.Connection") | Connection class |
| [`csc.update.InterfaceId`](#csc.update.InterfaceId "csc.update.InterfaceId") | InterfaceId is defined by the GroupId and the direction type of the node - input or output connection node. |`

*class* csc.update.ActivityAttribute[??](#csc.update.ActivityAttribute "Permalink to this definition")
:   ActivityAttribute represents the activity of the data function.
    It should be bool.
    If true - function is active, if false - inactive. If not set - always active.
    It is an input-only attribute.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ActivityAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ActivityAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ActivityAttribute.__module__ "Permalink to this definition")

*class* csc.update.ActualityAttribute[??](#csc.update.ActualityAttribute "Permalink to this definition")
:   ActualityAttribute shows whether data is actual at the start of the graphs update.
    It???s always an output attribute.
    It can be connected with setting functions.

    !Connections directly with data functions activity are not supported, use copy setting function instead)

    \_\_annotations\_\_ *= {}*[??](#csc.update.ActualityAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ActualityAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ActualityAttribute.__module__ "Permalink to this definition")

*class* csc.update.ActualityAttributeId[??](#csc.update.ActualityAttributeId "Permalink to this definition")
:   ActualityAttributeId is defined by the data id. It???s an output only attribute.
    Each data can be actual or non-actual at the start of the graphs update.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ActualityAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ActualityAttributeId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.update.ActualityAttributeId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.update.ActualityAttributeId, arg0: csc.model.DataId) -> None
        3. \_\_init\_\_(self: csc.update.ActualityAttributeId) -> None

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ActualityAttributeId.__module__ "Permalink to this definition")

*class* csc.update.Connection[??](#csc.update.Connection "Permalink to this definition")
:   Connection class

    Implements the Connection between two attributes

    Variables:
    :   * **source** ??? Get output AttributeId of the source
        * **destination** ??? Get input AttributeId of the destination

    AttributeId = std::variant<RegularFunctionAttributeId, ActivityAttributeId,
    :   RegularDataAttributeId, ActualityAttributeId,
        SettingFunctionAttributeId, SettingDataAttributeId,
        GroupAttributeId, ExternalPropertyAttributeId,
        ConstantDataAttributeId, ConstantSettingAttributeId>

    \_\_annotations\_\_ *= {}*[??](#csc.update.Connection.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.Connection](#csc.update.Connection "csc.update.Connection")*, *source: [csc.update.RegularFunctionAttributeId](#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*, *destination: [csc.update.RegularFunctionAttributeId](#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Connection.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Connection.__module__ "Permalink to this definition")

    *property* destination[??](#csc.update.Connection.destination "Permalink to this definition")

    *property* source[??](#csc.update.Connection.source "Permalink to this definition")

*class* csc.update.ConstantDataAttribute[??](#csc.update.ConstantDataAttribute "Permalink to this definition")
:   ConstantDataAttribute represents an attribute of a constant regular data.
    It???s always an output attribute.
    It can be connected with setting functions or data functions activity.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantDataAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantDataAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantDataAttribute.__module__ "Permalink to this definition")

*class* csc.update.ConstantDataAttributeId[??](#csc.update.ConstantDataAttributeId "Permalink to this definition")
:   ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant

    Implements the ConstantDataAttributeId.

    Variables:
    :   * **group\_id** ??? Get ConstantDatasId
        * **attribute\_id** ??? Get the data id (csc.model.DataId)

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantDataAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.ConstantDataAttributeId](#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId")*, *group\_id: [csc.update.ConstantDatasId](#csc.update.ConstantDatasId "csc.update.ConstantDatasId")*, *attribute\_id: [csc.model.DataId](#csc.model.DataId "csc.model.DataId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ConstantDataAttributeId.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantDataAttributeId.__module__ "Permalink to this definition")

    *property* attribute\_id[??](#csc.update.ConstantDataAttributeId.attribute_id "Permalink to this definition")

    *property* group\_id[??](#csc.update.ConstantDataAttributeId.group_id "Permalink to this definition")

*class* csc.update.ConstantDatas[??](#csc.update.ConstantDatas "Permalink to this definition")
:   ConstantDatas represents a node of constant datas. It is present in any place.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantDatas.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantDatas.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantDatas.__module__ "Permalink to this definition")

    add\_data(*self: [csc.update.ConstantDatas](#csc.update.ConstantDatas "csc.update.ConstantDatas")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | numpy.ndarray[numpy.float32[3, 1]] | numpy.ndarray[numpy.float32[4, 1]] | [csc.math.Rotation](#csc.math.Rotation "csc.math.Rotation") | numpy.ndarray[numpy.float32[3, 3]] | numpy.ndarray[numpy.float32[4, 4]] | [csc.math.Quaternion](#csc.math.Quaternion "csc.math.Quaternion") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | numpy.ndarray[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[3, 1]]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ConstantDatas.add_data "Permalink to this definition")
    :   value: Data.Value

*class* csc.update.ConstantDatasId[??](#csc.update.ConstantDatasId "Permalink to this definition")
:   ConstantDatasId is a guid based id.
    It is always equal to the group id, where the constant will be used.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantDatasId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantDatasId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.update.ConstantDatasId, arg0: csc.update.GroupId) -> None
        2. \_\_init\_\_(self: csc.update.ConstantDatasId, arg0: str) -> None
        3. \_\_init\_\_(self: csc.update.ConstantDatasId) -> None

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantDatasId.__module__ "Permalink to this definition")

*class* csc.update.ConstantSettingAttribute[??](#csc.update.ConstantSettingAttribute "Permalink to this definition")
:   ConstantSettingAttribute represents an attribute of a constant setting.
    It???s always an output attribute.
    It can be connected with data functions.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantSettingAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantSettingAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantSettingAttribute.__module__ "Permalink to this definition")

*class* csc.update.ConstantSettingAttributeId[??](#csc.update.ConstantSettingAttributeId "Permalink to this definition")
:   ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant

    Implements the ConstantSettingAttributeId.

    Variables:
    :   * **group\_id** ??? Get ConstantSettingsId
        * **attribute\_id** ??? Get csc.model.SettingId

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantSettingAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.ConstantSettingAttributeId](#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*, *group\_id: [csc.update.ConstantSettingsId](#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId")*, *attribute\_id: [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ConstantSettingAttributeId.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantSettingAttributeId.__module__ "Permalink to this definition")

    *property* attribute\_id[??](#csc.update.ConstantSettingAttributeId.attribute_id "Permalink to this definition")

    *property* group\_id[??](#csc.update.ConstantSettingAttributeId.group_id "Permalink to this definition")

*class* csc.update.ConstantSettings[??](#csc.update.ConstantSettings "Permalink to this definition")
:   ConstantSettings represents a node of constant settings. It is present in any place.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantSettings.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantSettings.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantSettings.__module__ "Permalink to this definition")

    add\_setting(*self: [csc.update.ConstantSettings](#csc.update.ConstantSettings "csc.update.ConstantSettings")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ConstantSettings.add_setting "Permalink to this definition")
    :   value: Setting.Value

*class* csc.update.ConstantSettingsId[??](#csc.update.ConstantSettingsId "Permalink to this definition")
:   ConstantSettingsId is a guid based id.
    It is always equal to the group id, where the constant will be used.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ConstantSettingsId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ConstantSettingsId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.update.ConstantSettingsId, arg0: csc.update.GroupId) -> None
        2. \_\_init\_\_(self: csc.update.ConstantSettingsId, arg0: str) -> None
        3. \_\_init\_\_(self: csc.update.ConstantSettingsId) -> None

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ConstantSettingsId.__module__ "Permalink to this definition")

*class* csc.update.External
**Properties:**
- `[??](#csc.update.ExternalProperties "Permalink to this definition")
:   ExternalProperties represents a node of external properties.
    (E.g. is this update called during interpolation or not)
    It is represent in any place.`

    \_\_annotations\_\_ *= {}*[??](#csc.update.External
**Properties:**
- .__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.External
**Properties:**
- .__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.External
**Properties:**
- .__module__ "Permalink to this definition")

    property\_outputs(*self: [csc.update.External
**Properties:**
- `](#csc.update.ExternalProperties "csc.update.ExternalProperties")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.ExternalPropertyAttribute](#csc.update.ExternalPropertyAttribute "csc.update.ExternalPropertyAttribute")][??](#csc.update.ExternalProperties.property_outputs "Permalink to this definition")`

*class* csc.update.External
**Properties:**
- `Id[??](#csc.update.ExternalPropertiesId "Permalink to this definition")
:   ExternalPropertiesId is a guid based id.
    It is always equal to the group id, where the external property will be used.`

    \_\_annotations\_\_ *= {}*[??](#csc.update.External
**Properties:**
- Id.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.External
**Properties:**
- Id.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.update.External
**Properties:**
- Id, arg0: csc.update.GroupId) -> None
        2. \_\_init\_\
- `_(self: csc.update.ExternalPropertiesId, arg0: str) -> None
        3. \_\_init\_\`
- `_(self: csc.update.ExternalPropertiesId) -> None`

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.External
**Properties:**
- Id.__module__ "Permalink to this definition")

*class* csc.update.ExternalProperty[??](#csc.update.ExternalProperty "Permalink to this definition")
:   > ExternalProperty enum
    >
    > This enumerates the basic types of ExternalProperty states:
    > Fixation,
    > IsForwardKinematics,
    > KinematicsType,
    > InterpolationType,
    > IsInterpolation,
    > AfterPhysics,
    > IsKey

    Members:

    > Fixation
    >
    > IsForwardKinematics
    >
    > KinematicsType
    >
    > InterpolationType
    >
    > IsInterpolation
    >
    > AfterPhysics
    >
    > IsKey

    AfterPhysics *= <ExternalProperty.AfterPhysics: 5>*[??](#csc.update.ExternalProperty.AfterPhysics "Permalink to this definition")

    Fixation *= <ExternalProperty.Fixation: 0>*[??](#csc.update.ExternalProperty.Fixation "Permalink to this definition")

    InterpolationType *= <ExternalProperty.InterpolationType: 3>*[??](#csc.update.ExternalProperty.InterpolationType "Permalink to this definition")

    IsForwardKinematics *= <ExternalProperty.IsForwardKinematics: 1>*[??](#csc.update.ExternalProperty.IsForwardKinematics "Permalink to this definition")

    IsInterpolation *= <ExternalProperty.IsInterpolation: 4>*[??](#csc.update.ExternalProperty.IsInterpolation "Permalink to this definition")

    IsKey *= <ExternalProperty.IsKey: 6>*[??](#csc.update.ExternalProperty.IsKey "Permalink to this definition")

    KinematicsType *= <ExternalProperty.KinematicsType: 2>*[??](#csc.update.ExternalProperty.KinematicsType "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.update.ExternalProperty.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.ExternalProperty.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.ExternalProperty.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.ExternalProperty.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.update.ExternalProperty](#csc.update.ExternalProperty "csc.update.ExternalProperty")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.ExternalProperty.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.ExternalProperty](#csc.update.ExternalProperty "csc.update.ExternalProperty")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ExternalProperty.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.update.ExternalProperty](#csc.update.ExternalProperty "csc.update.ExternalProperty")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.ExternalProperty.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'AfterPhysics': <ExternalProperty.AfterPhysics: 5>, 'Fixation': <ExternalProperty.Fixation: 0>, 'InterpolationType': <ExternalProperty.InterpolationType: 3>, 'IsForwardKinematics': <ExternalProperty.IsForwardKinematics: 1>, 'IsInterpolation': <ExternalProperty.IsInterpolation: 4>, 'IsKey': <ExternalProperty.IsKey: 6>, 'KinematicsType': <ExternalProperty.KinematicsType: 2>}*[??](#csc.update.ExternalProperty.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ExternalProperty.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.ExternalProperty.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.ExternalProperty.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.update.ExternalProperty](#csc.update.ExternalProperty "csc.update.ExternalProperty")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ExternalProperty.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.ExternalProperty.__str__ "Permalink to this definition")

    *property* name[??](#csc.update.ExternalProperty.name "Permalink to this definition")

    *property* value[??](#csc.update.ExternalProperty.value "Permalink to this definition")

*class* csc.update.ExternalPropertyAttribute[??](#csc.update.ExternalPropertyAttribute "Permalink to this definition")
:   ExternalPropertyAttribute represents an attribute of the external properties of the update.
    It???s always an output attribute.
    It is settings based and thus can be connected with setting functions or data functions activity.

    \_\_annotations\_\_ *= {}*[??](#csc.update.ExternalPropertyAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ExternalPropertyAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ExternalPropertyAttribute.__module__ "Permalink to this definition")

*class* csc.update.ExternalPropertyAttributeId[??](#csc.update.ExternalPropertyAttributeId "Permalink to this definition")
:   ExternalPropertyAttributeId is defined by the External
**Properties:**
- Id and the value of the ExternalProperty enum

    Implements the ExternalPropertyAttributeId.

    Variables:
    :   * **node\_id** ??? Get GroupId
        * **property** ??? Get ExternalProperty enum value

    \_\_annotations\_\_ *= {}*[??](#csc.update.ExternalPropertyAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.ExternalPropertyAttributeId](#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId")*, *node\_id: [csc.update.External
**Properties:**
- `Id](#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId")*, *property: [csc.update.ExternalProperty](#csc.update.ExternalProperty "csc.update.ExternalProperty")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.ExternalPropertyAttributeId.__init__ "Permalink to this definition")`

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ExternalPropertyAttributeId.__module__ "Permalink to this definition")

    *property* node\_id[??](#csc.update.ExternalPropertyAttributeId.node_id "Permalink to this definition")

    *property* property[??](#csc.update.ExternalPropertyAttributeId.property "Permalink to this definition")

*class* csc.update.Group[??](#csc.update.Group "Permalink to this definition")
:   Group class

    Variables:
    :   **node** ??? overridden by name || node, access node by name or id

    \_\_annotations\_\_ *= {}*[??](#csc.update.Group.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Group.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Group.__module__ "Permalink to this definition")

    add\_input(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.add_input "Permalink to this definition")

    add\_output(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.add_output "Permalink to this definition")

    constant\_datas(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [csc.update.ConstantDatas](#csc.update.ConstantDatas "csc.update.ConstantDatas")[??](#csc.update.Group.constant_datas "Permalink to this definition")
    :   get virtual node to access constant datas

    constant\_settings(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [csc.update.ConstantSettings](#csc.update.ConstantSettings "csc.update.ConstantSettings")[??](#csc.update.Group.constant_settings "Permalink to this definition")
    :   get virtual node to access constant settings

    create\_group(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Group](#csc.update.Group "csc.update.Group")[??](#csc.update.Group.create_group "Permalink to this definition")

    delete\_node(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *node: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Group.delete_node "Permalink to this definition")

    group(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *nodes: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Node](#csc.update.Node "csc.update.Node")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Group](#csc.update.Group "csc.update.Group")[??](#csc.update.Group.group "Permalink to this definition")

    group\_id(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")[??](#csc.update.Group.group_id "Permalink to this definition")
    :   create sub group

    has\_node(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Group.has_node "Permalink to this definition")
    :   check whether there is a child node with a given name

    input\_interface\_node(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")[??](#csc.update.Group.input_interface_node "Permalink to this definition")

    interface\_input(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.interface_input "Permalink to this definition")

    interface\_inputs(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")][??](#csc.update.Group.interface_inputs "Permalink to this definition")
    :   get group attributes as interface attributes

    interface\_node(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *direction: [csc.Direction](#csc.Direction "csc.Direction")*)  [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")[??](#csc.update.Group.interface_node "Permalink to this definition")
    :   access the interface node

    interface\_output(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Group.interface_output "Permalink to this definition")

    interface\_outputs(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")][??](#csc.update.Group.interface_outputs "Permalink to this definition")

    is\_root(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")[??](#csc.update.Group.is_root "Permalink to this definition")

    leaf\_children(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Node](#csc.update.Node "csc.update.Node")][??](#csc.update.Group.leaf_children "Permalink to this definition")
    :   get all leaf nodes (settings, datas, functions)

    node(*\*args*, *\*\*kwargs*)[??](#csc.update.Group.node "Permalink to this definition")
    :   Overloaded function.

        1. node(self: csc.update.Group, name: str) -> csc.update.Node
        2. node(self: csc.update.Group, node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.External
**Properties:**
- Id, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) -> csc.update.Node

    node\_deep(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Node](#csc.update.Node "csc.update.Node")[??](#csc.update.Group.node_deep "Permalink to this definition")
    :   access node by name or id recursively

    node\_with\_type(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *type\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Node](#csc.update.Node "csc.update.Node")[??](#csc.update.Group.node_with_type "Permalink to this definition")
    :   find node with name and type

    node\_with\_type\_deep(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*, *type\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.Node](#csc.update.Node "csc.update.Node")[??](#csc.update.Group.node_with_type_deep "Permalink to this definition")
    :   find node with name and type recursively

    nodes(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Node](#csc.update.Node "csc.update.Node")][??](#csc.update.Group.nodes "Permalink to this definition")
    :   get all children (their children are not included)

    output\_interface\_node(*self: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")[??](#csc.update.Group.output_interface_node "Permalink to this definition")

*class* csc.update.GroupAttributeId[??](#csc.update.GroupAttributeId "Permalink to this definition")
:   GroupAttributeId is defined by the GroupId and the guid-based id of the attribute.
    Group attribute names and indeces can change, so they are provided with their own guid

    Implements the GroupAttributeId.

    Variables:
    :   * **group\_id** ??? Get GroupId
        * **attribute\_id** ??? Get csc.Guid - id of the attribute

    \_\_annotations\_\_ *= {}*[??](#csc.update.GroupAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.GroupAttributeId](#csc.update.GroupAttributeId "csc.update.GroupAttributeId")*, *group\_id: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *attribute\_id: [csc.Guid](#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.GroupAttributeId.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.GroupAttributeId.__module__ "Permalink to this definition")

    *property* attribute\_id[??](#csc.update.GroupAttributeId.attribute_id "Permalink to this definition")

    *property* group\_id[??](#csc.update.GroupAttributeId.group_id "Permalink to this definition")

*class* csc.update.GroupId[??](#csc.update.GroupId "Permalink to this definition")
:   \_\_annotations\_\_ *= {}*[??](#csc.update.GroupId.__annotations__ "Permalink to this definition")

    \_\_cmp\_\_(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg0: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.GroupId.__cmp__ "Permalink to this definition")

    \_\_eq\_\_(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg0: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.GroupId.__eq__ "Permalink to this definition")

    \_\_hash\_\_(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.GroupId.__hash__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.GroupId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.update.GroupId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.update.GroupId) -> None

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.GroupId.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *arg0: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.GroupId.__ne__ "Permalink to this definition")

    \_\_str\_\_(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.GroupId.__str__ "Permalink to this definition")

    is\_null(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.GroupId.is_null "Permalink to this definition")

    *static* null()  [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")[??](#csc.update.GroupId.null "Permalink to this definition")

    to\_string(*self: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.GroupId.to_string "Permalink to this definition")

*class* csc.update.HierarchyUpdate[??](#csc.update.HierarchyUpdate "Permalink to this definition")
:   HierarchyUpdate class provides concrete operations with connections

    \_\_annotations\_\_ *= {}*[??](#csc.update.HierarchyUpdate.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.HierarchyUpdate.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.HierarchyUpdate.__module__ "Permalink to this definition")

    add\_connection(*self: [csc.update.HierarchyUpdate](#csc.update.HierarchyUpdate "csc.update.HierarchyUpdate")*, *connection: [csc.update.Connection](#csc.update.Connection "csc.update.Connection")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.HierarchyUpdate.add_connection "Permalink to this definition")

    remove\_connection(*self: [csc.update.HierarchyUpdate](#csc.update.HierarchyUpdate "csc.update.HierarchyUpdate")*, *connection: [csc.update.Connection](#csc.update.Connection "csc.update.Connection")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.HierarchyUpdate.remove_connection "Permalink to this definition")

*class* csc.update.InterfaceAttribute[??](#csc.update.InterfaceAttribute "Permalink to this definition")
:   InterfaceAttribute represents a group attribute.
    Can be potentially connected to any attribute.

    Interface attribute can be:
    1. An attribute of input/output node inside the group
    2. An attribute of the group node itself, in the parent group layout (outside the group)
    We will call this attributes ???paired???. For each attribute there is a paired one. They have the same attribute ids and names.
    Sometimes it???s easier to think of them as of one attribute that has 2 sides. But in terms of this class this are two separate objects.

    \_\_annotations\_\_ *= {}*[??](#csc.update.InterfaceAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.InterfaceAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.InterfaceAttribute.__module__ "Permalink to this definition")

    group\_attribute\_id(*self: [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*)  [csc.update.GroupAttributeId](#csc.update.GroupAttributeId "csc.update.GroupAttributeId")[??](#csc.update.InterfaceAttribute.group_attribute_id "Permalink to this definition")
    :   get the group attribute id

    other\_side(*self: [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.InterfaceAttribute.other_side "Permalink to this definition")
    :   Get the paired attribute (e.g. the other side of the attribute)

    set\_name(*self: [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceAttribute.set_name "Permalink to this definition")
    :   Rename the attribute

*class* csc.update.InterfaceAttributeSide[??](#csc.update.InterfaceAttributeSide "Permalink to this definition")
:   > InterfaceAttributeSide enumerable
    >
    > InterfaceSide - inside the group, GroupSide - when the group is a node

    Members:

    > InterfaceSide
    >
    > GroupSide

    GroupSide *= <InterfaceAttributeSide.GroupSide: 1>*[??](#csc.update.InterfaceAttributeSide.GroupSide "Permalink to this definition")

    InterfaceSide *= <InterfaceAttributeSide.InterfaceSide: 0>*[??](#csc.update.InterfaceAttributeSide.InterfaceSide "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.update.InterfaceAttributeSide.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.update.InterfaceAttributeSide](#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.InterfaceAttributeSide](#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__init__ "Permalink to this definition")

    \_\_int\_\_(*self: [csc.update.InterfaceAttributeSide](#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'GroupSide': <InterfaceAttributeSide.GroupSide: 1>, 'InterfaceSide': <InterfaceAttributeSide.InterfaceSide: 0>}*[??](#csc.update.InterfaceAttributeSide.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.InterfaceAttributeSide.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.update.InterfaceAttributeSide](#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.InterfaceAttributeSide.__str__ "Permalink to this definition")

    *property* name[??](#csc.update.InterfaceAttributeSide.name "Permalink to this definition")

    *property* value[??](#csc.update.InterfaceAttributeSide.value "Permalink to this definition")

*class* csc.update.InterfaceId[??](#csc.update.InterfaceId "Permalink to this definition")
:   InterfaceId is defined by the GroupId and the direction type of the node - input or output connection node.

    Implements the InterfaceId.

    Variables:
    :   * **group\_id** ??? Get GroupId
        * **direction** ??? Get direction type (csc.Direction)

    \_\_annotations\_\_ *= {}*[??](#csc.update.InterfaceId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.InterfaceId](#csc.update.InterfaceId "csc.update.InterfaceId")*, *group\_id: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*, *direction: [csc.Direction](#csc.Direction "csc.Direction")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceId.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.InterfaceId.__module__ "Permalink to this definition")

    *property* direction[??](#csc.update.InterfaceId.direction "Permalink to this definition")

    *property* group\_id[??](#csc.update.InterfaceId.group_id "Permalink to this definition")

*class* csc.update.InterfaceNode[??](#csc.update.InterfaceNode "Permalink to this definition")
:   InterfaceNode is a node inside the group that represents its connections with the ouside nodes.
    Its attributes are csc.update.Interface
**Attributes:**

    \_\_annotations\_\_ *= {}*[??](#csc.update.InterfaceNode.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.InterfaceNode.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.InterfaceNode.__module__ "Permalink to this definition")

    add\_attribute(*self: [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.InterfaceNode.add_attribute "Permalink to this definition")

    direction(*self: [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")*)  [csc.Direction](#csc.Direction "csc.Direction")[??](#csc.update.InterfaceNode.direction "Permalink to this definition")
    :   -> csc.DirectionValue

    interface\_attributes(*self: [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")][??](#csc.update.InterfaceNode.interface_attributes "Permalink to this definition")
    :   -> InterfaceAttribute[]

    move\_attribute(*self: [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")*, *attribute: [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*, *position: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceNode.move_attribute "Permalink to this definition")
    :   attribute: InterfaceAttribute | position: int

    remove\_attribute(*self: [csc.update.InterfaceNode](#csc.update.InterfaceNode "csc.update.InterfaceNode")*, *attribute: [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.InterfaceNode.remove_attribute "Permalink to this definition")
    :   attribute: InterfaceAttribute

*class* csc.update.Node[??](#csc.update.Node "Permalink to this definition")
:   Node class represents a generic Node and implements methods that are common for all nodes

    \_\_annotations\_\_ *= {}*[??](#csc.update.Node.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Node.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Node.__module__ "Permalink to this definition")

    attributes(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *d: [csc.Direction](#csc.Direction "csc.Direction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.Node.attributes "Permalink to this definition")
    :   array of all input and output attributes

    equal\_to(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *arg0: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.equal_to "Permalink to this definition")

    full\_name(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.Node.full_name "Permalink to this definition")
    :   name with all the parent nodes

    has\_input(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.has_input "Permalink to this definition")
    :   check if there is an input with such a name

    has\_output(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.has_output "Permalink to this definition")
    :   check if there is an output with such a name

    id(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId") | [csc.update.InterfaceId](#csc.update.InterfaceId "csc.update.InterfaceId") | [csc.update.External
**Properties:**
- `Id](#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") | [csc.update.ConstantDatasId](#csc.update.ConstantDatasId "csc.update.ConstantDatasId") | [csc.update.ConstantSettingsId](#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") | [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.model.DataId](#csc.model.DataId "csc.model.DataId") | [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId") | [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")[??](#csc.update.Node.id "Permalink to this definition")
    :   get uniqui id`

    input(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")[??](#csc.update.Node.input "Permalink to this definition")
    :   shortcut if node has only one input attribute

    inputs(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.Node.inputs "Permalink to this definition")
    :   array of all the inputes attributes

    is\_active(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.is_active "Permalink to this definition")
    :   check whether it is active for current actualities states
        (see Additional functionality in csc.update.UpdateEditor)

    is\_fictive(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.Node.is_fictive "Permalink to this definition")
    :   whether it is a fictive node (constants, inputs, outputs of a group or external properties)

    name(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.Node.name "Permalink to this definition")
    :   get name

    output(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")[??](#csc.update.Node.output "Permalink to this definition")
    :   shortcut if node has only one output attribute

    outputs(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.Node.outputs "Permalink to this definition")
    :   array of all the outputs attributes

    parent\_group(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  domain::update\_editor::Group[??](#csc.update.Node.parent_group "Permalink to this definition")
    :   return parent group (where this group node is located)

    parent\_object(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*)  domain::update\_editor::Object[??](#csc.update.Node.parent_object "Permalink to this definition")
    :   return object of the node. Will return null if this is not an update group

    set\_name(*self: [csc.update.Node](#csc.update.Node "csc.update.Node")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Node.set_name "Permalink to this definition")
    :   rename node

*class* csc.update.NodeAttribute[??](#csc.update.NodeAttribute "Permalink to this definition")
:   NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute.

    Variables:
    :   **disconnect** ??? overridden method with parameter attribute: NodeAttribute

    \_\_annotations\_\_ *= {}*[??](#csc.update.NodeAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.NodeAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.NodeAttribute.__module__ "Permalink to this definition")

    connect(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*, *attribute: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.NodeAttribute.connect "Permalink to this definition")
    :   attribute: NodeAttribute

    connected\_attributes(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.NodeAttribute.connected_attributes "Permalink to this definition")
    :   -> NodeAttribute[]

    connected\_leaves(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*, *get\_only\_first: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.NodeAttribute.connected_leaves "Permalink to this definition")
    :   -> NodeAttribute[]

    connected\_leaves\_in\_undirected\_graph(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")][??](#csc.update.NodeAttribute.connected_leaves_in_undirected_graph "Permalink to this definition")

    direction(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [csc.Direction](#csc.Direction "csc.Direction")[??](#csc.update.NodeAttribute.direction "Permalink to this definition")
    :   -> csc.DirectionValue

    disconnect(*\*args*, *\*\*kwargs*)[??](#csc.update.NodeAttribute.disconnect "Permalink to this definition")
    :   Overloaded function.

        1. disconnect(self: csc.update.NodeAttribute) -> None
        2. disconnect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) -> None

    id(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [csc.update.RegularFunctionAttributeId](#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")[??](#csc.update.NodeAttribute.id "Permalink to this definition")
    :   -> AttributeId

    is\_active(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.NodeAttribute.is_active "Permalink to this definition")

    name(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.update.NodeAttribute.name "Permalink to this definition")

    node(*self: [csc.update.NodeAttribute](#csc.update.NodeAttribute "csc.update.NodeAttribute")*)  domain::update\_editor::Node[??](#csc.update.NodeAttribute.node "Permalink to this definition")
    :   -> Node

*class* csc.update.Object[??](#csc.update.Object "Permalink to this definition")
:   Object class represents an object node. Functionality is limited - it???s better to use update group node instead.

    \_\_annotations\_\_ *= {}*[??](#csc.update.Object.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Object.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Object.__module__ "Permalink to this definition")

    add\_input(*self: [csc.update.Object](#csc.update.Object "csc.update.Object")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Object.add_input "Permalink to this definition")
    :   -> InterfaceAttribute

    add\_output(*self: [csc.update.Object](#csc.update.Object "csc.update.Object")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.InterfaceAttribute](#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")[??](#csc.update.Object.add_output "Permalink to this definition")
    :   -> InterfaceAttribute

    object\_id(*self: [csc.update.Object](#csc.update.Object "csc.update.Object")*)  [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.update.Object.object_id "Permalink to this definition")

    root\_group(*self: [csc.update.Object](#csc.update.Object "csc.update.Object")*)  domain::update\_editor::UpdateGroup[??](#csc.update.Object.root_group "Permalink to this definition")
    :   -> UpdateGroup

*class* csc.update.ObjectGroup[??](#csc.update.ObjectGroup "Permalink to this definition")
:   ObjectGroup class represents object group node

    \_\_annotations\_\_ *= {}*[??](#csc.update.ObjectGroup.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ObjectGroup.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ObjectGroup.__module__ "Permalink to this definition")

    create\_object(*\*args*, *\*\*kwargs*)[??](#csc.update.ObjectGroup.create_object "Permalink to this definition")
    :   Overloaded function.

        1. create\_object(self: csc.update.ObjectGroup, name: str) -> csc.update.Object
        2. create\_object(self: csc.update.ObjectGroup, name: str, id: csc.model.ObjectId) -> csc.update.Object

    create\_sub\_object\_group(*self: [csc.update.ObjectGroup](#csc.update.ObjectGroup "csc.update.ObjectGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.ObjectGroup](#csc.update.ObjectGroup "csc.update.ObjectGroup")[??](#csc.update.ObjectGroup.create_sub_object_group "Permalink to this definition")
    :   -> ObjectGroup

    object\_groups(*self: [csc.update.ObjectGroup](#csc.update.ObjectGroup "csc.update.ObjectGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.ObjectGroup](#csc.update.ObjectGroup "csc.update.ObjectGroup")][??](#csc.update.ObjectGroup.object_groups "Permalink to this definition")
    :   -> ObjectGroup{}

    objects(*self: [csc.update.ObjectGroup](#csc.update.ObjectGroup "csc.update.ObjectGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.Object](#csc.update.Object "csc.update.Object")][??](#csc.update.ObjectGroup.objects "Permalink to this definition")
    :   -> Object{}

*class* csc.update.RegularData[??](#csc.update.RegularData "Permalink to this definition")
:   RegularData class represents a node of a data.

    Variables:
    :   * **value** ??? overridden method by frame, get data value (requires frame if Animation data)
        * **set\_value** ??? overridden method by frame, set data value (requires frame if Animation data)

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularData.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularData.__module__ "Permalink to this definition")

    actuality(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [csc.update.ActualityAttribute](#csc.update.ActualityAttribute "csc.update.ActualityAttribute")[??](#csc.update.RegularData.actuality "Permalink to this definition")
    :   output attribute, that provides actuality status

    attribute(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *d: [csc.Direction](#csc.Direction "csc.Direction")*)  [csc.update.RegularDataAttribute](#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute")[??](#csc.update.RegularData.attribute "Permalink to this definition")
    :   get attribute by direction

    data\_id(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [csc.model.DataId](#csc.model.DataId "csc.model.DataId")[??](#csc.update.RegularData.data_id "Permalink to this definition")

    get\_apply\_euler\_filter(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularData.get_apply_euler_filter "Permalink to this definition")
    :   get apply euler filter

    get\_explicit\_linear(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularData.get_explicit_linear "Permalink to this definition")
    :   get explicit linear

    get\_lerp\_mode(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [csc.model.LerpMode](#csc.model.LerpMode "csc.model.LerpMode")[??](#csc.update.RegularData.get_lerp_mode "Permalink to this definition")
    :   get lerp mode

    input(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [csc.update.RegularDataAttribute](#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute")[??](#csc.update.RegularData.input "Permalink to this definition")
    :   input attribute

    is\_actual(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularData.is_actual "Permalink to this definition")
    :   check if this data is set to actual (see Additional functionality in csc.update.UpdateEditor)

    mode(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [csc.model.DataMode](#csc.model.DataMode "csc.model.DataMode")[??](#csc.update.RegularData.mode "Permalink to this definition")
    :   Check if data is Animation or Static

    output(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [csc.update.RegularDataAttribute](#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute")[??](#csc.update.RegularData.output "Permalink to this definition")
    :   output attribute

    remove\_period(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.remove_period "Permalink to this definition")
    :   in interpolation, remove period

    set\_actual(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *act: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_actual "Permalink to this definition")
    :   set this data as actual (see Additional functionality in csc.update.UpdateEditor)

    set\_apply\_euler\_filter(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *apply\_euler\_filter: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_apply_euler_filter "Permalink to this definition")
    :   set apply euler filter

    set\_description\_value(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_description_value "Permalink to this definition")
    :   setDescriptionValue

    set\_explicit\_linear(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *explicit\_linear: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_explicit_linear "Permalink to this definition")
    :   set explicit linear

    set\_lerp\_mode(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *mode: [csc.model.LerpMode](#csc.model.LerpMode "csc.model.LerpMode")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_lerp_mode "Permalink to this definition")
    :   can be slerp for Vector3 datas. Used in interpolation

    set\_period(*self: [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")*, *period: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularData.set_period "Permalink to this definition")
    :   in interpolation, if perion is provided, the data will be ???fixed??? to provide smoothness

    set\_value(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularData.set_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
        2. set\_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], frame: int) -> None

    value(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularData.value "Permalink to this definition")
    :   Overloaded function.

        1. value(self: csc.update.RegularData) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
        2. value(self: csc.update.RegularData, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

*class* csc.update.RegularDataAttribute[??](#csc.update.RegularDataAttribute "Permalink to this definition")
:   RegularDataAttribute represents an attribute of a regular data.
    It can be connected with data functions.

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularDataAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularDataAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularDataAttribute.__module__ "Permalink to this definition")

*class* csc.update.RegularDataAttributeId[??](#csc.update.RegularDataAttributeId "Permalink to this definition")
:   RegularDataAttributeId is defined by the data id.
    Data only has one input and one output attributes.

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularDataAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularDataAttributeId.__init__ "Permalink to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: csc.update.RegularDataAttributeId, arg0: str) -> None
        2. \_\_init\_\_(self: csc.update.RegularDataAttributeId, arg0: csc.model.DataId) -> None
        3. \_\_init\_\_(self: csc.update.RegularDataAttributeId) -> None

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularDataAttributeId.__module__ "Permalink to this definition")

*class* csc.update.RegularFunction[??](#csc.update.RegularFunction "Permalink to this definition")
:   RegularFunction class represents a node that calculates same operation, done with datas.

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularFunction.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularFunction.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularFunction.__module__ "Permalink to this definition")

    activity(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*)  [csc.update.ActivityAttribute](#csc.update.ActivityAttribute "csc.update.ActivityAttribute")[??](#csc.update.RegularFunction.activity "Permalink to this definition")
    :   activity attributes

    arguments(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.RegularFunctionAttribute](#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")][??](#csc.update.RegularFunction.arguments "Permalink to this definition")
    :   its input arguments

    decrease\_vector(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *direction: [csc.Direction](#csc.Direction "csc.Direction")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.decrease_vector "Permalink to this definition")
    :   method that decreases vector attribute

    func\_id(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*)  [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")[??](#csc.update.RegularFunction.func_id "Permalink to this definition")
    :   its id

    increase\_vector(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *direction: [csc.Direction](#csc.Direction "csc.Direction")*)  [csc.update.RegularFunctionAttribute](#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")[??](#csc.update.RegularFunction.increase_vector "Permalink to this definition")
    :   method that increases vector attribute

    is\_convertible(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.RegularFunction.is_convertible "Permalink to this definition")
    :   check whether this function will make it to the resulting data graph

    remove\_attribute(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*, *attribute: [csc.update.RegularFunctionAttribute](#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.remove_attribute "Permalink to this definition")
    :   method that removes one in vector attribute

    resize\_vector\_inputs(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.resize_vector_inputs "Permalink to this definition")
    :   method that resizes input vector attribute

    resize\_vector\_outputs(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.resize_vector_outputs "Permalink to this definition")
    :   method that resizes output vector attribute

    results(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.RegularFunctionAttribute](#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")][??](#csc.update.RegularFunction.results "Permalink to this definition")
    :   its output arguments

    set\_convertible(*self: [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")*, *convertible: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunction.set_convertible "Permalink to this definition")
    :   set the state of the function, whether it will be used or not

*class* csc.update.RegularFunctionAttribute[??](#csc.update.RegularFunctionAttribute "Permalink to this definition")
:   RegularFunctionAttribute represents an attribute of a data function.
    It can be connected with data attributes.

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularFunctionAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.RegularFunctionAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularFunctionAttribute.__module__ "Permalink to this definition")

*class* csc.update.RegularFunctionAttributeId[??](#csc.update.RegularFunctionAttributeId "Permalink to this definition")
:   RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute

    Variables:
    :   * **function\_id** ??? Get SettingFunctionId
        * **attribute\_id** ??? Get name of the attribute

    \_\_annotations\_\_ *= {}*[??](#csc.update.RegularFunctionAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.RegularFunctionAttributeId](#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId")*, *function\_id: [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId")*, *attribute\_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.RegularFunctionAttributeId.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.RegularFunctionAttributeId.__module__ "Permalink to this definition")

    *property* attribute\_id[??](#csc.update.RegularFunctionAttributeId.attribute_id "Permalink to this definition")

    *property* function\_id[??](#csc.update.RegularFunctionAttributeId.function_id "Permalink to this definition")

*class* csc.update.SettingData[??](#csc.update.SettingData "Permalink to this definition")
:   SettingData class represents a node that calculates same operation, done with settings.
    It can comprise bool or std::int8\_t (Min: -128, Max: 127) value, please be carefull when you set this.

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingData.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingData.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingData.__module__ "Permalink to this definition")

    data\_id(*self: [csc.update.SettingData](#csc.update.SettingData "csc.update.SettingData")*)  [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")[??](#csc.update.SettingData.data_id "Permalink to this definition")
    :   get setting unique id

    output(*self: [csc.update.SettingData](#csc.update.SettingData "csc.update.SettingData")*)  [csc.update.SettingDataAttribute](#csc.update.SettingDataAttribute "csc.update.SettingDataAttribute")[??](#csc.update.SettingData.output "Permalink to this definition")
    :   output attribute

    set\_value(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingData.set_value "Permalink to this definition")
    :   Overloaded function.

        1. set\_value(self: csc.update.SettingData, value: Union[bool, int]) -> None

           > set setting value
        2. set\_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) -> None

           > set setting value

    value(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingData.value "Permalink to this definition")
    :   Overloaded function.

        1. value(self: csc.update.SettingData) -> Union[bool, int]

           > get setting value
        2. value(self: csc.update.SettingData, frame: int) -> Union[bool, int]

           > get setting value

*class* csc.update.SettingDataAttribute[??](#csc.update.SettingDataAttribute "Permalink to this definition")
:   SettingDataAttribute represents an attribute of a setting.
    It can be connected with setting functions.

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingDataAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingDataAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingDataAttribute.__module__ "Permalink to this definition")

*class* csc.update.SettingFunction[??](#csc.update.SettingFunction "Permalink to this definition")
:   SettingFunction class

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingFunction.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingFunction.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingFunction.__module__ "Permalink to this definition")

    arguments(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.SettingFunctionAttribute](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")][??](#csc.update.SettingFunction.arguments "Permalink to this definition")
    :   input attributes

    decrease\_input\_vector(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.decrease_input_vector "Permalink to this definition")
    :   method that decreases input vector attribute

    func\_id(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*)  [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")[??](#csc.update.SettingFunction.func_id "Permalink to this definition")
    :   its id

    increase\_input\_vector(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.update.SettingFunctionAttribute](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")[??](#csc.update.SettingFunction.increase_input_vector "Permalink to this definition")
    :   method that increases input vector attribute

    is\_convertible(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.SettingFunction.is_convertible "Permalink to this definition")
    :   check whether this function will make it to the resulting setting graph

    remove\_attribute(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*, *attribute: [csc.update.SettingFunctionAttribute](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.remove_attribute "Permalink to this definition")
    :   method that removes one in input vector attribute

    resize\_vector\_inputs(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.resize_vector_inputs "Permalink to this definition")
    :   method that resizes input vector attribute

    results(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.update.SettingFunctionAttribute](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")][??](#csc.update.SettingFunction.results "Permalink to this definition")
    :   output attributes

    set\_convertible(*self: [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")*, *convertible: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunction.set_convertible "Permalink to this definition")
    :   set the state of the function, whether it will be used or not

*class* csc.update.SettingFunctionAttribute[??](#csc.update.SettingFunctionAttribute "Permalink to this definition")
:   SettingFunctionAttribute represents an attribute of a setting function.
    It can be connected with setting functions or data function activeness attributes.

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingFunctionAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.SettingFunctionAttribute.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingFunctionAttribute.__module__ "Permalink to this definition")

    is\_out\_true(*self: [csc.update.SettingFunctionAttribute](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.update.SettingFunctionAttribute.is_out_true "Permalink to this definition")

    output\_id(*self: [csc.update.SettingFunctionAttribute](#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")*)  [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")[??](#csc.update.SettingFunctionAttribute.output_id "Permalink to this definition")

*class* csc.update.SettingFunctionAttributeId[??](#csc.update.SettingFunctionAttributeId "Permalink to this definition")
:   SettingFunctionAttributeId is defined by the SettingFunctionId and the index of the attribute

    Implements the SettingFunctionAttributeId.

    Variables:
    :   * **function\_id** ??? Get SettingFunctionId
        * **attribute\_index** ??? Get index of the attribute
        * **attribute\_sub\_index** ??? Get index of the attribute in array

    \_\_annotations\_\_ *= {}*[??](#csc.update.SettingFunctionAttributeId.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.SettingFunctionAttributeId](#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId")*, *function\_id: [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId")*, *attribute\_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *attribute\_sub\_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = 0*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.SettingFunctionAttributeId.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.SettingFunctionAttributeId.__module__ "Permalink to this definition")

    *property* attribute\_index[??](#csc.update.SettingFunctionAttributeId.attribute_index "Permalink to this definition")

    *property* attribute\_sub\_index[??](#csc.update.SettingFunctionAttributeId.attribute_sub_index "Permalink to this definition")

    *property* function\_id[??](#csc.update.SettingFunctionAttributeId.function_id "Permalink to this definition")

*class* csc.update.Update[??](#csc.update.Update "Permalink to this definition")
:   Update class represents the whole update editor

    \_\_annotations\_\_ *= {}*[??](#csc.update.Update.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.Update.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Update.__module__ "Permalink to this definition")

    delete\_node(*self: [csc.update.Update](#csc.update.Update "csc.update.Update")*, *id: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId") | [csc.update.InterfaceId](#csc.update.InterfaceId "csc.update.InterfaceId") | [csc.update.External
**Properties:**
- `Id](#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") | [csc.update.ConstantDatasId](#csc.update.ConstantDatasId "csc.update.ConstantDatasId") | [csc.update.ConstantSettingsId](#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") | [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.model.DataId](#csc.model.DataId "csc.model.DataId") | [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId") | [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Update.delete_node "Permalink to this definition")`

    get\_node\_by\_id(*self: [csc.update.Update](#csc.update.Update "csc.update.Update")*, *id: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId") | [csc.update.InterfaceId](#csc.update.InterfaceId "csc.update.InterfaceId") | [csc.update.External
**Properties:**
- `Id](#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") | [csc.update.ConstantDatasId](#csc.update.ConstantDatasId "csc.update.ConstantDatasId") | [csc.update.ConstantSettingsId](#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") | [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId") | [csc.model.HyperedgeId](#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.model.DataId](#csc.model.DataId "csc.model.DataId") | [csc.model.SettingFunctionId](#csc.model.SettingFunctionId "csc.model.SettingFunctionId") | [csc.model.SettingId](#csc.model.SettingId "csc.model.SettingId")*)  [csc.update.Node](#csc.update.Node "csc.update.Node")[??](#csc.update.Update.get_node_by_id "Permalink to this definition")`

    get\_object\_by\_id(*self: [csc.update.Update](#csc.update.Update "csc.update.Update")*, *arg0: [csc.model.ObjectId](#csc.model.ObjectId "csc.model.ObjectId")*)  [csc.update.Object](#csc.update.Object "csc.update.Object")[??](#csc.update.Update.get_object_by_id "Permalink to this definition")

    root(*self: [csc.update.Update](#csc.update.Update "csc.update.Update")*)  [csc.update.ObjectGroup](#csc.update.ObjectGroup "csc.update.ObjectGroup")[??](#csc.update.Update.root "Permalink to this definition")
    :   -> ObjectGroup

    ungroup(*self: [csc.update.Update](#csc.update.Update "csc.update.Update")*, *group: [csc.update.Group](#csc.update.Group "csc.update.Group")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Update.ungroup "Permalink to this definition")

*class* csc.update.UpdateGroup[??](#csc.update.UpdateGroup "Permalink to this definition")
:   UpdateGroup class represents update group node

    \_\_annotations\_\_ *= {}*[??](#csc.update.UpdateGroup.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.UpdateGroup.__init__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.UpdateGroup.__module__ "Permalink to this definition")

    create\_regular\_data(*self: csc.update.UpdateGroup, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], mode: csc.model.DataMode = <DataMode.Static: 0>*)  [csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")[??](#csc.update.UpdateGroup.create_regular_data "Permalink to this definition")

    create\_regular\_function(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *function: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")[??](#csc.update.UpdateGroup.create_regular_function "Permalink to this definition")

    create\_setting\_data(*self: csc.update.UpdateGroup, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>*)  [csc.update.SettingData](#csc.update.SettingData "csc.update.SettingData")[??](#csc.update.UpdateGroup.create_setting_data "Permalink to this definition")

    create\_setting\_function(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *function\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")[??](#csc.update.UpdateGroup.create_setting_function "Permalink to this definition")

    create\_sub\_update\_group(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")[??](#csc.update.UpdateGroup.create_sub_update_group "Permalink to this definition")

    create\_sub\_update\_group2(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *group\_id: [csc.update.GroupId](#csc.update.GroupId "csc.update.GroupId")*)  [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")[??](#csc.update.UpdateGroup.create_sub_update_group2 "Permalink to this definition")
    :   -> UpdateGroup

    external\_properties(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [csc.update.External
**Properties:**
- `](#csc.update.ExternalProperties "csc.update.ExternalProperties")[??](#csc.update.UpdateGroup.external_properties "Permalink to this definition")
    :   -> ExternalProperties`

    groups(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")][??](#csc.update.UpdateGroup.groups "Permalink to this definition")
    :   -> UpdateGroup{}

    regular\_datas(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.RegularData](#csc.update.RegularData "csc.update.RegularData")][??](#csc.update.UpdateGroup.regular_datas "Permalink to this definition")
    :   -> RegularData{}

    regular\_functions(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.RegularFunction](#csc.update.RegularFunction "csc.update.RegularFunction")][??](#csc.update.UpdateGroup.regular_functions "Permalink to this definition")
    :   -> RegularFunction{}

    setting\_functions(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.SettingFunction](#csc.update.SettingFunction "csc.update.SettingFunction")][??](#csc.update.UpdateGroup.setting_functions "Permalink to this definition")
    :   -> SettingFunction{}

    settings\_datas(*self: [csc.update.UpdateGroup](#csc.update.UpdateGroup "csc.update.UpdateGroup")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.SettingData](#csc.update.SettingData "csc.update.SettingData")][??](#csc.update.UpdateGroup.settings_datas "Permalink to this definition")
    :   -> SettingsData{}