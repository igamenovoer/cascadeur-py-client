---
source_url: https://cascadeur.com/python-api/csc.html
html_file: 60c8cf5e3e5950beaef8ff0a113d9830.html
module: csc
---

# CSC 

## csc The main Cascadeur python module. 

csc.Guid csc.math.Quaternion 
Quaternion class csc.math.Rotation 
Rotation class csc.math.transform_point (*args, **kwargs) Overloaded function. csc.math.inverse_transform_point (transform, ...) -> Vector3f csc.math.basic_transform_from_triangle (triangle) -> csc.math.OrthogonalTransform csc.math.project_point_on_basic_line (...) -> Vector3f csc.math.euler_angles_to_quaternion_x_y_z (...) -> Quaternionf csc.math.modify_position_by_matrix (matrix, ...) -> Vector3f csc.math.transforms_difference (...) -> csc.math.OrthogonalTransform csc.math.transform_point (*args, **kwargs) Overloaded function. csc.math.get_m3f_diag (matrix) -> Vector3f csc.physics.PosMass 
PosMass class csc.physics.inertia_tensor (mass_and_poses, ...) -> Matrix3f csc.DirectionValue 
DirectionValue enumeration csc.Direction 
Direction class Implements direction. csc.Version 
Version class csc.SystemVariables csc.math.ScaledTransform 
ScaledTransform class csc.math.OrthogonalTransform 
OrthogonalTransform class csc.math.Triangle 
Triangle class csc.math.SizesInterval 
SizesInterval class csc.parts.Type Type of the parts, enum csc.parts.Info 
Info class csc.parts.GroupInfo 
GroupInfo class csc.parts.Buffer 
Buffer class 
Direction class
Implements direction. value ( csc.DirectionValue ) –
> 
DirectionValue enumeration
> In, Out, Unknown

DirectionValue enumeration
In, Out, Unknown Members:
> In
> Out
> Unknown

In Out Unknown Overloaded function.
1. __init__(self: csc.Guid, arg0: str) -> None
2. __init__(self: csc.Guid) -> None

__init__(self: csc.Guid, arg0: str) -> None __init__(self: csc.Guid) -> None 
Version class Implements Version.
- major – Get set int
- minor – Get set int
- patch – Get set int

major – Get set int minor – Get set int patch – Get set int
## csc.tools The Cascadeur python module provides tools. 

csc.tools.ActivateDeactivate 
ActivateDeactivate class csc.tools.selection.Mode 
Mode enumeration csc.tools.selection.Group 
Group class csc.tools.selection.Core 
Core class csc.tools.SelectionGroups 
SelectionGroups class csc.tools.mirror.Core Mirror tool 
core class csc.tools.MirrorTool Mirror 
tool class csc.tools.JointData csc.tools.ObjectKey csc.tools.DataKey csc.tools.RiggingModeTool Rigging mode 
tool class csc.tools.attractor.SpaceMode attractor::Mode enum csc.tools.attractor.ArgsMode attractor::Mode enum csc.tools.attractor.GSRotationAxis GeneralSettings::RotationAxis enum csc.tools.attractor.GSAxisFlag GeneralSettings::RotationAxis enum csc.tools.attractor.GSAxisIndex GeneralSettings::RotationAxis enum csc.tools.attractor.GSPhysicsType GeneralSettings::RotationAxis enum csc.tools.attractor.AttractorGeneralSettings csc.tools.attractor.Args csc.tools.attractor.attract (args) csc.tools.AttractorTool Attractor 
tool class csc.tools.AutoPhysicTool Auto physics 
tool class csc.tools.AnimationPointsTypes Class of basic types of points which physics tools and change through animation for target center of mass it contains csc.tools.CollisionInfoForPoint Structure with which the point collides. csc.tools.BallisticTrajectory 
BallisticTrajectory class csc.tools.Trajectory 
Trajectory class csc.tools.AutoPosingTool 
AutoPosingTool class csc.tools.AnimationUnbakingTool 
AnimationUnbakingTool class csc.tools.RenderParameters Parameters for rendering csc.tools.RenderToFile Render to file 
tool class 
ActivateDeactivate class Class of basic types of points which physics tools and change through animation
for target center of mass it contains get_fulcrum_points – all fulcrum point with collision
get_fixed_points – all points need to fix with collision
get_local_fixed_points – points that should keep local coordinates after apply
get_collision_surface_points – collision points with normal type
get_collision_pin_points – collision points with pin type
get_collision_fixed_points – collision points with fulcrum groups
get_fulcrum_floor_points – points collide with only floor
get_fixed_floor_points – points collide with only floor and fulcrum groups
get_frame_collision_info_points – collision info about points Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, Dict[csc.model.ObjectId, CollisionInfoForPoint]] Dict[frame number, set of points] Dict[frame number, set of points] Dict[frame number, set of points] 
AnimationUnbakingTool class Attractor 
tool class Auto physics 
tool class 
AutoPosingTool class 
BallisticTrajectory class Structure with which the point collides.
When used, it is assumed that the normal goes from other to point. Vector3d csc.model.ObjectId double Vector3d Mirror 
tool class Parameters for rendering Render to file 
tool class Rigging mode 
tool class 
SelectionGroups class 
SelectionGroups class Class of basic types of points which physics tools use and dont change through animation
for target center of mass it contains get_main_points – all points that can be associated with center of mass
get_direction_controllers – all direction controller associated with center of mass
get_interpolation_group – all points that should be interpolated and use instead direction controller in apply set[ModelId] set[ModelId] set[ModelId] 
Trajectory class 
Core class pbdoc( -> Group )pbdoc pbdoc( -> std::map<GroupIndex, Group> )pbdoc 
Group class
- objects – std::set<ModelObjectId>
- pivot – ModelObjectId

objects – std::set<ModelObjectId> pivot – ModelObjectId Overloaded function.
1. __init__(self: csc.tools.selection.Group) -> None
2. __init__(self: csc.tools.selection.Group, arg0: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], arg1: Union[csc.model.ObjectId, csc.domain.Tool_object_id]) -> None

__init__(self: csc.tools.selection.Group) -> None __init__(self: csc.tools.selection.Group, arg0: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], arg1: Union[csc.model.ObjectId, csc.domain.Tool_object_id]) -> None
> 
Mode enumeration
> SetGroup, SingleSelect, MultiSelect

Mode enumeration SetGroup, SingleSelect, MultiSelect Members:
> SetGroup
> SingleSelect
> MultiSelect

SetGroup SingleSelect MultiSelect Mirror tool 
core class
> attractor::Mode enum
> Previous, Next, Inertial, InverseInertial, Average, Interpolation

attractor::Mode enum Previous, Next, Inertial, InverseInertial, Average, Interpolation Members:
> Previous
> Next
> Inertial
> InverseInertial
> Average
> Interpolation

Previous Next Inertial InverseInertial Average Interpolation
> GeneralSettings::RotationAxis enum
> X, Y, Z, XYZ, Empty

GeneralSettings::RotationAxis enum X, Y, Z, XYZ, Empty Members:
> X
> Y
> Z
> XYZ
> Empty

X Y Z XYZ Empty
> GeneralSettings::RotationAxis enum
> X, Y, Z

GeneralSettings::RotationAxis enum X, Y, Z Members:
> X
> Y
> Z

X Y Z
> GeneralSettings::RotationAxis enum
> FrameRelax, InterpolationRelax

GeneralSettings::RotationAxis enum FrameRelax, InterpolationRelax Members:
> FrameRelax
> InterpolationRelax

FrameRelax InterpolationRelax
> GeneralSettings::RotationAxis enum
> X, Y, Z, Whole, Empty

GeneralSettings::RotationAxis enum X, Y, Z, Whole, Empty Members:
> X
> Y
> Z
> Whole
> Empty

X Y Z Whole Empty
> attractor::Mode enum
> Global, Local

attractor::Mode enum Global, Local Members:
> Global
> Local

Global Local
## csc.view The Cascadeur python module provides basic methods to operate GUI. 

csc.view.StandardButton StandardButton enum csc.view.DialogButton 
DialogButton class csc.view.DialogManager 
DialogManager class csc.view.FileDialogManager 
FileDialogManager class csc.view.Scene 
SceneView class csc.view.AnimationBoundary 
AnimationBoundary class csc.view.CameraType CameraType enumerable csc.view.SphericalCameraStruct 
SphericalCameraStruct class csc.view.Camera Domain Spherical 
camera class csc.view.ViewportDomain Domain 
Viewport class csc.view.Viewport 
Viewport class 
AnimationBoundary class Set first frame of animation Set first visible frame of animation Set last frame of animation Set last visible frame of animation Domain Spherical 
camera class
> CameraType enumerable

CameraType enumerable Members:
> ISOMETRIC
> PERSPECTIVE

ISOMETRIC PERSPECTIVE 
DialogButton class Overloaded function.
1. __init__(self: csc.view.DialogButton) -> None
2. __init__(self: csc.view.DialogButton, arg0: str) -> None
3. __init__(self: csc.view.DialogButton, text: str, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None
4. __init__(self: csc.view.DialogButton, arg0: csc.view.StandardButton) -> None
5. __init__(self: csc.view.DialogButton, button: csc.view.StandardButton, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None

__init__(self: csc.view.DialogButton) -> None __init__(self: csc.view.DialogButton, arg0: str) -> None __init__(self: csc.view.DialogButton, text: str, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None __init__(self: csc.view.DialogButton, arg0: csc.view.StandardButton) -> None __init__(self: csc.view.DialogButton, button: csc.view.StandardButton, handler: Callable, force_active_focus: bool = False, accent: bool = False) -> None -> string 
DialogManager class Overloaded function.
1. show_input_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable) -> None
2. show_input_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable, arg4: Callable) -> None

show_input_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable) -> None show_input_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: Callable, arg4: Callable) -> None 
FileDialogManager class 
SceneView class Returns active csc.view.Viewport -> csc.view.AnimationBoundary Return current csc.domain.Scene Provides all of csc.view.Viewport objects 
SphericalCameraStruct class
- target – Get set Vector3f
- position – Get set Vector3f
- type – Get set CameraType

target – Get set Vector3f position – Get set Vector3f type – Get set CameraType
> StandardButton enum
> This enumerates the basic types of standard buttons.
> Ok, Cancel, Yes, No

StandardButton enum This enumerates the basic types of standard buttons.
Ok, Cancel, Yes, No Members:
> Ok
> Cancel
> No
> Yes

Ok Cancel No Yes 
Viewport class Domain 
Viewport class
> ViewportMode enumerable

ViewportMode enumerable Members:
> View
> AutoPosing
> PointController
> Controller
> Joint
> Mesh
> Rigging
> ModeCount

View AutoPosing PointController Controller Joint Mesh Rigging ModeCount
## csc.view.camera_utils The Cascadeur python module provides utulity methods to manage viewport cameras. 

csc.view.camera_utils.CameraData 
CameraData class 
CameraData class
## csc.app The Cascadeur python module provides basic methods to operate GUI. 

csc.app.Analytics 
Analytics class csc.app.ActionManager 
ActionManager class csc.app.DataSourceManager 
DataSourceManager class csc.app.SettingsManager 
SettingsManager class csc.app.SceneManager 
SceneManager class csc.app.SceneTool 
SceneTool class csc.app.CascadeurTool 
CascadeurTool class csc.app.ToolsManager 
ToolsManager class csc.app.Application 
Application class csc.app.ProjectLoader 
ProjectLoader class csc.app.StatusManager 
StatusManager class csc.app.SimpleStatusInformer 
SimpleStatusInformer class 
ActionManager class 
Analytics class 
Application class 
CascadeurTool class 
DataSourceManager class Load scene and all additional datas (selection groups etc)
Example:
ds_m = csc.app.get_application().get_data_source_manager()
ds_m.load_scene(file_path) Overloaded function.
1. save_current_scene(self: csc.app.DataSourceManager, handler: Callable[[bool], None]) -> None
2. save_current_scene(self: csc.app.DataSourceManager) -> None

save_current_scene(self: csc.app.DataSourceManager, handler: Callable[[bool], None]) -> None save_current_scene(self: csc.app.DataSourceManager) -> None Overloaded function.
1. save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene, handler: Callable[[bool], None]) -> None
2. save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene) -> None

save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene, handler: Callable[[bool], None]) -> None save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene) -> None 
ProjectLoader class Provides methods to load domain scene. Minimal Load. This method doesn't load selection groups, control picker and etc.
Better use data_source_manager's load_scene method.
Example:
csc.app.ProjectLoader.load_from(file_path, scene) 
SceneManager class 
SceneTool class 
SettingsHandler class 
SettingsManager class 
SimpleStatusInformer class 
StatusInformer class 
StatusManager class 
ToolsManager class
## csc.parts The Cascadeur python module provides basic methods to operate scene parts. 

csc.parts.Type Type of the parts, enum csc.parts.Info 
Info class csc.parts.GroupInfo 
GroupInfo class csc.parts.SceneClipboard 
SceneClipboard class csc.parts.Buffer 
Buffer class 
Buffer class Provides methods to operate parts of the scene. 
GroupInfo class
- type – Get set Data::Id{}
- name – Get set Setting::Id{}
- path – Get set HyperedgeId{}
- object_id – Get set SettingFunctionId{}

type – Get set Data::Id{} name – Get set Setting::Id{} path – Get set HyperedgeId{} object_id – Get set SettingFunctionId{} 
Info class
- type – Get csc.parts.Type
- name – Get string
- path – Get string
- object_id – Get csc.model.ObjectId

type – Get csc.parts.Type name – Get string path – Get string object_id – Get csc.model.ObjectId 
SceneClipboard class Provides methods to operate parts of the scene.
> Type of the parts, enum
> Elementary: includes only regular and setting functions + regular and setting data + connections that link them
> UpdateGroup: sub update groups and their elementary entities + connections that link them
> Object: includes all related entities of some object
> ObjectGroup: includes all objects and sub object groups and all related entities
> SelectedObjects: selected objects from different groups

Type of the parts, enum Elementary: includes only regular and setting functions + regular and setting data + connections that link them
UpdateGroup: sub update groups and their elementary entities + connections that link them
Object: includes all related entities of some object
ObjectGroup: includes all objects and sub object groups and all related entities
SelectedObjects: selected objects from different groups Members:
> Elementary
> UpdateGroup
> Object
> ObjectGroup
> SelectedObjects

Elementary UpdateGroup Object ObjectGroup SelectedObjects
## csc.external The Cascadeur python module provides basic api to external data formats. 

csc.external.fbx.ExtraDatas 
ExtraDatas class csc.external.fbx.FbxDatas 
FbxDatas class 
ExtraDatas class 
FbxDatas class
## csc.fbx The Cascadeur python module provides basic methods to operate fbx. 

csc.fbx.FbxSettingsMode 
FbxSettingsMode enumeration csc.fbx.FbxSettingsAxis 
FbxSettingsAxis enumeration csc.fbx.FbxSettings 
FbxSettings class csc.fbx.FbxLoader 
FbxLoader class csc.fbx.FbxSceneLoader 
FbxSceneLoader class 
FbxLoader class 
FbxSceneLoader class 
FbxSettings class
> 
FbxSettingsAxis enumeration
> Binary, Ascii

FbxSettingsAxis enumeration Binary, Ascii Members:
> X
> Y
> Z

X Y Z
> 
FbxSettingsMode enumeration
> Binary, Ascii

FbxSettingsMode enumeration Binary, Ascii Members:
> Binary
> Ascii

Binary Ascii
## csc.rig The Cascadeur python module that implements the basic functions for operating a rig. 

csc.rig.AddElementData csc.rig.BoneProperty csc.rig.TwistProperty csc.rig.TwistBoneProperty csc.rig.QrtData Overloaded function.
1. __init__(self: csc.rig.AddElementData) -> None
2. __init__(self: csc.rig.AddElementData, arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: float, arg8: numpy.ndarray[numpy.float32[3, 1]]) -> None

__init__(self: csc.rig.AddElementData) -> None __init__(self: csc.rig.AddElementData, arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: float, arg8: numpy.ndarray[numpy.float32[3, 1]]) -> None
## csc.layers The Cascadeur python module that implements scene layers functionality. 

LayerId == FolderId == ItemId == Guid csc.layers.Header 
Header class csc.layers.ItemVariant 
ItemVariant class csc.layers.Folder 
Folder class csc.layers.Layer 
Layer class csc.layers.Viewer 
Viewer class csc.layers.Editor 
Editor class csc.layers.Selector 
Selector class csc.layers.LayersContainer 
LayersContainer class csc.layers.UserLabelData 
UserLabelData class csc.layers.Layers 
Layers class csc.layers.Cycle 
Cycle class csc.layers.CyclesViewer Cycle 
viewer class csc.layers.CyclesEditor Cycle 
editor class csc.layers.LayersSelectionChanger Layer 
SelectionChanger class csc.layers.layer.Interpolation Interpolation enumerable csc.layers.layer.Tangents Layer Frame Tangents enumerable csc.layers.layer.IkFk Layer Frame IkFk enumerable csc.layers.layer.Fixation Layer Frame Fixation enumerable csc.layers.layer.Common 
Common class csc.layers.layer.Key 
Key class csc.layers.layer.Interval 
Interval class csc.layers.layer.Section 
Section class csc.layers.layer.Cell 
Cell class csc.layers.index.FramesInterval 
FramesInterval class csc.layers.index.FramesIndices 
FramesIndices class csc.layers.index.CellIndex 
CellIndex class csc.layers.index.RectIndicesContainer 
RectIndicesContainer class csc.layers.index.IndicesContainer 
IndicesContainer class 
Cycle class -> bool -> Pos -> Pos Cycle 
editor class Cycle 
viewer class 
Editor class 
This class contains all methods and properties that need to edit the structure of scene objects' interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.
- create_folder – name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId
- create_layer – name : string, parent : FolderId, pos : int or None, -> FolderId
- set_fixed_interpolation_if_need – overridden method by ItemId, int, int || LayerId, int (frame)
- set_fixed_interpolation_or_key_if_need – overridden method by LayerId, int, bool

create_folder – name : string, parent : FolderId, withDefaultLayer : bool (true), pos : int or None, -> FolderId create_layer – name : string, parent : FolderId, pos : int or None, -> FolderId set_fixed_interpolation_if_need – overridden method by ItemId, int, int || LayerId, int (frame) set_fixed_interpolation_or_key_if_need – overridden method by LayerId, int, bool name : string | parent : FolderId | withDefaultLayer : bool (true) | pos : int or None | -> FolderId name : string | parent : FolderId | pos : int or None | -> FolderId -> Header layer : Layer | pos : int or None pos : int or None Overloaded function.
1. set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool
2. set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool

set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, start: int, end: int) -> bool set_fixed_interpolation_if_need(self: csc.layers.Editor, id: csc.Guid, frame: int) -> bool isL : bool | id : ItemId isL : bool | id : LayerId section : Section | pos : int | id : ItemId section : <Pos, Section>{} | id : LayerId isV : bool | id : ItemId isV : bool | id : LayerId pos : int | id : ItemId 
Folder class Implements the parent folder properties of children layers and sub folders items -> ItemId pos : int
-> ItemId id : ItemId | -> int -> int -> ItemId[] -> ItemId[] -> Header 
Header class Describes the header properties for a folder
- parent – Get set csc.Guid
- id – Get set csc.Guid
- name – Get set string

parent – Get set csc.Guid id – Get set csc.Guid name – Get set string 
ItemVariant class Can implement a folder or layer for a header -> Folder (if it has folder otherwise none) -> Header -> Layer (if it has layer otherwise none) 
Layer class The Layer is the basic element that implements intervals and sections to set
interpolation properties of scene objects
- header – Get Header
- is_locked – Get bool
- is_visible – Get bool
- obj_ids – Get csc.Guid{}
- sections – Get std::map<Pos, Section>

header – Get Header is_locked – Get bool is_visible – Get bool obj_ids – Get csc.Guid{} sections – Get std::map<Pos, Section> -> Key -> int -> Section -> int pos : int | -> Section -> Interval -> Key -> FramesIndices -> int -> csc.model.ObjectId{} -> Section -> std::map<Pos, Section> 
Layers class The 
root class describes the layers' hierarchy of the scene.
Each scene object can be placed on any layer to define its personal interpolation properties. root_id – Get csc.Guid -> <FolderId, Folder>{} -> LayersContainer -> UserLabels 
LayersContainer class It is the container of layers. -> Layer -> LayerId -> LayerId -> <LayerId, Layer>{} -> <csc.model.ObjectId, LayerId>{} Layer 
SelectionChanger class Overloaded function.
1. set_full_selection_by_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None inds : IndicesContainer
2. set_full_selection_by_parts(self: csc.layers.LayersSelectionChanger, itms: list[csc.Guid], first: int, last: int) -> bool

set_full_selection_by_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None
> inds : IndicesContainer

inds : IndicesContainer set_full_selection_by_parts(self: csc.layers.LayersSelectionChanger, itms: list[csc.Guid], first: int, last: int) -> bool 
Selector class 
This class contains methods to observe and to set selected layers and folders set_full_selection_by_parts – overridden method by ItemId[] (itms), int (first), int (last) || IndicesContainer (inds) ignoreLocked : bool (false) | -> LayerId[] ignoreLocked : bool (false) | -> IndicesContainer -> IndicesContainer Overloaded function.
1. set_full_selection_by_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None inds : IndicesContainer
2. set_full_selection_by_parts(self: csc.layers.Selector, itms: list[csc.Guid], first: int, last: int) -> None

set_full_selection_by_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None
> inds : IndicesContainer

inds : IndicesContainer set_full_selection_by_parts(self: csc.layers.Selector, itms: list[csc.Guid], first: int, last: int) -> None id : ItemId | uncheckable : bool 
UserLabelData class The data of user defined label. 
UserLabels class It is the storage of user defined labels. -> index Overloaded function.
1. remove(self: csc.layers.UserLabels, index: int) -> None
2. remove(self: csc.layers.UserLabels, arg0: int) -> object -> UserLabelData

remove(self: csc.layers.UserLabels, index: int) -> None remove(self: csc.layers.UserLabels, arg0: int) -> object
> -> UserLabelData

-> UserLabelData -> UserLabelData[] 
Viewer class 
This class contains all methods and properties that describe the structure of scene objects' interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.
- top_layer_id – overridden method by ItemId || ItemId[]
- merged_layer – overridden method like static and member LayerId[]
- last_key_pos – overridden method by LayerId[], -> Layer
- frames_count – overridden method by LayerId[], -> int
- significant_frames – overridden method by LayerId{}, -> int{}

top_layer_id – overridden method by ItemId || ItemId[] merged_layer – overridden method like static and member LayerId[] last_key_pos – overridden method by LayerId[], -> Layer frames_count – overridden method by LayerId[], -> int significant_frames – overridden method by LayerId{}, -> int{} -> ItemId[] items : ItemId[] | ignoreLocked : bool (false) | -> LayerId[] -> LayerId[] -> FolderId[] -> LayerId id : FolderId | -> Folder id : LayerId | -> Layer id : FolderId | -> Folder -> <FolderId, Folder>{} Overloaded function.
1. frames_count(self: csc.layers.Viewer) -> int
2. frames_count(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int

frames_count(self: csc.layers.Viewer) -> int frames_count(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int -> bool id : ItemId | -> Header -> bool id : ItemId | -> ItemVariant Overloaded function.
1. last_key_pos(self: csc.layers.Viewer) -> int
2. last_key_pos(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int

last_key_pos(self: csc.layers.Viewer) -> int last_key_pos(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> int id : LayerId | -> Layer id : csc.model.ObjectId | -> LayerId id : csc.model.ObjectId | -> LayerId ids : csc.model.ObjectId[] | -> LayerId{} -> IndicesContainer -> <LayerId, Layer>{} -> LayerId[] -> int -> FolderId Overloaded function.
1. significant_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices
2. significant_frames(self: csc.layers.Viewer, id_arr: set[csc.Guid]) -> domain::scene::layers::index::FramesIndices

significant_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices significant_frames(self: csc.layers.Viewer, id_arr: set[csc.Guid]) -> domain::scene::layers::index::FramesIndices Overloaded function.
1. top_layer_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid
2. top_layer_id(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> csc.Guid

top_layer_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid top_layer_id(self: csc.layers.Viewer, id_arr: list[csc.Guid]) -> csc.Guid -> LayerId[]
## csc.model The Cascadeur python module that implements model and behaviors scene editors methods. 

Eigen::Matrix3f, Eigen::Matrix4f, Eigen::Quaternionf,
std::string, common::Vector3b>; Setting.Value = std::variant<bool, int>; ClusterId = int csc.model.Data 
Data class csc.model.Setting 
Setting class csc.model.ClusterViewer 
ClusterViewer class csc.model.ClusterEditor 
ClusterEditor class csc.model.DataViewer 
DataViewer class csc.model.DataEditor 
DataEditor class csc.model.BehaviourViewer 
BehaviourViewer class csc.model.BehaviourEditor 
BehaviourEditor class csc.model.ModelViewer 
ModelViewer class csc.model.ModelEditor 
ModelEditor class csc.model.DataMode Data::Mode enum csc.model.SettingMode Setting::Mode enum csc.model.ObjectId csc.model.DataId csc.model.BehaviourId csc.model.SettingId csc.model.HyperedgeId csc.model.SettingFunctionId csc.model.LerpMode LerpMode enumerable csc.model.DescriptionTerm csc.model.CustomSelectionPolicy CustomSelectionPolicy enumerable csc.model.PropertyType PropertyType enumerable csc.model.PathName csc.model.ClustersEdge 
ClustersEdge class 
BehaviourEditor class 
This class allows editing of scene behaviours and their properties. Overloaded function.
1. add_behaviour(self: csc.model.BehaviourEditor, arg0: csc.model.ObjectId, arg1: str) -> csc.model.BehaviourId object_id : csc.model.ObjectId | behaviour_type : string | -> csc.model.BehaviourId
2. add_behaviour(self: csc.model.BehaviourEditor, object_id: csc.model.ObjectId, behaviour_type: str, behaviour_id: csc.model.BehaviourId) -> csc.model.BehaviourId object_id : csc.model.ObjectId | behaviour_type : string | behaviour_id : csc.model.BehaviourId | -> csc.model.BehaviourId

add_behaviour(self: csc.model.BehaviourEditor, arg0: csc.model.ObjectId, arg1: str) -> csc.model.BehaviourId
> object_id : csc.model.ObjectId | behaviour_type : string | -> csc.model.BehaviourId

object_id : csc.model.ObjectId | behaviour_type : string | -> csc.model.BehaviourId add_behaviour(self: csc.model.BehaviourEditor, object_id: csc.model.ObjectId, behaviour_type: str, behaviour_id: csc.model.BehaviourId) -> csc.model.BehaviourId
> object_id : csc.model.ObjectId | behaviour_type : string | behaviour_id : csc.model.BehaviourId | -> csc.model.BehaviourId

object_id : csc.model.ObjectId | behaviour_type : string | behaviour_id : csc.model.BehaviourId | -> csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | asset_id : csc.domain.AssetId behaviour_id : csc.model.BehaviourId | name : string | data_id : csc.model.DataId behaviour_id : csc.model.BehaviourId | name : string | mo_id : csc.model.ObjectId behaviour_id : csc.model.BehaviourId | name : string | beh_id : csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | setting_id : csc.model.SettingId behaviour_id : csc.model.BehaviourId objectsId : {csc.model.ObjectId} behaviour_id : csc.model.BehaviourId | name : string | data_id : csc.model.DataId behaviour_id : csc.model.BehaviourId | name : string | mo_id : csc.model.ObjectId behaviour_id : csc.model.BehaviourId | name : string | beh_id : csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | setting_id : csc.model.SettingId behaviour_id : csc.model.BehaviourId | hidden : bool(true) -> bool behaviour_id : csc.model.BehaviourId | name : string | asset_id : csc.domain.AssetId behaviour_id : csc.model.BehaviourId | name : string | dataId : csc.model.DataId behaviour_id : csc.model.BehaviourId | name : string | inserted_ids : csc.model.DataId behaviour_id : csc.model.BehaviourId | name : string | name_value : string behaviour_id : csc.model.BehaviourId | name : string | mo_id : csc.model.ObjectId behaviour_id : csc.model.BehaviourId | name : string | inserted_ids : csc.model.ObjectId[] behaviour_id : csc.model.BehaviourId | name : string | beh_id : csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | inserted_ids : csc.model.BehaviourId[] behaviour_id : csc.model.BehaviourId | name : string | setting_id : csc.model.SettingId behaviour_id : csc.model.BehaviourId | name : string | inserted_ids : csc.model.SettingId[] behaviour_id : csc.model.BehaviourId | name : string | str : string Overloaded function.
1. __init__(self: csc.model.BehaviourId, arg0: str) -> None
2. __init__(self: csc.model.BehaviourId) -> None

__init__(self: csc.model.BehaviourId, arg0: str) -> None __init__(self: csc.model.BehaviourId) -> None 
BehaviourViewer class 
This class allows viewing of scene behaviours and their properties. objectId : csc.model.ObjectId | behaviour_name : string | -> csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[] objectId : csc.model.ObjectId | behaviour_name : string | -> csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.DataId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.DataId[] behaviour_id : csc.model.BehaviourId | -> string behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId[] behaviour_id : csc.model.BehaviourId | -> csc.model.ObjectId -> string[] behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[] behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId behaviour_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId[] behaviour_id : csc.model.BehaviourId | name : string | -> string Overloaded function.
1. get_behaviours(self: csc.model.BehaviourViewer, type_name: str) -> list[csc.model.BehaviourId] typeName : string | -> csc.model.BehaviourId[]
2. get_behaviours(self: csc.model.BehaviourViewer, object_id: csc.model.ObjectId) -> list[csc.model.BehaviourId] objectId : csc.model.ObjectId | -> csc.model.BehaviourId[]

get_behaviours(self: csc.model.BehaviourViewer, type_name: str) -> list[csc.model.BehaviourId]
> typeName : string | -> csc.model.BehaviourId[]

typeName : string | -> csc.model.BehaviourId[] get_behaviours(self: csc.model.BehaviourViewer, object_id: csc.model.ObjectId) -> list[csc.model.BehaviourId]
> objectId : csc.model.ObjectId | -> csc.model.BehaviourId[]

objectId : csc.model.ObjectId | -> csc.model.BehaviourId[] -> Children behs ids behaviour_id : csc.model.BehaviourId | name : string | -> Type[] -> bool behaviour_name : string | -> bool 
ClusterEditor class 
This class lets edit scene data clusters. insertedIds : csc.model.DataId[] | name : string (ââ) | -> ClusterId cluster_index : ClusterId | insertedIds : csc.model.DataId[] cluster_id_first : ClusterId | cluster_id_second : ClusterId cluster_id : ClusterId data_id : csc.model.DataId cluster_id : ClusterId | name : string cluster_id : ClusterId cluster_id_first : ClusterId | cluster_id_second : ClusterId 
ClusterViewer class 
This class lets read scene data clusters. data_id : csc.model.DataId | -> ClusterId cluster_id : ClusterId | -> csc.model.DataId[] cluster_id : ClusterId | -> string -> ClusterId[] -> (ClusterId,ClusterId)[] 
ClustersEdge class 
This class contains link between clusters
> CustomSelectionPolicy enumerable
> Default, // the entity is selected with other entities
> Single, // the entity is selected only if the selection contains only from this entity
> SingleType // the entity is selected only if the selection contains only entities of the same type

CustomSelectionPolicy enumerable Default, // the entity is selected with other entities Single, // the entity is selected only if the selection contains only from this entity SingleType // the entity is selected only if the selection contains only entities of the same type Members:
> Default
> Single
> SingleType

Default Single SingleType 
Data class 
This class serves to represent any special type of data.
These data can be used in the update calculation or as behaviors' properties.
- id – Get Set csc.model.DataId
- object_id – Get Set csc.model.ObjectId
- name – Get Set string
- mode – Get Set csc.model.DataMode

id – Get Set csc.model.DataId object_id – Get Set csc.model.ObjectId name – Get Set string mode – Get Set csc.model.DataMode 
DataEditor class 
This class has the possibility to edit scene data and their properties.
- add_data – overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data
- add_setting – overridden method by string, Setting.Value || csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting
- add_constant_data – overridden method by string, Data.Value || string, Data.Value, csc.model.DataId -> Data
- add_constant_setting – overridden method by string, Setting.Value || string, Setting.Value, csc.model.SettingId -> Setting
- set_data_value – overridden method by csc.model.DataId&, Data.Value || csc.model.DataId, int{}, Data.Value || csc.model.DataId, int, Data.Value

add_data – overridden method by csc.model.ObjectId, string, DataMode, Data.Value, csc.model.DataId -> Data add_setting – overridden method by string, Setting.Value || csc.model.ObjectId, string, Setting.Value, csc.model.SettingId -> Setting add_constant_data – overridden method by string, Data.Value || string, Data.Value, csc.model.DataId -> Data add_constant_setting – overridden method by string, Setting.Value || string, Setting.Value, csc.model.SettingId -> Setting set_data_value – overridden method by csc.model.DataId&, Data.Value || csc.model.DataId, int{}, Data.Value || csc.model.DataId, int, Data.Value Overloaded function.
1. add_constant_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data
2. add_constant_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data

add_constant_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data add_constant_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data Overloaded function.
1. add_constant_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) -> csc.model.Setting
2. add_constant_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting

add_constant_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) -> csc.model.Setting add_constant_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) -> csc.model.Setting Overloaded function.
1. add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data -> Data
2. add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data -> Data

add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> csc.model.Data
> -> Data

-> Data add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) -> csc.model.Data
> -> Data

-> Data Overloaded function.
1. add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting -> Setting
2. add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting -> Setting

add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) -> csc.model.Setting
> -> Setting

-> Setting add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) -> csc.model.Setting
> -> Setting

-> Setting -> ClusterEditor Overloaded function.
1. reset_description_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None
2. reset_description_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None

reset_description_value(self: csc.model.DataEditor, id: csc.model.DataId) -> None reset_description_value(self: csc.model.DataEditor, id: csc.model.SettingId) -> None Overloaded function.
1. set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
2. set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
3. set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None

set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None Overloaded function.
1. set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None
2. set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None

set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.DataId) -> None set_description_value(self: csc.model.DataEditor, name: str, id: csc.model.SettingId) -> None Overloaded function.
1. set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) -> None
2. set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None

set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) -> None set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, frame: int, value: Union[bool, int]) -> None Overloaded function.
1. __init__(self: csc.model.DataId, arg0: str) -> None
2. __init__(self: csc.model.DataId) -> None

__init__(self: csc.model.DataId, arg0: str) -> None __init__(self: csc.model.DataId) -> None
> Data::Mode
> enum
> This enumerates the basic types of data.
> Static, Animation

Data::Mode enum This enumerates the basic types of data.
Static, Animation Members:
> Static
> Animation

Static Animation 
DataViewer class 
This class allows to view scene data and their properties.
- get_data_value – overridden method by id : csc.model.DataId || csc.model.DataId, int (frame) -> Data.Value
- get_behaviour_property – overridden method by : csc.model.BehaviourId, string -> Data.Value || csc.model.BehaviourId, string, int (frame) -> Setiing.Value

get_data_value – overridden method by id : csc.model.DataId || csc.model.DataId, int (frame) -> Data.Value get_behaviour_property – overridden method by : csc.model.BehaviourId, string -> Data.Value || csc.model.BehaviourId, string, int (frame) -> Setiing.Value -> ClusterViewer -> csc.model.DataId[] -> csc.model.SettingId[] -> int id : csc.model.Beh id | name : string | -> csc.model.DataValue Overloaded function.
1. get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
2. get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union[bool, int]

get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] get_behaviour_property(self: csc.model.DataViewer, id: csc.model.BehaviourId, name: str) -> Union[bool, int] id : csc.model.DataId | -> Data id : csc.model.ObjectId | name : string | -> csc.model.DataId Overloaded function.
1. get_data_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
2. get_data_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

get_data_value(self: csc.model.DataViewer, id: csc.model.DataId) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] get_data_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] -> string -> string[] Overloaded function.
1. get_description_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str id : csc.model.DataId -> string
2. get_description_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str id : csc.model.SettingId -> string

get_description_value(self: csc.model.DataViewer, id: csc.model.DataId) -> str
> id : csc.model.DataId -> string

id : csc.model.DataId -> string get_description_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> str
> id : csc.model.SettingId -> string

id : csc.model.SettingId -> string id : csc.model.SettingId | -> Setting id : csc.model.ObjectId | name : string | -> csc.model.DataId Overloaded function.
1. get_setting_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union[bool, int] id : csc.model.SettingId | -> Setting.Value
2. get_setting_value(self: csc.model.DataViewer, setting_id: csc.model.SettingId, position: int) -> Union[bool, int] id : csc.model.SettingId, position : int | -> Setting.Value

get_setting_value(self: csc.model.DataViewer, id: csc.model.SettingId) -> Union[bool, int]
> id : csc.model.SettingId | -> Setting.Value

id : csc.model.SettingId | -> Setting.Value get_setting_value(self: csc.model.DataViewer, setting_id: csc.model.SettingId, position: int) -> Union[bool, int]
> id : csc.model.SettingId, position : int | -> Setting.Value

id : csc.model.SettingId, position : int | -> Setting.Value id : csc.model.DataId | -> Data.Value Overloaded function.
1. __init__(self: csc.model.HyperedgeId, arg0: str) -> None
2. __init__(self: csc.model.HyperedgeId) -> None

__init__(self: csc.model.HyperedgeId, arg0: str) -> None __init__(self: csc.model.HyperedgeId) -> None
> LerpMode enumerable
> Empty, Linear, Spherical

LerpMode enumerable Empty, Linear, Spherical Members:
> Empty
> Linear
> Spherical

Empty Linear Spherical 
ModelEditor class Represents basic methods to edit the scene model add_object – overridden method by GroupId -> csc.model.ObjectId Overloaded function.
1. add_object(self: csc.model.ModelEditor) -> csc.model.ObjectId
2. add_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId

add_object(self: csc.model.ModelEditor) -> csc.model.ObjectId add_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId -> BehaviourEditor -> DataEditor -> csc.layers.Layers -> csc.layers.Editor -> csc.layers.Selector 
ModelViewer class Represents basic methods to view the scene model get_objects – overridden method by string -> csc.model.ObjectId[] -> BehaviourViewer -> DataViewer Overloaded function.
1. get_objects(self: csc.model.ModelViewer) -> list[csc.model.ObjectId]
2. get_objects(self: csc.model.ModelViewer, name: str) -> list[csc.model.ObjectId]

get_objects(self: csc.model.ModelViewer) -> list[csc.model.ObjectId] get_objects(self: csc.model.ModelViewer, name: str) -> list[csc.model.ObjectId] Overloaded function.
1. __init__(self: csc.model.ObjectId, arg0: str) -> None
2. __init__(self: csc.model.ObjectId) -> None

__init__(self: csc.model.ObjectId, arg0: str) -> None __init__(self: csc.model.ObjectId) -> None Overloaded function.
1. __init__(self: csc.model.PathName) -> None 
PathName class Implements a hierarchical name
2. __init__(self: csc.model.PathName, arg0: str, arg1: list[str]) -> None 
PathName class Implements a hierarchical name ivar name : Get Set string ivar path : Get Set string[]

__init__(self: csc.model.PathName) -> None
> 
PathName class
> Implements a hierarchical name

PathName class Implements a hierarchical name __init__(self: csc.model.PathName, arg0: str, arg1: list[str]) -> None
> 
PathName class
> Implements a hierarchical name
> ivar name
> :
> Get Set string
> ivar path
> :
> Get Set string[]

PathName class Implements a hierarchical name Get Set string Get Set string[]
> PropertyType enumerable
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

PropertyType enumerable Undefined,
DataType,
DataRangeType,
SettingType,
SettingRangeType,
ObjectType,
ObjectRangeType,
BehaviourType,
BehaviourRangeType,
AssetType,
AssetRangeType,
StringType Members:
> Undefined
> DataType
> DataRangeType
> SettingType
> SettingRangeType
> ObjectType
> ObjectRangeType
> BehaviourType
> BehaviourRangeType
> AssetType
> AssetRangeType
> StringType

Undefined DataType DataRangeType SettingType SettingRangeType ObjectType ObjectRangeType BehaviourType BehaviourRangeType AssetType AssetRangeType StringType 
Setting class 
This class serves to represent int or bool value that using in the update calculation.
- id – Get csc.model.DataId
- object_id – Get csc.model.ObjectId
- name – Get string
- type – Get int
- mode – Get csc.model.SettingMode

id – Get csc.model.DataId object_id – Get csc.model.ObjectId name – Get string type – Get int mode – Get csc.model.SettingMode object_id ( csc.model.ObjectId ) – object_id Overloaded function.
1. __init__(self: csc.model.Setting, id: csc.model.SettingId, object_id: csc.model.ObjectId, name: str, type: int) -> None
2. __init__(self: csc.model.Setting, object_id: csc.model.ObjectId, name: str, type: int) -> None

__init__(self: csc.model.Setting, id: csc.model.SettingId, object_id: csc.model.ObjectId, name: str, type: int) -> None __init__(self: csc.model.Setting, object_id: csc.model.ObjectId, name: str, type: int) -> None Overloaded function.
1. __init__(self: csc.model.SettingFunctionId, arg0: str) -> None
2. __init__(self: csc.model.SettingFunctionId) -> None

__init__(self: csc.model.SettingFunctionId, arg0: str) -> None __init__(self: csc.model.SettingFunctionId) -> None Overloaded function.
1. __init__(self: csc.model.SettingId, arg0: str) -> None
2. __init__(self: csc.model.SettingId) -> None

__init__(self: csc.model.SettingId, arg0: str) -> None __init__(self: csc.model.SettingId) -> None
> Setting::Mode enum
> This enumerates the basic types of data.
> Static, Animation

Setting::Mode enum This enumerates the basic types of data.
Static, Animation Members:
> Static
> Animation

Static Animation -> PathName
## csc.domain The Cascadeur python module that implements basic scene properties and infrastructure. 

Entity3d_id = std::variant<model::ModelObject::Id, Tool_object_id> csc.domain.Pivot 
Pivot class csc.domain.Selection 
Selection class csc.domain.Selector 
Selector class csc.domain.AssetId csc.domain.Asset 
Asset class csc.domain.LocalInterpolator 
LocalInterpolator class csc.domain.SceneUpdater 
SceneUpdater class csc.domain.ProcessorsStorage 
ProcessorsStorage class csc.domain.IMessageHandler IMessageHandler interface csc.domain.Scene 
Scene class csc.domain.Session 
Session class csc.domain.Tool_object_id csc.domain.StatePivot StatePivot enum csc.domain.FrameActionOnChange FrameActionOnChange enum csc.domain.IntervalActionOnChange IntervalActionOnChange enum csc.domain.SelectorMode SelectorMode enumerable csc.domain.SelectorFilter SelectorFilter enumerable csc.domain.Select 
Select class csc.domain.assets.FigureVertex 
FigureVertex class csc.domain.assets.Triangle 
Triangle class csc.domain.assets.Mesh 
Mesh class csc.domain.assets.MeshDependency 
MeshDependency class csc.domain.assets.AssetsManager 
AssetsManager class 
Asset class Assets are objects resources that have content like meshes or textures. id – Get csc.Guid Overloaded function.
1. __init__(self: csc.domain.AssetId, arg0: str) -> None
2. __init__(self: csc.domain.AssetId) -> None

__init__(self: csc.domain.AssetId, arg0: str) -> None __init__(self: csc.domain.AssetId) -> None
> FrameActionOnChange enum
> AutoKey = 0, Fixing = 1, DoNothing = 2

FrameActionOnChange enum AutoKey = 0, Fixing = 1, DoNothing = 2 Members:
> AutoKey
> Fixing
> DoNothing

AutoKey Fixing DoNothing IMessageHandler interface
> IntervalActionOnChange enum
> Fixing = 0, DoNothing = 1

IntervalActionOnChange enum Fixing = 0, DoNothing = 1 Members:
> Fixing
> DoNothing

Fixing DoNothing 
LocalInterpolator class 
Pivot class Represents basic Pivot methods.
- position – overridden method by … || int (frame) || int, StatePivot (pivot)
- rotation – overridden method by … || int (frame) || int, StatePivot (pivot)

position – overridden method by … || int (frame) || int, StatePivot (pivot) rotation – overridden method by … || int (frame) || int, StatePivot (pivot) Overloaded function.
1. position(self: csc.domain.Pivot) -> numpy.ndarray[numpy.float32[3, 1]]
2. position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray[numpy.float32[3, 1]]
3. position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]]

position(self: csc.domain.Pivot) -> numpy.ndarray[numpy.float32[3, 1]] position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray[numpy.float32[3, 1]] position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]] Overloaded function.
1. rotation(self: csc.domain.Pivot) -> csc.math.Quaternion
2. rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion
3. rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion

rotation(self: csc.domain.Pivot) -> csc.math.Quaternion rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion 
ProcessorsStorage class 
The class serves to contain entity 3d processors 
Scene class 
Root class that represents a scene and its methods for modifying or observing it. Modify scene by func modify:
- name – Name of the modifier
- func – Modify functor void(modelEditor, updateEditor, scene)

name – Name of the modifier func – Modify functor void(modelEditor, updateEditor, scene) Modify scene by func modify_update:
- name – Name of the modifier
- func – Modify functor void(modelEditor, updateEditor, sceneUpdater)

name – Name of the modifier func – Modify functor void(modelEditor, updateEditor, sceneUpdater) -> AssetsManager -> csc.model.BehaviourViewer -> csc.model.DataViewer -> csc.layers.Selector -> csc.layers.Viewer -> csc.model.ModelViewer -> bool -> bool -> bool -> bool -> Selector 
SceneUpdater class The SceneUpdater serves to rule the scene modify.
If we changed the update, we should regenerate it, also it has the possible to run the update with certain data. run_update – overridden method by csc.model.DataId{} (localIds), int (frame) || csc.model.DataId{}, int{} (frames) Overloaded function.
1. run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frame: int) -> None
2. run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None

run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frame: int) -> None run_update(self: csc.domain.SceneUpdater, local_ids: set[csc.model.DataId], frames: csc.layers.index.FramesIndices) -> None 
Select class Represents properties of the current selection state of the scene
- object_ids – Get Set (csc.model.ObjectId or csc.scene.Tool_object_id){}
- pivot_id – Get Set (csc.model.ObjectId or csc.scene.Tool_object_id)
- filter – Get Set csc.scene.SelectorFilter
- mode – Get Set csc.scene.SelectorMode
- types_filter – Get Set string{}

object_ids – Get Set (csc.model.ObjectId or csc.scene.Tool_object_id){} pivot_id – Get Set (csc.model.ObjectId or csc.scene.Tool_object_id) filter – Get Set csc.scene.SelectorFilter mode – Get Set csc.scene.SelectorMode types_filter – Get Set string{} 
Selection class Contains selected objects ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){} 
SelectionChanger class Contains basic methods and properties to operate current selected scene objects
- ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){}
- select – overridden method by Select || Entity3d_id{}, Entity3d_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)

ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){} select – overridden method by Select || Entity3d_id{}, Entity3d_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter) Overloaded function.
1. select(self: csc.domain.SelectionChanger, select: csc.domain.Select) -> None
2. select(self: csc.domain.SelectionChanger, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = <csc.model.ObjectId object at 0x7f3d3ffa9b30>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, types_filter: set[str] = set(), auto_pivot: bool = False) -> None

select(self: csc.domain.SelectionChanger, select: csc.domain.Select) -> None select(self: csc.domain.SelectionChanger, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = <csc.model.ObjectId object at 0x7f3d3ffa9b30>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, types_filter: set[str] = set(), auto_pivot: bool = False) -> None 
Selector class Contains basic methods and properties to operate current selected scene objects
- ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){}
- select – overridden method by Select || Entity3d_id{}, Entity3d_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)

ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){} select – overridden method by Select || Entity3d_id{}, Entity3d_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter) -> Pivot Overloaded function.
1. select(self: csc.domain.Selector, select: csc.domain.Select) -> None
2. select(self: csc.domain.Selector, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type_filter: set[str] = set(), auto_pivot: bool = False) -> None

select(self: csc.domain.Selector, select: csc.domain.Select) -> None select(self: csc.domain.Selector, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type_filter: set[str] = set(), auto_pivot: bool = False) -> None -> Selection
> SelectorFilter enumerable
> Free = 0x00,
> Selectable = 0x01,
> ObjectType = 0x02,
> Layer = 0x04,
> CustomSelectionPolicy = 0x08,
> Standart = Selectable | ObjectType | Layer,
> Full = 0xFF,

SelectorFilter enumerable Free = 0x00,
Selectable = 0x01,
ObjectType = 0x02,
Layer = 0x04,
CustomSelectionPolicy = 0x08,
Standart = Selectable | ObjectType | Layer,
Full = 0xFF, Members:
> Free
> Selectable
> ObjectType
> Layer
> CustomSelectionPolicy
> Standart
> Full

Free Selectable ObjectType Layer CustomSelectionPolicy Standart Full
> SelectorMode enumerable
> SingleSelection, // Resets if new objects were selected, and nothing changes if already selected ones were selected
> MultiSelection, // Multiple selections. If not all objects were selected, adds, otherwise subtracts
> NewSelection, // Resets everything and highlights the selection
> AdditionSelection, // Adds all selections to selections
> SubtractionSelection // Subtracts highlighted entities from selections

SelectorMode enumerable SingleSelection, // Resets if new objects were selected, and nothing changes if already selected ones were selected MultiSelection, // Multiple selections. If not all objects were selected, adds, otherwise subtracts NewSelection, // Resets everything and highlights the selection AdditionSelection, // Adds all selections to selections SubtractionSelection // Subtracts highlighted entities from selections Members:
> SingleSelection
> MultiSelection
> NewSelection
> AdditionSelection
> SubtractionSelection

SingleSelection MultiSelection NewSelection AdditionSelection SubtractionSelection 
Session class
> StatePivot enum
> This enumerates the basic types of pivot states.
> Fixed = 0, Moving = 1

StatePivot enum This enumerates the basic types of pivot states.
Fixed = 0, Moving = 1 Members:
> Fixed
> Moving

Fixed Moving Overloaded function.
1. __init__(self: csc.domain.Tool_object_id, arg0: str) -> None
2. __init__(self: csc.domain.Tool_object_id) -> None

__init__(self: csc.domain.Tool_object_id, arg0: str) -> None __init__(self: csc.domain.Tool_object_id) -> None 
AngleAxis class 
Circle3d class 
OrthogonalTransform class Implements orthogonal transform
- position – Get set Vector3f
- rotation – Get set Rotation

position – Get set Vector3f rotation – Get set Rotation Overloaded function.
1. __init__(self: csc.math.OrthogonalTransform, position: numpy.ndarray[numpy.float32[3, 1]], rotate: csc.math.Quaternion) -> None
2. __init__(self: csc.math.OrthogonalTransform) -> None

__init__(self: csc.math.OrthogonalTransform, position: numpy.ndarray[numpy.float32[3, 1]], rotate: csc.math.Quaternion) -> None __init__(self: csc.math.OrthogonalTransform) -> None 
ParametrizedLine class 
Hyperplane class 
Quaternion class 
This class is useful to calculate rotation operations. Overloaded function.
1. __mul__(self: csc.math.Quaternion, arg0: csc.math.Quaternion) -> csc.math.Quaternion
2. __mul__(self: csc.math.Quaternion, arg0: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]

__mul__(self: csc.math.Quaternion, arg0: csc.math.Quaternion) -> csc.math.Quaternion __mul__(self: csc.math.Quaternion, arg0: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]] 
Rotation class The Euler angles implementation. Overloaded function.
1. from_angle_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation
2. from_angle_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation

from_angle_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation from_angle_axis(arg0: csc.math.AngleAxis) -> csc.math.Rotation Overloaded function.
1. from_euler(x: float, y: float, z: float) -> csc.math.Rotation
2. from_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation

from_euler(x: float, y: float, z: float) -> csc.math.Rotation from_euler(vec3f: numpy.ndarray[numpy.float32[3, 1]]) -> csc.math.Rotation Overloaded function.
1. from_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation
2. from_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation

from_quaternion(w: float, x: float, y: float, z: float) -> csc.math.Rotation from_quaternion(quaternion: csc.math.Quaternion) -> csc.math.Rotation 
ScaledTransform class Implements transform with the scale possibility.
- position – Get set Vector3f
- rotation – Get set Rotation
- scale – Get set Vector3f

position – Get set Vector3f rotation – Get set Rotation scale – Get set Vector3f 
SizesInterval class Implements the sizes interval basic methods Overloaded function.
1. __init__(self: csc.math.SizesInterval) -> None
2. __init__(self: csc.math.SizesInterval, start: int, end: int) -> None

__init__(self: csc.math.SizesInterval) -> None __init__(self: csc.math.SizesInterval, start: int, end: int) -> None -> bool -> int -> int 
Sphere class 
Triangle class Structure from three points
- point1 – Get set Vector3f
- point2 – Get set Vector3f
- point3 – Get set Vector3f

point1 – Get set Vector3f point2 – Get set Vector3f point3 – Get set Vector3f -> csc.math.OrthogonalTransform -> csc.math.OrthogonalTransform -> Quaternionf -> Vector3f -> Tuple<vector<Vector3f>, vector<Quaternion>> -> Tuple<vector<Vector3f>, vector<Quaternion>> -> Tuple<vector<Vector3f>, vector<Quaternion>> -> Vector3f -> Vector3f -> Vector3f -> Vector3f Overloaded function.
1. transform_point(transform: math::OrthogonalTransform, point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]] -> Vector3f
2. transform_point(matrix: numpy.ndarray[numpy.float32[4, 4]], point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]] -> Vector3f

transform_point(transform: math::OrthogonalTransform, point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]
> -> Vector3f

-> Vector3f transform_point(matrix: numpy.ndarray[numpy.float32[4, 4]], point: numpy.ndarray[numpy.float32[3, 1]]) -> numpy.ndarray[numpy.float32[3, 1]]
> -> Vector3f

-> Vector3f -> csc.math.OrthogonalTransform (weight:float,roll:float,axis:int,negate:bool,
parentMatrix:Matrix4f,objectMatrix:Matrix4f) -> Matrix4f 
PosMass class This structure contains the mass and the position
- mass – Get Set float.
- position – Get Set Vector3f.

mass – Get Set float. position – Get Set Vector3f. -> Matrix3f
## csc.update The Cascadeur python module that implements basic update editor methods and its infrastructure. 

Update editor provides a node-like interface to edit data and setting graphs.
Naming conventions: regular means the same as data. It differs stuff from settings. Additional functionality.
Update editor can be used to check what data functions will be active if you set some datas as actual. RegularDataAttributeId, ActualityAttributeId,
SettingFunctionAttributeId, SettingDataAttributeId,
GroupAttributeId, ExternalPropertyAttributeId,
ConstantDataAttributeId, ConstantSettingAttributeId>; csc.update.NodeAttribute NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute. csc.update.RegularDataAttribute RegularDataAttribute represents an attribute of a regular data. csc.update.ActualityAttribute ActualityAttribute shows whether data is actual at the start of the graphs update. csc.update.ConstantDataAttribute ConstantDataAttribute represents an attribute of a constant regular data. csc.update.ConstantSettingAttribute ConstantSettingAttribute represents an attribute of a constant setting. csc.update.ExternalPropertyAttribute ExternalPropertyAttribute represents an attribute of the external properties of the update. csc.update.SettingFunctionAttribute SettingFunctionAttribute represents an attribute of a setting function. csc.update.InterfaceAttributeSide InterfaceAttributeSide enumerable csc.update.InterfaceAttribute InterfaceAttribute represents a group attribute. csc.update.RegularFunctionAttribute RegularFunctionAttribute represents an attribute of a data function. csc.update.ActivityAttribute ActivityAttribute represents the activity of the data function. csc.update.SettingDataAttribute SettingDataAttribute represents an attribute of a setting. csc.update.Node 
Node class represents a generic Node and implements methods that are common for all nodes csc.update.InterfaceNode InterfaceNode is a node inside the group that represents its connections with the ouside nodes. csc.update.ConstantDatas ConstantDatas represents a node of constant datas. csc.update.ConstantSettings ConstantSettings represents a node of constant settings. csc.update.ExternalProperties ExternalProperties represents a node of external properties. csc.update.RegularFunction 
RegularFunction class represents a node that calculates same operation, done with datas. csc.update.SettingData 
SettingData class represents a node that calculates same operation, done with settings. csc.update.SettingFunction 
SettingFunction class csc.update.Object 
Object class represents an object node. csc.update.RegularData 
RegularData class represents a node of a data. csc.update.Group 
Group class csc.update.ObjectGroup 
ObjectGroup class represents object group node csc.update.UpdateGroup 
UpdateGroup class represents update group node csc.update.HierarchyUpdate 
HierarchyUpdate class provides concrete operations with connections csc.update.Update 
Update class represents the whole update editor csc.update.RegularFunctionAttributeId RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute csc.update.RegularDataAttributeId RegularDataAttributeId is defined by the data id. csc.update.ActualityAttributeId ActualityAttributeId is defined by the data id. csc.update.SettingFunctionAttributeId SettingFunctionAttributeId is defined by the SettingFunctionId and the index of the attribute csc.update.GroupId csc.update.GroupAttributeId GroupAttributeId is defined by the GroupId and the guid-based id of the attribute. csc.update.ExternalPropertiesId ExternalPropertiesId is a guid based id. csc.update.ExternalProperty ExternalProperty enum csc.update.ExternalPropertyAttributeId ExternalPropertyAttributeId is defined by the ExternalPropertiesId and the value of the ExternalProperty enum csc.update.ConstantDatasId ConstantDatasId is a guid based id. csc.update.ConstantDataAttributeId ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant csc.update.ConstantSettingsId ConstantSettingsId is a guid based id. csc.update.ConstantSettingAttributeId ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant csc.update.Connection 
Connection class csc.update.InterfaceId InterfaceId is defined by the GroupId and the direction type of the node - input or output connection node. ActivityAttribute represents the activity of the data function.
It should be bool.
If true - function is active, if false - inactive. If not set - always active.
It is an input-only attribute. ActualityAttribute shows whether data is actual at the start of the graphs update.
It's always an output attribute.
It can be connected with setting functions. !Connections directly with data functions activity are not supported, use copy setting function instead) ActualityAttributeId is defined by the data id. It's an output only attribute.
Each data can be actual or non-actual at the start of the graphs update. Overloaded function.
1. __init__(self: csc.update.ActualityAttributeId, arg0: str) -> None
2. __init__(self: csc.update.ActualityAttributeId, arg0: csc.model.DataId) -> None
3. __init__(self: csc.update.ActualityAttributeId) -> None

__init__(self: csc.update.ActualityAttributeId, arg0: str) -> None __init__(self: csc.update.ActualityAttributeId, arg0: csc.model.DataId) -> None __init__(self: csc.update.ActualityAttributeId) -> None 
Connection class Implements the Connection between two attributes
- source – Get output AttributeId of the source
- destination – Get input AttributeId of the destination

source – Get output AttributeId of the source destination – Get input AttributeId of the destination RegularDataAttributeId, ActualityAttributeId,
SettingFunctionAttributeId, SettingDataAttributeId,
GroupAttributeId, ExternalPropertyAttributeId,
ConstantDataAttributeId, ConstantSettingAttributeId> ConstantDataAttribute represents an attribute of a constant regular data.
It's always an output attribute.
It can be connected with setting functions or data functions activity. ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant Implements the ConstantDataAttributeId.
- group_id – Get ConstantDatasId
- attribute_id – Get the data id (csc.model.DataId)

group_id – Get ConstantDatasId attribute_id – Get the data id (csc.model.DataId) ConstantDatas represents a node of constant datas. It is present in any place. value: Data.Value ConstantDatasId is a guid based id.
It is always equal to the group id, where the constant will be used. Overloaded function.
1. __init__(self: csc.update.ConstantDatasId, arg0: csc.update.GroupId) -> None
2. __init__(self: csc.update.ConstantDatasId, arg0: str) -> None
3. __init__(self: csc.update.ConstantDatasId) -> None

__init__(self: csc.update.ConstantDatasId, arg0: csc.update.GroupId) -> None __init__(self: csc.update.ConstantDatasId, arg0: str) -> None __init__(self: csc.update.ConstantDatasId) -> None ConstantSettingAttribute represents an attribute of a constant setting.
It's always an output attribute.
It can be connected with data functions. ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant Implements the ConstantSettingAttributeId.
- group_id – Get ConstantSettingsId
- attribute_id – Get csc.model.SettingId

group_id – Get ConstantSettingsId attribute_id – Get csc.model.SettingId ConstantSettings represents a node of constant settings. It is present in any place. value: Setting.Value ConstantSettingsId is a guid based id.
It is always equal to the group id, where the constant will be used. Overloaded function.
1. __init__(self: csc.update.ConstantSettingsId, arg0: csc.update.GroupId) -> None
2. __init__(self: csc.update.ConstantSettingsId, arg0: str) -> None
3. __init__(self: csc.update.ConstantSettingsId) -> None

__init__(self: csc.update.ConstantSettingsId, arg0: csc.update.GroupId) -> None __init__(self: csc.update.ConstantSettingsId, arg0: str) -> None __init__(self: csc.update.ConstantSettingsId) -> None ExternalProperties represents a node of external properties.
(E.g. is this update called during interpolation or not)
It is represent in any place. ExternalPropertiesId is a guid based id.
It is always equal to the group id, where the external property will be used. Overloaded function.
1. __init__(self: csc.update.ExternalPropertiesId, arg0: csc.update.GroupId) -> None
2. __init__(self: csc.update.ExternalPropertiesId, arg0: str) -> None
3. __init__(self: csc.update.ExternalPropertiesId) -> None

__init__(self: csc.update.ExternalPropertiesId, arg0: csc.update.GroupId) -> None __init__(self: csc.update.ExternalPropertiesId, arg0: str) -> None __init__(self: csc.update.ExternalPropertiesId) -> None
> ExternalProperty enum
> This enumerates the basic types of ExternalProperty states:
> Fixation,
> IsForwardKinematics,
> KinematicsType,
> InterpolationType,
> IsInterpolation,
> AfterPhysics,
> IsKey

ExternalProperty enum This enumerates the basic types of ExternalProperty states:
Fixation,
IsForwardKinematics,
KinematicsType,
InterpolationType,
IsInterpolation,
AfterPhysics,
IsKey Members:
> Fixation
> IsForwardKinematics
> KinematicsType
> InterpolationType
> IsInterpolation
> AfterPhysics
> IsKey

Fixation IsForwardKinematics KinematicsType InterpolationType IsInterpolation AfterPhysics IsKey ExternalPropertyAttribute represents an attribute of the external properties of the update.
It's always an output attribute.
It is settings based and thus can be connected with setting functions or data functions activity. ExternalPropertyAttributeId is defined by the ExternalPropertiesId and the value of the ExternalProperty enum Implements the ExternalPropertyAttributeId.
- node_id – Get GroupId
- property – Get ExternalProperty enum value

node_id – Get GroupId property – Get ExternalProperty enum value 
Group class node – overridden by name || node, access node by name or id get virtual node to access constant datas get virtual node to access constant settings create sub group check whether there is a child node with a given name get group attributes as interface attributes access the interface node get all leaf nodes (settings, datas, functions) Overloaded function.
1. node(self: csc.update.Group, name: str) -> csc.update.Node
2. node(self: csc.update.Group, node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) -> csc.update.Node

node(self: csc.update.Group, name: str) -> csc.update.Node node(self: csc.update.Group, node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) -> csc.update.Node access node by name or id recursively find node with name and type find node with name and type recursively get all children (their children are not included) GroupAttributeId is defined by the GroupId and the guid-based id of the attribute.
Group attribute names and indeces can change, so they are provided with their own guid Implements the GroupAttributeId.
- group_id – Get GroupId
- attribute_id – Get csc.Guid - id of the attribute

group_id – Get GroupId attribute_id – Get csc.Guid - id of the attribute Overloaded function.
1. __init__(self: csc.update.GroupId, arg0: str) -> None
2. __init__(self: csc.update.GroupId) -> None

__init__(self: csc.update.GroupId, arg0: str) -> None __init__(self: csc.update.GroupId) -> None 
HierarchyUpdate class provides concrete operations with connections InterfaceAttribute represents a group attribute.
Can be potentially connected to any attribute. Interface attribute can be:
1. An attribute of input/output node inside the group
2. An attribute of the group node itself, in the parent group layout (outside the group)
We will call this attributes âpairedâ. For each attribute there is a paired one. They have the same attribute ids and names.
Sometimes it's easier to think of them as of one attribute that has 2 sides. But in terms of 
this class this are two separate objects. get the group attribute id Get the paired attribute (e.g. the other side of the attribute) Rename the attribute
> InterfaceAttributeSide enumerable
> InterfaceSide - inside the group, GroupSide - when the group is a node

InterfaceAttributeSide enumerable InterfaceSide - inside the group, GroupSide - when the group is a node Members:
> InterfaceSide
> GroupSide

InterfaceSide GroupSide InterfaceId is defined by the GroupId and the direction type of the node - input or output connection node. Implements the InterfaceId.
- group_id – Get GroupId
- direction – Get direction type (csc.Direction)

group_id – Get GroupId direction – Get direction type (csc.Direction) InterfaceNode is a node inside the group that represents its connections with the ouside nodes.
Its attributes are csc.update.InterfaceAttributes -> csc.DirectionValue -> InterfaceAttribute[] attribute: InterfaceAttribute | position: int attribute: InterfaceAttribute 
Node class represents a generic Node and implements methods that are common for all nodes array of all input and output attributes name with all the parent nodes check if there is an input with such a name check if there is an output with such a name get uniqui id shortcut if node has only one input attribute array of all the inputes attributes check whether it is active for current actualities states
(see Additional functionality in csc.update.UpdateEditor) whether it is a fictive node (constants, inputs, outputs of a group or external properties) get name shortcut if node has only one output attribute array of all the outputs attributes return parent group (where this group node is located) return object of the node. Will return null if this is not an update group rename node NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute. disconnect – overridden method with parameter attribute: NodeAttribute attribute: NodeAttribute -> NodeAttribute[] -> NodeAttribute[] -> csc.DirectionValue Overloaded function.
1. disconnect(self: csc.update.NodeAttribute) -> None
2. disconnect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) -> None

disconnect(self: csc.update.NodeAttribute) -> None disconnect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) -> None -> AttributeId -> Node 
Object class represents an object node. Functionality is limited - it's better to use update group node instead. -> InterfaceAttribute -> InterfaceAttribute -> UpdateGroup 
ObjectGroup class represents object group node Overloaded function.
1. create_object(self: csc.update.ObjectGroup, name: str) -> csc.update.Object
2. create_object(self: csc.update.ObjectGroup, name: str, id: csc.model.ObjectId) -> csc.update.Object

create_object(self: csc.update.ObjectGroup, name: str) -> csc.update.Object create_object(self: csc.update.ObjectGroup, name: str, id: csc.model.ObjectId) -> csc.update.Object -> ObjectGroup -> ObjectGroup{} -> Object{} 
RegularData class represents a node of a data.
- value – overridden method by frame, get data value (requires frame if Animation data)
- set_value – overridden method by frame, set data value (requires frame if Animation data)

value – overridden method by frame, get data value (requires frame if Animation data) set_value – overridden method by frame, set data value (requires frame if Animation data) output attribute, that provides actuality status get attribute by direction get apply euler filter get explicit linear get lerp mode input attribute check if this data is set to actual (see Additional functionality in csc.update.UpdateEditor) Check if data is Animation or Static output attribute in interpolation, remove period set this data as actual (see Additional functionality in csc.update.UpdateEditor) set apply euler filter setDescriptionValue set explicit linear can be slerp for Vector3 datas. Used in interpolation in interpolation, if perion is provided, the data will be âfixedâ to provide smoothness Overloaded function.
1. set_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None
2. set_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], frame: int) -> None

set_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) -> None set_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], frame: int) -> None Overloaded function.
1. value(self: csc.update.RegularData) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
2. value(self: csc.update.RegularData, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]

value(self: csc.update.RegularData) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] value(self: csc.update.RegularData, frame: int) -> Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], numpy.ndarray[numpy.float32[4, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]] RegularDataAttribute represents an attribute of a regular data.
It can be connected with data functions. RegularDataAttributeId is defined by the data id.
Data only has one input and one output attributes. Overloaded function.
1. __init__(self: csc.update.RegularDataAttributeId, arg0: str) -> None
2. __init__(self: csc.update.RegularDataAttributeId, arg0: csc.model.DataId) -> None
3. __init__(self: csc.update.RegularDataAttributeId) -> None

__init__(self: csc.update.RegularDataAttributeId, arg0: str) -> None __init__(self: csc.update.RegularDataAttributeId, arg0: csc.model.DataId) -> None __init__(self: csc.update.RegularDataAttributeId) -> None 
RegularFunction class represents a node that calculates same operation, done with datas. activity attributes its input arguments method that decreases vector attribute its id method that increases vector attribute check whether this function will make it to the resulting data graph method that removes one in vector attribute method that resizes input vector attribute method that resizes output vector attribute its output arguments set the state of the function, whether it will be used or not RegularFunctionAttribute represents an attribute of a data function.
It can be connected with data attributes. RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute
- function_id – Get SettingFunctionId
- attribute_id – Get name of the attribute

function_id – Get SettingFunctionId attribute_id – Get name of the attribute 
SettingData class represents a node that calculates same operation, done with settings.
It can comprise bool or std::int8_t (Min: -128, Max: 127) value, please be carefull when you set this. get setting unique id output attribute Overloaded function.
1. set_value(self: csc.update.SettingData, value: Union[bool, int]) -> None set setting value
2. set_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) -> None set setting value

set_value(self: csc.update.SettingData, value: Union[bool, int]) -> None
> set setting value

set setting value set_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) -> None
> set setting value

set setting value Overloaded function.
1. value(self: csc.update.SettingData) -> Union[bool, int] get setting value
2. value(self: csc.update.SettingData, frame: int) -> Union[bool, int] get setting value

value(self: csc.update.SettingData) -> Union[bool, int]
> get setting value

get setting value value(self: csc.update.SettingData, frame: int) -> Union[bool, int]
> get setting value

get setting value SettingDataAttribute represents an attribute of a setting.
It can be connected with setting functions. 
SettingFunction class input attributes method that decreases input vector attribute its id method that increases input vector attribute check whether this function will make it to the resulting setting graph method that removes one in input vector attribute method that resizes input vector attribute output attributes set the state of the function, whether it will be used or not SettingFunctionAttribute represents an attribute of a setting function.
It can be connected with setting functions or data function activeness attributes. SettingFunctionAttributeId is defined by the SettingFunctionId and the index of the attribute Implements the SettingFunctionAttributeId.
- function_id – Get SettingFunctionId
- attribute_index – Get index of the attribute
- attribute_sub_index – Get index of the attribute in array

function_id – Get SettingFunctionId attribute_index – Get index of the attribute attribute_sub_index – Get index of the attribute in array 
Update class represents the whole update editor -> ObjectGroup 
UpdateGroup class represents update group node -> UpdateGroup -> ExternalProperties -> UpdateGroup{} -> RegularData{} -> RegularFunction{} -> SettingFunction{} -> SettingsData{}