---
title: 
source: https://cascadeur.com/python-api/csc.html
scraped: 2025-08-28 23:43:15
---
# CSC [¶](https://cascadeur.com/python-api/csc.html\#module-csc "Permalink to this heading")

## csc The main Cascadeur python module. [¶](https://cascadeur.com/python-api/csc.html\#csc-the-main-cascadeur-python-module "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.Guid`](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") |  |
| [`csc.math.Quaternion`](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") | Quaternion class |
| [`csc.math.Rotation`](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") | Rotation class |
| [`csc.math.transform_point`](https://cascadeur.com/python-api/csc.html#csc.math.transform_point "csc.math.transform_point")(\*args, \*\*kwargs) | Overloaded function. |
| [`csc.math.inverse_transform_point`](https://cascadeur.com/python-api/csc.html#csc.math.inverse_transform_point "csc.math.inverse_transform_point")(transform, ...) | -\> Vector3f |
| [`csc.math.basic_transform_from_triangle`](https://cascadeur.com/python-api/csc.html#csc.math.basic_transform_from_triangle "csc.math.basic_transform_from_triangle")(triangle) | -\> csc.math.OrthogonalTransform |
| [`csc.math.project_point_on_basic_line`](https://cascadeur.com/python-api/csc.html#csc.math.project_point_on_basic_line "csc.math.project_point_on_basic_line")(...) | -\> Vector3f |
| [`csc.math.euler_angles_to_quaternion_x_y_z`](https://cascadeur.com/python-api/csc.html#csc.math.euler_angles_to_quaternion_x_y_z "csc.math.euler_angles_to_quaternion_x_y_z")(...) | -\> Quaternionf |
| [`csc.math.modify_position_by_matrix`](https://cascadeur.com/python-api/csc.html#csc.math.modify_position_by_matrix "csc.math.modify_position_by_matrix")(matrix, ...) | -\> Vector3f |
| [`csc.math.transforms_difference`](https://cascadeur.com/python-api/csc.html#csc.math.transforms_difference "csc.math.transforms_difference")(...) | -\> csc.math.OrthogonalTransform |
| [`csc.math.transform_point`](https://cascadeur.com/python-api/csc.html#csc.math.transform_point "csc.math.transform_point")(\*args, \*\*kwargs) | Overloaded function. |
| [`csc.math.get_m3f_diag`](https://cascadeur.com/python-api/csc.html#csc.math.get_m3f_diag "csc.math.get_m3f_diag")(matrix) | -\> Vector3f |
| [`csc.physics.PosMass`](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass "csc.physics.PosMass") | PosMass class |
| [`csc.physics.inertia_tensor`](https://cascadeur.com/python-api/csc.html#csc.physics.inertia_tensor "csc.physics.inertia_tensor")(mass\_and\_poses, ...) | -\> Matrix3f |
| [`csc.DirectionValue`](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue") | DirectionValue enumeration |
| [`csc.Direction`](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction") | Direction class Implements direction. |
| [`csc.Version`](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version") | Version class |
| [`csc.SystemVariables`](https://cascadeur.com/python-api/csc.html#csc.SystemVariables "csc.SystemVariables") |  |
| [`csc.math.ScaledTransform`](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "csc.math.ScaledTransform") | ScaledTransform class |
| [`csc.math.OrthogonalTransform`](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform "csc.math.OrthogonalTransform") | OrthogonalTransform class |
| [`csc.math.Triangle`](https://cascadeur.com/python-api/csc.html#csc.math.Triangle "csc.math.Triangle") | Triangle class |
| [`csc.math.SizesInterval`](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") | SizesInterval class |
| [`csc.parts.Type`](https://cascadeur.com/python-api/csc.html#csc.parts.Type "csc.parts.Type") | Type of the parts, enum |
| [`csc.parts.Info`](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") | Info class |
| [`csc.parts.GroupInfo`](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo") | GroupInfo class |
| [`csc.parts.Buffer`](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer") | Buffer class |

_class_ csc.Direction [¶](https://cascadeur.com/python-api/csc.html#csc.Direction "Permalink to this definition")

Direction class
Implements direction.

Parameters:

**value** ( [_csc.DirectionValue_](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue")) –

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.Direction.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:csc.Direction_, _value:csc.DirectionValue=<DirectionValue.Unknown:2>_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Direction.__init__ "Permalink to this definition")\_\_module\_\_ _='csc'_ [¶](https://cascadeur.com/python-api/csc.html#csc.Direction.__module__ "Permalink to this definition")inverse( _self:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[csc.DirectionValue](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue") [¶](https://cascadeur.com/python-api/csc.html#csc.Direction.inverse "Permalink to this definition")to\_string( _self:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Direction.to_string "Permalink to this definition")value( _self:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[csc.DirectionValue](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue") [¶](https://cascadeur.com/python-api/csc.html#csc.Direction.value "Permalink to this definition")_class_ csc.DirectionValue [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "Permalink to this definition")

> DirectionValue enumeration
> In, Out, Unknown

Members:

> In
>
> Out
>
> Unknown

In _=<DirectionValue.In:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.In "Permalink to this definition")Out _=<DirectionValue.Out:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.Out "Permalink to this definition")Unknown _=<DirectionValue.Unknown:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.Unknown "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.DirectionValue](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.DirectionValue](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.DirectionValue](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__int__ "Permalink to this definition")\_\_members\_\_ _={'In':<DirectionValue.In:0>,'Out':<DirectionValue.Out:1>,'Unknown':<DirectionValue.Unknown:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__members__ "Permalink to this definition")\_\_module\_\_ _='csc'_ [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.DirectionValue](https://cascadeur.com/python-api/csc.html#csc.DirectionValue "csc.DirectionValue")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.DirectionValue.value "Permalink to this definition")_class_ csc.Guid [¶](https://cascadeur.com/python-api/csc.html#csc.Guid "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.Guid, arg0: str) -> None

2. \_\_init\_\_(self: csc.Guid) -> None


\_\_module\_\_ _='csc'_ [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.__str__ "Permalink to this definition")is\_null( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.is_null "Permalink to this definition")_static_ null()→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.null "Permalink to this definition")to\_string( _self:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Guid.to_string "Permalink to this definition")_class_ csc.SystemVariables [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.__init__ "Permalink to this definition")\_\_module\_\_ _='csc'_ [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.__module__ "Permalink to this definition")_static_ git\_count()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.git_count "Permalink to this definition")_static_ git\_date()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.git_date "Permalink to this definition")_static_ git\_sha()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.git_sha "Permalink to this definition")_static_ git\_version()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.SystemVariables.git_version "Permalink to this definition")_class_ csc.Version [¶](https://cascadeur.com/python-api/csc.html#csc.Version "Permalink to this definition")

Version class

Implements Version.

Variables:

- **major** – Get set int

- **minor** – Get set int

- **patch** – Get set int


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_, _arg0:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_, _arg0:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__eq__ "Permalink to this definition")\_\_hash\_\_ _=None_ [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__hash__ "Permalink to this definition")\_\_init\_\_( _self:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_, _major:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _minor:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _patch:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__init__ "Permalink to this definition")\_\_lt\_\_( _self:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_, _arg0:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__lt__ "Permalink to this definition")\_\_module\_\_ _='csc'_ [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_, _arg0:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.__ne__ "Permalink to this definition")_static_ from\_string( _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.from_string "Permalink to this definition")_property_ major [¶](https://cascadeur.com/python-api/csc.html#csc.Version.major "Permalink to this definition")_property_ minor [¶](https://cascadeur.com/python-api/csc.html#csc.Version.minor "Permalink to this definition")_property_ patch [¶](https://cascadeur.com/python-api/csc.html#csc.Version.patch "Permalink to this definition")to\_string( _self:[csc.Version](https://cascadeur.com/python-api/csc.html#csc.Version "csc.Version")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.Version.to_string "Permalink to this definition")csc.get\_meaningful\_list()→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.get_meaningful_list "Permalink to this definition")

## csc.tools The Cascadeur python module provides tools. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.tools "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.tools.ActivateDeactivate`](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate "csc.tools.ActivateDeactivate") | ActivateDeactivate class |
| [`csc.tools.selection.Mode`](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "csc.tools.selection.Mode") | Mode enumeration |
| [`csc.tools.selection.Group`](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group "csc.tools.selection.Group") | Group class |
| [`csc.tools.selection.Core`](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "csc.tools.selection.Core") | Core class |
| [`csc.tools.SelectionGroups`](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups "csc.tools.SelectionGroups") | SelectionGroups class |
| [`csc.tools.mirror.Core`](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core "csc.tools.mirror.Core") | Mirror tool core class |
| [`csc.tools.MirrorTool`](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool "csc.tools.MirrorTool") | Mirror tool class |
| [`csc.tools.JointData`](https://cascadeur.com/python-api/csc.html#csc.tools.JointData "csc.tools.JointData") |  |
| [`csc.tools.ObjectKey`](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey") |  |
| [`csc.tools.DataKey`](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey") |  |
| [`csc.tools.RiggingModeTool`](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool") | Rigging mode tool class |
| [`csc.tools.attractor.SpaceMode`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode") | attractor::Mode enum |
| [`csc.tools.attractor.ArgsMode`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode") | attractor::Mode enum |
| [`csc.tools.attractor.GSRotationAxis`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.GSAxisFlag`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.GSAxisIndex`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.GSPhysicsType`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType") | GeneralSettings::RotationAxis enum |
| [`csc.tools.attractor.AttractorGeneralSettings`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings "csc.tools.attractor.AttractorGeneralSettings") |  |
| [`csc.tools.attractor.Args`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args "csc.tools.attractor.Args") |  |
| [`csc.tools.attractor.attract`](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.attract "csc.tools.attractor.attract")(args) |  |
| [`csc.tools.AttractorTool`](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool "csc.tools.AttractorTool") | Attractor tool class |
| [`csc.tools.AutoPhysicTool`](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool "csc.tools.AutoPhysicTool") | Auto physics tool class |
| [`csc.tools.AnimationPointsTypes`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes") | Class of basic types of points which physics tools and change through animation for target center of mass it contains |
| [`csc.tools.CollisionInfoForPoint`](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint "csc.tools.CollisionInfoForPoint") | Structure with which the point collides. |
| [`csc.tools.BallisticTrajectory`](https://cascadeur.com/python-api/csc.html#csc.tools.BallisticTrajectory "csc.tools.BallisticTrajectory") | BallisticTrajectory class |
| [`csc.tools.Trajectory`](https://cascadeur.com/python-api/csc.html#csc.tools.Trajectory "csc.tools.Trajectory") | Trajectory class |
| [`csc.tools.AutoPosingTool`](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool "csc.tools.AutoPosingTool") | AutoPosingTool class |
| [`csc.tools.AnimationUnbakingTool`](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool "csc.tools.AnimationUnbakingTool") | AnimationUnbakingTool class |
| [`csc.tools.RenderParameters`](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters "csc.tools.RenderParameters") | Parameters for rendering |
| [`csc.tools.RenderToFile`](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile "csc.tools.RenderToFile") | Render to file tool class |

_class_ csc.tools.ActivateDeactivate [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate "Permalink to this definition")

ActivateDeactivate class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate.__module__ "Permalink to this definition")activate( _self:[csc.tools.ActivateDeactivate](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate "csc.tools.ActivateDeactivate")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId"), [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate.activate "Permalink to this definition")deactivate( _self:[csc.tools.ActivateDeactivate](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate "csc.tools.ActivateDeactivate")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ActivateDeactivate.deactivate "Permalink to this definition")_class_ csc.tools.AnimationPointsTypes [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "Permalink to this definition")

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

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg2:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg3:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.__module__ "Permalink to this definition")get\_collision\_fixed\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_collision_fixed_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_collision\_pin\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_collision_pin_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_collision\_surface\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_collision_surface_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_fixed\_floor\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fixed_floor_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_fixed\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fixed_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_frame\_collision\_info\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→dict\[int,dict\[csc.model.ObjectId,domain::scene::collision::CollisionInfoForPoint\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_frame_collision_info_points "Permalink to this definition")

Dict\[frame number, Dict\[csc.model.ObjectId, CollisionInfoForPoint\]\]

get\_fulcrum\_floor\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fulcrum_floor_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_fulcrum\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_fulcrum_points "Permalink to this definition")

Dict\[frame number, set of points\]

get\_local\_fixed\_points( _self:[csc.tools.AnimationPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes "csc.tools.AnimationPointsTypes")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationPointsTypes.get_local_fixed_points "Permalink to this definition")

Dict\[frame number, set of points\]

_class_ csc.tools.AnimationUnbakingTool [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool "Permalink to this definition")

AnimationUnbakingTool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool.__module__ "Permalink to this definition")get\_interpolation\_difference( _self:[csc.tools.AnimationUnbakingTool](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool "csc.tools.AnimationUnbakingTool")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AnimationUnbakingTool.get_interpolation_difference "Permalink to this definition")_class_ csc.tools.AttractorTool [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool "Permalink to this definition")

Attractor tool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool.__module__ "Permalink to this definition")get\_general\_settings( _self:[csc.tools.AttractorTool](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool "csc.tools.AttractorTool")_)→[csc.tools.attractor.AttractorGeneralSettings](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings "csc.tools.attractor.AttractorGeneralSettings") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool.get_general_settings "Permalink to this definition")is\_only\_key\_frames( _self:[csc.tools.AttractorTool](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool "csc.tools.AttractorTool")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AttractorTool.is_only_key_frames "Permalink to this definition")_class_ csc.tools.AutoPhysicTool [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool "Permalink to this definition")

Auto physics tool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool.__module__ "Permalink to this definition")turn\_off( _self:[csc.tools.AutoPhysicTool](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool "csc.tools.AutoPhysicTool")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool.turn_off "Permalink to this definition")turn\_off\_all\_fulcrum\_points( _self:[csc.tools.AutoPhysicTool](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool "csc.tools.AutoPhysicTool")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPhysicTool.turn_off_all_fulcrum_points "Permalink to this definition")_class_ csc.tools.AutoPosingTool [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool "Permalink to this definition")

AutoPosingTool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool.__module__ "Permalink to this definition")add( _self:[csc.tools.AutoPosingTool](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool "csc.tools.AutoPosingTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool.add "Permalink to this definition")update( _self:[csc.tools.AutoPosingTool](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool "csc.tools.AutoPosingTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.AutoPosingTool.update "Permalink to this definition")_class_ csc.tools.BallisticTrajectory [¶](https://cascadeur.com/python-api/csc.html#csc.tools.BallisticTrajectory "Permalink to this definition")

BallisticTrajectory class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.BallisticTrajectory.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.BallisticTrajectory.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.BallisticTrajectory.__module__ "Permalink to this definition")_class_ csc.tools.CollisionInfoForPoint [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint "Permalink to this definition")

Structure with which the point collides.
When used, it is assumed that the normal goes from other to point.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.__module__ "Permalink to this definition")_property_ normal [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.normal "Permalink to this definition")

Vector3d

_property_ other [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.other "Permalink to this definition")

csc.model.ObjectId

_property_ penetration\_depth [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.penetration_depth "Permalink to this definition")

double

_property_ pos [¶](https://cascadeur.com/python-api/csc.html#csc.tools.CollisionInfoForPoint.pos "Permalink to this definition")

Vector3d

_class_ csc.tools.DataKey [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey")_, _arg0:[csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.__hash__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey")_, _arg0:[csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.__ne__ "Permalink to this definition")_property_ data\_name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.data_name "Permalink to this definition")_property_ object\_key [¶](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey.object_key "Permalink to this definition")_class_ csc.tools.JointData [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.JointData](https://cascadeur.com/python-api/csc.html#csc.tools.JointData "csc.tools.JointData")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.__module__ "Permalink to this definition")_property_ local\_position [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.local_position "Permalink to this definition")_property_ local\_rotation [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.local_rotation "Permalink to this definition")_property_ local\_scale [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.local_scale "Permalink to this definition")_property_ visibility [¶](https://cascadeur.com/python-api/csc.html#csc.tools.JointData.visibility "Permalink to this definition")_class_ csc.tools.MirrorTool [¶](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool "Permalink to this definition")

Mirror tool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool.__module__ "Permalink to this definition")core( _self:[csc.tools.MirrorTool](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool "csc.tools.MirrorTool")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.MirrorTool.core "Permalink to this definition")_class_ csc.tools.ObjectKey [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.tools.ObjectKey](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey")_, _arg0:[csc.tools.ObjectKey](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.tools.ObjectKey](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.__hash__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.ObjectKey](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.tools.ObjectKey](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey")_, _arg0:[csc.tools.ObjectKey](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey "csc.tools.ObjectKey")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.__ne__ "Permalink to this definition")_property_ behaviour\_name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.behaviour_name "Permalink to this definition")_property_ path\_name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.ObjectKey.path_name "Permalink to this definition")_class_ csc.tools.RenderParameters [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters "Permalink to this definition")

Parameters for rendering

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.RenderParameters](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters "csc.tools.RenderParameters")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters.__module__ "Permalink to this definition")_property_ height [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters.height "Permalink to this definition")_property_ samples [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters.samples "Permalink to this definition")_property_ width [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters.width "Permalink to this definition")_class_ csc.tools.RenderToFile [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile "Permalink to this definition")

Render to file tool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile.__module__ "Permalink to this definition")play\_to\_images\_sequence( _self:[csc.tools.RenderToFile](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile "csc.tools.RenderToFile")_, _scene\_view:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _render\_parameters:[csc.tools.RenderParameters](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters "csc.tools.RenderParameters")_, _folder\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile.play_to_images_sequence "Permalink to this definition")play\_to\_video\_file( _self:[csc.tools.RenderToFile](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile "csc.tools.RenderToFile")_, _scene\_view:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _render\_parameters:[csc.tools.RenderParameters](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters "csc.tools.RenderParameters")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile.play_to_video_file "Permalink to this definition")take\_image( _self:[csc.tools.RenderToFile](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile "csc.tools.RenderToFile")_, _scene\_view:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _render\_parameters:[csc.tools.RenderParameters](https://cascadeur.com/python-api/csc.html#csc.tools.RenderParameters "csc.tools.RenderParameters")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RenderToFile.take_image "Permalink to this definition")_class_ csc.tools.RiggingModeTool [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "Permalink to this definition")

Rigging mode tool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.__module__ "Permalink to this definition")erase\_joints\_data( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.erase_joints_data "Permalink to this definition")erase\_layer\_id\_by\_object\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.erase_layer_id_by_object_ids "Permalink to this definition")erase\_layers\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.erase_layers_ids "Permalink to this definition")erase\_preserved\_data( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.erase_preserved_data "Permalink to this definition")erase\_preserved\_object\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.erase_preserved_object_ids "Permalink to this definition")erase\_preserved\_setting( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.erase_preserved_setting "Permalink to this definition")get\_joints\_data( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.tools.JointData](https://cascadeur.com/python-api/csc.html#csc.tools.JointData "csc.tools.JointData")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.get_joints_data "Permalink to this definition")get\_layer\_id\_by\_object\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.get_layer_id_by_object_ids "Permalink to this definition")get\_layers\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.get_layers_ids "Permalink to this definition")get\_preserved\_data( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") \|numpy.ndarray\[numpy.float32\[3,1\]\]\|numpy.ndarray\[numpy.float32\[4,1\]\]\| [csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") \|numpy.ndarray\[numpy.float32\[3,3\]\]\|numpy.ndarray\[numpy.float32\[4,4\]\]\| [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \|numpy.ndarray\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\[3,1\]\]\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.get_preserved_data "Permalink to this definition")get\_preserved\_object\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.get_preserved_object_ids "Permalink to this definition")get\_preserved\_setting( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.get_preserved_setting "Permalink to this definition")set\_joints\_data( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.tools.JointData](https://cascadeur.com/python-api/csc.html#csc.tools.JointData "csc.tools.JointData")\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.set_joints_data "Permalink to this definition")set\_layers\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.set_layers_ids "Permalink to this definition")set\_preserved\_data( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") \|numpy.ndarray\[numpy.float32\[3,1\]\]\|numpy.ndarray\[numpy.float32\[4,1\]\]\| [csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") \|numpy.ndarray\[numpy.float32\[3,3\]\]\|numpy.ndarray\[numpy.float32\[4,4\]\]\| [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \|numpy.ndarray\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\[3,1\]\]\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.set_preserved_data "Permalink to this definition")set\_preserved\_object\_ids( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.set_preserved_object_ids "Permalink to this definition")set\_preserved\_setting( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.tools.DataKey](https://cascadeur.com/python-api/csc.html#csc.tools.DataKey "csc.tools.DataKey"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.set_preserved_setting "Permalink to this definition")set\_undo\_redo\_context( _self:[csc.tools.RiggingModeTool](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool "csc.tools.RiggingModeTool")_, _arg0:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _arg1:Callable_, _arg2:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _arg3:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingModeTool.set_undo_redo_context "Permalink to this definition")_class_ csc.tools.RiggingWindow [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "Permalink to this definition")

SelectionGroups class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.__module__ "Permalink to this definition")create\_from\_qrt\_by\_content( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.create_from_qrt_by_content "Permalink to this definition")create\_from\_qrt\_by\_fileName( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.create_from_qrt_by_fileName "Permalink to this definition")generate\_rig\_elements( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.generate_rig_elements "Permalink to this definition")get\_character\_mirror\_plane( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.get_character_mirror_plane "Permalink to this definition")get\_is\_create\_autoposing( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.get_is_create_autoposing "Permalink to this definition")get\_template\_from\_qrt( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.get_template_from_qrt "Permalink to this definition")is\_create\_qrt( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.is_create_qrt "Permalink to this definition")load\_template\_by\_content( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.load_template_by_content "Permalink to this definition")load\_template\_by\_fileName( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.load_template_by_fileName "Permalink to this definition")open\_quick\_rigging\_tool( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.open_quick_rigging_tool "Permalink to this definition")set\_axis\_after\_qrt( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _axis:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.set_axis_after_qrt "Permalink to this definition")set\_character\_mirror\_plane( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _plane:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.set_character_mirror_plane "Permalink to this definition")set\_is\_create\_autoposing( _self:[csc.tools.RiggingWindow](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow "csc.tools.RiggingWindow")_, _on:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.RiggingWindow.set_is_create_autoposing "Permalink to this definition")_class_ csc.tools.SelectionGroups [¶](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups "Permalink to this definition")

SelectionGroups class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups.__module__ "Permalink to this definition")core( _self:[csc.tools.SelectionGroups](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups "csc.tools.SelectionGroups")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups.core "Permalink to this definition")import\_file( _self:[csc.tools.SelectionGroups](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups "csc.tools.SelectionGroups")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.SelectionGroups.import_file "Permalink to this definition")_class_ csc.tools.StaticPointsTypes [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "Permalink to this definition")

Class of basic types of points which physics tools use and dont change through animation
for target center of mass it contains

get\_main\_points – all points that can be associated with center of mass
get\_direction\_controllers – all direction controller associated with center of mass
get\_interpolation\_group – all points that should be interpolated and use instead direction controller in apply

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_, _arg0:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg1:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes.__module__ "Permalink to this definition")get\_direction\_controllers( _self:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes.get_direction_controllers "Permalink to this definition")

set\[ModelId\]

get\_interpolation\_group( _self:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes.get_interpolation_group "Permalink to this definition")

set\[ModelId\]

get\_main\_points( _self:[csc.tools.StaticPointsTypes](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes "csc.tools.StaticPointsTypes")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.StaticPointsTypes.get_main_points "Permalink to this definition")

set\[ModelId\]

_class_ csc.tools.Trajectory [¶](https://cascadeur.com/python-api/csc.html#csc.tools.Trajectory "Permalink to this definition")

Trajectory class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.Trajectory.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.Trajectory.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.Trajectory.__module__ "Permalink to this definition")_class_ csc.tools.selection.Core [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "Permalink to this definition")

Core class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.selection'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.__module__ "Permalink to this definition")get\_group( _self:[csc.tools.selection.Core](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "csc.tools.selection.Core")_, _idx:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.tools.selection.Group](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group "csc.tools.selection.Group") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.get_group "Permalink to this definition")

pbdoc( -> Group )pbdoc

get\_groups( _self:[csc.tools.selection.Core](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "csc.tools.selection.Core")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [csc.tools.selection.Group](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group "csc.tools.selection.Group")\] [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.get_groups "Permalink to this definition")

pbdoc( -> std::map<GroupIndex, Group> )pbdoc

process( _self:[csc.tools.selection.Core](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "csc.tools.selection.Core")_, _index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _mode:[csc.tools.selection.Mode](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "csc.tools.selection.Mode")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.process "Permalink to this definition")set\_group( _self:[csc.tools.selection.Core](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "csc.tools.selection.Core")_, _index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _group:[csc.tools.selection.Group](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group "csc.tools.selection.Group")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.set_group "Permalink to this definition")set\_groups( _self:[csc.tools.selection.Core](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core "csc.tools.selection.Core")_, _groups:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [csc.tools.selection.Group](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group "csc.tools.selection.Group")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Core.set_groups "Permalink to this definition")_class_ csc.tools.selection.Group [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group "Permalink to this definition")

Group class

Variables:

- **objects** – std::set<ModelObjectId>

- **pivot** – ModelObjectId


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.tools.selection.Group) -> None

2. \_\_init\_\_(self: csc.tools.selection.Group, arg0: set\[Union\[csc.model.ObjectId, csc.domain.Tool\_object\_id\]\], arg1: Union\[csc.model.ObjectId, csc.domain.Tool\_object\_id\]) -> None


\_\_module\_\_ _='csc.tools.selection'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group.__module__ "Permalink to this definition")_property_ objects [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group.objects "Permalink to this definition")_property_ pivot [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Group.pivot "Permalink to this definition")_class_ csc.tools.selection.Mode [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "Permalink to this definition")

> Mode enumeration
>
> SetGroup, SingleSelect, MultiSelect

Members:

> SetGroup
>
> SingleSelect
>
> MultiSelect

MultiSelect _=<Mode.MultiSelect:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.MultiSelect "Permalink to this definition")SetGroup _=<Mode.SetGroup:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.SetGroup "Permalink to this definition")SingleSelect _=<Mode.SingleSelect:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.SingleSelect "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.selection.Mode](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "csc.tools.selection.Mode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.selection.Mode](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "csc.tools.selection.Mode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.selection.Mode](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "csc.tools.selection.Mode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__int__ "Permalink to this definition")\_\_members\_\_ _={'MultiSelect':<Mode.MultiSelect:2>,'SetGroup':<Mode.SetGroup:0>,'SingleSelect':<Mode.SingleSelect:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.selection'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.selection.Mode](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode "csc.tools.selection.Mode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.selection.Mode.value "Permalink to this definition")_class_ csc.tools.mirror.Core [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core "Permalink to this definition")

Mirror tool core class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.mirror'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.__module__ "Permalink to this definition")mirror\_frame( _self:[csc.tools.mirror.Core](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core "csc.tools.mirror.Core")_, _arg0:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.mirror_frame "Permalink to this definition")mirror\_interval( _self:[csc.tools.mirror.Core](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core "csc.tools.mirror.Core")_, _arg0:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.mirror_interval "Permalink to this definition")plane( _self:[csc.tools.mirror.Core](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core "csc.tools.mirror.Core")_)→[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.plane "Permalink to this definition")set\_plane( _self:[csc.tools.mirror.Core](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core "csc.tools.mirror.Core")_, _plane:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.mirror.Core.set_plane "Permalink to this definition")_class_ csc.tools.attractor.Args [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:csc.tools.attractor.Args_, _scene:csc.domain.Scene_, _gravity:float_, _general\_settings:csc.tools.attractor.AttractorGeneralSettings_, _only\_key\_frames:bool_, _mode:csc.tools.attractor.ArgsMode_, _for\_interval:bool=False_, _hard:bool=False_, _frame\_action\_on\_change:csc.domain.FrameActionOnChange=<FrameActionOnChange.DoNothing:2>_, _interval\_action\_on\_change:csc.domain.IntervalActionOnChange=<IntervalActionOnChange.Fixing:0>_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.__module__ "Permalink to this definition")_property_ for\_interval [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.for_interval "Permalink to this definition")_property_ frame\_action\_on\_change [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.frame_action_on_change "Permalink to this definition")_property_ general\_settings [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.general_settings "Permalink to this definition")_property_ interval\_action\_on\_change [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.interval_action_on_change "Permalink to this definition")_property_ mode [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.mode "Permalink to this definition")_property_ only\_key\_frames [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args.only_key_frames "Permalink to this definition")_class_ csc.tools.attractor.ArgsMode [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode "Permalink to this definition")

> attractor::Mode enum
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

Average _=<ArgsMode.Average:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.Average "Permalink to this definition")Inertial _=<ArgsMode.Inertial:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.Inertial "Permalink to this definition")Interpolation _=<ArgsMode.Interpolation:5>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.Interpolation "Permalink to this definition")InverseInertial _=<ArgsMode.InverseInertial:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.InverseInertial "Permalink to this definition")Next _=<ArgsMode.Next:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.Next "Permalink to this definition")Previous _=<ArgsMode.Previous:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.Previous "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.attractor.ArgsMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.ArgsMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.attractor.ArgsMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'Average':<ArgsMode.Average:4>,'Inertial':<ArgsMode.Inertial:2>,'Interpolation':<ArgsMode.Interpolation:5>,'InverseInertial':<ArgsMode.InverseInertial:3>,'Next':<ArgsMode.Next:1>,'Previous':<ArgsMode.Previous:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.attractor.ArgsMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode "csc.tools.attractor.ArgsMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.ArgsMode.value "Permalink to this definition")_class_ csc.tools.attractor.AttractorGeneralSettings [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.AttractorGeneralSettings](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings "csc.tools.attractor.AttractorGeneralSettings")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.__module__ "Permalink to this definition")_property_ factor [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.factor "Permalink to this definition")_property_ mode [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.mode "Permalink to this definition")_property_ mode\_relative\_to\_pivot [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.mode_relative_to_pivot "Permalink to this definition")_property_ physic\_type [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.physic_type "Permalink to this definition")_property_ pivot [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.pivot "Permalink to this definition")_property_ position\_axis [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.position_axis "Permalink to this definition")_property_ rotation\_axis [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.rotation_axis "Permalink to this definition")_property_ scale\_axis [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.AttractorGeneralSettings.scale_axis "Permalink to this definition")_class_ csc.tools.attractor.GSAxisFlag [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag "Permalink to this definition")

> GeneralSettings::RotationAxis enum
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

Empty _=<GSAxisFlag.Empty:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.Empty "Permalink to this definition")X _=<GSAxisFlag.X:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.X "Permalink to this definition")XYZ _=<GSAxisFlag.XYZ:7>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.XYZ "Permalink to this definition")Y _=<GSAxisFlag.Y:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.Y "Permalink to this definition")Z _=<GSAxisFlag.Z:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.Z "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.attractor.GSAxisFlag](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.GSAxisFlag](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.attractor.GSAxisFlag](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__int__ "Permalink to this definition")\_\_members\_\_ _={'Empty':<GSAxisFlag.Empty:0>,'X':<GSAxisFlag.X:1>,'XYZ':<GSAxisFlag.XYZ:7>,'Y':<GSAxisFlag.Y:2>,'Z':<GSAxisFlag.Z:4>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.attractor.GSAxisFlag](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag "csc.tools.attractor.GSAxisFlag")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisFlag.value "Permalink to this definition")_class_ csc.tools.attractor.GSAxisIndex [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex "Permalink to this definition")

> GeneralSettings::RotationAxis enum
>
> X, Y, Z

Members:

> X
>
> Y
>
> Z

X _=<GSAxisIndex.X:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.X "Permalink to this definition")Y _=<GSAxisIndex.Y:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.Y "Permalink to this definition")Z _=<GSAxisIndex.Z:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.Z "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.attractor.GSAxisIndex](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.GSAxisIndex](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.attractor.GSAxisIndex](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__int__ "Permalink to this definition")\_\_members\_\_ _={'X':<GSAxisIndex.X:0>,'Y':<GSAxisIndex.Y:1>,'Z':<GSAxisIndex.Z:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.attractor.GSAxisIndex](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex "csc.tools.attractor.GSAxisIndex")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSAxisIndex.value "Permalink to this definition")_class_ csc.tools.attractor.GSPhysicsType [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType "Permalink to this definition")

> GeneralSettings::RotationAxis enum
>
> FrameRelax, InterpolationRelax

Members:

> FrameRelax
>
> InterpolationRelax

FrameRelax _=<GSPhysicsType.FrameRelax:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.FrameRelax "Permalink to this definition")InterpolationRelax _=<GSPhysicsType.InterpolationRelax:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.InterpolationRelax "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.attractor.GSPhysicsType](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.GSPhysicsType](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.attractor.GSPhysicsType](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__int__ "Permalink to this definition")\_\_members\_\_ _={'FrameRelax':<GSPhysicsType.FrameRelax:0>,'InterpolationRelax':<GSPhysicsType.InterpolationRelax:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.attractor.GSPhysicsType](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType "csc.tools.attractor.GSPhysicsType")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSPhysicsType.value "Permalink to this definition")_class_ csc.tools.attractor.GSRotationAxis [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis "Permalink to this definition")

> GeneralSettings::RotationAxis enum
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

Empty _=<GSRotationAxis.Empty:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.Empty "Permalink to this definition")Whole _=<GSRotationAxis.Whole:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.Whole "Permalink to this definition")X _=<GSRotationAxis.X:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.X "Permalink to this definition")Y _=<GSRotationAxis.Y:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.Y "Permalink to this definition")Z _=<GSRotationAxis.Z:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.Z "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.attractor.GSRotationAxis](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.GSRotationAxis](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.attractor.GSRotationAxis](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__int__ "Permalink to this definition")\_\_members\_\_ _={'Empty':<GSRotationAxis.Empty:4>,'Whole':<GSRotationAxis.Whole:3>,'X':<GSRotationAxis.X:0>,'Y':<GSRotationAxis.Y:1>,'Z':<GSRotationAxis.Z:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.attractor.GSRotationAxis](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis "csc.tools.attractor.GSRotationAxis")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.GSRotationAxis.value "Permalink to this definition")_class_ csc.tools.attractor.SpaceMode [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode "Permalink to this definition")

> attractor::Mode enum
>
> Global, Local

Members:

> Global
>
> Local

Global _=<SpaceMode.Global:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.Global "Permalink to this definition")Local _=<SpaceMode.Local:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.Local "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.tools.attractor.SpaceMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.tools.attractor.SpaceMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.tools.attractor.SpaceMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'Global':<SpaceMode.Global:0>,'Local':<SpaceMode.Local:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.tools.attractor'_ [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.tools.attractor.SpaceMode](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode "csc.tools.attractor.SpaceMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.SpaceMode.value "Permalink to this definition")csc.tools.attractor.attract( _args:[csc.tools.attractor.Args](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.Args "csc.tools.attractor.Args")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.tools.attractor.attract "Permalink to this definition")

## csc.view The Cascadeur python module provides basic methods to operate GUI. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.view "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.view.StandardButton`](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton "csc.view.StandardButton") | StandardButton enum |
| [`csc.view.DialogButton`](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton "csc.view.DialogButton") | DialogButton class |
| [`csc.view.DialogManager`](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager "csc.view.DialogManager") | DialogManager class |
| [`csc.view.FileDialogManager`](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager "csc.view.FileDialogManager") | FileDialogManager class |
| [`csc.view.Scene`](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene") | SceneView class |
| [`csc.view.AnimationBoundary`](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary "csc.view.AnimationBoundary") | AnimationBoundary class |
| [`csc.view.CameraType`](https://cascadeur.com/python-api/csc.html#csc.view.CameraType "csc.view.CameraType") | CameraType enumerable |
| [`csc.view.SphericalCameraStruct`](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct") | SphericalCameraStruct class |
| [`csc.view.Camera`](https://cascadeur.com/python-api/csc.html#csc.view.Camera "csc.view.Camera") | Domain Spherical camera class |
| [`csc.view.ViewportDomain`](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain") | Domain Viewport class |
| [`csc.view.Viewport`](https://cascadeur.com/python-api/csc.html#csc.view.Viewport "csc.view.Viewport") | Viewport class |

_class_ csc.view.AnimationBoundary [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary "Permalink to this definition")

AnimationBoundary class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.__module__ "Permalink to this definition")_property_ first\_frame [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.first_frame "Permalink to this definition")

Set first frame of animation

_property_ first\_visible\_frame [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.first_visible_frame "Permalink to this definition")

Set first visible frame of animation

_property_ last\_frame [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.last_frame "Permalink to this definition")

Set last frame of animation

_property_ last\_visible\_frame [¶](https://cascadeur.com/python-api/csc.html#csc.view.AnimationBoundary.last_visible_frame "Permalink to this definition")

Set last visible frame of animation

_class_ csc.view.Camera [¶](https://cascadeur.com/python-api/csc.html#csc.view.Camera "Permalink to this definition")

Domain Spherical camera class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.Camera.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.Camera.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.Camera.__module__ "Permalink to this definition")set\_target( _self:[csc.view.Camera](https://cascadeur.com/python-api/csc.html#csc.view.Camera "csc.view.Camera")_, _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Camera.set_target "Permalink to this definition")zoom\_to\_points( _self:[csc.view.Camera](https://cascadeur.com/python-api/csc.html#csc.view.Camera "csc.view.Camera")_, _arg0:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Camera.zoom_to_points "Permalink to this definition")_class_ csc.view.CameraType [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType "Permalink to this definition")

> CameraType enumerable

Members:

> ISOMETRIC
>
> PERSPECTIVE

ISOMETRIC _=<CameraType.ISOMETRIC:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.ISOMETRIC "Permalink to this definition")PERSPECTIVE _=<CameraType.PERSPECTIVE:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.PERSPECTIVE "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.view.CameraType](https://cascadeur.com/python-api/csc.html#csc.view.CameraType "csc.view.CameraType")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.view.CameraType](https://cascadeur.com/python-api/csc.html#csc.view.CameraType "csc.view.CameraType")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.view.CameraType](https://cascadeur.com/python-api/csc.html#csc.view.CameraType "csc.view.CameraType")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__int__ "Permalink to this definition")\_\_members\_\_ _={'ISOMETRIC':<CameraType.ISOMETRIC:0>,'PERSPECTIVE':<CameraType.PERSPECTIVE:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.view.CameraType](https://cascadeur.com/python-api/csc.html#csc.view.CameraType "csc.view.CameraType")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.view.CameraType.value "Permalink to this definition")_class_ csc.view.DialogButton [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton "Permalink to this definition")

DialogButton class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.view.DialogButton) -> None

2. \_\_init\_\_(self: csc.view.DialogButton, arg0: str) -> None

3. \_\_init\_\_(self: csc.view.DialogButton, text: str, handler: Callable, force\_active\_focus: bool = False, accent: bool = False) -> None

4. \_\_init\_\_(self: csc.view.DialogButton, arg0: csc.view.StandardButton) -> None

5. \_\_init\_\_(self: csc.view.DialogButton, button: csc.view.StandardButton, handler: Callable, force\_active\_focus: bool = False, accent: bool = False) -> None


\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton.__module__ "Permalink to this definition")force\_active\_focus( _self:[csc.view.DialogButton](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton "csc.view.DialogButton")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton.force_active_focus "Permalink to this definition")text( _self:[csc.view.DialogButton](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton "csc.view.DialogButton")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton.text "Permalink to this definition")

-\> string

_class_ csc.view.DialogManager [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager "Permalink to this definition")

DialogManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.__module__ "Permalink to this definition")_static_ instance()→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.instance "Permalink to this definition")show\_buttons\_dialog( _self:[csc.view.DialogManager](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager "csc.view.DialogManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg2:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.view.DialogButton](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton "csc.view.DialogButton")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.show_buttons_dialog "Permalink to this definition")show\_info( _self:[csc.view.DialogManager](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager "csc.view.DialogManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.show_info "Permalink to this definition")show\_input\_dialog( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.show_input_dialog "Permalink to this definition")

Overloaded function.

1. show\_input\_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable) -> None

2. show\_input\_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable, arg4: Callable) -> None


show\_inputs\_dialog( _self:[csc.view.DialogManager](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager "csc.view.DialogManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]_, _arg2:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]_, _arg3:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg4:Callable_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.show_inputs_dialog "Permalink to this definition")show\_styled\_buttons\_dialog( _self:[csc.view.DialogManager](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager "csc.view.DialogManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg2:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.view.DialogButton](https://cascadeur.com/python-api/csc.html#csc.view.DialogButton "csc.view.DialogButton")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.DialogManager.show_styled_buttons_dialog "Permalink to this definition")_class_ csc.view.FileDialogManager [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager "Permalink to this definition")

FileDialogManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager.__module__ "Permalink to this definition")show\_folder\_dialog( _self:[csc.view.FileDialogManager](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager "csc.view.FileDialogManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:Callable_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager.show_folder_dialog "Permalink to this definition")show\_open\_file\_dialog( _self:[csc.view.FileDialogManager](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager "csc.view.FileDialogManager")_, _title:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _filters:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]_, _handler:Callable_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager.show_open_file_dialog "Permalink to this definition")show\_save\_file\_dialog( _self:[csc.view.FileDialogManager](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager "csc.view.FileDialogManager")_, _title:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _filters:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]_, _handler:Callable_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.FileDialogManager.show_save_file_dialog "Permalink to this definition")_class_ csc.view.Scene [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene "Permalink to this definition")

SceneView class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.__module__ "Permalink to this definition")active\_viewport( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.active_viewport "Permalink to this definition")

Returns active csc.view.Viewport

animation\_boundary( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.animation_boundary "Permalink to this definition")

-\> csc.view.AnimationBoundary

domain\_scene( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.domain_scene "Permalink to this definition")

Return current csc.domain.Scene

get\_setting\_handler( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.get_setting_handler "Permalink to this definition")gravity\_per\_frame( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.gravity_per_frame "Permalink to this definition")name( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.name "Permalink to this definition")save( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _path\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.save "Permalink to this definition")viewports( _self:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.view.Scene.viewports "Permalink to this definition")

Provides all of csc.view.Viewport objects

_class_ csc.view.SphericalCameraStruct [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct "Permalink to this definition")

SphericalCameraStruct class

Variables:

- **target** – Get set Vector3f

- **position** – Get set Vector3f

- **type** – Get set CameraType


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.view.SphericalCameraStruct](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct.__module__ "Permalink to this definition")_property_ position [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct.position "Permalink to this definition")_property_ target [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct.target "Permalink to this definition")_property_ type [¶](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct.type "Permalink to this definition")_class_ csc.view.StandardButton [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton "Permalink to this definition")

> StandardButton enum
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

Cancel _=<StandardButton.Cancel:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.Cancel "Permalink to this definition")No _=<StandardButton.No:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.No "Permalink to this definition")Ok _=<StandardButton.Ok:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.Ok "Permalink to this definition")Yes _=<StandardButton.Yes:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.Yes "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.view.StandardButton](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton "csc.view.StandardButton")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.view.StandardButton](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton "csc.view.StandardButton")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.view.StandardButton](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton "csc.view.StandardButton")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__int__ "Permalink to this definition")\_\_members\_\_ _={'Cancel':<StandardButton.Cancel:1>,'No':<StandardButton.No:3>,'Ok':<StandardButton.Ok:0>,'Yes':<StandardButton.Yes:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.view.StandardButton](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton "csc.view.StandardButton")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.view.StandardButton.value "Permalink to this definition")_class_ csc.view.Viewport [¶](https://cascadeur.com/python-api/csc.html#csc.view.Viewport "Permalink to this definition")

Viewport class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.Viewport.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.Viewport.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.Viewport.__module__ "Permalink to this definition")domain\_viewport( _self:[csc.view.Viewport](https://cascadeur.com/python-api/csc.html#csc.view.Viewport "csc.view.Viewport")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.Viewport.domain_viewport "Permalink to this definition")_class_ csc.view.ViewportDomain [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "Permalink to this definition")

Domain Viewport class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.__module__ "Permalink to this definition")camera( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.camera "Permalink to this definition")camera\_struct( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_)→[csc.view.SphericalCameraStruct](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.camera_struct "Permalink to this definition")id( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.id "Permalink to this definition")is\_main( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.is_main "Permalink to this definition")mode\_visualizers( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_)→[csc.view.ViewportMode](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "csc.view.ViewportMode") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.mode_visualizers "Permalink to this definition")set\_camera\_struct( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_, _camera\_struct:[csc.view.SphericalCameraStruct](https://cascadeur.com/python-api/csc.html#csc.view.SphericalCameraStruct "csc.view.SphericalCameraStruct")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.set_camera_struct "Permalink to this definition")set\_mode\_visualizers( _self:[csc.view.ViewportDomain](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain "csc.view.ViewportDomain")_, _mode:[csc.view.ViewportMode](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "csc.view.ViewportMode")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportDomain.set_mode_visualizers "Permalink to this definition")_class_ csc.view.ViewportMode [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "Permalink to this definition")

> ViewportMode enumerable

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

AutoPosing _=<ViewportMode.AutoPosing:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.AutoPosing "Permalink to this definition")Controller _=<ViewportMode.Controller:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.Controller "Permalink to this definition")Joint _=<ViewportMode.Joint:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.Joint "Permalink to this definition")Mesh _=<ViewportMode.Mesh:5>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.Mesh "Permalink to this definition")ModeCount _=<ViewportMode.ModeCount:7>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.ModeCount "Permalink to this definition")PointController _=<ViewportMode.PointController:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.PointController "Permalink to this definition")Rigging _=<ViewportMode.Rigging:6>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.Rigging "Permalink to this definition")View _=<ViewportMode.View:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.View "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.view.ViewportMode](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "csc.view.ViewportMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.view.ViewportMode](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "csc.view.ViewportMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.view.ViewportMode](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "csc.view.ViewportMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'AutoPosing':<ViewportMode.AutoPosing:1>,'Controller':<ViewportMode.Controller:3>,'Joint':<ViewportMode.Joint:4>,'Mesh':<ViewportMode.Mesh:5>,'ModeCount':<ViewportMode.ModeCount:7>,'PointController':<ViewportMode.PointController:2>,'Rigging':<ViewportMode.Rigging:6>,'View':<ViewportMode.View:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.view'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.view.ViewportMode](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode "csc.view.ViewportMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.view.ViewportMode.value "Permalink to this definition")

## csc.view.camera\_utils The Cascadeur python module provides utulity methods to manage viewport cameras. [¶](https://cascadeur.com/python-api/csc.html\#csc-view-camera-utils-the-cascadeur-python-module-provides-utulity-methods-to-manage-viewport-cameras "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.view.camera_utils.CameraData`](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData") | CameraData class |

_class_ csc.view.camera\_utils.CameraData [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "Permalink to this definition")

CameraData class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.view.camera\_utils'_ [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData.__module__ "Permalink to this definition")id( _self:[csc.view.camera\_utils.CameraData](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")_)→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData.id "Permalink to this definition")isCustom( _self:[csc.view.camera\_utils.CameraData](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData.isCustom "Permalink to this definition")name( _self:[csc.view.camera\_utils.CameraData](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData.name "Permalink to this definition")csc.view.camera\_utils.get\_cameras( _scene:cascadeur::Scene_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.view.camera\_utils.CameraData](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")\] [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.get_cameras "Permalink to this definition")csc.view.camera\_utils.is\_camera\_active( _viewport:[csc.view.Viewport](https://cascadeur.com/python-api/csc.html#csc.view.Viewport "csc.view.Viewport")_, _camera:[csc.view.camera\_utils.CameraData](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.is_camera_active "Permalink to this definition")csc.view.camera\_utils.reset\_camera( _scene:[csc.view.Viewport](https://cascadeur.com/python-api/csc.html#csc.view.Viewport "csc.view.Viewport")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.reset_camera "Permalink to this definition")csc.view.camera\_utils.set\_camera\_active( _viewport:[csc.view.Viewport](https://cascadeur.com/python-api/csc.html#csc.view.Viewport "csc.view.Viewport")_, _camera:[csc.view.camera\_utils.CameraData](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.CameraData "csc.view.camera_utils.CameraData")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.view.camera_utils.set_camera_active "Permalink to this definition")

## csc.app The Cascadeur python module provides basic methods to operate GUI. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.app "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.app.Analytics`](https://cascadeur.com/python-api/csc.html#csc.app.Analytics "csc.app.Analytics") | Analytics class |
| [`csc.app.ActionManager`](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager "csc.app.ActionManager") | ActionManager class |
| [`csc.app.DataSourceManager`](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager") | DataSourceManager class |
| [`csc.app.SettingsManager`](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager "csc.app.SettingsManager") | SettingsManager class |
| [`csc.app.SceneManager`](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "csc.app.SceneManager") | SceneManager class |
| [`csc.app.SceneTool`](https://cascadeur.com/python-api/csc.html#csc.app.SceneTool "csc.app.SceneTool") | SceneTool class |
| [`csc.app.CascadeurTool`](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool "csc.app.CascadeurTool") | CascadeurTool class |
| [`csc.app.ToolsManager`](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager "csc.app.ToolsManager") | ToolsManager class |
| [`csc.app.Application`](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application") | Application class |
| [`csc.app.ProjectLoader`](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader "csc.app.ProjectLoader") | ProjectLoader class |
| [`csc.app.StatusManager`](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager "csc.app.StatusManager") | StatusManager class |
| [`csc.app.SimpleStatusInformer`](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer") | SimpleStatusInformer class |

_class_ csc.app.ActionManager [¶](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager "Permalink to this definition")

ActionManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager.__module__ "Permalink to this definition")call\_action( _self:[csc.app.ActionManager](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager "csc.app.ActionManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.ActionManager.call_action "Permalink to this definition")_class_ csc.app.Analytics [¶](https://cascadeur.com/python-api/csc.html#csc.app.Analytics "Permalink to this definition")

Analytics class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.Analytics.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.Analytics.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.Analytics.__module__ "Permalink to this definition")_static_ send\_action( _type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _key:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")=''_, _label:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")=''_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Analytics.send_action "Permalink to this definition")_class_ csc.app.Application [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application "Permalink to this definition")

Application class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.__module__ "Permalink to this definition")current\_scene( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.current_scene "Permalink to this definition")get\_action\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_action_manager "Permalink to this definition")get\_data\_source\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_data_source_manager "Permalink to this definition")get\_file\_dialog\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_file_dialog_manager "Permalink to this definition")get\_scene\_clipboard( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_scene_clipboard "Permalink to this definition")get\_scene\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_scene_manager "Permalink to this definition")get\_setting\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_setting_manager "Permalink to this definition")get\_status\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_status_manager "Permalink to this definition")get\_tools\_manager( _self:[csc.app.Application](https://cascadeur.com/python-api/csc.html#csc.app.Application "csc.app.Application")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.Application.get_tools_manager "Permalink to this definition")_class_ csc.app.CascadeurTool [¶](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool "Permalink to this definition")

CascadeurTool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool.__module__ "Permalink to this definition")editor( _self:[csc.app.CascadeurTool](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool "csc.app.CascadeurTool")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[csc.app.SceneTool](https://cascadeur.com/python-api/csc.html#csc.app.SceneTool "csc.app.SceneTool") [¶](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool.editor "Permalink to this definition")name( _self:[csc.app.CascadeurTool](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool "csc.app.CascadeurTool")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.CascadeurTool.name "Permalink to this definition")_class_ csc.app.DataSourceManager [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "Permalink to this definition")

DataSourceManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.__module__ "Permalink to this definition")close\_scene( _self:[csc.app.DataSourceManager](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.close_scene "Permalink to this definition")load\_scene( _self:[csc.app.DataSourceManager](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.load_scene "Permalink to this definition")

Load scene and all additional datas (selection groups etc)
Example:
ds\_m = csc.app.get\_application().get\_data\_source\_manager()
ds\_m.load\_scene(file\_path)

save\_current\_scene( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.save_current_scene "Permalink to this definition")

Overloaded function.

1. save\_current\_scene(self: csc.app.DataSourceManager, handler: Callable\[\[bool\], None\]) -> None

2. save\_current\_scene(self: csc.app.DataSourceManager) -> None


save\_scene( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.save_scene "Permalink to this definition")

Overloaded function.

1. save\_scene(self: csc.app.DataSourceManager, scene\_view: csc.view.Scene, handler: Callable\[\[bool\], None\]) -> None

2. save\_scene(self: csc.app.DataSourceManager, scene\_view: csc.view.Scene) -> None


save\_scene\_as( _self:[csc.app.DataSourceManager](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager "csc.app.DataSourceManager")_, _scene\_view:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _full\_file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.DataSourceManager.save_scene_as "Permalink to this definition")_class_ csc.app.ProjectLoader [¶](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader "Permalink to this definition")

ProjectLoader class

Provides methods to load domain scene.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader.__module__ "Permalink to this definition")_static_ load\_from( _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.ProjectLoader.load_from "Permalink to this definition")

Minimal Load. This method doesn’t load selection groups, control picker and etc.
Better use data\_source\_manager’s load\_scene method.
Example:
csc.app.ProjectLoader.load\_from(file\_path, scene)

_class_ csc.app.SceneManager [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "Permalink to this definition")

SceneManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.__module__ "Permalink to this definition")create\_application\_scene( _self:[csc.app.SceneManager](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "csc.app.SceneManager")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.create_application_scene "Permalink to this definition")current\_scene( _self:[csc.app.SceneManager](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "csc.app.SceneManager")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.current_scene "Permalink to this definition")remove\_application\_scene( _self:[csc.app.SceneManager](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "csc.app.SceneManager")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.remove_application_scene "Permalink to this definition")scenes( _self:[csc.app.SceneManager](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "csc.app.SceneManager")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.scenes "Permalink to this definition")set\_current\_scene( _self:[csc.app.SceneManager](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager "csc.app.SceneManager")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneManager.set_current_scene "Permalink to this definition")_class_ csc.app.SceneTool [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneTool "Permalink to this definition")

SceneTool class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneTool.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneTool.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SceneTool.__module__ "Permalink to this definition")_class_ csc.app.SettingsHandler [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler "Permalink to this definition")

SettingsHandler class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.__module__ "Permalink to this definition")get\_bool\_value( _self:[csc.app.SettingsHandler](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler "csc.app.SettingsHandler")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.get_bool_value "Permalink to this definition")get\_float\_value( _self:[csc.app.SettingsHandler](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler "csc.app.SettingsHandler")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.get_float_value "Permalink to this definition")get\_int\_value( _self:[csc.app.SettingsHandler](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler "csc.app.SettingsHandler")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.get_int_value "Permalink to this definition")get\_string\_value( _self:[csc.app.SettingsHandler](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler "csc.app.SettingsHandler")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsHandler.get_string_value "Permalink to this definition")_class_ csc.app.SettingsManager [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager "Permalink to this definition")

SettingsManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager.__module__ "Permalink to this definition")get\_bool\_value( _self:[csc.app.SettingsManager](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager "csc.app.SettingsManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager.get_bool_value "Permalink to this definition")get\_color\_value( _self:[csc.app.SettingsManager](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager "csc.app.SettingsManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager.get_color_value "Permalink to this definition")get\_float\_value( _self:[csc.app.SettingsManager](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager "csc.app.SettingsManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SettingsManager.get_float_value "Permalink to this definition")_class_ csc.app.SimpleStatusInformer [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "Permalink to this definition")

SimpleStatusInformer class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.app.SimpleStatusInformer](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.__module__ "Permalink to this definition")is\_canceled( _self:[csc.app.SimpleStatusInformer](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.is_canceled "Permalink to this definition")set\_blocking( _self:[csc.app.SimpleStatusInformer](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")_, _arg0:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.set_blocking "Permalink to this definition")set\_cancelable( _self:[csc.app.SimpleStatusInformer](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")_, _arg0:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.set_cancelable "Permalink to this definition")set\_text( _self:[csc.app.SimpleStatusInformer](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer "csc.app.SimpleStatusInformer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.SimpleStatusInformer.set_text "Permalink to this definition")_class_ csc.app.StatusInformer [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusInformer "Permalink to this definition")

StatusInformer class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusInformer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusInformer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusInformer.__module__ "Permalink to this definition")_class_ csc.app.StatusManager [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager "Permalink to this definition")

StatusManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager.__module__ "Permalink to this definition")remove\_status( _self:csc.app.StatusManager_, _arg0:cascadeur::StatusInformer_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager.remove_status "Permalink to this definition")set\_status( _self:csc.app.StatusManager_, _arg0:cascadeur::StatusInformer_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.StatusManager.set_status "Permalink to this definition")_class_ csc.app.ToolsManager [¶](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager "Permalink to this definition")

ToolsManager class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.app'_ [¶](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager.__module__ "Permalink to this definition")get\_tool( _self:[csc.app.ToolsManager](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager "csc.app.ToolsManager")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager.get_tool "Permalink to this definition")tools( _self:[csc.app.ToolsManager](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager "csc.app.ToolsManager")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.app.ToolsManager.tools "Permalink to this definition")csc.app.get\_application()→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.app.get_application "Permalink to this definition")

## csc.parts The Cascadeur python module provides basic methods to operate scene parts. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.parts "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.parts.Type`](https://cascadeur.com/python-api/csc.html#csc.parts.Type "csc.parts.Type") | Type of the parts, enum |
| [`csc.parts.Info`](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") | Info class |
| [`csc.parts.GroupInfo`](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo") | GroupInfo class |
| [`csc.parts.SceneClipboard`](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard "csc.parts.SceneClipboard") | SceneClipboard class |
| [`csc.parts.Buffer`](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer") | Buffer class |

_class_ csc.parts.Buffer [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "Permalink to this definition")

Buffer class

Provides methods to operate parts of the scene.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.parts'_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.__module__ "Permalink to this definition")_static_ get( _source\_dir:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")=''_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.get "Permalink to this definition")get\_parts\_info\_by\_id( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.parts.Info](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info")\] [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.get_parts_info_by_id "Permalink to this definition")get\_src\_dir( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.get_src_dir "Permalink to this definition")insert\_elementary\_by\_id( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_elementary_by_id "Permalink to this definition")insert\_elementary\_by\_path( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_elementary_by_path "Permalink to this definition")insert\_object\_by\_id( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _arg3:[csc.domain.assets.AssetsManager](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")_)→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_object_by_id "Permalink to this definition")insert\_object\_by\_path( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _arg3:[csc.domain.assets.AssetsManager](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")_)→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_object_by_path "Permalink to this definition")insert\_objects\_by\_id( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _arg3:[csc.domain.assets.AssetsManager](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\], [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_objects_by_id "Permalink to this definition")insert\_objects\_by\_path( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _arg3:[csc.domain.assets.AssetsManager](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\], [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_objects_by_path "Permalink to this definition")insert\_selected\_objects\_by\_path( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _arg3:[csc.domain.assets.AssetsManager](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_selected_objects_by_path "Permalink to this definition")insert\_update\_group\_by\_id( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId"), [csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_update_group_by_id "Permalink to this definition")insert\_update\_group\_by\_path( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg2:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId"), [csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.insert_update_group_by_path "Permalink to this definition")refresh( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.refresh "Permalink to this definition")reset\_cache( _self:[csc.parts.Buffer](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer "csc.parts.Buffer")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.reset_cache "Permalink to this definition")take\_elementary\_to\_parts( _self:csc.parts.Buffer_, _part\_name:str_, _from:csc.domain.Scene_, _object\_id:csc.model.ObjectId_, _parent\_group:csc.update.GroupId_, _elementary:csc.parts.GroupInfo_, _path\_to\_scene\_parts:str_)→[csc.parts.Info](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.take_elementary_to_parts "Permalink to this definition")take\_object\_to\_parts( _self:csc.parts.Buffer_, _part\_name:str_, _from:csc.domain.Scene_, _object\_id:csc.model.ObjectId_, _path\_to\_scene\_parts:str_)→[csc.parts.Info](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.take_object_to_parts "Permalink to this definition")take\_objects\_to\_parts( _self:csc.parts.Buffer,part\_name:str,from:csc.domain.Scene,objects:list\[csc.model.ObjectId\],objects\_grs:list\[csc.update.GroupId\],path\_to\_scene\_parts:str_)→[csc.parts.Info](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.take_objects_to_parts "Permalink to this definition")take\_selected\_objects\_to\_parts( _self:csc.parts.Buffer,part\_name:str,from:csc.domain.Scene,selected\_objects:list\[csc.model.ObjectId\],path\_to\_scene\_parts:str_)→[csc.parts.Info](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.take_selected_objects_to_parts "Permalink to this definition")take\_update\_group\_to\_parts( _self:csc.parts.Buffer,part\_name:str,from:csc.domain.Scene,object\_id:csc.model.ObjectId,parent\_group:csc.update.GroupId,elementary:csc.parts.GroupInfo,sub\_groups:list\[csc.update.GroupId\],path\_to\_scene\_parts:str_)→[csc.parts.Info](https://cascadeur.com/python-api/csc.html#csc.parts.Info "csc.parts.Info") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Buffer.take_update_group_to_parts "Permalink to this definition")_class_ csc.parts.GroupInfo [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "Permalink to this definition")

GroupInfo class

Variables:

- **type** – Get set Data::Id{}

- **name** – Get set Setting::Id{}

- **path** – Get set HyperedgeId{}

- **object\_id** – Get set SettingFunctionId{}


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.parts.GroupInfo](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.parts'_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.__module__ "Permalink to this definition")_property_ datas [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.datas "Permalink to this definition")_property_ regular\_funcs [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.regular_funcs "Permalink to this definition")_property_ settings [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.settings "Permalink to this definition")_property_ settings\_funcs [¶](https://cascadeur.com/python-api/csc.html#csc.parts.GroupInfo.settings_funcs "Permalink to this definition")_class_ csc.parts.Info [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info "Permalink to this definition")

Info class

Variables:

- **type** – Get csc.parts.Type

- **name** – Get string

- **path** – Get string

- **object\_id** – Get csc.model.ObjectId


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.parts'_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.__module__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.name "Permalink to this definition")_property_ object\_id [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.object_id "Permalink to this definition")_property_ path [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.path "Permalink to this definition")_property_ type [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Info.type "Permalink to this definition")_class_ csc.parts.SceneClipboard [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard "Permalink to this definition")

SceneClipboard class

Provides methods to operate parts of the scene.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.parts'_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.__module__ "Permalink to this definition")copy( _self:[csc.parts.SceneClipboard](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard "csc.parts.SceneClipboard")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.copy "Permalink to this definition")copy\_image\_to\_clipboard( _self:[csc.parts.SceneClipboard](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard "csc.parts.SceneClipboard")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.copy_image_to_clipboard "Permalink to this definition")paste( _self:[csc.parts.SceneClipboard](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard "csc.parts.SceneClipboard")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.paste "Permalink to this definition")paste\_with\_session( _self:[csc.parts.SceneClipboard](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard "csc.parts.SceneClipboard")_, _arg0:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _arg1:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.SceneClipboard.paste_with_session "Permalink to this definition")_class_ csc.parts.Type [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type "Permalink to this definition")

> Type of the parts, enum
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

Elementary _=<Type.Elementary:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.Elementary "Permalink to this definition")Object _=<Type.Object:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.Object "Permalink to this definition")ObjectGroup _=<Type.ObjectGroup:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.ObjectGroup "Permalink to this definition")SelectedObjects _=<Type.SelectedObjects:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.SelectedObjects "Permalink to this definition")UpdateGroup _=<Type.UpdateGroup:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.UpdateGroup "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.parts.Type](https://cascadeur.com/python-api/csc.html#csc.parts.Type "csc.parts.Type")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.parts.Type](https://cascadeur.com/python-api/csc.html#csc.parts.Type "csc.parts.Type")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.parts.Type](https://cascadeur.com/python-api/csc.html#csc.parts.Type "csc.parts.Type")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__int__ "Permalink to this definition")\_\_members\_\_ _={'Elementary':<Type.Elementary:0>,'Object':<Type.Object:2>,'ObjectGroup':<Type.ObjectGroup:3>,'SelectedObjects':<Type.SelectedObjects:4>,'UpdateGroup':<Type.UpdateGroup:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.parts'_ [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.parts.Type](https://cascadeur.com/python-api/csc.html#csc.parts.Type "csc.parts.Type")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.parts.Type.value "Permalink to this definition")

## csc.external The Cascadeur python module provides basic api to external data formats. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.external.fbx "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.external.fbx.ExtraDatas`](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas "csc.external.fbx.ExtraDatas") | ExtraDatas class |
| [`csc.external.fbx.FbxDatas`](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas "csc.external.fbx.FbxDatas") | FbxDatas class |

_class_ csc.external.fbx.ExtraDatas [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas "Permalink to this definition")

ExtraDatas class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.external.fbx.ExtraDatas](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas "csc.external.fbx.ExtraDatas")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.external.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.__module__ "Permalink to this definition")_property_ look [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.look "Permalink to this definition")_property_ node\_index [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.node_index "Permalink to this definition")_property_ post\_rotation [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.post_rotation "Permalink to this definition")_property_ pre\_rotation [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.pre_rotation "Permalink to this definition")_property_ size [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.ExtraDatas.size "Permalink to this definition")_class_ csc.external.fbx.FbxDatas [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas "Permalink to this definition")

FbxDatas class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.external.fbx.FbxDatas](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas "csc.external.fbx.FbxDatas")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.external.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.__module__ "Permalink to this definition")_property_ ignore\_namespace [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.ignore_namespace "Permalink to this definition")_property_ order [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.order "Permalink to this definition")_property_ rotation [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.rotation "Permalink to this definition")_property_ scale [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.scale "Permalink to this definition")_property_ translation [¶](https://cascadeur.com/python-api/csc.html#csc.external.fbx.FbxDatas.translation "Permalink to this definition")

## csc.fbx The Cascadeur python module provides basic methods to operate fbx. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.fbx "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.fbx.FbxSettingsMode`](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode") | FbxSettingsMode enumeration |
| [`csc.fbx.FbxSettingsAxis`](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis") | FbxSettingsAxis enumeration |
| [`csc.fbx.FbxSettings`](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings "csc.fbx.FbxSettings") | FbxSettings class |
| [`csc.fbx.FbxLoader`](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader") | FbxLoader class |
| [`csc.fbx.FbxSceneLoader`](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader") | FbxSceneLoader class |

_class_ csc.fbx.FbxLoader [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "Permalink to this definition")

FbxLoader class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _fps:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _handler:[csc.domain.IMessageHandler](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler "csc.domain.IMessageHandler")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.__module__ "Permalink to this definition")add\_model( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.add_model "Permalink to this definition")add\_model\_to\_selected( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.add_model_to_selected "Permalink to this definition")export\_all\_objects( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_all_objects "Permalink to this definition")export\_joints( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_joints "Permalink to this definition")export\_joints\_selected( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_joints_selected "Permalink to this definition")export\_joints\_selected\_frames( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_joints_selected_frames "Permalink to this definition")export\_joints\_selected\_objects( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_joints_selected_objects "Permalink to this definition")export\_model( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_model "Permalink to this definition")export\_scene\_selected( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_scene_selected "Permalink to this definition")export\_scene\_selected\_frames( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_scene_selected_frames "Permalink to this definition")export\_scene\_selected\_objects( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.export_scene_selected_objects "Permalink to this definition")import\_animation( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.import_animation "Permalink to this definition")import\_animation\_to\_selected\_frames( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.import_animation_to_selected_frames "Permalink to this definition")import\_animation\_to\_selected\_objects( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.import_animation_to_selected_objects "Permalink to this definition")import\_model( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.import_model "Permalink to this definition")import\_scene( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.import_scene "Permalink to this definition")set\_settings( _self:[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader")_, _settings:[csc.fbx.FbxSettings](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings "csc.fbx.FbxSettings")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader.set_settings "Permalink to this definition")_class_ csc.fbx.FbxSceneLoader [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader "Permalink to this definition")

FbxSceneLoader class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.__module__ "Permalink to this definition")export\_fbx\_scene( _self:[csc.fbx.FbxSceneLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.export_fbx_scene "Permalink to this definition")get\_fbx\_loader( _self:[csc.fbx.FbxSceneLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_)→[csc.fbx.FbxLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxLoader "csc.fbx.FbxLoader") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.get_fbx_loader "Permalink to this definition")import\_fbx\_animation( _self:[csc.fbx.FbxSceneLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.import_fbx_animation "Permalink to this definition")import\_fbx\_scene( _self:[csc.fbx.FbxSceneLoader](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader "csc.fbx.FbxSceneLoader")_, _scene:[csc.view.Scene](https://cascadeur.com/python-api/csc.html#csc.view.Scene "csc.view.Scene")_, _file\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSceneLoader.import_fbx_scene "Permalink to this definition")_class_ csc.fbx.FbxSettings [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings "Permalink to this definition")

FbxSettings class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.fbx.FbxSettings](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings "csc.fbx.FbxSettings")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.__module__ "Permalink to this definition")_property_ apply\_euler\_filter [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.apply_euler_filter "Permalink to this definition")_property_ bake\_animation [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.bake_animation "Permalink to this definition")_property_ mode [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.mode "Permalink to this definition")_property_ up\_axis [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettings.up_axis "Permalink to this definition")_class_ csc.fbx.FbxSettingsAxis [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis "Permalink to this definition")

> FbxSettingsAxis enumeration
>
> Binary, Ascii

Members:

> X
>
> Y
>
> Z

X _=<FbxSettingsAxis.X:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.X "Permalink to this definition")Y _=<FbxSettingsAxis.Y:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.Y "Permalink to this definition")Z _=<FbxSettingsAxis.Z:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.Z "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.fbx.FbxSettingsAxis](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.fbx.FbxSettingsAxis](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.fbx.FbxSettingsAxis](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__int__ "Permalink to this definition")\_\_members\_\_ _={'X':<FbxSettingsAxis.X:0>,'Y':<FbxSettingsAxis.Y:1>,'Z':<FbxSettingsAxis.Z:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.fbx.FbxSettingsAxis](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis "csc.fbx.FbxSettingsAxis")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsAxis.value "Permalink to this definition")_class_ csc.fbx.FbxSettingsMode [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode "Permalink to this definition")

> FbxSettingsMode enumeration
>
> Binary, Ascii

Members:

> Binary
>
> Ascii

Ascii _=<FbxSettingsMode.Ascii:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.Ascii "Permalink to this definition")Binary _=<FbxSettingsMode.Binary:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.Binary "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.fbx.FbxSettingsMode](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.fbx.FbxSettingsMode](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.fbx.FbxSettingsMode](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'Ascii':<FbxSettingsMode.Ascii:1>,'Binary':<FbxSettingsMode.Binary:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.fbx'_ [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.fbx.FbxSettingsMode](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode "csc.fbx.FbxSettingsMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.fbx.FbxSettingsMode.value "Permalink to this definition")

## csc.rig The Cascadeur python module that implements the basic functions for operating a rig. [¶](https://cascadeur.com/python-api/csc.html\#module-csc.rig "Permalink to this heading")

|     |     |
| --- | --- |
| [`csc.rig.AddElementData`](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData "csc.rig.AddElementData") |  |
| [`csc.rig.BoneProperty`](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty "csc.rig.BoneProperty") |  |
| [`csc.rig.TwistProperty`](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty "csc.rig.TwistProperty") |  |
| [`csc.rig.TwistBoneProperty`](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty "csc.rig.TwistBoneProperty") |  |
| [`csc.rig.QrtData`](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData "csc.rig.QrtData") |  |

_class_ csc.rig.AddElementData [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.rig.AddElementData) -> None

2. \_\_init\_\_(self: csc.rig.AddElementData, arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: float, arg8: numpy.ndarray\[numpy.float32\[3, 1\]\]) -> None


\_\_module\_\_ _='csc.rig'_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.__module__ "Permalink to this definition")_property_ axis\_point\_controller [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.axis_point_controller "Permalink to this definition")_property_ box\_multiplier [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.box_multiplier "Permalink to this definition")_property_ is\_multiple [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.is_multiple "Permalink to this definition")_property_ joint\_size\_without\_child [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.joint_size_without_child "Permalink to this definition")_property_ offset\_point\_controller [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.offset_point_controller "Permalink to this definition")_property_ only\_box\_controller [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.only_box_controller "Permalink to this definition")_property_ orthogonal\_with\_parent [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.orthogonal_with_parent "Permalink to this definition")_property_ point\_color [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.point_color "Permalink to this definition")_property_ use\_global\_axis [¶](https://cascadeur.com/python-api/csc.html#csc.rig.AddElementData.use_global_axis "Permalink to this definition")_class_ csc.rig.BoneProperty [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.rig.BoneProperty](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty "csc.rig.BoneProperty")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.rig'_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.__module__ "Permalink to this definition")_property_ bone\_name [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.bone_name "Permalink to this definition")_property_ joint\_path\_name [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.joint_path_name "Permalink to this definition")_property_ object\_id [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.object_id "Permalink to this definition")_property_ required\_field [¶](https://cascadeur.com/python-api/csc.html#csc.rig.BoneProperty.required_field "Permalink to this definition")_class_ csc.rig.QrtData [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.rig.QrtData](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData "csc.rig.QrtData")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.rig'_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.__module__ "Permalink to this definition")_property_ body [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.body "Permalink to this definition")_property_ hinge\_arm\_direction [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.hinge_arm_direction "Permalink to this definition")_property_ hinge\_leg\_direction [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.hinge_leg_direction "Permalink to this definition")_property_ is\_align\_pelvis [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.is_align_pelvis "Permalink to this definition")_property_ is\_create\_layers [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.is_create_layers "Permalink to this definition")_property_ is\_replace\_existing [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.is_replace_existing "Permalink to this definition")_property_ is\_spline\_ik [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.is_spline_ik "Permalink to this definition")_property_ left\_hand [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.left_hand "Permalink to this definition")_property_ right\_hand [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.right_hand "Permalink to this definition")_property_ twists [¶](https://cascadeur.com/python-api/csc.html#csc.rig.QrtData.twists "Permalink to this definition")_class_ csc.rig.TwistBoneProperty [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.rig.TwistBoneProperty](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty "csc.rig.TwistBoneProperty")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.rig'_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty.__module__ "Permalink to this definition")_property_ bone\_name [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty.bone_name "Permalink to this definition")_property_ twist\_properties [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistBoneProperty.twist_properties "Permalink to this definition")_class_ csc.rig.TwistProperty [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.rig.TwistProperty](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty "csc.rig.TwistProperty")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.rig'_ [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.__module__ "Permalink to this definition")_property_ joint\_path\_name [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.joint_path_name "Permalink to this definition")_property_ object\_id [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.object_id "Permalink to this definition")_property_ twist\_axis [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.twist_axis "Permalink to this definition")_property_ twist\_strength [¶](https://cascadeur.com/python-api/csc.html#csc.rig.TwistProperty.twist_strength "Permalink to this definition")

## csc.layers The Cascadeur python module that implements scene layers functionality. [¶](https://cascadeur.com/python-api/csc.html\#csc-layers-the-cascadeur-python-module-that-implements-scene-layers-functionality "Permalink to this heading")

LayerId == FolderId == ItemId == Guid

|     |     |
| --- | --- |
| [`csc.layers.Header`](https://cascadeur.com/python-api/csc.html#csc.layers.Header "csc.layers.Header") | Header class |
| [`csc.layers.ItemVariant`](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant") | ItemVariant class |
| [`csc.layers.Folder`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder") | Folder class |
| [`csc.layers.Layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer") | Layer class |
| [`csc.layers.Viewer`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer") | Viewer class |
| [`csc.layers.Editor`](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor") | Editor class |
| [`csc.layers.Selector`](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector") | Selector class |
| [`csc.layers.LayersContainer`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer") | LayersContainer class |
| [`csc.layers.UserLabelData`](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData "csc.layers.UserLabelData") | UserLabelData class |
| [`csc.layers.Layers`](https://cascadeur.com/python-api/csc.html#csc.layers.Layers "csc.layers.Layers") | Layers class |
| [`csc.layers.Cycle`](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle") | Cycle class |
| [`csc.layers.CyclesViewer`](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer") | Cycle viewer class |
| [`csc.layers.CyclesEditor`](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor") | Cycle editor class |
| [`csc.layers.LayersSelectionChanger`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger") | Layer SelectionChanger class |
| [`csc.layers.layer.Interpolation`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Interpolation.html#csc.layers.layer.Interpolation "csc.layers.layer.Interpolation") | Interpolation enumerable |
| [`csc.layers.layer.Tangents`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Tangents.html#csc.layers.layer.Tangents "csc.layers.layer.Tangents") | Layer Frame Tangents enumerable |
| [`csc.layers.layer.IkFk`](https://cascadeur.com/python-api/_generate/csc.layers.layer.IkFk.html#csc.layers.layer.IkFk "csc.layers.layer.IkFk") | Layer Frame IkFk enumerable |
| [`csc.layers.layer.Fixation`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Fixation.html#csc.layers.layer.Fixation "csc.layers.layer.Fixation") | Layer Frame Fixation enumerable |
| [`csc.layers.layer.Common`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Common.html#csc.layers.layer.Common "csc.layers.layer.Common") | Common class |
| [`csc.layers.layer.Key`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Key.html#csc.layers.layer.Key "csc.layers.layer.Key") | Key class |
| [`csc.layers.layer.Interval`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Interval.html#csc.layers.layer.Interval "csc.layers.layer.Interval") | Interval class |
| [`csc.layers.layer.Section`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Section.html#csc.layers.layer.Section "csc.layers.layer.Section") | Section class |
| [`csc.layers.layer.Cell`](https://cascadeur.com/python-api/_generate/csc.layers.layer.Cell.html#csc.layers.layer.Cell "csc.layers.layer.Cell") | Cell class |
| [`csc.layers.index.FramesInterval`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesInterval.html#csc.layers.index.FramesInterval "csc.layers.index.FramesInterval") | FramesInterval class |
| [`csc.layers.index.FramesIndices`](https://cascadeur.com/python-api/_generate/csc.layers.index.FramesIndices.html#csc.layers.index.FramesIndices "csc.layers.index.FramesIndices") | FramesIndices class |
| [`csc.layers.index.CellIndex`](https://cascadeur.com/python-api/_generate/csc.layers.index.CellIndex.html#csc.layers.index.CellIndex "csc.layers.index.CellIndex") | CellIndex class |
| [`csc.layers.index.RectIndicesContainer`](https://cascadeur.com/python-api/_generate/csc.layers.index.RectIndicesContainer.html#csc.layers.index.RectIndicesContainer "csc.layers.index.RectIndicesContainer") | RectIndicesContainer class |
| [`csc.layers.index.IndicesContainer`](https://cascadeur.com/python-api/_generate/csc.layers.index.IndicesContainer.html#csc.layers.index.IndicesContainer "csc.layers.index.IndicesContainer") | IndicesContainer class |

_class_ csc.layers.Cycle [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "Permalink to this definition")

Cycle class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.__module__ "Permalink to this definition")_property_ first\_active\_frame\_index [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.first_active_frame_index "Permalink to this definition")_property_ following\_interval [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.following_interval "Permalink to this definition")_static_ get\_no\_pos()→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.get_no_pos "Permalink to this definition")is\_the\_same\_frames\_as( _self:[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")_, _other\_cycle:[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.is_the_same_frames_as "Permalink to this definition")

-\> bool

_property_ last\_active\_frame\_index [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.last_active_frame_index "Permalink to this definition")left\_frame\_index( _self:[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.left_frame_index "Permalink to this definition")

-\> Pos

_property_ left\_inactive\_frame\_index [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.left_inactive_frame_index "Permalink to this definition")right\_frame\_index( _self:[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.right_frame_index "Permalink to this definition")

-\> Pos

_property_ right\_inactive\_frame\_index [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle.right_inactive_frame_index "Permalink to this definition")_class_ csc.layers.CyclesEditor [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "Permalink to this definition")

Cycle editor class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.layers.CyclesEditor](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor")_, _layer:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.__module__ "Permalink to this definition")change\_inactive\_parts( _self:[csc.layers.CyclesEditor](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg2:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.change_inactive_parts "Permalink to this definition")create\_cycle( _self:[csc.layers.CyclesEditor](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg2:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.create_cycle "Permalink to this definition")delete\_cycle( _self:[csc.layers.CyclesEditor](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.delete_cycle "Permalink to this definition")find\_cycle( _self:[csc.layers.CyclesEditor](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.find_cycle "Permalink to this definition")normalize( _self:[csc.layers.CyclesEditor](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor "csc.layers.CyclesEditor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesEditor.normalize "Permalink to this definition")_class_ csc.layers.CyclesViewer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "Permalink to this definition")

Cycle viewer class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _layer:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.__module__ "Permalink to this definition")any\_cycles\_exist\_in\_frames( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.any_cycles_exist_in_frames "Permalink to this definition")cycle\_contains\_frame\_index( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.cycle_contains_frame_index "Permalink to this definition")find\_cycle( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.find_cycle "Permalink to this definition")get\_active\_pos( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.get_active_pos "Permalink to this definition")get\_active\_section\_pos( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.get_active_section_pos "Permalink to this definition")get\_cycles\_in\_frames( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.get_cycles_in_frames "Permalink to this definition")get\_most\_left\_and\_right\_frame\_indices\_of\_cycle( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[csc.layers.Cycle](https://cascadeur.com/python-api/csc.html#csc.layers.Cycle "csc.layers.Cycle")_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.get_most_left_and_right_frame_indices_of_cycle "Permalink to this definition")is\_pos\_in\_active\_cycle\_zone( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.is_pos_in_active_cycle_zone "Permalink to this definition")is\_pos\_in\_inactive\_cycle\_zone( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.is_pos_in_inactive_cycle_zone "Permalink to this definition")last\_pos( _self:[csc.layers.CyclesViewer](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.CyclesViewer.last_pos "Permalink to this definition")_class_ csc.layers.Editor [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "Permalink to this definition")

Editor class

This class contains all methods and properties that need to edit the structure of scene objects’ interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.

Variables:

- **create\_folder** – name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId

- **create\_layer** – name : string, parent : FolderId, pos : int or None, -> FolderId

- **set\_fixed\_interpolation\_if\_need** – overridden method by ItemId, int, int \|\| LayerId, int (frame)

- **set\_fixed\_interpolation\_or\_key\_if\_need** – overridden method by LayerId, int, bool


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.__module__ "Permalink to this definition")change\_section( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _arg0:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg1:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _arg2:Callable_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.change_section "Permalink to this definition")clear( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.clear "Permalink to this definition")create\_folder( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _parent:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _with\_default\_layer:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=True_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")=None_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.create_folder "Permalink to this definition")

name : string \| parent : FolderId \| withDefaultLayer : bool (true) \| pos : int or None \| -> FolderId

create\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _parent:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")=None_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.create_layer "Permalink to this definition")

name : string \| parent : FolderId \| pos : int or None \| -> FolderId

delete\_empty\_folders( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_empty_folders "Permalink to this definition")delete\_empty\_layers( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_empty_layers "Permalink to this definition")delete\_folder( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_folder "Permalink to this definition")delete\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.delete_layer "Permalink to this definition")find\_header( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.find_header "Permalink to this definition")

-\> Header

insert\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _layer:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.insert_layer "Permalink to this definition")

layer : Layer \| pos : int or None

move\_item( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _item\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _folder\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.move_item "Permalink to this definition")

pos : int or None

normalize\_sections( _self:csc.layers.Editor_, _scene:domain::scene::Scene_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.normalize_sections "Permalink to this definition")set\_default( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_default "Permalink to this definition")set\_fixed\_interpolation\_if\_need( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_fixed_interpolation_if_need "Permalink to this definition")

Overloaded function.

1. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool

2. set\_fixed\_interpolation\_if\_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool


set\_fixed\_interpolation\_or\_key\_if\_need( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _frame:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _set\_key:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_fixed_interpolation_or_key_if_need "Permalink to this definition")set\_locked\_for\_item( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_l:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_locked_for_item "Permalink to this definition")

isL : bool \| id : ItemId

set\_locked\_for\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_l:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_locked_for_layer "Permalink to this definition")

isL : bool \| id : LayerId

set\_name( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_name "Permalink to this definition")set\_section( _self:csc.layers.Editor_, _section:domain::scene::layers::layer::Section_, _pos:int_, _id:csc.Guid_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_section "Permalink to this definition")

section : Section \| pos : int \| id : ItemId

set\_sections( _self:csc.layers.Editor,arg0:dict\[int,domain::scene::layers::layer::Section\],arg1:csc.Guid_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_sections "Permalink to this definition")

section : <Pos, Section>{} \| id : LayerId

set\_visible\_for\_item( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_v:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_visible_for_item "Permalink to this definition")

isV : bool \| id : ItemId

set\_visible\_for\_layer( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _is\_v:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.set_visible_for_layer "Permalink to this definition")

isV : bool \| id : LayerId

unset\_section( _self:[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Editor.unset_section "Permalink to this definition")

pos : int \| id : ItemId

_class_ csc.layers.Folder [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "Permalink to this definition")

Folder class

Implements the parent folder properties of children layers and sub folders items

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.__module__ "Permalink to this definition")child\_by\_id( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.child_by_id "Permalink to this definition")

-\> ItemId

child\_by\_pos( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.child_by_pos "Permalink to this definition")

pos : int
-\> ItemId

child\_pos( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.child_pos "Permalink to this definition")

id : ItemId \| -> int

children\_cnt( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.children_cnt "Permalink to this definition")

-\> int

children\_ids( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.children_ids "Permalink to this definition")

-\> ItemId\[\]

children\_ordered( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.children_ordered "Permalink to this definition")

-\> ItemId\[\]

has\_child( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.has_child "Permalink to this definition")_property_ header [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.header "Permalink to this definition")

-\> Header

is\_empty( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.is_empty "Permalink to this definition")_class_ csc.layers.Header [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header "Permalink to this definition")

Header class

Describes the header properties for a folder

Variables:

- **parent** – Get set csc.Guid

- **id** – Get set csc.Guid

- **name** – Get set string


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header.__module__ "Permalink to this definition")_property_ id [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header.id "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header.name "Permalink to this definition")_property_ parent [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Header.parent "Permalink to this definition")_class_ csc.layers.ItemVariant [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "Permalink to this definition")

ItemVariant class

Can implement a folder or layer for a header

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.__module__ "Permalink to this definition")folder( _self:[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")_)→domain::scene::layers::Folder [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.folder "Permalink to this definition")

-\> Folder (if it has folder otherwise none)

header( _self:[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")_)→[csc.layers.Header](https://cascadeur.com/python-api/csc.html#csc.layers.Header "csc.layers.Header") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.header "Permalink to this definition")

-\> Header

is\_folder( _self:[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.is_folder "Permalink to this definition")is\_layer( _self:[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.is_layer "Permalink to this definition")layer( _self:[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")_)→domain::scene::layers::Layer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant.layer "Permalink to this definition")

-\> Layer (if it has layer otherwise none)

_class_ csc.layers.Layer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "Permalink to this definition")

Layer class

The Layer is the basic element that implements intervals and sections to set
interpolation properties of scene objects

Variables:

- **header** – Get Header

- **is\_locked** – Get bool

- **is\_visible** – Get bool

- **obj\_ids** – Get csc.Guid{}

- **sections** – Get std::map<Pos, Section>


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.__module__ "Permalink to this definition")actual\_key( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Key [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_key "Permalink to this definition")

-\> Key

actual\_key\_pos( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_key_pos "Permalink to this definition")

-\> int

actual\_section( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Section [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_section "Permalink to this definition")

-\> Section

actual\_section\_pos( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_section_pos "Permalink to this definition")

-\> int

find\_section( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.find_section "Permalink to this definition")

pos : int \| -> Section

_property_ header [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.header "Permalink to this definition")interval( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Interval [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.interval "Permalink to this definition")

-\> Interval

is\_key( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_key "Permalink to this definition")is\_key\_or\_fixed( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_key_or_fixed "Permalink to this definition")_property_ is\_locked [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_locked "Permalink to this definition")_property_ is\_visible [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_visible "Permalink to this definition")key( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Key [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.key "Permalink to this definition")

-\> Key

key\_frame\_indices( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_)→domain::scene::layers::index::FramesIndices [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.key_frame_indices "Permalink to this definition")

-\> FramesIndices

last\_key\_pos( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.last_key_pos "Permalink to this definition")

-\> int

_property_ obj\_ids [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.obj_ids "Permalink to this definition")

-\> csc.model.ObjectId{}

section( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Section [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.section "Permalink to this definition")

-\> Section

_property_ sections [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.sections "Permalink to this definition")

-\> std::map<Pos, Section>

_class_ csc.layers.Layers [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers "Permalink to this definition")

Layers class

The root class describes the layers’ hierarchy of the scene.
Each scene object can be placed on any layer to define its personal interpolation properties.

Variables:

**root\_id** – Get csc.Guid

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.__module__ "Permalink to this definition")folders( _self:[csc.layers.Layers](https://cascadeur.com/python-api/csc.html#csc.layers.Layers "csc.layers.Layers")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.folders "Permalink to this definition")

-\> <FolderId, Folder>{}

layers( _self:[csc.layers.Layers](https://cascadeur.com/python-api/csc.html#csc.layers.Layers "csc.layers.Layers")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.layers "Permalink to this definition")

-\> LayersContainer

_property_ root\_id [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.root_id "Permalink to this definition")userLabels( _self:[csc.layers.Layers](https://cascadeur.com/python-api/csc.html#csc.layers.Layers "csc.layers.Layers")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Layers.userLabels "Permalink to this definition")

-\> UserLabels

_class_ csc.layers.LayersContainer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "Permalink to this definition")

LayersContainer class

It is the container of layers.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.__module__ "Permalink to this definition")at( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.at "Permalink to this definition")

-\> Layer

has\_any\_obj\_ids( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.has_any_obj_ids "Permalink to this definition")has\_obj\_id( _self:csc.layers.LayersContainer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.has_obj_id "Permalink to this definition")layer\_id\_by\_obj\_id( _self:csc.layers.LayersContainer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.layer_id_by_obj_id "Permalink to this definition")

-\> LayerId

layer\_id\_by\_obj\_id\_or\_null( _self:csc.layers.LayersContainer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.layer_id_by_obj_id_or_null "Permalink to this definition")

-\> LayerId

map( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.map "Permalink to this definition")

-\> <LayerId, Layer>{}

obj\_ids( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.obj_ids "Permalink to this definition")

-\> <csc.model.ObjectId, LayerId>{}

_class_ csc.layers.LayersSelectionChanger [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger "Permalink to this definition")

Layer SelectionChanger class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.__module__ "Permalink to this definition")refresh( _self:[csc.layers.LayersSelectionChanger](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.refresh "Permalink to this definition")selectDefault( _self:[csc.layers.LayersSelectionChanger](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger "csc.layers.LayersSelectionChanger")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.selectDefault "Permalink to this definition")set\_full\_selection\_by\_parts( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.LayersSelectionChanger.set_full_selection_by_parts "Permalink to this definition")

Overloaded function.

1. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None


> inds : IndicesContainer

2. set\_full\_selection\_by\_parts(self: csc.layers.LayersSelectionChanger, itms: list\[csc.Guid\], first: int, last: int) -> bool


_class_ csc.layers.Selector [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "Permalink to this definition")

Selector class

This class contains methods to observe and to set selected layers and folders

Variables:

**set\_full\_selection\_by\_parts** – overridden method by ItemId\[\] (itms), int (first), int (last) \|\| IndicesContainer (inds)

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.__module__ "Permalink to this definition")all\_included\_layer\_ids( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.all_included_layer_ids "Permalink to this definition")

ignoreLocked : bool (false) \| -> LayerId\[\]

all\_included\_layer\_indices( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→domain::scene::layers::index::IndicesContainer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.all_included_layer_indices "Permalink to this definition")

ignoreLocked : bool (false) \| -> IndicesContainer

is\_selected( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.is_selected "Permalink to this definition")select\_default( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.select_default "Permalink to this definition")selection( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_)→domain::scene::layers::index::IndicesContainer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.selection "Permalink to this definition")

-\> IndicesContainer

set\_full\_selection\_by\_parts( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.set_full_selection_by_parts "Permalink to this definition")

Overloaded function.

1. set\_full\_selection\_by\_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None


> inds : IndicesContainer

2. set\_full\_selection\_by\_parts(self: csc.layers.Selector, itms: list\[csc.Guid\], first: int, last: int) -> None


set\_uncheckable\_folder\_id( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _uncheckable:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.set_uncheckable_folder_id "Permalink to this definition")

id : ItemId \| uncheckable : bool

top\_layer\_id( _self:[csc.layers.Selector](https://cascadeur.com/python-api/csc.html#csc.layers.Selector "csc.layers.Selector")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Selector.top_layer_id "Permalink to this definition")_class_ csc.layers.UserLabelData [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData "Permalink to this definition")

UserLabelData class

The data of user defined label.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData.__module__ "Permalink to this definition")_property_ color [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData.color "Permalink to this definition")_property_ id [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData.id "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData.name "Permalink to this definition")_class_ csc.layers.UserLabels [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels "Permalink to this definition")

UserLabels class

It is the storage of user defined labels.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.__module__ "Permalink to this definition")add( _self:[csc.layers.UserLabels](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels "csc.layers.UserLabels")_, _label:[csc.layers.UserLabelData](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabelData "csc.layers.UserLabelData")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.add "Permalink to this definition")find( _self:[csc.layers.UserLabels](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels "csc.layers.UserLabels")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.find "Permalink to this definition")

-\> index

remove( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.remove "Permalink to this definition")

Overloaded function.

1. remove(self: csc.layers.UserLabels, index: int) -> None

2. remove(self: csc.layers.UserLabels, arg0: int) -> object


> -\> UserLabelData


storage( _self:[csc.layers.UserLabels](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels "csc.layers.UserLabels")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.UserLabels.storage "Permalink to this definition")

-\> UserLabelData\[\]

_class_ csc.layers.Viewer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "Permalink to this definition")

Viewer class

This class contains all methods and properties that describe the structure of scene objects’ interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.

Variables:

- **top\_layer\_id** – overridden method by ItemId \|\| ItemId\[\]

- **merged\_layer** – overridden method like static and member LayerId\[\]

- **last\_key\_pos** – overridden method by LayerId\[\], -> Layer

- **frames\_count** – overridden method by LayerId\[\], -> int

- **significant\_frames** – overridden method by LayerId{}, -> int{}


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.__module__ "Permalink to this definition")actual\_key\_pos( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.actual_key_pos "Permalink to this definition")all\_child\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_child_ids "Permalink to this definition")

-\> ItemId\[\]

all\_included\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _items:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_included_layer_ids "Permalink to this definition")

items : ItemId\[\] \| ignoreLocked : bool (false) \| -> LayerId\[\]

all\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_layer_ids "Permalink to this definition")

-\> LayerId\[\]

all\_parent\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_parent_ids "Permalink to this definition")

-\> FolderId\[\]

default\_layer\_id( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.default_layer_id "Permalink to this definition")

-\> LayerId

find\_folder( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.find_folder "Permalink to this definition")

id : FolderId \| -> Folder

find\_layer( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.find_layer "Permalink to this definition")

id : LayerId \| -> Layer

folder( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.folder "Permalink to this definition")

id : FolderId \| -> Folder

folders\_map( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid"), [csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.folders_map "Permalink to this definition")

-\> <FolderId, Folder>{}

for\_all\_ordered\_items( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _arg0:Callable\[\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.for_all_ordered_items "Permalink to this definition")frames\_count( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.frames_count "Permalink to this definition")

Overloaded function.

1. frames\_count(self: csc.layers.Viewer) -> int

2. frames\_count(self: csc.layers.Viewer, id\_arr: list\[csc.Guid\]) -> int


has\_item( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.has_item "Permalink to this definition")

-\> bool

header( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.header "Permalink to this definition")

id : ItemId \| -> Header

is\_deep\_child( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _item\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _folder\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.is_deep_child "Permalink to this definition")

-\> bool

item( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.item "Permalink to this definition")

id : ItemId \| -> ItemVariant

last\_key\_pos( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.last_key_pos "Permalink to this definition")

Overloaded function.

1. last\_key\_pos(self: csc.layers.Viewer) -> int

2. last\_key\_pos(self: csc.layers.Viewer, id\_arr: list\[csc.Guid\]) -> int


layer( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer "Permalink to this definition")

id : LayerId \| -> Layer

layer\_id\_by\_obj\_id( _self:csc.layers.Viewer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer_id_by_obj_id "Permalink to this definition")

id : csc.model.ObjectId \| -> LayerId

layer\_id\_by\_obj\_id\_or\_null( _self:csc.layers.Viewer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer_id_by_obj_id_or_null "Permalink to this definition")

id : csc.model.ObjectId \| -> LayerId

layer\_ids\_by\_obj\_ids( _self:csc.layers.Viewer,ids:list\[common::GenericId<domain::scene::model::ModelObject>\]_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer_ids_by_obj_ids "Permalink to this definition")

ids : csc.model.ObjectId\[\] \| -> LayerId{}

layers\_indices( _self:csc.layers.Viewer_, _id\_arr:domain::scene::layers::index::IndicesContainer_, _ignore\_locked:bool=False_)→domain::scene::layers::index::IndicesContainer [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layers_indices "Permalink to this definition")

-\> IndicesContainer

layers\_map( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid"), [csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layers_map "Permalink to this definition")

-\> <LayerId, Layer>{}

merged\_layer( _self:csc.layers.Viewer,scene:domain::scene::Scene,ids:list\[csc.Guid\],normalize:bool=True_)→[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.merged_layer "Permalink to this definition")obj\_ids\_by\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id\_arr:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_)→list\[common::GenericId<domain::scene::model::ModelObject>\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.obj_ids_by_layer_ids "Permalink to this definition")

-\> LayerId\[\]

pos\_in\_parent( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.pos_in_parent "Permalink to this definition")

-\> int

root\_id( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.root_id "Permalink to this definition")

-\> FolderId

significant\_frames( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.significant_frames "Permalink to this definition")

Overloaded function.

1. significant\_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices

2. significant\_frames(self: csc.layers.Viewer, id\_arr: set\[csc.Guid\]) -> domain::scene::layers::index::FramesIndices


top\_layer\_id( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.top_layer_id "Permalink to this definition")

Overloaded function.

1. top\_layer\_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid

2. top\_layer\_id(self: csc.layers.Viewer, id\_arr: list\[csc.Guid\]) -> csc.Guid


unlocked\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id\_arr:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.unlocked_layer_ids "Permalink to this definition")

-\> LayerId\[\]

## csc.model The Cascadeur python module that implements model and behaviors scene editors methods. [¶](https://cascadeur.com/python-api/csc.html\#csc-model-the-cascadeur-python-module-that-implements-model-and-behaviors-scene-editors-methods "Permalink to this heading")

Data.Value = std::variant<bool, int, float, Eigen::Vector3f, math::Rotation,

Eigen::Matrix3f, Eigen::Matrix4f, Eigen::Quaternionf,
std::string, common::Vector3b>;

Setting.Value = std::variant<bool, int>;

ClusterId = int

|     |     |
| --- | --- |
| [`csc.model.Data`](https://cascadeur.com/python-api/csc.html#csc.model.Data "csc.model.Data") | Data class |
| [`csc.model.Setting`](https://cascadeur.com/python-api/csc.html#csc.model.Setting "csc.model.Setting") | Setting class |
| [`csc.model.ClusterViewer`](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer") | ClusterViewer class |
| [`csc.model.ClusterEditor`](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor") | ClusterEditor class |
| [`csc.model.DataViewer`](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer") | DataViewer class |
| [`csc.model.DataEditor`](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor") | DataEditor class |
| [`csc.model.BehaviourViewer`](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer") | BehaviourViewer class |
| [`csc.model.BehaviourEditor`](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor") | BehaviourEditor class |
| [`csc.model.ModelViewer`](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer") | ModelViewer class |
| [`csc.model.ModelEditor`](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor") | ModelEditor class |
| [`csc.model.DataMode`](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "csc.model.DataMode") | [Data::Mode](data::Mode) enum |
| [`csc.model.SettingMode`](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode "csc.model.SettingMode") | Setting::Mode enum |
| [`csc.model.ObjectId`](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") |  |
| [`csc.model.DataId`](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") |  |
| [`csc.model.BehaviourId`](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId") |  |
| [`csc.model.SettingId`](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") |  |
| [`csc.model.HyperedgeId`](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") |  |
| [`csc.model.SettingFunctionId`](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") |  |
| [`csc.model.LerpMode`](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode") | LerpMode enumerable |
| [`csc.model.DescriptionTerm`](https://cascadeur.com/python-api/csc.html#csc.model.DescriptionTerm "csc.model.DescriptionTerm") |  |
| [`csc.model.CustomSelectionPolicy`](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy") | CustomSelectionPolicy enumerable |
| [`csc.model.PropertyType`](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "csc.model.PropertyType") | PropertyType enumerable |
| [`csc.model.PathName`](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName") |  |
| [`csc.model.ClustersEdge`](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge "csc.model.ClustersEdge") | ClustersEdge class |

_class_ csc.model.BehaviourEditor [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "Permalink to this definition")

BehaviourEditor class

This class allows editing of scene behaviours and their properties.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.__module__ "Permalink to this definition")add\_behaviour( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.add_behaviour "Permalink to this definition")

Overloaded function.

1. add\_behaviour(self: csc.model.BehaviourEditor, arg0: csc.model.ObjectId, arg1: str) -> csc.model.BehaviourId


> object\_id : csc.model.ObjectId \| behaviour\_type : string \| -> csc.model.BehaviourId

2. add\_behaviour(self: csc.model.BehaviourEditor, object\_id: csc.model.ObjectId, behaviour\_type: str, behaviour\_id: csc.model.BehaviourId) -> csc.model.BehaviourId


> object\_id : csc.model.ObjectId \| behaviour\_type : string \| behaviour\_id : csc.model.BehaviourId \| -> csc.model.BehaviourId


add\_behaviour\_asset\_to\_range( _self:csc.model.BehaviourEditor_, _behaviour\_id:csc.model.BehaviourId_, _name:str_, _asset\_id:common::GenericId<domain::scene::assets::Asset>_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.add_behaviour_asset_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| asset\_id : csc.domain.AssetId

add\_behaviour\_data\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _data\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.add_behaviour_data_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| data\_id : csc.model.DataId

add\_behaviour\_model\_object\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _mo\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.add_behaviour_model_object_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| mo\_id : csc.model.ObjectId

add\_behaviour\_reference\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _beh\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.add_behaviour_reference_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| beh\_id : csc.model.BehaviourId

add\_behaviour\_setting\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _setting\_id:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.add_behaviour_setting_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| setting\_id : csc.model.SettingId

delete\_behaviour( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.delete_behaviour "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId

delete\_behaviours( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _objects\_id:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.delete_behaviours "Permalink to this definition")

objectsId : {csc.model.ObjectId}

erase\_behaviour\_data\_from\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _data\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.erase_behaviour_data_from_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| data\_id : csc.model.DataId

erase\_behaviour\_model\_object\_from\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _mo\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.erase_behaviour_model_object_from_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| mo\_id : csc.model.ObjectId

erase\_behaviour\_reference\_from\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _beh\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.erase_behaviour_reference_from_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| beh\_id : csc.model.BehaviourId

erase\_behaviour\_setting\_from\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _setting\_id:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.erase_behaviour_setting_from_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| setting\_id : csc.model.SettingId

get\_viewer( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_)→[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.get_viewer "Permalink to this definition")hide\_behaviour( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _hidden:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=True_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.hide_behaviour "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| hidden : bool(true) -> bool

set\_behaviour\_asset( _self:csc.model.BehaviourEditor_, _behaviour\_id:csc.model.BehaviourId_, _name:str_, _asset\_id:common::GenericId<domain::scene::assets::Asset>_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_asset "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| asset\_id : csc.domain.AssetId

set\_behaviour\_data( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _data\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_data "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| dataId : csc.model.DataId

set\_behaviour\_data\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _inserted\_ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\]_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_data_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| inserted\_ids : csc.model.DataId

set\_behaviour\_field\_value( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _name\_value:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_field_value "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| name\_value : string

set\_behaviour\_model\_object( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _mo\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_model_object "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| mo\_id : csc.model.ObjectId

set\_behaviour\_model\_objects\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _inserted\_ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_model_objects_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| inserted\_ids : csc.model.ObjectId\[\]

set\_behaviour\_reference( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _beh\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_reference "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| beh\_id : csc.model.BehaviourId

set\_behaviour\_references\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _inserted\_ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")\]_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_references_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| inserted\_ids : csc.model.BehaviourId\[\]

set\_behaviour\_setting( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _setting\_id:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_setting "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| setting\_id : csc.model.SettingId

set\_behaviour\_settings\_to\_range( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _inserted\_ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")\]_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_settings_to_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| inserted\_ids : csc.model.SettingId\[\]

set\_behaviour\_string( _self:[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _str:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor.set_behaviour_string "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| str : string

_class_ csc.model.BehaviourId [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _arg0:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _arg0:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.BehaviourId, arg0: str) -> None

2. \_\_init\_\_(self: csc.model.BehaviourId) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _arg0:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.__str__ "Permalink to this definition")is\_null( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.is_null "Permalink to this definition")_static_ null()→[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.null "Permalink to this definition")to\_string( _self:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId.to_string "Permalink to this definition")_class_ csc.model.BehaviourViewer [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "Permalink to this definition")

BehaviourViewer class

This class allows viewing of scene behaviours and their properties.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.__module__ "Permalink to this definition")behaviour\_id( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _object\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _behaviour\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.behaviour_id "Permalink to this definition")

objectId : csc.model.ObjectId \| behaviour\_name : string \| -> csc.model.BehaviourId

get\_behaviour\_asset( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→common::GenericId<domain::scene::assets::Asset> [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_asset "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.BehaviourId

get\_behaviour\_asset\_range( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→list\[common::GenericId<domain::scene::assets::Asset>\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_asset_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.BehaviourId\[\]

get\_behaviour\_by\_name( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _object\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _behaviour\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_by_name "Permalink to this definition")

objectId : csc.model.ObjectId \| behaviour\_name : string \| -> csc.model.BehaviourId

get\_behaviour\_data( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_data "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.DataId

get\_behaviour\_data\_range( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_data_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.DataId\[\]

get\_behaviour\_name( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_name "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| -> string

get\_behaviour\_object( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_object "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.ObjectId

get\_behaviour\_objects\_range( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_objects_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.ObjectId\[\]

get\_behaviour\_owner( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_owner "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| -> csc.model.ObjectId

get\_behaviour\_property\_names( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_property_names "Permalink to this definition")

-\> string\[\]

get\_behaviour\_reference( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_reference "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.BehaviourId

get\_behaviour\_reference\_range( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_reference_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.BehaviourId\[\]

get\_behaviour\_setting( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_setting "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.SettingId

get\_behaviour\_settings\_range( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_settings_range "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> csc.model.SettingId\[\]

get\_behaviour\_string( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviour_string "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> string

get\_behaviours( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_behaviours "Permalink to this definition")

Overloaded function.

1. get\_behaviours(self: csc.model.BehaviourViewer, type\_name: str) -> list\[csc.model.BehaviourId\]


> typeName : string \| -> csc.model.BehaviourId\[\]

2. get\_behaviours(self: csc.model.BehaviourViewer, object\_id: csc.model.ObjectId) -> list\[csc.model.BehaviourId\]


> objectId : csc.model.ObjectId \| -> csc.model.BehaviourId\[\]


get\_children( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _object\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_children "Permalink to this definition")

-\> Children behs ids

get\_property\_type( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.PropertyType](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "csc.model.PropertyType") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.get_property_type "Permalink to this definition")

behaviour\_id : csc.model.BehaviourId \| name : string \| -> Type\[\]

is\_hidden( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.is_hidden "Permalink to this definition")

-\> bool

is\_valid\_behaviour\_type( _self:[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")_, _behaviour\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer.is_valid_behaviour_type "Permalink to this definition")

behaviour\_name : string \| -> bool

_class_ csc.model.ClusterEditor [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "Permalink to this definition")

ClusterEditor class

This class lets edit scene data clusters.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.__module__ "Permalink to this definition")add\_cluster( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _inserted\_ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\]_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.add_cluster "Permalink to this definition")

insertedIds : csc.model.DataId\[\] \| name : string (“”) \| -> ClusterId

add\_data\_to\_cluster( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _cluster\_index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _inserted\_ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.add_data_to_cluster "Permalink to this definition")

cluster\_index : ClusterId \| insertedIds : csc.model.DataId\[\]

bind\_clusters( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _cluster\_id\_first:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _cluster\_id\_second:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.bind_clusters "Permalink to this definition")

cluster\_id\_first : ClusterId \| cluster\_id\_second : ClusterId

remove\_cluster( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _cluster\_id:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.remove_cluster "Permalink to this definition")

cluster\_id : ClusterId

remove\_data\_from\_cluster( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _data\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.remove_data_from_cluster "Permalink to this definition")

data\_id : csc.model.DataId

set\_cluster\_name( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _cluster\_id:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.set_cluster_name "Permalink to this definition")

cluster\_id : ClusterId \| name : string

unbind\_cluster( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _cluster\_id:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.unbind_cluster "Permalink to this definition")

cluster\_id : ClusterId

unbind\_clusters( _self:[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")_, _cluster\_id\_first:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _cluster\_id\_second:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor.unbind_clusters "Permalink to this definition")

cluster\_id\_first : ClusterId \| cluster\_id\_second : ClusterId

_class_ csc.model.ClusterViewer [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "Permalink to this definition")

ClusterViewer class

This class lets read scene data clusters.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.__module__ "Permalink to this definition")cluster\_by\_data( _self:[csc.model.ClusterViewer](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")_, _data\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.cluster_by_data "Permalink to this definition")

data\_id : csc.model.DataId \| -> ClusterId

cluster\_datas( _self:[csc.model.ClusterViewer](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")_, _cluster\_id:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.cluster_datas "Permalink to this definition")

cluster\_id : ClusterId \| -> csc.model.DataId\[\]

cluster\_name( _self:[csc.model.ClusterViewer](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")_, _cluster\_id:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.cluster_name "Permalink to this definition")

cluster\_id : ClusterId \| -> string

clusters( _self:[csc.model.ClusterViewer](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.clusters "Permalink to this definition")

-\> ClusterId\[\]

clusters\_bindings( _self:[csc.model.ClusterViewer](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.ClustersEdge](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge "csc.model.ClustersEdge")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer.clusters_bindings "Permalink to this definition")

-\> (ClusterId,ClusterId)\[\]

_class_ csc.model.ClustersEdge [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge "Permalink to this definition")

ClustersEdge class

This class contains link between clusters

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge.__module__ "Permalink to this definition")_property_ a [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge.a "Permalink to this definition")_property_ b [¶](https://cascadeur.com/python-api/csc.html#csc.model.ClustersEdge.b "Permalink to this definition")_class_ csc.model.CustomSelectionPolicy [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy "Permalink to this definition")

> CustomSelectionPolicy enumerable
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

Default _=<CustomSelectionPolicy.Default:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.Default "Permalink to this definition")Single _=<CustomSelectionPolicy.Single:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.Single "Permalink to this definition")SingleType _=<CustomSelectionPolicy.SingleType:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.SingleType "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.model.CustomSelectionPolicy](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.model.CustomSelectionPolicy](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.model.CustomSelectionPolicy](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__int__ "Permalink to this definition")\_\_members\_\_ _={'Default':<CustomSelectionPolicy.Default:0>,'Single':<CustomSelectionPolicy.Single:1>,'SingleType':<CustomSelectionPolicy.SingleType:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.model.CustomSelectionPolicy](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy "csc.model.CustomSelectionPolicy")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.model.CustomSelectionPolicy.value "Permalink to this definition")_class_ csc.model.Data [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data "Permalink to this definition")

Data class

This class serves to represent any special type of data.
These data can be used in the update calculation or as behaviors’ properties.

Variables:

- **id** – Get Set csc.model.DataId

- **object\_id** – Get Set csc.model.ObjectId

- **name** – Get Set string

- **mode** – Get Set csc.model.DataMode


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.__module__ "Permalink to this definition")_property_ id [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.id "Permalink to this definition")_property_ mode [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.mode "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.name "Permalink to this definition")_property_ object\_id [¶](https://cascadeur.com/python-api/csc.html#csc.model.Data.object_id "Permalink to this definition")_class_ csc.model.DataEditor [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "Permalink to this definition")

DataEditor class

This class has the possibility to edit scene data and their properties.

Variables:

- **add\_data** – overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data

- **add\_setting** – overridden method by string, Setting.Value \|\| csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting

- **add\_constant\_data** – overridden method by string, Data.Value \|\| string, Data.Value, csc.model.DataId -> Data

- **add\_constant\_setting** – overridden method by string, Setting.Value \|\| string, Setting.Value, csc.model.SettingId -> Setting

- **set\_data\_value** – overridden method by csc.model.DataId&, Data.Value \|\| csc.model.DataId, int{}, Data.Value \|\| csc.model.DataId, int, Data.Value


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.__module__ "Permalink to this definition")add\_constant\_data( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.add_constant_data "Permalink to this definition")

Overloaded function.

1. add\_constant\_data(self: csc.model.DataEditor, arg0: str, arg1: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]) -> csc.model.Data

2. add\_constant\_data(self: csc.model.DataEditor, name: str, value: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\], id: csc.model.DataId) -> csc.model.Data


add\_constant\_setting( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.add_constant_setting "Permalink to this definition")

Overloaded function.

1. add\_constant\_setting(self: csc.model.DataEditor, arg0: str, arg1: Union\[bool, int\]) -> csc.model.Setting

2. add\_constant\_setting(self: csc.model.DataEditor, name: str, value: Union\[bool, int\], id: csc.model.SettingId) -> csc.model.Setting


add\_data( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.add_data "Permalink to this definition")

Overloaded function.

1. add\_data(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]) -> csc.model.Data


> -\> Data

2. add\_data(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\], id: csc.model.DataId) -> csc.model.Data


> -\> Data


add\_description( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _id:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.add_description "Permalink to this definition")add\_setting( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.add_setting "Permalink to this definition")

Overloaded function.

1. add\_setting(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, value: Union\[bool, int\], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting


> -\> Setting

2. add\_setting(self: csc.model.DataEditor, object\_id: csc.model.ObjectId, name: str, value: Union\[bool, int\], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting


> -\> Setting


change\_description( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _description:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.change_description "Permalink to this definition")cluster\_editor( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_)→[csc.model.ClusterEditor](https://cascadeur.com/python-api/csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.cluster_editor "Permalink to this definition")

-\> ClusterEditor

copy\_data( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_, _from\_to:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId"), [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.copy_data "Permalink to this definition")delete\_data( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_, _id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.delete_data "Permalink to this definition")delete\_setting( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_, _id:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.delete_setting "Permalink to this definition")remove\_description( _self:[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.remove_description "Permalink to this definition")reset\_description\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.reset_description_value "Permalink to this definition")

Overloaded function.

1. reset\_description\_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None

2. reset\_description\_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None


set\_data\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.set_data_value "Permalink to this definition")

Overloaded function.

1. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]) -> None

2. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set\[int\], value: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]) -> None

3. set\_data\_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]) -> None


set\_description\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.set_description_value "Permalink to this definition")

Overloaded function.

1. set\_description\_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None

2. set\_description\_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None


set\_setting\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor.set_setting_value "Permalink to this definition")

Overloaded function.

1. set\_setting\_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union\[bool, int\]) -> None

2. set\_setting\_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union\[bool, int\]) -> None


_class_ csc.model.DataId [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_, _arg0:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_, _arg0:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.DataId, arg0: str) -> None

2. \_\_init\_\_(self: csc.model.DataId) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_, _arg0:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.__str__ "Permalink to this definition")is\_null( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.is_null "Permalink to this definition")_static_ null()→[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.null "Permalink to this definition")to\_string( _self:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataId.to_string "Permalink to this definition")_class_ csc.model.DataMode [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "Permalink to this definition")

> [Data::Mode](data::Mode) enum
>
> This enumerates the basic types of data.
> Static, Animation

Members:

> Static
>
> Animation

Animation _=<DataMode.Animation:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.Animation "Permalink to this definition")Static _=<DataMode.Static:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.Static "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.model.DataMode](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "csc.model.DataMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.model.DataMode](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "csc.model.DataMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.model.DataMode](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "csc.model.DataMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'Animation':<DataMode.Animation:1>,'Static':<DataMode.Static:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.model.DataMode](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "csc.model.DataMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataMode.value "Permalink to this definition")_class_ csc.model.DataViewer [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "Permalink to this definition")

DataViewer class

This class allows to view scene data and their properties.

Variables:

- **get\_data\_value** – overridden method by id : csc.model.DataId \|\| csc.model.DataId, int (frame) -> Data.Value

- **get\_behaviour\_property** – overridden method by : csc.model.BehaviourId, string -> Data.Value \|\| csc.model.BehaviourId, string, int (frame) -> Setiing.Value


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.__module__ "Permalink to this definition")cluster\_viewer( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_)→[csc.model.ClusterViewer](https://cascadeur.com/python-api/csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.cluster_viewer "Permalink to this definition")

-\> ClusterViewer

get\_all\_data\_id( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _object\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_all_data_id "Permalink to this definition")

-\> csc.model.DataId\[\]

get\_all\_settings\_id( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _object\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_all_settings_id "Permalink to this definition")

-\> csc.model.SettingId\[\]

get\_animation\_size( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_animation_size "Permalink to this definition")

-\> int

get\_behaviour\_default\_data\_value( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _id:[csc.model.BehaviourId](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourId "csc.model.BehaviourId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") \|numpy.ndarray\[numpy.float32\[3,1\]\]\|numpy.ndarray\[numpy.float32\[4,1\]\]\| [csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") \|numpy.ndarray\[numpy.float32\[3,3\]\]\|numpy.ndarray\[numpy.float32\[4,4\]\]\| [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \|numpy.ndarray\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\[3,1\]\]\| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_behaviour_default_data_value "Permalink to this definition")

id : csc.model.Beh id \| name : string \| -> csc.model.DataValue

get\_behaviour\_property( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_behaviour_property "Permalink to this definition")

Overloaded function.

1. get\_behaviour\_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]

2. get\_behaviour\_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union\[bool, int\]


get\_data( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[csc.model.Data](https://cascadeur.com/python-api/csc.html#csc.model.Data "csc.model.Data") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_data "Permalink to this definition")

id : csc.model.DataId \| -> Data

get\_data\_id( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_data_id "Permalink to this definition")

id : csc.model.ObjectId \| name : string \| -> csc.model.DataId

get\_data\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_data_value "Permalink to this definition")

Overloaded function.

1. get\_data\_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]

2. get\_data\_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]


get\_description\_by\_name( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_description_by_name "Permalink to this definition")

-\> string

get\_description\_names( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_description_names "Permalink to this definition")

-\> string\[\]

get\_description\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_description_value "Permalink to this definition")

Overloaded function.

1. get\_description\_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str


> id : csc.model.DataId -> string

2. get\_description\_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str


> id : csc.model.SettingId -> string


get\_setting( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _id:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[csc.model.Setting](https://cascadeur.com/python-api/csc.html#csc.model.Setting "csc.model.Setting") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_setting "Permalink to this definition")

id : csc.model.SettingId \| -> Setting

get\_setting\_id( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_setting_id "Permalink to this definition")

id : csc.model.ObjectId \| name : string \| -> csc.model.DataId

get\_setting\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.get_setting_value "Permalink to this definition")

Overloaded function.

1. get\_setting\_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union\[bool, int\]


> id : csc.model.SettingId \| -> Setting.Value

2. get\_setting\_value(self: csc.model.DataViewer, setting\_id: csc.model.SettingId, position: int) -> Union\[bool, int\]


> id : csc.model.SettingId, position : int \| -> Setting.Value


union\_get\_data\_value( _self:[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer")_, _data\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_, _frame:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")=0_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") \|numpy.ndarray\[numpy.float32\[3,1\]\]\|numpy.ndarray\[numpy.float32\[4,1\]\]\| [csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") \|numpy.ndarray\[numpy.float32\[3,3\]\]\|numpy.ndarray\[numpy.float32\[4,4\]\]\| [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \|numpy.ndarray\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer.union_get_data_value "Permalink to this definition")

id : csc.model.DataId \| -> Data.Value

_class_ csc.model.DescriptionTerm [¶](https://cascadeur.com/python-api/csc.html#csc.model.DescriptionTerm "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DescriptionTerm.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.model.DescriptionTerm](https://cascadeur.com/python-api/csc.html#csc.model.DescriptionTerm "csc.model.DescriptionTerm")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.DescriptionTerm.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.DescriptionTerm.__module__ "Permalink to this definition")_class_ csc.model.HyperedgeId [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_, _arg0:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_, _arg0:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.HyperedgeId, arg0: str) -> None

2. \_\_init\_\_(self: csc.model.HyperedgeId) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_, _arg0:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.__str__ "Permalink to this definition")is\_null( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.is_null "Permalink to this definition")_static_ null()→[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.null "Permalink to this definition")to\_string( _self:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId.to_string "Permalink to this definition")_class_ csc.model.LerpMode [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "Permalink to this definition")

> LerpMode enumerable
>
> Empty, Linear, Spherical

Members:

> Empty
>
> Linear
>
> Spherical

Empty _=<LerpMode.Empty:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.Empty "Permalink to this definition")Linear _=<LerpMode.Linear:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.Linear "Permalink to this definition")Spherical _=<LerpMode.Spherical:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.Spherical "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.model.LerpMode](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.model.LerpMode](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.model.LerpMode](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'Empty':<LerpMode.Empty:0>,'Linear':<LerpMode.Linear:1>,'Spherical':<LerpMode.Spherical:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.model.LerpMode](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode.value "Permalink to this definition")_class_ csc.model.ModelEditor [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "Permalink to this definition")

ModelEditor class

Represents basic methods to edit the scene model

Variables:

**add\_object** – overridden method by GroupId -> csc.model.ObjectId

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.__module__ "Permalink to this definition")add\_object( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.add_object "Permalink to this definition")

Overloaded function.

1. add\_object(self: csc.model.ModelEditor) -> csc.model.ObjectId

2. add\_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId


behaviour\_editor( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[csc.model.BehaviourEditor](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.behaviour_editor "Permalink to this definition")

-\> BehaviourEditor

data\_editor( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[csc.model.DataEditor](https://cascadeur.com/python-api/csc.html#csc.model.DataEditor "csc.model.DataEditor") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.data_editor "Permalink to this definition")

-\> DataEditor

delete\_objects( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _ids:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_, _close\_connections:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=True_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.delete_objects "Permalink to this definition")fit\_animation\_size\_by\_layers( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.fit_animation_size_by_layers "Permalink to this definition")get\_viewer( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[csc.model.ModelViewer](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.get_viewer "Permalink to this definition")init\_default\_constants( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.init_default_constants "Permalink to this definition")layers( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.layers "Permalink to this definition")

-\> csc.layers.Layers

layers\_editor( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[csc.layers.Editor](https://cascadeur.com/python-api/csc.html#csc.layers.Editor "csc.layers.Editor") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.layers_editor "Permalink to this definition")

-\> csc.layers.Editor

layers\_selector( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.layers_selector "Permalink to this definition")

-\> csc.layers.Selector

move\_obj\_ids\_in\_layers( _self:csc.model.ModelEditor,objIds=csc.model.ObjectId\[\]:list\[csc.model.ObjectId\],layer\_id:csc.Guid_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.move_obj_ids_in_layers "Permalink to this definition")move\_objects\_to\_layer( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _ids:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\]_, _target\_layer\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.move_objects_to_layer "Permalink to this definition")set\_fixed\_interpolation\_if\_need( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _actuals:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")\]_, _frame:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.set_fixed_interpolation_if_need "Permalink to this definition")set\_object\_name( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.set_object_name "Permalink to this definition")set\_object\_type\_name( _self:[csc.model.ModelEditor](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor "csc.model.ModelEditor")_, _id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelEditor.set_object_type_name "Permalink to this definition")_class_ csc.model.ModelViewer [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "Permalink to this definition")

ModelViewer class

Represents basic methods to view the scene model

Variables:

**get\_objects** – overridden method by string -> csc.model.ObjectId\[\]

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.__module__ "Permalink to this definition")behaviour\_viewer( _self:[csc.model.ModelViewer](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer")_)→[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.behaviour_viewer "Permalink to this definition")

-\> BehaviourViewer

data\_viewer( _self:[csc.model.ModelViewer](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer")_)→[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.data_viewer "Permalink to this definition")

-\> DataViewer

get\_object\_name( _self:[csc.model.ModelViewer](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer")_, _id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.get_object_name "Permalink to this definition")get\_object\_type\_name( _self:[csc.model.ModelViewer](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer")_, _id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.get_object_type_name "Permalink to this definition")get\_objects( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer.get_objects "Permalink to this definition")

Overloaded function.

1. get\_objects(self: csc.model.ModelViewer) -> list\[csc.model.ObjectId\]

2. get\_objects(self: csc.model.ModelViewer, name: str) -> list\[csc.model.ObjectId\]


_class_ csc.model.ObjectId [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.ObjectId, arg0: str) -> None

2. \_\_init\_\_(self: csc.model.ObjectId) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.__str__ "Permalink to this definition")is\_null( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.is_null "Permalink to this definition")_static_ null()→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.null "Permalink to this definition")to\_string( _self:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId.to_string "Permalink to this definition")_class_ csc.model.PathName [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_, _arg0:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__cmp__ "Permalink to this definition")\_\_copy\_\_( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__copy__ "Permalink to this definition")\_\_deepcopy\_\_( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_, _arg0:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")_)→[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__deepcopy__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_, _arg0:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.PathName) -> None


> PathName class
>
> Implements a hierarchical name

2. \_\_init\_\_(self: csc.model.PathName, arg0: str, arg1: list\[str\]) -> None


> PathName class
>
> Implements a hierarchical name
>
> ivar name:
>
> Get Set string
>
> ivar path:
>
> Get Set string\[\]


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_, _arg0:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.__ne__ "Permalink to this definition")clear( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.clear "Permalink to this definition")empty( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.empty "Permalink to this definition")full\_path( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.full_path "Permalink to this definition")get\_namespace( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.get_namespace "Permalink to this definition")_static_ get\_path\_name( _obj\_id:csc.model.ObjectId_, _mv:domain::scene::model::ModelViewer_, _beh\_name:str='Joint'_)→[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.get_path_name "Permalink to this definition")_static_ get\_path\_names( _arg0:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.get_path_names "Permalink to this definition")_static_ get\_path\_names\_by\_behavior( _arg0:str_, _arg1:domain::scene::model::ModelViewer_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.get_path_names_by_behavior "Permalink to this definition")_static_ get\_path\_names\_for\_objects( _arg0:set\[csc.model.ObjectId\],arg1:domain::scene::model::ModelViewer_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName"), [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")\] [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.get_path_names_for_objects "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.name "Permalink to this definition")_property_ path [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.path "Permalink to this definition")set\_namespace( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_, _namespace:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.set_namespace "Permalink to this definition")to\_string( _self:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PathName.to_string "Permalink to this definition")_class_ csc.model.PropertyType [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "Permalink to this definition")

> PropertyType enumerable
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

AssetRangeType _=<PropertyType.AssetRangeType:10>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.AssetRangeType "Permalink to this definition")AssetType _=<PropertyType.AssetType:9>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.AssetType "Permalink to this definition")BehaviourRangeType _=<PropertyType.BehaviourRangeType:8>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.BehaviourRangeType "Permalink to this definition")BehaviourType _=<PropertyType.BehaviourType:7>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.BehaviourType "Permalink to this definition")DataRangeType _=<PropertyType.DataRangeType:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.DataRangeType "Permalink to this definition")DataType _=<PropertyType.DataType:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.DataType "Permalink to this definition")ObjectRangeType _=<PropertyType.ObjectRangeType:6>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.ObjectRangeType "Permalink to this definition")ObjectType _=<PropertyType.ObjectType:5>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.ObjectType "Permalink to this definition")SettingRangeType _=<PropertyType.SettingRangeType:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.SettingRangeType "Permalink to this definition")SettingType _=<PropertyType.SettingType:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.SettingType "Permalink to this definition")StringType _=<PropertyType.StringType:11>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.StringType "Permalink to this definition")Undefined _=<PropertyType.Undefined:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.Undefined "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.model.PropertyType](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "csc.model.PropertyType")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.model.PropertyType](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "csc.model.PropertyType")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.model.PropertyType](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "csc.model.PropertyType")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__int__ "Permalink to this definition")\_\_members\_\_ _={'AssetRangeType':<PropertyType.AssetRangeType:10>,'AssetType':<PropertyType.AssetType:9>,'BehaviourRangeType':<PropertyType.BehaviourRangeType:8>,'BehaviourType':<PropertyType.BehaviourType:7>,'DataRangeType':<PropertyType.DataRangeType:2>,'DataType':<PropertyType.DataType:1>,'ObjectRangeType':<PropertyType.ObjectRangeType:6>,'ObjectType':<PropertyType.ObjectType:5>,'SettingRangeType':<PropertyType.SettingRangeType:4>,'SettingType':<PropertyType.SettingType:3>,'StringType':<PropertyType.StringType:11>,'Undefined':<PropertyType.Undefined:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.model.PropertyType](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType "csc.model.PropertyType")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.model.PropertyType.value "Permalink to this definition")_class_ csc.model.Setting [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting "Permalink to this definition")

Setting class

This class serves to represent int or bool value that using in the update calculation.

Variables:

- **id** – Get csc.model.DataId

- **object\_id** – Get csc.model.ObjectId

- **name** – Get string

- **type** – Get int

- **mode** – Get csc.model.SettingMode


Parameters:

**object\_id** ( [_csc.model.ObjectId_](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")) – object\_id

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.Setting, id: csc.model.SettingId, object\_id: csc.model.ObjectId, name: str, type: int) -> None

2. \_\_init\_\_(self: csc.model.Setting, object\_id: csc.model.ObjectId, name: str, type: int) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.__module__ "Permalink to this definition")_property_ id [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.id "Permalink to this definition")_property_ mode [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.mode "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.name "Permalink to this definition")_property_ object\_id [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.object_id "Permalink to this definition")_property_ type [¶](https://cascadeur.com/python-api/csc.html#csc.model.Setting.type "Permalink to this definition")_class_ csc.model.SettingFunctionId [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_, _arg0:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_, _arg0:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.SettingFunctionId, arg0: str) -> None

2. \_\_init\_\_(self: csc.model.SettingFunctionId) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_, _arg0:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.__str__ "Permalink to this definition")is\_null( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.is_null "Permalink to this definition")_static_ null()→[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.null "Permalink to this definition")to\_string( _self:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId.to_string "Permalink to this definition")_class_ csc.model.SettingId [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_, _arg0:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_, _arg0:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.model.SettingId, arg0: str) -> None

2. \_\_init\_\_(self: csc.model.SettingId) -> None


\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_, _arg0:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.__str__ "Permalink to this definition")is\_null( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.is_null "Permalink to this definition")_static_ null()→[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.null "Permalink to this definition")to\_string( _self:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingId.to_string "Permalink to this definition")_class_ csc.model.SettingMode [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode "Permalink to this definition")

> Setting::Mode enum
>
> This enumerates the basic types of data.
> Static, Animation

Members:

> Static
>
> Animation

Animation _=<SettingMode.Animation:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.Animation "Permalink to this definition")Static _=<SettingMode.Static:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.Static "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.model.SettingMode](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode "csc.model.SettingMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.model.SettingMode](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode "csc.model.SettingMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.model.SettingMode](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode "csc.model.SettingMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'Animation':<SettingMode.Animation:1>,'Static':<SettingMode.Static:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.model'_ [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.model.SettingMode](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode "csc.model.SettingMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.model.SettingMode.value "Permalink to this definition")csc.model.get\_path\_without\_namespace( _path\_name:[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName")_)→[csc.model.PathName](https://cascadeur.com/python-api/csc.html#csc.model.PathName "csc.model.PathName") [¶](https://cascadeur.com/python-api/csc.html#csc.model.get_path_without_namespace "Permalink to this definition")

-\> PathName

## csc.domain The Cascadeur python module that implements basic scene properties and infrastructure. [¶](https://cascadeur.com/python-api/csc.html\#csc-domain-the-cascadeur-python-module-that-implements-basic-scene-properties-and-infrastructure "Permalink to this heading")

Entity3d\_id = std::variant<model::ModelObject::Id, Tool\_object\_id>

|     |     |
| --- | --- |
| [`csc.domain.Pivot`](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot "csc.domain.Pivot") | Pivot class |
| [`csc.domain.Selection`](https://cascadeur.com/python-api/csc.html#csc.domain.Selection "csc.domain.Selection") | Selection class |
| [`csc.domain.Selector`](https://cascadeur.com/python-api/csc.html#csc.domain.Selector "csc.domain.Selector") | Selector class |
| [`csc.domain.AssetId`](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId") |  |
| [`csc.domain.Asset`](https://cascadeur.com/python-api/csc.html#csc.domain.Asset "csc.domain.Asset") | Asset class |
| [`csc.domain.LocalInterpolator`](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator") | LocalInterpolator class |
| [`csc.domain.SceneUpdater`](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater") | SceneUpdater class |
| [`csc.domain.ProcessorsStorage`](https://cascadeur.com/python-api/csc.html#csc.domain.ProcessorsStorage "csc.domain.ProcessorsStorage") | ProcessorsStorage class |
| [`csc.domain.IMessageHandler`](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler "csc.domain.IMessageHandler") | IMessageHandler interface |
| [`csc.domain.Scene`](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene") | Scene class |
| [`csc.domain.Session`](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session") | Session class |
| [`csc.domain.Tool_object_id`](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id") |  |
| [`csc.domain.StatePivot`](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot "csc.domain.StatePivot") | StatePivot enum |
| [`csc.domain.FrameActionOnChange`](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange") | FrameActionOnChange enum |
| [`csc.domain.IntervalActionOnChange`](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange") | IntervalActionOnChange enum |
| [`csc.domain.SelectorMode`](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode") | SelectorMode enumerable |
| [`csc.domain.SelectorFilter`](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter "csc.domain.SelectorFilter") | SelectorFilter enumerable |
| [`csc.domain.Select`](https://cascadeur.com/python-api/csc.html#csc.domain.Select "csc.domain.Select") | Select class |
| [`csc.domain.assets.FigureVertex`](https://cascadeur.com/python-api/_generate/csc.domain.assets.FigureVertex.html#csc.domain.assets.FigureVertex "csc.domain.assets.FigureVertex") | FigureVertex class |
| [`csc.domain.assets.Triangle`](https://cascadeur.com/python-api/_generate/csc.domain.assets.Triangle.html#csc.domain.assets.Triangle "csc.domain.assets.Triangle") | Triangle class |
| [`csc.domain.assets.Mesh`](https://cascadeur.com/python-api/_generate/csc.domain.assets.Mesh.html#csc.domain.assets.Mesh "csc.domain.assets.Mesh") | Mesh class |
| [`csc.domain.assets.MeshDependency`](https://cascadeur.com/python-api/_generate/csc.domain.assets.MeshDependency.html#csc.domain.assets.MeshDependency "csc.domain.assets.MeshDependency") | MeshDependency class |
| [`csc.domain.assets.AssetsManager`](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager") | AssetsManager class |

_class_ csc.domain.Asset [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Asset "Permalink to this definition")

Asset class

Assets are objects resources that have content like meshes or textures.

Variables:

**id** – Get csc.Guid

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Asset.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Asset.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Asset.__module__ "Permalink to this definition")_property_ id [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Asset.id "Permalink to this definition")_class_ csc.domain.AssetId [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_, _arg0:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_, _arg0:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.domain.AssetId, arg0: str) -> None

2. \_\_init\_\_(self: csc.domain.AssetId) -> None


\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_, _arg0:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.__str__ "Permalink to this definition")is\_null( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.is_null "Permalink to this definition")_static_ null()→[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.null "Permalink to this definition")to\_string( _self:[csc.domain.AssetId](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId "csc.domain.AssetId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.AssetId.to_string "Permalink to this definition")_class_ csc.domain.FrameActionOnChange [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange "Permalink to this definition")

> FrameActionOnChange enum
>
> AutoKey = 0, Fixing = 1, DoNothing = 2

Members:

> AutoKey
>
> Fixing
>
> DoNothing

AutoKey _=<FrameActionOnChange.AutoKey:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.AutoKey "Permalink to this definition")DoNothing _=<FrameActionOnChange.DoNothing:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.DoNothing "Permalink to this definition")Fixing _=<FrameActionOnChange.Fixing:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.Fixing "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.domain.FrameActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.FrameActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.domain.FrameActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__int__ "Permalink to this definition")\_\_members\_\_ _={'AutoKey':<FrameActionOnChange.AutoKey:0>,'DoNothing':<FrameActionOnChange.DoNothing:2>,'Fixing':<FrameActionOnChange.Fixing:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.domain.FrameActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange "csc.domain.FrameActionOnChange")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.domain.FrameActionOnChange.value "Permalink to this definition")_class_ csc.domain.IMessageHandler [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler "Permalink to this definition")

IMessageHandler interface

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler.__module__ "Permalink to this definition")_class_ csc.domain.IntervalActionOnChange [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange "Permalink to this definition")

> IntervalActionOnChange enum
>
> Fixing = 0, DoNothing = 1

Members:

> Fixing
>
> DoNothing

DoNothing _=<IntervalActionOnChange.DoNothing:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.DoNothing "Permalink to this definition")Fixing _=<IntervalActionOnChange.Fixing:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.Fixing "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.domain.IntervalActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.IntervalActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.domain.IntervalActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__int__ "Permalink to this definition")\_\_members\_\_ _={'DoNothing':<IntervalActionOnChange.DoNothing:1>,'Fixing':<IntervalActionOnChange.Fixing:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.domain.IntervalActionOnChange](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange "csc.domain.IntervalActionOnChange")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.domain.IntervalActionOnChange.value "Permalink to this definition")_class_ csc.domain.LocalInterpolator [¶](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator "Permalink to this definition")

LocalInterpolator class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator.__module__ "Permalink to this definition")interpolate( _self:[csc.domain.LocalInterpolator](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator.interpolate "Permalink to this definition")reload( _self:[csc.domain.LocalInterpolator](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator.reload "Permalink to this definition")_class_ csc.domain.Pivot [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot "Permalink to this definition")

Pivot class

Represents basic Pivot methods.

Variables:

- **position** – overridden method by … \|\| int (frame) \|\| int, StatePivot (pivot)

- **rotation** – overridden method by … \|\| int (frame) \|\| int, StatePivot (pivot)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.__module__ "Permalink to this definition")center\_of\_top\_objects( _self:[csc.domain.Pivot](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot "csc.domain.Pivot")_, _arg0:Callable\[\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")\],numpy.ndarray\[numpy.float32\[3,1\]\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.center_of_top_objects "Permalink to this definition")position( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.position "Permalink to this definition")

Overloaded function.

1. position(self: csc.domain.Pivot) -> numpy.ndarray\[numpy.float32\[3, 1\]\]

2. position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray\[numpy.float32\[3, 1\]\]

3. position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray\[numpy.float32\[3, 1\]\]


rotation( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.rotation "Permalink to this definition")

Overloaded function.

1. rotation(self: csc.domain.Pivot) -> csc.math.Quaternion

2. rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion

3. rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion


select( _self:[csc.domain.Pivot](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot "csc.domain.Pivot")_, _entity\_id:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Pivot.select "Permalink to this definition")_class_ csc.domain.ProcessorsStorage [¶](https://cascadeur.com/python-api/csc.html#csc.domain.ProcessorsStorage "Permalink to this definition")

ProcessorsStorage class

The class serves to contain entity 3d processors

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.ProcessorsStorage.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.ProcessorsStorage.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.ProcessorsStorage.__module__ "Permalink to this definition")_class_ csc.domain.Scene [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "Permalink to this definition")

Scene class

Root class that represents a scene and its methods for modifying or observing it.

Modify scene by func modify:

Parameters:

- **name** – Name of the modifier

- **func** – Modify functor void(modelEditor, updateEditor, scene)


Modify scene by func modify\_update:

Parameters:

- **name** – Name of the modifier

- **func** – Modify functor void(modelEditor, updateEditor, sceneUpdater)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.__module__ "Permalink to this definition")assets\_manager( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→domain::scene::AssetsManager [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.assets_manager "Permalink to this definition")

-\> AssetsManager

behaviour\_viewer( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[csc.model.BehaviourViewer](https://cascadeur.com/python-api/csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.behaviour_viewer "Permalink to this definition")

-\> csc.model.BehaviourViewer

data\_viewer( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[csc.model.DataViewer](https://cascadeur.com/python-api/csc.html#csc.model.DataViewer "csc.model.DataViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.data_viewer "Permalink to this definition")

-\> csc.model.DataViewer

error( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.error "Permalink to this definition")get\_current\_frame( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _clamp\_animation:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=True_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.get_current_frame "Permalink to this definition")

-\> int

get\_event\_log\_or\_null( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.get_event_log_or_null "Permalink to this definition")get\_layers\_selector( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.get_layers_selector "Permalink to this definition")

-\> csc.layers.Selector

info( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.info "Permalink to this definition")layers\_viewer( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.layers_viewer "Permalink to this definition")

-\> csc.layers.Viewer

model\_viewer( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[csc.model.ModelViewer](https://cascadeur.com/python-api/csc.html#csc.model.ModelViewer "csc.model.ModelViewer") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.model_viewer "Permalink to this definition")

-\> csc.model.ModelViewer

modify( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:Callable_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.modify "Permalink to this definition")

-\> bool

modify\_update( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:Callable_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.modify_update "Permalink to this definition")

-\> bool

modify\_update\_with\_session( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:Callable_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.modify_update_with_session "Permalink to this definition")

-\> bool

modify\_with\_session( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _arg1:Callable_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.modify_with_session "Permalink to this definition")

-\> bool

selector( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.selector "Permalink to this definition")

-\> Selector

set\_current\_frame( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _frame:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.set_current_frame "Permalink to this definition")set\_event\_log( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _message\_handler:[csc.domain.IMessageHandler](https://cascadeur.com/python-api/csc.html#csc.domain.IMessageHandler "csc.domain.IMessageHandler")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.set_event_log "Permalink to this definition")success( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.success "Permalink to this definition")warning( _self:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Scene.warning "Permalink to this definition")_class_ csc.domain.SceneUpdater [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater "Permalink to this definition")

SceneUpdater class

The SceneUpdater serves to rule the scene modify.
If we changed the update, we should regenerate it, also it has the possible to run the update with certain data.

Variables:

**run\_update** – overridden method by csc.model.DataId{} (localIds), int (frame) \|\| csc.model.DataId{}, int{} (frames)

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.__module__ "Permalink to this definition")generate\_update( _self:[csc.domain.SceneUpdater](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.generate_update "Permalink to this definition")get\_interpolator( _self:[csc.domain.SceneUpdater](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater")_)→[csc.domain.LocalInterpolator](https://cascadeur.com/python-api/csc.html#csc.domain.LocalInterpolator "csc.domain.LocalInterpolator") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.get_interpolator "Permalink to this definition")run\_update( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.run_update "Permalink to this definition")

Overloaded function.

1. run\_update(self: csc.domain.SceneUpdater, local\_ids: set\[csc.model.DataId\], frame: int) -> None

2. run\_update(self: csc.domain.SceneUpdater, local\_ids: set\[csc.model.DataId\], frames: csc.layers.index.FramesIndices) -> None


scene( _self:[csc.domain.SceneUpdater](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater "csc.domain.SceneUpdater")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SceneUpdater.scene "Permalink to this definition")_class_ csc.domain.Select [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select "Permalink to this definition")

Select class

Represents properties of the current selection state of the scene

Variables:

- **object\_ids** – Get Set (csc.model.ObjectId or csc.scene.Tool\_object\_id){}

- **pivot\_id** – Get Set (csc.model.ObjectId or csc.scene.Tool\_object\_id)

- **filter** – Get Set csc.scene.SelectorFilter

- **mode** – Get Set csc.scene.SelectorMode

- **types\_filter** – Get Set string{}


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.Select](https://cascadeur.com/python-api/csc.html#csc.domain.Select "csc.domain.Select")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.__module__ "Permalink to this definition")_property_ filter [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.filter "Permalink to this definition")_property_ mode [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.mode "Permalink to this definition")_property_ object\_ids [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.object_ids "Permalink to this definition")_property_ pivot\_id [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.pivot_id "Permalink to this definition")_property_ types\_filter [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Select.types_filter "Permalink to this definition")_class_ csc.domain.Selection [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selection "Permalink to this definition")

Selection class

Contains selected objects

Variables:

**ids** – Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selection.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selection.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selection.__module__ "Permalink to this definition")_property_ ids [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selection.ids "Permalink to this definition")_property_ ordered\_ids [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selection.ordered_ids "Permalink to this definition")_class_ csc.domain.SelectionChanger [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger "Permalink to this definition")

SelectionChanger class

Contains basic methods and properties to operate current selected scene objects

Variables:

- **ids** – Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}

- **select** – overridden method by Select \|\| Entity3d\_id{}, Entity3d\_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger.__module__ "Permalink to this definition")clear\_selection( _self:[csc.domain.SelectionChanger](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger "csc.domain.SelectionChanger")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger.clear_selection "Permalink to this definition")refresh\_selection( _self:[csc.domain.SelectionChanger](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger "csc.domain.SelectionChanger")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger.refresh_selection "Permalink to this definition")select( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectionChanger.select "Permalink to this definition")

Overloaded function.

1. select(self: csc.domain.SelectionChanger, select: csc.domain.Select) -> None

2. select(self: csc.domain.SelectionChanger, ids: set\[Union\[csc.model.ObjectId, csc.domain.Tool\_object\_id\]\], id: Union\[csc.model.ObjectId, csc.domain.Tool\_object\_id\] = <csc.model.ObjectId object at 0x7f3d3ffa9b30>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, types\_filter: set\[str\] = set(), auto\_pivot: bool = False) -> None


_class_ csc.domain.Selector [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector "Permalink to this definition")

Selector class

Contains basic methods and properties to operate current selected scene objects

Variables:

- **ids** – Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}

- **select** – overridden method by Select \|\| Entity3d\_id{}, Entity3d\_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector.__module__ "Permalink to this definition")pivot( _self:[csc.domain.Selector](https://cascadeur.com/python-api/csc.html#csc.domain.Selector "csc.domain.Selector")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector.pivot "Permalink to this definition")

-\> Pivot

select( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector.select "Permalink to this definition")

Overloaded function.

1. select(self: csc.domain.Selector, select: csc.domain.Select) -> None

2. select(self: csc.domain.Selector, ids: set\[Union\[csc.model.ObjectId, csc.domain.Tool\_object\_id\]\], id: Union\[csc.model.ObjectId, csc.domain.Tool\_object\_id\] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type\_filter: set\[str\] = set(), auto\_pivot: bool = False) -> None


selected( _self:[csc.domain.Selector](https://cascadeur.com/python-api/csc.html#csc.domain.Selector "csc.domain.Selector")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Selector.selected "Permalink to this definition")

-\> Selection

_class_ csc.domain.SelectorFilter [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter "Permalink to this definition")

> SelectorFilter enumerable
>
> Free = 0x00,
> Selectable = 0x01,
> ObjectType = 0x02,
> Layer = 0x04,
> CustomSelectionPolicy = 0x08,
> Standart = Selectable \| ObjectType \| Layer,
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

CustomSelectionPolicy _=<SelectorFilter.CustomSelectionPolicy:8>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.CustomSelectionPolicy "Permalink to this definition")Free _=<SelectorFilter.Free:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.Free "Permalink to this definition")Full _=<SelectorFilter.Full:255>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.Full "Permalink to this definition")Layer _=<SelectorFilter.Layer:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.Layer "Permalink to this definition")ObjectType _=<SelectorFilter.ObjectType:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.ObjectType "Permalink to this definition")Selectable _=<SelectorFilter.Selectable:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.Selectable "Permalink to this definition")Standart _=<SelectorFilter.Standart:7>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.Standart "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.domain.SelectorFilter](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter "csc.domain.SelectorFilter")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.SelectorFilter](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter "csc.domain.SelectorFilter")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.domain.SelectorFilter](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter "csc.domain.SelectorFilter")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__int__ "Permalink to this definition")\_\_members\_\_ _={'CustomSelectionPolicy':<SelectorFilter.CustomSelectionPolicy:8>,'Free':<SelectorFilter.Free:0>,'Full':<SelectorFilter.Full:255>,'Layer':<SelectorFilter.Layer:4>,'ObjectType':<SelectorFilter.ObjectType:2>,'Selectable':<SelectorFilter.Selectable:1>,'Standart':<SelectorFilter.Standart:7>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.domain.SelectorFilter](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter "csc.domain.SelectorFilter")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorFilter.value "Permalink to this definition")_class_ csc.domain.SelectorMode [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode "Permalink to this definition")

> SelectorMode enumerable
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

AdditionSelection _=<SelectorMode.AdditionSelection:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.AdditionSelection "Permalink to this definition")MultiSelection _=<SelectorMode.MultiSelection:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.MultiSelection "Permalink to this definition")NewSelection _=<SelectorMode.NewSelection:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.NewSelection "Permalink to this definition")SingleSelection _=<SelectorMode.SingleSelection:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.SingleSelection "Permalink to this definition")SubtractionSelection _=<SelectorMode.SubtractionSelection:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.SubtractionSelection "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.domain.SelectorMode](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.SelectorMode](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.domain.SelectorMode](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__int__ "Permalink to this definition")\_\_members\_\_ _={'AdditionSelection':<SelectorMode.AdditionSelection:3>,'MultiSelection':<SelectorMode.MultiSelection:1>,'NewSelection':<SelectorMode.NewSelection:2>,'SingleSelection':<SelectorMode.SingleSelection:0>,'SubtractionSelection':<SelectorMode.SubtractionSelection:4>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.domain.SelectorMode](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.domain.SelectorMode.value "Permalink to this definition")_class_ csc.domain.Session [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session "Permalink to this definition")

Session class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session.__module__ "Permalink to this definition")set\_current\_frame( _self:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_, _frame:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session.set_current_frame "Permalink to this definition")take\_layers\_selector( _self:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session.take_layers_selector "Permalink to this definition")take\_selector( _self:[csc.domain.Session](https://cascadeur.com/python-api/csc.html#csc.domain.Session "csc.domain.Session")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Session.take_selector "Permalink to this definition")_class_ csc.domain.StatePivot [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot "Permalink to this definition")

> StatePivot enum
>
> This enumerates the basic types of pivot states.
> Fixed = 0, Moving = 1

Members:

> Fixed
>
> Moving

Fixed _=<StatePivot.Fixed:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.Fixed "Permalink to this definition")Moving _=<StatePivot.Moving:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.Moving "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.domain.StatePivot](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot "csc.domain.StatePivot")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.domain.StatePivot](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot "csc.domain.StatePivot")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.domain.StatePivot](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot "csc.domain.StatePivot")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__int__ "Permalink to this definition")\_\_members\_\_ _={'Fixed':<StatePivot.Fixed:0>,'Moving':<StatePivot.Moving:1>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.domain.StatePivot](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot "csc.domain.StatePivot")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.domain.StatePivot.value "Permalink to this definition")_class_ csc.domain.Tool\_object\_id [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_, _arg0:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_, _arg0:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.domain.Tool\_object\_id, arg0: str) -> None

2. \_\_init\_\_(self: csc.domain.Tool\_object\_id) -> None


\_\_module\_\_ _='csc.domain'_ [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_, _arg0:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.__str__ "Permalink to this definition")is\_null( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.is_null "Permalink to this definition")_static_ null()→[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.null "Permalink to this definition")to\_string( _self:[csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id.to_string "Permalink to this definition")csc.domain.delete\_entity\_3d\_processor( _scene:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _ids:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.delete_entity_3d_processor "Permalink to this definition")csc.domain.get\_tool\_name( _scene:[csc.domain.Scene](https://cascadeur.com/python-api/csc.html#csc.domain.Scene "csc.domain.Scene")_, _ids:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.domain.Tool\_object\_id](https://cascadeur.com/python-api/csc.html#csc.domain.Tool_object_id "csc.domain.Tool_object_id")\]_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.domain.get_tool_name "Permalink to this definition")_class_ csc.math.Affine [¶](https://cascadeur.com/python-api/csc.html#csc.math.Affine "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Affine.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Affine](https://cascadeur.com/python-api/csc.html#csc.math.Affine "csc.math.Affine")_, _angle\_axisf:[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Affine.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Affine.__module__ "Permalink to this definition")linear( _self:[csc.math.Affine](https://cascadeur.com/python-api/csc.html#csc.math.Affine "csc.math.Affine")_)→numpy.ndarray\[numpy.float32\[3,3\],flags.f\_contiguous\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Affine.linear "Permalink to this definition")_class_ csc.math.AngleAxis [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "Permalink to this definition")

AngleAxis class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis")_, _angle:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _axis:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis.__module__ "Permalink to this definition")affine\_linear( _self:[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis")_)→numpy.ndarray\[numpy.float32\[3,3\],flags.writeable,flags.f\_contiguous\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis.affine_linear "Permalink to this definition")angle( _self:[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis.angle "Permalink to this definition")axis( _self:[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis.axis "Permalink to this definition")_class_ csc.math.Circle [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle "Permalink to this definition")

Circle3d class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Circle](https://cascadeur.com/python-api/csc.html#csc.math.Circle "csc.math.Circle")_, _radius:numpy.ndarray\[numpy.float32\[3,1\]\]_, _center:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _normal:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle.__module__ "Permalink to this definition")center( _self:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle.center "Permalink to this definition")normal( _self:[csc.math.Circle](https://cascadeur.com/python-api/csc.html#csc.math.Circle "csc.math.Circle")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle.normal "Permalink to this definition")radius( _self:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Circle.radius "Permalink to this definition")_class_ csc.math.OrthogonalTransform [¶](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform "Permalink to this definition")

OrthogonalTransform class

Implements orthogonal transform

Variables:

- **position** – Get set Vector3f

- **rotation** – Get set Rotation


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.math.OrthogonalTransform, position: numpy.ndarray\[numpy.float32\[3, 1\]\], rotate: csc.math.Quaternion) -> None

2. \_\_init\_\_(self: csc.math.OrthogonalTransform) -> None


\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform.__module__ "Permalink to this definition")_property_ position [¶](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform.position "Permalink to this definition")_property_ rotation [¶](https://cascadeur.com/python-api/csc.html#csc.math.OrthogonalTransform.rotation "Permalink to this definition")_class_ csc.math.ParametrizedLine [¶](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine "Permalink to this definition")

ParametrizedLine class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.ParametrizedLine](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine "csc.math.ParametrizedLine")_, _origin:numpy.ndarray\[numpy.float32\[3,1\]\]_, _direction:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine.__module__ "Permalink to this definition")projection( _self:[csc.math.ParametrizedLine](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine "csc.math.ParametrizedLine")_, _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine.projection "Permalink to this definition")_class_ csc.math.Plane [¶](https://cascadeur.com/python-api/csc.html#csc.math.Plane "Permalink to this definition")

Hyperplane class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Plane.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_, _normal:numpy.ndarray\[numpy.float32\[3,1\]\]_, _point:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Plane.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Plane.__module__ "Permalink to this definition")projection( _self:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_, _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Plane.projection "Permalink to this definition")_class_ csc.math.Quaternion [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "Permalink to this definition")

Quaternion class

This class is useful to calculate rotation operations.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_, _w:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _x:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _y:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _z:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.__module__ "Permalink to this definition")\_\_mul\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.__mul__ "Permalink to this definition")

Overloaded function.

1. \_\_mul\_\_(self: csc.math.Quaternion, arg0: csc.math.Quaternion) -> csc.math.Quaternion

2. \_\_mul\_\_(self: csc.math.Quaternion, arg0: numpy.ndarray\[numpy.float32\[3, 1\]\]) -> numpy.ndarray\[numpy.float32\[3, 1\]\]


_static_ from\_two\_vectors( _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_, _arg1:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.from_two_vectors "Permalink to this definition")_static_ identity()→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.identity "Permalink to this definition")inverse( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.inverse "Permalink to this definition")w( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.w "Permalink to this definition")x( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.x "Permalink to this definition")y( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.y "Permalink to this definition")z( _self:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion.z "Permalink to this definition")_class_ csc.math.Rotation [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "Permalink to this definition")

Rotation class

The Euler angles implementation.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.__module__ "Permalink to this definition")_static_ from\_angle\_axis( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_angle_axis "Permalink to this definition")

Overloaded function.

1. from\_angle\_axis(arg0: float, arg1: numpy.ndarray\[numpy.float32\[3, 1\]\]) -> csc.math.Rotation

2. from\_angle\_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation


_static_ from\_euler( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_euler "Permalink to this definition")

Overloaded function.

1. from\_euler(x: float, y: float, z: float) -> csc.math.Rotation

2. from\_euler(vec3f: numpy.ndarray\[numpy.float32\[3, 1\]\]) -> csc.math.Rotation


_static_ from\_quaternion( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_quaternion "Permalink to this definition")

Overloaded function.

1. from\_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation

2. from\_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation


_static_ from\_rotation\_matrix( _arg0:numpy.ndarray\[numpy.float32\[3,3\]\]_)→[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.from_rotation_matrix "Permalink to this definition")to\_angle\_axis( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[csc.math.AngleAxis](https://cascadeur.com/python-api/csc.html#csc.math.AngleAxis "csc.math.AngleAxis") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_angle_axis "Permalink to this definition")to\_euler\_angles( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_euler_angles "Permalink to this definition")to\_euler\_angles\_x\_y\_z( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_euler_angles_x_y_z "Permalink to this definition")to\_quaternion( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_quaternion "Permalink to this definition")to\_rotation\_matrix( _self:[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation")_)→numpy.ndarray\[numpy.float32\[3,3\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Rotation.to_rotation_matrix "Permalink to this definition")_class_ csc.math.ScaledTransform [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "Permalink to this definition")

ScaledTransform class

Implements transform with the scale possibility.

Variables:

- **position** – Get set Vector3f

- **rotation** – Get set Rotation

- **scale** – Get set Vector3f


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.__annotations__ "Permalink to this definition")\_\_copy\_\_( _self:[csc.math.ScaledTransform](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "csc.math.ScaledTransform")_)→[csc.math.ScaledTransform](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "csc.math.ScaledTransform") [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.__copy__ "Permalink to this definition")\_\_deepcopy\_\_( _self:[csc.math.ScaledTransform](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "csc.math.ScaledTransform")_, _arg0:[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")_)→[csc.math.ScaledTransform](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "csc.math.ScaledTransform") [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.__deepcopy__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.ScaledTransform](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform "csc.math.ScaledTransform")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.__module__ "Permalink to this definition")_property_ position [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.position "Permalink to this definition")_property_ rotation [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.rotation "Permalink to this definition")_property_ scale [¶](https://cascadeur.com/python-api/csc.html#csc.math.ScaledTransform.scale "Permalink to this definition")_class_ csc.math.SizesInterval [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "Permalink to this definition")

SizesInterval class

Implements the sizes interval basic methods

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _arg0:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__eq__ "Permalink to this definition")\_\_hash\_\_ _=None_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.math.SizesInterval) -> None

2. \_\_init\_\_(self: csc.math.SizesInterval, start: int, end: int) -> None


\_\_lt\_\_( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _arg0:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__lt__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.__module__ "Permalink to this definition")_static_ construct\_in\_right\_order( _first:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _second:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.construct_in_right_order "Permalink to this definition")contains( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _i:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.contains "Permalink to this definition")empty( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.empty "Permalink to this definition")

-\> bool

end( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.end "Permalink to this definition")

-\> int

inside\_interval\_inclusive( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _number:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.inside_interval_inclusive "Permalink to this definition")_static_ intersect\_intervals( _first:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _second:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.intersect_intervals "Permalink to this definition")_static_ safe\_construct( _first:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _second:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.safe_construct "Permalink to this definition")start( _self:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.start "Permalink to this definition")

-\> int

_static_ union\_overlaping\_intervals( _first:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_, _second:[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval")_)→[csc.math.SizesInterval](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval "csc.math.SizesInterval") [¶](https://cascadeur.com/python-api/csc.html#csc.math.SizesInterval.union_overlaping_intervals "Permalink to this definition")_class_ csc.math.Sphere [¶](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "Permalink to this definition")

Sphere class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Sphere.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_, _radius:numpy.ndarray\[numpy.float32\[3,1\]\]_, _center:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Sphere.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Sphere.__module__ "Permalink to this definition")center( _self:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.Sphere.center "Permalink to this definition")radius( _self:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Sphere.radius "Permalink to this definition")_class_ csc.math.Triangle [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle "Permalink to this definition")

Triangle class

Structure from three points

Variables:

- **point1** – Get set Vector3f

- **point2** – Get set Vector3f

- **point3** – Get set Vector3f


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.math.Triangle](https://cascadeur.com/python-api/csc.html#csc.math.Triangle "csc.math.Triangle")_, _point1:numpy.ndarray\[numpy.float32\[3,1\]\]_, _point2:numpy.ndarray\[numpy.float32\[3,1\]\]_, _point3:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.math'_ [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle.__module__ "Permalink to this definition")_property_ point1 [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle.point1 "Permalink to this definition")_property_ point2 [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle.point2 "Permalink to this definition")_property_ point3 [¶](https://cascadeur.com/python-api/csc.html#csc.math.Triangle.point3 "Permalink to this definition")csc.math.basic\_transform\_from\_triangle( _triangle:math::Triangle_)→math::OrthogonalTransform [¶](https://cascadeur.com/python-api/csc.html#csc.math.basic_transform_from_triangle "Permalink to this definition")

-\> csc.math.OrthogonalTransform

csc.math.combine\_transforms( _firstorthogonaltransform:math::OrthogonalTransform_, _secondorthogonaltransform:math::OrthogonalTransform_)→math::OrthogonalTransform [¶](https://cascadeur.com/python-api/csc.html#csc.math.combine_transforms "Permalink to this definition")

-\> csc.math.OrthogonalTransform

csc.math.decompose\_matrix( _arg0:numpy.ndarray\[numpy.float32\[4,4\]\]_)→domain::scene::model::data\_struct::ScaledTransform [¶](https://cascadeur.com/python-api/csc.html#csc.math.decompose_matrix "Permalink to this definition")csc.math.euler\_angles\_to\_quaternion\_x\_y\_z( _euler\_angles:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") [¶](https://cascadeur.com/python-api/csc.html#csc.math.euler_angles_to_quaternion_x_y_z "Permalink to this definition")

-\> Quaternionf

csc.math.euler\_flip( _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_, _arg1:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") [¶](https://cascadeur.com/python-api/csc.html#csc.math.euler_flip "Permalink to this definition")csc.math.get\_m3f\_diag( _matrix:numpy.ndarray\[numpy.float32\[3,3\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.get_m3f_diag "Permalink to this definition")

-\> Vector3f

csc.math.ik\_spline( _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_, _arg1:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\]_, _arg2:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")\]_, _arg3:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.ik_spline "Permalink to this definition")

-\> Tuple<vector<Vector3f>, vector<Quaternion>>

csc.math.ik\_spline\_2( _arg0:numpy.ndarray\[numpy.float32\[3,1\]\]_, _arg1:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\]_, _arg2:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")\]_, _arg3:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.ik_spline_2 "Permalink to this definition")

-\> Tuple<vector<Vector3f>, vector<Quaternion>>

csc.math.ik\_spline\_3( _arg0:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\]_, _arg1:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")\]_, _arg2:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")\]_)→[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")\[ [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[numpy.ndarray\[numpy.float32\[3,1\]\]\], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.ik_spline_3 "Permalink to this definition")

-\> Tuple<vector<Vector3f>, vector<Quaternion>>

csc.math.inverse\_transform\_point( _transform:math::OrthogonalTransform,point:numpy.ndarray\[numpy.float32\[3,1\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.inverse_transform_point "Permalink to this definition")

-\> Vector3f

csc.math.line\_on\_intersection\_planes( _arg0:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_, _arg1:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_)→[csc.math.ParametrizedLine](https://cascadeur.com/python-api/csc.html#csc.math.ParametrizedLine "csc.math.ParametrizedLine") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.line_on_intersection_planes "Permalink to this definition")csc.math.modify\_position\_by\_matrix( _matrix:numpy.ndarray\[numpy.float32\[3,3\]\]_, _position:numpy.ndarray\[numpy.float32\[3,1\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.modify_position_by_matrix "Permalink to this definition")

-\> Vector3f

csc.math.point\_on\_intersection\_planes( _arg0:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_, _arg1:[csc.math.Plane](https://cascadeur.com/python-api/csc.html#csc.math.Plane "csc.math.Plane")_)→numpy.ndarray\[numpy.float32\[3,1\]\]\| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.point_on_intersection_planes "Permalink to this definition")csc.math.project\_point\_on\_basic\_line( _line\_direction:numpy.ndarray\[numpy.float32\[3,1\]\]_, _point:numpy.ndarray\[numpy.float32\[3,1\]\]_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.project_point_on_basic_line "Permalink to this definition")

-\> Vector3f

csc.math.quaternion\_to\_euler\_angles\_x\_y\_z( _quaternion:[csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion")_)→numpy.ndarray\[numpy.float32\[3,1\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.quaternion_to_euler_angles_x_y_z "Permalink to this definition")

-\> Vector3f

csc.math.spheres\_intersection( _arg0:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_, _arg1:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_)→[csc.math.Circle](https://cascadeur.com/python-api/csc.html#csc.math.Circle "csc.math.Circle") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.spheres_intersection "Permalink to this definition")csc.math.spheres\_intersection\_extended( _arg0:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_, _arg1:[csc.math.Sphere](https://cascadeur.com/python-api/csc.html#csc.math.Sphere "csc.math.Sphere")_)→[csc.math.Circle](https://cascadeur.com/python-api/csc.html#csc.math.Circle "csc.math.Circle") \| [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.spheres_intersection_extended "Permalink to this definition")csc.math.step\_linear\_func( _arg0:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _arg1:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _arg2:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_)→[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.math.step_linear_func "Permalink to this definition")csc.math.transform\_point( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.math.transform_point "Permalink to this definition")

Overloaded function.

1. transform\_point(transform: math::OrthogonalTransform, point: numpy.ndarray\[numpy.float32\[3, 1\]\]) -> numpy.ndarray\[numpy.float32\[3, 1\]\]


> -\> Vector3f

2. transform\_point(matrix: numpy.ndarray\[numpy.float32\[4, 4\]\], point: numpy.ndarray\[numpy.float32\[3, 1\]\]) -> numpy.ndarray\[numpy.float32\[3, 1\]\]


> -\> Vector3f


csc.math.transforms\_difference( _firstorthogonaltransform:math::OrthogonalTransform_, _secondorthogonaltransform:math::OrthogonalTransform_)→math::OrthogonalTransform [¶](https://cascadeur.com/python-api/csc.html#csc.math.transforms_difference "Permalink to this definition")

-\> csc.math.OrthogonalTransform

csc.math.untwist( _arg0:numpy.ndarray\[numpy.float32\[4,4\]\]_, _arg1:numpy.ndarray\[numpy.float32\[4,4\]\]_, _arg2:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _arg3:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _arg4:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _arg5:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→numpy.ndarray\[numpy.float32\[4,4\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.math.untwist "Permalink to this definition")

(weight:float,roll:float,axis:int,negate:bool,
parentMatrix:Matrix4f,objectMatrix:Matrix4f) -> Matrix4f

_class_ csc.physics.PosMass [¶](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass "Permalink to this definition")

PosMass class

This structure contains the mass and the position

Variables:

- **mass** – Get Set float.

- **position** – Get Set Vector3f.


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.physics.PosMass](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass "csc.physics.PosMass")_, _mass:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_, _position:numpy.ndarray\[numpy.float32\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.physics'_ [¶](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass.__module__ "Permalink to this definition")_property_ mass [¶](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass.mass "Permalink to this definition")_property_ position [¶](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass.position "Permalink to this definition")csc.physics.inertia\_tensor( _mass\_and\_poses:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.physics.PosMass](https://cascadeur.com/python-api/csc.html#csc.physics.PosMass "csc.physics.PosMass")\]_, _center:numpy.ndarray\[numpy.float32\[3,1\]\]_)→numpy.ndarray\[numpy.float32\[3,3\]\] [¶](https://cascadeur.com/python-api/csc.html#csc.physics.inertia_tensor "Permalink to this definition")

-\> Matrix3f

## csc.update The Cascadeur python module that implements basic update editor methods and its infrastructure. [¶](https://cascadeur.com/python-api/csc.html\#csc-update-the-cascadeur-python-module-that-implements-basic-update-editor-methods-and-its-infrastructure "Permalink to this heading")

Update editor provides a node-like interface to edit data and setting graphs.
Naming conventions: regular means the same as data. It differs stuff from settings.

Additional functionality.
Update editor can be used to check what data functions will be active if you set some datas as actual.

AttributeId = std::variant<RegularFunctionAttributeId, ActivityAttributeId,

RegularDataAttributeId, ActualityAttributeId,
SettingFunctionAttributeId, SettingDataAttributeId,
GroupAttributeId, ExternalPropertyAttributeId,
ConstantDataAttributeId, ConstantSettingAttributeId>;

|     |     |
| --- | --- |
| [`csc.update.NodeAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute") | NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute. |
| [`csc.update.RegularDataAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute") | RegularDataAttribute represents an attribute of a regular data. |
| [`csc.update.ActualityAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttribute "csc.update.ActualityAttribute") | ActualityAttribute shows whether data is actual at the start of the graphs update. |
| [`csc.update.ConstantDataAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttribute "csc.update.ConstantDataAttribute") | ConstantDataAttribute represents an attribute of a constant regular data. |
| [`csc.update.ConstantSettingAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttribute "csc.update.ConstantSettingAttribute") | ConstantSettingAttribute represents an attribute of a constant setting. |
| [`csc.update.ExternalPropertyAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttribute "csc.update.ExternalPropertyAttribute") | ExternalPropertyAttribute represents an attribute of the external properties of the update. |
| [`csc.update.SettingFunctionAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute") | SettingFunctionAttribute represents an attribute of a setting function. |
| [`csc.update.InterfaceAttributeSide`](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide") | InterfaceAttributeSide enumerable |
| [`csc.update.InterfaceAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") | InterfaceAttribute represents a group attribute. |
| [`csc.update.RegularFunctionAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute") | RegularFunctionAttribute represents an attribute of a data function. |
| [`csc.update.ActivityAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.ActivityAttribute "csc.update.ActivityAttribute") | ActivityAttribute represents the activity of the data function. |
| [`csc.update.SettingDataAttribute`](https://cascadeur.com/python-api/csc.html#csc.update.SettingDataAttribute "csc.update.SettingDataAttribute") | SettingDataAttribute represents an attribute of a setting. |
| [`csc.update.Node`](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node") | Node class represents a generic Node and implements methods that are common for all nodes |
| [`csc.update.InterfaceNode`](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode") | InterfaceNode is a node inside the group that represents its connections with the ouside nodes. |
| [`csc.update.ConstantDatas`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas "csc.update.ConstantDatas") | ConstantDatas represents a node of constant datas. |
| [`csc.update.ConstantSettings`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings "csc.update.ConstantSettings") | ConstantSettings represents a node of constant settings. |
| [`csc.update.ExternalProperties`](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties "csc.update.ExternalProperties") | ExternalProperties represents a node of external properties. |
| [`csc.update.RegularFunction`](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction") | RegularFunction class represents a node that calculates same operation, done with datas. |
| [`csc.update.SettingData`](https://cascadeur.com/python-api/csc.html#csc.update.SettingData "csc.update.SettingData") | SettingData class represents a node that calculates same operation, done with settings. |
| [`csc.update.SettingFunction`](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction") | SettingFunction class |
| [`csc.update.Object`](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object") | Object class represents an object node. |
| [`csc.update.RegularData`](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData") | RegularData class represents a node of a data. |
| [`csc.update.Group`](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group") | Group class |
| [`csc.update.ObjectGroup`](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup") | ObjectGroup class represents object group node |
| [`csc.update.UpdateGroup`](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup") | UpdateGroup class represents update group node |
| [`csc.update.HierarchyUpdate`](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate "csc.update.HierarchyUpdate") | HierarchyUpdate class provides concrete operations with connections |
| [`csc.update.Update`](https://cascadeur.com/python-api/csc.html#csc.update.Update "csc.update.Update") | Update class represents the whole update editor |
| [`csc.update.RegularFunctionAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute |
| [`csc.update.RegularDataAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | RegularDataAttributeId is defined by the data id. |
| [`csc.update.ActualityAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | ActualityAttributeId is defined by the data id. |
| [`csc.update.SettingFunctionAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | SettingFunctionAttributeId is defined by the SettingFunctionId and the index of the attribute |
| [`csc.update.GroupId`](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") |  |
| [`csc.update.GroupAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | GroupAttributeId is defined by the GroupId and the guid-based id of the attribute. |
| [`csc.update.ExternalPropertiesId`](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") | ExternalPropertiesId is a guid based id. |
| [`csc.update.ExternalProperty`](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "csc.update.ExternalProperty") | ExternalProperty enum |
| [`csc.update.ExternalPropertyAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | ExternalPropertyAttributeId is defined by the ExternalPropertiesId and the value of the ExternalProperty enum |
| [`csc.update.ConstantDatasId`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId "csc.update.ConstantDatasId") | ConstantDatasId is a guid based id. |
| [`csc.update.ConstantDataAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant |
| [`csc.update.ConstantSettingsId`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") | ConstantSettingsId is a guid based id. |
| [`csc.update.ConstantSettingAttributeId`](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId") | ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant |
| [`csc.update.Connection`](https://cascadeur.com/python-api/csc.html#csc.update.Connection "csc.update.Connection") | Connection class |
| [`csc.update.InterfaceId`](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId "csc.update.InterfaceId") | InterfaceId is defined by the GroupId and the direction type of the node - input or output connection node. |

_class_ csc.update.ActivityAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActivityAttribute "Permalink to this definition")

ActivityAttribute represents the activity of the data function.
It should be bool.
If true - function is active, if false - inactive. If not set - always active.
It is an input-only attribute.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActivityAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActivityAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActivityAttribute.__module__ "Permalink to this definition")_class_ csc.update.ActualityAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttribute "Permalink to this definition")

ActualityAttribute shows whether data is actual at the start of the graphs update.
It’s always an output attribute.
It can be connected with setting functions.

!Connections directly with data functions activity are not supported, use copy setting function instead)

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttribute.__module__ "Permalink to this definition")_class_ csc.update.ActualityAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId "Permalink to this definition")

ActualityAttributeId is defined by the data id. It’s an output only attribute.
Each data can be actual or non-actual at the start of the graphs update.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.update.ActualityAttributeId, arg0: str) -> None

2. \_\_init\_\_(self: csc.update.ActualityAttributeId, arg0: csc.model.DataId) -> None

3. \_\_init\_\_(self: csc.update.ActualityAttributeId) -> None


\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId.__module__ "Permalink to this definition")_class_ csc.update.Connection [¶](https://cascadeur.com/python-api/csc.html#csc.update.Connection "Permalink to this definition")

Connection class

Implements the Connection between two attributes

Variables:

- **source** – Get output AttributeId of the source

- **destination** – Get input AttributeId of the destination


AttributeId = std::variant<RegularFunctionAttributeId, ActivityAttributeId,

RegularDataAttributeId, ActualityAttributeId,
SettingFunctionAttributeId, SettingDataAttributeId,
GroupAttributeId, ExternalPropertyAttributeId,
ConstantDataAttributeId, ConstantSettingAttributeId>

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Connection.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.Connection](https://cascadeur.com/python-api/csc.html#csc.update.Connection "csc.update.Connection")_, _source:[csc.update.RegularFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") \| [csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") \| [csc.update.RegularDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") \| [csc.update.ActualityAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") \| [csc.update.SettingFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") \| [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") \| [csc.update.GroupAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") \| [csc.update.ExternalPropertyAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") \| [csc.update.ConstantDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") \| [csc.update.ConstantSettingAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")_, _destination:[csc.update.RegularFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") \| [csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") \| [csc.update.RegularDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") \| [csc.update.ActualityAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") \| [csc.update.SettingFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") \| [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") \| [csc.update.GroupAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") \| [csc.update.ExternalPropertyAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") \| [csc.update.ConstantDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") \| [csc.update.ConstantSettingAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Connection.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Connection.__module__ "Permalink to this definition")_property_ destination [¶](https://cascadeur.com/python-api/csc.html#csc.update.Connection.destination "Permalink to this definition")_property_ source [¶](https://cascadeur.com/python-api/csc.html#csc.update.Connection.source "Permalink to this definition")_class_ csc.update.ConstantDataAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttribute "Permalink to this definition")

ConstantDataAttribute represents an attribute of a constant regular data.
It’s always an output attribute.
It can be connected with setting functions or data functions activity.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttribute.__module__ "Permalink to this definition")_class_ csc.update.ConstantDataAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId "Permalink to this definition")

ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant

Implements the ConstantDataAttributeId.

Variables:

- **group\_id** – Get ConstantDatasId

- **attribute\_id** – Get the data id (csc.model.DataId)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.ConstantDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId")_, _group\_id:[csc.update.ConstantDatasId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId "csc.update.ConstantDatasId")_, _attribute\_id:[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId.__module__ "Permalink to this definition")_property_ attribute\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId.attribute_id "Permalink to this definition")_property_ group\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId.group_id "Permalink to this definition")_class_ csc.update.ConstantDatas [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas "Permalink to this definition")

ConstantDatas represents a node of constant datas. It is present in any place.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas.__module__ "Permalink to this definition")add\_data( _self:[csc.update.ConstantDatas](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas "csc.update.ConstantDatas")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _value:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") \| [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") \|numpy.ndarray\[numpy.float32\[3,1\]\]\|numpy.ndarray\[numpy.float32\[4,1\]\]\| [csc.math.Rotation](https://cascadeur.com/python-api/csc.html#csc.math.Rotation "csc.math.Rotation") \|numpy.ndarray\[numpy.float32\[3,3\]\]\|numpy.ndarray\[numpy.float32\[4,4\]\]\| [csc.math.Quaternion](https://cascadeur.com/python-api/csc.html#csc.math.Quaternion "csc.math.Quaternion") \| [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \|numpy.ndarray\[ [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\[3,1\]\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas.add_data "Permalink to this definition")

value: Data.Value

_class_ csc.update.ConstantDatasId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId "Permalink to this definition")

ConstantDatasId is a guid based id.
It is always equal to the group id, where the constant will be used.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.update.ConstantDatasId, arg0: csc.update.GroupId) -> None

2. \_\_init\_\_(self: csc.update.ConstantDatasId, arg0: str) -> None

3. \_\_init\_\_(self: csc.update.ConstantDatasId) -> None


\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId.__module__ "Permalink to this definition")_class_ csc.update.ConstantSettingAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttribute "Permalink to this definition")

ConstantSettingAttribute represents an attribute of a constant setting.
It’s always an output attribute.
It can be connected with data functions.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttribute.__module__ "Permalink to this definition")_class_ csc.update.ConstantSettingAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId "Permalink to this definition")

ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant

Implements the ConstantSettingAttributeId.

Variables:

- **group\_id** – Get ConstantSettingsId

- **attribute\_id** – Get csc.model.SettingId


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.ConstantSettingAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")_, _group\_id:[csc.update.ConstantSettingsId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId")_, _attribute\_id:[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId.__module__ "Permalink to this definition")_property_ attribute\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId.attribute_id "Permalink to this definition")_property_ group\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId.group_id "Permalink to this definition")_class_ csc.update.ConstantSettings [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings "Permalink to this definition")

ConstantSettings represents a node of constant settings. It is present in any place.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings.__module__ "Permalink to this definition")add\_setting( _self:[csc.update.ConstantSettings](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings "csc.update.ConstantSettings")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _value:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings.add_setting "Permalink to this definition")

value: Setting.Value

_class_ csc.update.ConstantSettingsId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId "Permalink to this definition")

ConstantSettingsId is a guid based id.
It is always equal to the group id, where the constant will be used.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.update.ConstantSettingsId, arg0: csc.update.GroupId) -> None

2. \_\_init\_\_(self: csc.update.ConstantSettingsId, arg0: str) -> None

3. \_\_init\_\_(self: csc.update.ConstantSettingsId) -> None


\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId.__module__ "Permalink to this definition")_class_ csc.update.ExternalProperties [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties "Permalink to this definition")

ExternalProperties represents a node of external properties.
(E.g. is this update called during interpolation or not)
It is represent in any place.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties.__module__ "Permalink to this definition")property\_outputs( _self:[csc.update.ExternalProperties](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties "csc.update.ExternalProperties")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.ExternalPropertyAttribute](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttribute "csc.update.ExternalPropertyAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties.property_outputs "Permalink to this definition")_class_ csc.update.ExternalPropertiesId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId "Permalink to this definition")

ExternalPropertiesId is a guid based id.
It is always equal to the group id, where the external property will be used.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.update.ExternalPropertiesId, arg0: csc.update.GroupId) -> None

2. \_\_init\_\_(self: csc.update.ExternalPropertiesId, arg0: str) -> None

3. \_\_init\_\_(self: csc.update.ExternalPropertiesId) -> None


\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId.__module__ "Permalink to this definition")_class_ csc.update.ExternalProperty [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "Permalink to this definition")

> ExternalProperty enum
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

AfterPhysics _=<ExternalProperty.AfterPhysics:5>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.AfterPhysics "Permalink to this definition")Fixation _=<ExternalProperty.Fixation:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.Fixation "Permalink to this definition")InterpolationType _=<ExternalProperty.InterpolationType:3>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.InterpolationType "Permalink to this definition")IsForwardKinematics _=<ExternalProperty.IsForwardKinematics:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.IsForwardKinematics "Permalink to this definition")IsInterpolation _=<ExternalProperty.IsInterpolation:4>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.IsInterpolation "Permalink to this definition")IsKey _=<ExternalProperty.IsKey:6>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.IsKey "Permalink to this definition")KinematicsType _=<ExternalProperty.KinematicsType:2>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.KinematicsType "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.update.ExternalProperty](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "csc.update.ExternalProperty")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.ExternalProperty](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "csc.update.ExternalProperty")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.update.ExternalProperty](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "csc.update.ExternalProperty")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__int__ "Permalink to this definition")\_\_members\_\_ _={'AfterPhysics':<ExternalProperty.AfterPhysics:5>,'Fixation':<ExternalProperty.Fixation:0>,'InterpolationType':<ExternalProperty.InterpolationType:3>,'IsForwardKinematics':<ExternalProperty.IsForwardKinematics:1>,'IsInterpolation':<ExternalProperty.IsInterpolation:4>,'IsKey':<ExternalProperty.IsKey:6>,'KinematicsType':<ExternalProperty.KinematicsType:2>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.update.ExternalProperty](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "csc.update.ExternalProperty")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty.value "Permalink to this definition")_class_ csc.update.ExternalPropertyAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttribute "Permalink to this definition")

ExternalPropertyAttribute represents an attribute of the external properties of the update.
It’s always an output attribute.
It is settings based and thus can be connected with setting functions or data functions activity.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttribute.__module__ "Permalink to this definition")_class_ csc.update.ExternalPropertyAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId "Permalink to this definition")

ExternalPropertyAttributeId is defined by the ExternalPropertiesId and the value of the ExternalProperty enum

Implements the ExternalPropertyAttributeId.

Variables:

- **node\_id** – Get GroupId

- **property** – Get ExternalProperty enum value


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.ExternalPropertyAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId")_, _node\_id:[csc.update.ExternalPropertiesId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId")_, _property:[csc.update.ExternalProperty](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperty "csc.update.ExternalProperty")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId.__module__ "Permalink to this definition")_property_ node\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId.node_id "Permalink to this definition")_property_ property [¶](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId.property "Permalink to this definition")_class_ csc.update.Group [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group "Permalink to this definition")

Group class

Variables:

**node** – overridden by name \|\| node, access node by name or id

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.__module__ "Permalink to this definition")add\_input( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.add_input "Permalink to this definition")add\_output( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.add_output "Permalink to this definition")constant\_datas( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[csc.update.ConstantDatas](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatas "csc.update.ConstantDatas") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.constant_datas "Permalink to this definition")

get virtual node to access constant datas

constant\_settings( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[csc.update.ConstantSettings](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettings "csc.update.ConstantSettings") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.constant_settings "Permalink to this definition")

get virtual node to access constant settings

create\_group( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.create_group "Permalink to this definition")delete\_node( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _node:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.delete_node "Permalink to this definition")group( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _nodes:[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")\]_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.group "Permalink to this definition")group\_id( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.group_id "Permalink to this definition")

create sub group

has\_node( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.has_node "Permalink to this definition")

check whether there is a child node with a given name

input\_interface\_node( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.input_interface_node "Permalink to this definition")interface\_input( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.interface_input "Permalink to this definition")interface\_inputs( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.interface_inputs "Permalink to this definition")

get group attributes as interface attributes

interface\_node( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _direction:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.interface_node "Permalink to this definition")

access the interface node

interface\_output( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.interface_output "Permalink to this definition")interface\_outputs( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.interface_outputs "Permalink to this definition")is\_root( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.is_root "Permalink to this definition")leaf\_children( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.leaf_children "Permalink to this definition")

get all leaf nodes (settings, datas, functions)

node( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.node "Permalink to this definition")

Overloaded function.

1. node(self: csc.update.Group, name: str) -> csc.update.Node

2. node(self: csc.update.Group, node: Union\[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId\]) -> csc.update.Node


node\_deep( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.node_deep "Permalink to this definition")

access node by name or id recursively

node\_with\_type( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _type\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.node_with_type "Permalink to this definition")

find node with name and type

node\_with\_type\_deep( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_, _type\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.node_with_type_deep "Permalink to this definition")

find node with name and type recursively

nodes( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.nodes "Permalink to this definition")

get all children (their children are not included)

output\_interface\_node( _self:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Group.output_interface_node "Permalink to this definition")_class_ csc.update.GroupAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "Permalink to this definition")

GroupAttributeId is defined by the GroupId and the guid-based id of the attribute.
Group attribute names and indeces can change, so they are provided with their own guid

Implements the GroupAttributeId.

Variables:

- **group\_id** – Get GroupId

- **attribute\_id** – Get csc.Guid - id of the attribute


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.GroupAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId")_, _group\_id:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _attribute\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId.__module__ "Permalink to this definition")_property_ attribute\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId.attribute_id "Permalink to this definition")_property_ group\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId.group_id "Permalink to this definition")_class_ csc.update.GroupId [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__annotations__ "Permalink to this definition")\_\_cmp\_\_( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg0:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__cmp__ "Permalink to this definition")\_\_eq\_\_( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg0:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__eq__ "Permalink to this definition")\_\_hash\_\_( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__hash__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.update.GroupId, arg0: str) -> None

2. \_\_init\_\_(self: csc.update.GroupId) -> None


\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _arg0:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__ne__ "Permalink to this definition")\_\_str\_\_( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.__str__ "Permalink to this definition")is\_null( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.is_null "Permalink to this definition")_static_ null()→[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.null "Permalink to this definition")to\_string( _self:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.GroupId.to_string "Permalink to this definition")_class_ csc.update.HierarchyUpdate [¶](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate "Permalink to this definition")

HierarchyUpdate class provides concrete operations with connections

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate.__module__ "Permalink to this definition")add\_connection( _self:[csc.update.HierarchyUpdate](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate "csc.update.HierarchyUpdate")_, _connection:[csc.update.Connection](https://cascadeur.com/python-api/csc.html#csc.update.Connection "csc.update.Connection")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate.add_connection "Permalink to this definition")remove\_connection( _self:[csc.update.HierarchyUpdate](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate "csc.update.HierarchyUpdate")_, _connection:[csc.update.Connection](https://cascadeur.com/python-api/csc.html#csc.update.Connection "csc.update.Connection")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.HierarchyUpdate.remove_connection "Permalink to this definition")_class_ csc.update.InterfaceAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "Permalink to this definition")

InterfaceAttribute represents a group attribute.
Can be potentially connected to any attribute.

Interface attribute can be:
1\. An attribute of input/output node inside the group
2\. An attribute of the group node itself, in the parent group layout (outside the group)
We will call this attributes “paired”. For each attribute there is a paired one. They have the same attribute ids and names.
Sometimes it’s easier to think of them as of one attribute that has 2 sides. But in terms of this class this are two separate objects.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute.__module__ "Permalink to this definition")group\_attribute\_id( _self:[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")_)→[csc.update.GroupAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute.group_attribute_id "Permalink to this definition")

get the group attribute id

other\_side( _self:[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute.other_side "Permalink to this definition")

Get the paired attribute (e.g. the other side of the attribute)

set\_name( _self:[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute.set_name "Permalink to this definition")

Rename the attribute

_class_ csc.update.InterfaceAttributeSide [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide "Permalink to this definition")

> InterfaceAttributeSide enumerable
>
> InterfaceSide - inside the group, GroupSide - when the group is a node

Members:

> InterfaceSide
>
> GroupSide

GroupSide _=<InterfaceAttributeSide.GroupSide:1>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.GroupSide "Permalink to this definition")InterfaceSide _=<InterfaceAttributeSide.InterfaceSide:0>_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.InterfaceSide "Permalink to this definition")\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__annotations__ "Permalink to this definition")\_\_eq\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__eq__ "Permalink to this definition")\_\_getstate\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__getstate__ "Permalink to this definition")\_\_hash\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__hash__ "Permalink to this definition")\_\_index\_\_( _self:[csc.update.InterfaceAttributeSide](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__index__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.InterfaceAttributeSide](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")_, _value:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__init__ "Permalink to this definition")\_\_int\_\_( _self:[csc.update.InterfaceAttributeSide](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__int__ "Permalink to this definition")\_\_members\_\_ _={'GroupSide':<InterfaceAttributeSide.GroupSide:1>,'InterfaceSide':<InterfaceAttributeSide.InterfaceSide:0>}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__members__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__module__ "Permalink to this definition")\_\_ne\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_, _other:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__ne__ "Permalink to this definition")\_\_repr\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__repr__ "Permalink to this definition")\_\_setstate\_\_( _self:[csc.update.InterfaceAttributeSide](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide "csc.update.InterfaceAttributeSide")_, _state:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__setstate__ "Permalink to this definition")\_\_str\_\_( _self:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.__str__ "Permalink to this definition")_property_ name [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.name "Permalink to this definition")_property_ value [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttributeSide.value "Permalink to this definition")_class_ csc.update.InterfaceId [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId "Permalink to this definition")

InterfaceId is defined by the GroupId and the direction type of the node - input or output connection node.

Implements the InterfaceId.

Variables:

- **group\_id** – Get GroupId

- **direction** – Get direction type (csc.Direction)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.InterfaceId](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId "csc.update.InterfaceId")_, _group\_id:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_, _direction:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId.__module__ "Permalink to this definition")_property_ direction [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId.direction "Permalink to this definition")_property_ group\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId.group_id "Permalink to this definition")_class_ csc.update.InterfaceNode [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "Permalink to this definition")

InterfaceNode is a node inside the group that represents its connections with the ouside nodes.
Its attributes are csc.update.InterfaceAttributes

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.__module__ "Permalink to this definition")add\_attribute( _self:[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.add_attribute "Permalink to this definition")direction( _self:[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")_)→[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.direction "Permalink to this definition")

-\> csc.DirectionValue

interface\_attributes( _self:[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.interface_attributes "Permalink to this definition")

-\> InterfaceAttribute\[\]

move\_attribute( _self:[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")_, _attribute:[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")_, _position:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.move_attribute "Permalink to this definition")

attribute: InterfaceAttribute \| position: int

remove\_attribute( _self:[csc.update.InterfaceNode](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode "csc.update.InterfaceNode")_, _attribute:[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceNode.remove_attribute "Permalink to this definition")

attribute: InterfaceAttribute

_class_ csc.update.Node [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node "Permalink to this definition")

Node class represents a generic Node and implements methods that are common for all nodes

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.__module__ "Permalink to this definition")attributes( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _d:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.attributes "Permalink to this definition")

array of all input and output attributes

equal\_to( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _arg0:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.equal_to "Permalink to this definition")full\_name( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.full_name "Permalink to this definition")

name with all the parent nodes

has\_input( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.has_input "Permalink to this definition")

check if there is an input with such a name

has\_output( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.has_output "Permalink to this definition")

check if there is an output with such a name

id( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") \| [csc.update.InterfaceId](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId "csc.update.InterfaceId") \| [csc.update.ExternalPropertiesId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") \| [csc.update.ConstantDatasId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId "csc.update.ConstantDatasId") \| [csc.update.ConstantSettingsId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") \| [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") \| [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") \| [csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") \| [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.id "Permalink to this definition")

get uniqui id

input( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.input "Permalink to this definition")

shortcut if node has only one input attribute

inputs( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.inputs "Permalink to this definition")

array of all the inputes attributes

is\_active( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.is_active "Permalink to this definition")

check whether it is active for current actualities states
(see Additional functionality in csc.update.UpdateEditor)

is\_fictive( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.is_fictive "Permalink to this definition")

whether it is a fictive node (constants, inputs, outputs of a group or external properties)

name( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.name "Permalink to this definition")

get name

output( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.output "Permalink to this definition")

shortcut if node has only one output attribute

outputs( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.outputs "Permalink to this definition")

array of all the outputs attributes

parent\_group( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→domain::update\_editor::Group [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.parent_group "Permalink to this definition")

return parent group (where this group node is located)

parent\_object( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_)→domain::update\_editor::Object [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.parent_object "Permalink to this definition")

return object of the node. Will return null if this is not an update group

set\_name( _self:[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Node.set_name "Permalink to this definition")

rename node

_class_ csc.update.NodeAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "Permalink to this definition")

NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute.

Variables:

**disconnect** – overridden method with parameter attribute: NodeAttribute

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.__module__ "Permalink to this definition")connect( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_, _attribute:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.connect "Permalink to this definition")

attribute: NodeAttribute

connected\_attributes( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.connected_attributes "Permalink to this definition")

-\> NodeAttribute\[\]

connected\_leaves( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_, _get\_only\_first:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.connected_leaves "Permalink to this definition")

-\> NodeAttribute\[\]

connected\_leaves\_in\_undirected\_graph( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.connected_leaves_in_undirected_graph "Permalink to this definition")direction( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction") [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.direction "Permalink to this definition")

-\> csc.DirectionValue

disconnect( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.disconnect "Permalink to this definition")

Overloaded function.

1. disconnect(self: csc.update.NodeAttribute) -> None

2. disconnect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) -> None


id( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[csc.update.RegularFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") \| [csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") \| [csc.update.RegularDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") \| [csc.update.ActualityAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") \| [csc.update.SettingFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") \| [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") \| [csc.update.GroupAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") \| [csc.update.ExternalPropertyAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") \| [csc.update.ConstantDataAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") \| [csc.update.ConstantSettingAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.id "Permalink to this definition")

-\> AttributeId

is\_active( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.is_active "Permalink to this definition")name( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.name "Permalink to this definition")node( _self:[csc.update.NodeAttribute](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute "csc.update.NodeAttribute")_)→domain::update\_editor::Node [¶](https://cascadeur.com/python-api/csc.html#csc.update.NodeAttribute.node "Permalink to this definition")

-\> Node

_class_ csc.update.Object [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object "Permalink to this definition")

Object class represents an object node. Functionality is limited - it’s better to use update group node instead.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.__module__ "Permalink to this definition")add\_input( _self:[csc.update.Object](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.add_input "Permalink to this definition")

-\> InterfaceAttribute

add\_output( _self:[csc.update.Object](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.InterfaceAttribute](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceAttribute "csc.update.InterfaceAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.add_output "Permalink to this definition")

-\> InterfaceAttribute

object\_id( _self:[csc.update.Object](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object")_)→[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.object_id "Permalink to this definition")root\_group( _self:[csc.update.Object](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object")_)→domain::update\_editor::UpdateGroup [¶](https://cascadeur.com/python-api/csc.html#csc.update.Object.root_group "Permalink to this definition")

-\> UpdateGroup

_class_ csc.update.ObjectGroup [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "Permalink to this definition")

ObjectGroup class represents object group node

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.__module__ "Permalink to this definition")create\_object( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.create_object "Permalink to this definition")

Overloaded function.

1. create\_object(self: csc.update.ObjectGroup, name: str) -> csc.update.Object

2. create\_object(self: csc.update.ObjectGroup, name: str, id: csc.model.ObjectId) -> csc.update.Object


create\_sub\_object\_group( _self:[csc.update.ObjectGroup](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.ObjectGroup](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup") [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.create_sub_object_group "Permalink to this definition")

-\> ObjectGroup

object\_groups( _self:[csc.update.ObjectGroup](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.ObjectGroup](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.object_groups "Permalink to this definition")

-\> ObjectGroup{}

objects( _self:[csc.update.ObjectGroup](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.Object](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup.objects "Permalink to this definition")

-\> Object{}

_class_ csc.update.RegularData [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "Permalink to this definition")

RegularData class represents a node of a data.

Variables:

- **value** – overridden method by frame, get data value (requires frame if Animation data)

- **set\_value** – overridden method by frame, set data value (requires frame if Animation data)


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.__module__ "Permalink to this definition")actuality( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[csc.update.ActualityAttribute](https://cascadeur.com/python-api/csc.html#csc.update.ActualityAttribute "csc.update.ActualityAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.actuality "Permalink to this definition")

output attribute, that provides actuality status

attribute( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _d:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[csc.update.RegularDataAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.attribute "Permalink to this definition")

get attribute by direction

data\_id( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.data_id "Permalink to this definition")get\_apply\_euler\_filter( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.get_apply_euler_filter "Permalink to this definition")

get apply euler filter

get\_explicit\_linear( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.get_explicit_linear "Permalink to this definition")

get explicit linear

get\_lerp\_mode( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[csc.model.LerpMode](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.get_lerp_mode "Permalink to this definition")

get lerp mode

input( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[csc.update.RegularDataAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.input "Permalink to this definition")

input attribute

is\_actual( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.is_actual "Permalink to this definition")

check if this data is set to actual (see Additional functionality in csc.update.UpdateEditor)

mode( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[csc.model.DataMode](https://cascadeur.com/python-api/csc.html#csc.model.DataMode "csc.model.DataMode") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.mode "Permalink to this definition")

Check if data is Animation or Static

output( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[csc.update.RegularDataAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute "csc.update.RegularDataAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.output "Permalink to this definition")

output attribute

remove\_period( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.remove_period "Permalink to this definition")

in interpolation, remove period

set\_actual( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _act:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_actual "Permalink to this definition")

set this data as actual (see Additional functionality in csc.update.UpdateEditor)

set\_apply\_euler\_filter( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _apply\_euler\_filter:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_apply_euler_filter "Permalink to this definition")

set apply euler filter

set\_description\_value( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_description_value "Permalink to this definition")

setDescriptionValue

set\_explicit\_linear( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _explicit\_linear:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_explicit_linear "Permalink to this definition")

set explicit linear

set\_lerp\_mode( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _mode:[csc.model.LerpMode](https://cascadeur.com/python-api/csc.html#csc.model.LerpMode "csc.model.LerpMode")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_lerp_mode "Permalink to this definition")

can be slerp for Vector3 datas. Used in interpolation

set\_period( _self:[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")_, _period:[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_period "Permalink to this definition")

in interpolation, if perion is provided, the data will be “fixed” to provide smoothness

set\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.set_value "Permalink to this definition")

Overloaded function.

1. set\_value(self: csc.update.RegularData, v: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]) -> None

2. set\_value(self: csc.update.RegularData, v: Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\], frame: int) -> None


value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularData.value "Permalink to this definition")

Overloaded function.

1. value(self: csc.update.RegularData) -> Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]

2. value(self: csc.update.RegularData, frame: int) -> Union\[bool, int, float, numpy.ndarray\[numpy.float32\[3, 1\]\], numpy.ndarray\[numpy.float32\[4, 1\]\], csc.math.Rotation, numpy.ndarray\[numpy.float32\[3, 3\]\], numpy.ndarray\[numpy.float32\[4, 4\]\], csc.math.Quaternion, str, numpy.ndarray\[bool\[3, 1\]\]\]


_class_ csc.update.RegularDataAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute "Permalink to this definition")

RegularDataAttribute represents an attribute of a regular data.
It can be connected with data functions.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttribute.__module__ "Permalink to this definition")_class_ csc.update.RegularDataAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId "Permalink to this definition")

RegularDataAttributeId is defined by the data id.
Data only has one input and one output attributes.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId.__init__ "Permalink to this definition")

Overloaded function.

1. \_\_init\_\_(self: csc.update.RegularDataAttributeId, arg0: str) -> None

2. \_\_init\_\_(self: csc.update.RegularDataAttributeId, arg0: csc.model.DataId) -> None

3. \_\_init\_\_(self: csc.update.RegularDataAttributeId) -> None


\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularDataAttributeId.__module__ "Permalink to this definition")_class_ csc.update.RegularFunction [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "Permalink to this definition")

RegularFunction class represents a node that calculates same operation, done with datas.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.__module__ "Permalink to this definition")activity( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_)→[csc.update.ActivityAttribute](https://cascadeur.com/python-api/csc.html#csc.update.ActivityAttribute "csc.update.ActivityAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.activity "Permalink to this definition")

activity attributes

arguments( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.RegularFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.arguments "Permalink to this definition")

its input arguments

decrease\_vector( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _direction:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.decrease_vector "Permalink to this definition")

method that decreases vector attribute

func\_id( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_)→[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.func_id "Permalink to this definition")

its id

increase\_vector( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _direction:[csc.Direction](https://cascadeur.com/python-api/csc.html#csc.Direction "csc.Direction")_)→[csc.update.RegularFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.increase_vector "Permalink to this definition")

method that increases vector attribute

is\_convertible( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.is_convertible "Permalink to this definition")

check whether this function will make it to the resulting data graph

remove\_attribute( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_, _attribute:[csc.update.RegularFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.remove_attribute "Permalink to this definition")

method that removes one in vector attribute

resize\_vector\_inputs( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_, _count:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.resize_vector_inputs "Permalink to this definition")

method that resizes input vector attribute

resize\_vector\_outputs( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_, _count:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.resize_vector_outputs "Permalink to this definition")

method that resizes output vector attribute

results( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.RegularFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute "csc.update.RegularFunctionAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.results "Permalink to this definition")

its output arguments

set\_convertible( _self:[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")_, _convertible:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction.set_convertible "Permalink to this definition")

set the state of the function, whether it will be used or not

_class_ csc.update.RegularFunctionAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute "Permalink to this definition")

RegularFunctionAttribute represents an attribute of a data function.
It can be connected with data attributes.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttribute.__module__ "Permalink to this definition")_class_ csc.update.RegularFunctionAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId "Permalink to this definition")

RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute

Variables:

- **function\_id** – Get SettingFunctionId

- **attribute\_id** – Get name of the attribute


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.RegularFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId")_, _function\_id:[csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId")_, _attribute\_id:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId.__module__ "Permalink to this definition")_property_ attribute\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId.attribute_id "Permalink to this definition")_property_ function\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunctionAttributeId.function_id "Permalink to this definition")_class_ csc.update.SettingData [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData "Permalink to this definition")

SettingData class represents a node that calculates same operation, done with settings.
It can comprise bool or std::int8\_t (Min: -128, Max: 127) value, please be carefull when you set this.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.__module__ "Permalink to this definition")data\_id( _self:[csc.update.SettingData](https://cascadeur.com/python-api/csc.html#csc.update.SettingData "csc.update.SettingData")_)→[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.data_id "Permalink to this definition")

get setting unique id

output( _self:[csc.update.SettingData](https://cascadeur.com/python-api/csc.html#csc.update.SettingData "csc.update.SettingData")_)→[csc.update.SettingDataAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingDataAttribute "csc.update.SettingDataAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.output "Permalink to this definition")

output attribute

set\_value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.set_value "Permalink to this definition")

Overloaded function.

1. set\_value(self: csc.update.SettingData, value: Union\[bool, int\]) -> None


> set setting value

2. set\_value(self: csc.update.SettingData, value: Union\[bool, int\], frame: int) -> None


> set setting value


value( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingData.value "Permalink to this definition")

Overloaded function.

1. value(self: csc.update.SettingData) -> Union\[bool, int\]


> get setting value

2. value(self: csc.update.SettingData, frame: int) -> Union\[bool, int\]


> get setting value


_class_ csc.update.SettingDataAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingDataAttribute "Permalink to this definition")

SettingDataAttribute represents an attribute of a setting.
It can be connected with setting functions.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingDataAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingDataAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingDataAttribute.__module__ "Permalink to this definition")_class_ csc.update.SettingFunction [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "Permalink to this definition")

SettingFunction class

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.__module__ "Permalink to this definition")arguments( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.SettingFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.arguments "Permalink to this definition")

input attributes

decrease\_input\_vector( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_, _index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.decrease_input_vector "Permalink to this definition")

method that decreases input vector attribute

func\_id( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_)→[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.func_id "Permalink to this definition")

its id

increase\_input\_vector( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_, _index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.update.SettingFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.increase_input_vector "Permalink to this definition")

method that increases input vector attribute

is\_convertible( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.is_convertible "Permalink to this definition")

check whether this function will make it to the resulting setting graph

remove\_attribute( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_, _attribute:[csc.update.SettingFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.remove_attribute "Permalink to this definition")

method that removes one in input vector attribute

resize\_vector\_inputs( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_, _index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _count:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.resize_vector_inputs "Permalink to this definition")

method that resizes input vector attribute

results( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.update.SettingFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.results "Permalink to this definition")

output attributes

set\_convertible( _self:[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")_, _convertible:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction.set_convertible "Permalink to this definition")

set the state of the function, whether it will be used or not

_class_ csc.update.SettingFunctionAttribute [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "Permalink to this definition")

SettingFunctionAttribute represents an attribute of a setting function.
It can be connected with setting functions or data function activeness attributes.

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute.__module__ "Permalink to this definition")is\_out\_true( _self:[csc.update.SettingFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute.is_out_true "Permalink to this definition")output\_id( _self:[csc.update.SettingFunctionAttribute](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute "csc.update.SettingFunctionAttribute")_)→[csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttribute.output_id "Permalink to this definition")_class_ csc.update.SettingFunctionAttributeId [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId "Permalink to this definition")

SettingFunctionAttributeId is defined by the SettingFunctionId and the index of the attribute

Implements the SettingFunctionAttributeId.

Variables:

- **function\_id** – Get SettingFunctionId

- **attribute\_index** – Get index of the attribute

- **attribute\_sub\_index** – Get index of the attribute in array


\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId.__annotations__ "Permalink to this definition")\_\_init\_\_( _self:[csc.update.SettingFunctionAttributeId](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId")_, _function\_id:[csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId")_, _attribute\_index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_, _attribute\_sub\_index:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")=0_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId.__module__ "Permalink to this definition")_property_ attribute\_index [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId.attribute_index "Permalink to this definition")_property_ attribute\_sub\_index [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId.attribute_sub_index "Permalink to this definition")_property_ function\_id [¶](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunctionAttributeId.function_id "Permalink to this definition")_class_ csc.update.Update [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update "Permalink to this definition")

Update class represents the whole update editor

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.__module__ "Permalink to this definition")delete\_node( _self:[csc.update.Update](https://cascadeur.com/python-api/csc.html#csc.update.Update "csc.update.Update")_, _id:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") \| [csc.update.InterfaceId](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId "csc.update.InterfaceId") \| [csc.update.ExternalPropertiesId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") \| [csc.update.ConstantDatasId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId "csc.update.ConstantDatasId") \| [csc.update.ConstantSettingsId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") \| [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") \| [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") \| [csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") \| [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.delete_node "Permalink to this definition")get\_node\_by\_id( _self:[csc.update.Update](https://cascadeur.com/python-api/csc.html#csc.update.Update "csc.update.Update")_, _id:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId") \| [csc.update.InterfaceId](https://cascadeur.com/python-api/csc.html#csc.update.InterfaceId "csc.update.InterfaceId") \| [csc.update.ExternalPropertiesId](https://cascadeur.com/python-api/csc.html#csc.update.ExternalPropertiesId "csc.update.ExternalPropertiesId") \| [csc.update.ConstantDatasId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantDatasId "csc.update.ConstantDatasId") \| [csc.update.ConstantSettingsId](https://cascadeur.com/python-api/csc.html#csc.update.ConstantSettingsId "csc.update.ConstantSettingsId") \| [csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId") \| [csc.model.HyperedgeId](https://cascadeur.com/python-api/csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") \| [csc.model.DataId](https://cascadeur.com/python-api/csc.html#csc.model.DataId "csc.model.DataId") \| [csc.model.SettingFunctionId](https://cascadeur.com/python-api/csc.html#csc.model.SettingFunctionId "csc.model.SettingFunctionId") \| [csc.model.SettingId](https://cascadeur.com/python-api/csc.html#csc.model.SettingId "csc.model.SettingId")_)→[csc.update.Node](https://cascadeur.com/python-api/csc.html#csc.update.Node "csc.update.Node") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.get_node_by_id "Permalink to this definition")get\_object\_by\_id( _self:[csc.update.Update](https://cascadeur.com/python-api/csc.html#csc.update.Update "csc.update.Update")_, _arg0:[csc.model.ObjectId](https://cascadeur.com/python-api/csc.html#csc.model.ObjectId "csc.model.ObjectId")_)→[csc.update.Object](https://cascadeur.com/python-api/csc.html#csc.update.Object "csc.update.Object") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.get_object_by_id "Permalink to this definition")root( _self:[csc.update.Update](https://cascadeur.com/python-api/csc.html#csc.update.Update "csc.update.Update")_)→[csc.update.ObjectGroup](https://cascadeur.com/python-api/csc.html#csc.update.ObjectGroup "csc.update.ObjectGroup") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.root "Permalink to this definition")

-\> ObjectGroup

ungroup( _self:[csc.update.Update](https://cascadeur.com/python-api/csc.html#csc.update.Update "csc.update.Update")_, _group:[csc.update.Group](https://cascadeur.com/python-api/csc.html#csc.update.Group "csc.update.Group")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/csc.html#csc.update.Update.ungroup "Permalink to this definition")_class_ csc.update.UpdateGroup [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "Permalink to this definition")

UpdateGroup class represents update group node

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.__init__ "Permalink to this definition")\_\_module\_\_ _='csc.update'_ [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.__module__ "Permalink to this definition")create\_regular\_data( _self:csc.update.UpdateGroup,name:str,value:Union\[bool,int,float,numpy.ndarray\[numpy.float32\[3,1\]\],numpy.ndarray\[numpy.float32\[4,1\]\],csc.math.Rotation,numpy.ndarray\[numpy.float32\[3,3\]\],numpy.ndarray\[numpy.float32\[4,4\]\],csc.math.Quaternion,str,numpy.ndarray\[bool\[3,1\]\]\],mode:csc.model.DataMode=<DataMode.Static:0>_)→[csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.create_regular_data "Permalink to this definition")create\_regular\_function( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _function:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.create_regular_function "Permalink to this definition")create\_setting\_data( _self:csc.update.UpdateGroup,name:str,value:Union\[bool,int\],mode:csc.model.SettingMode=<SettingMode.Static:0>_)→[csc.update.SettingData](https://cascadeur.com/python-api/csc.html#csc.update.SettingData "csc.update.SettingData") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.create_setting_data "Permalink to this definition")create\_setting\_function( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _function\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.create_setting_function "Permalink to this definition")create\_sub\_update\_group( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_, _arg0:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_)→[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.create_sub_update_group "Permalink to this definition")create\_sub\_update\_group2( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _group\_id:[csc.update.GroupId](https://cascadeur.com/python-api/csc.html#csc.update.GroupId "csc.update.GroupId")_)→[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.create_sub_update_group2 "Permalink to this definition")

-\> UpdateGroup

external\_properties( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_)→[csc.update.ExternalProperties](https://cascadeur.com/python-api/csc.html#csc.update.ExternalProperties "csc.update.ExternalProperties") [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.external_properties "Permalink to this definition")

-\> ExternalProperties

groups( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.groups "Permalink to this definition")

-\> UpdateGroup{}

regular\_datas( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.RegularData](https://cascadeur.com/python-api/csc.html#csc.update.RegularData "csc.update.RegularData")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.regular_datas "Permalink to this definition")

-\> RegularData{}

regular\_functions( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.RegularFunction](https://cascadeur.com/python-api/csc.html#csc.update.RegularFunction "csc.update.RegularFunction")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.regular_functions "Permalink to this definition")

-\> RegularFunction{}

setting\_functions( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.SettingFunction](https://cascadeur.com/python-api/csc.html#csc.update.SettingFunction "csc.update.SettingFunction")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.setting_functions "Permalink to this definition")

-\> SettingFunction{}

settings\_datas( _self:[csc.update.UpdateGroup](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup "csc.update.UpdateGroup")_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.update.SettingData](https://cascadeur.com/python-api/csc.html#csc.update.SettingData "csc.update.SettingData")\] [¶](https://cascadeur.com/python-api/csc.html#csc.update.UpdateGroup.settings_datas "Permalink to this definition")

-\> SettingsData{}