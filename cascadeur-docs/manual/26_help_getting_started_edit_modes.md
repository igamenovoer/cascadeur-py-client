# Untitled

Source: https://cascadeur.com/help/getting_started/edit_modes

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- Edit Modes

EN

# Edit Modes

**On this page**

- [Available Edit Modes](https://cascadeur.com/help/getting_started/edit_modes#available_edit_modes)
- [Customizing Edit Modes](https://cascadeur.com/help/getting_started/edit_modes#edit_modes_custom)
  - [Visible Menu](https://cascadeur.com/help/getting_started/edit_modes#visible_menu)
  - [Selectable Menu](https://cascadeur.com/help/getting_started/edit_modes#selectable_menu)

As working with an entire rig can be cumbersome and inconvenient, Cascadeur includes several **Edit Modes**. Each edit mode makes available for editing only some types of controllers, and each edit mode is better suited for a particular task. Using different modes for different purposes is necessary for fast and efficient work with character poses.

Edit modes are selected by clicking buttons on the dedicated panel right below the [**Toolbar**](https://cascadeur.com/help/interface/toolbar):

![](https://cascadeur.com/images/category/2023/03/01/1bab294bef3294694e76c8b06350bb5b.png)

_Panel for selecting **Edit Modes** on the Toolbar_

## Available Edit Modes

There is a total of seven edit modes:

|     |     |     |
| --- | --- | --- |
| ![](https://cascadeur.com/images/category/2023/03/01/9d0823c1cc45efcd239a0b825f10309d.png) | [![](https://cascadeur.com/images/category/2023/03/01/ae34ade5e88befcd6847ff900c775560.png)](https://cascadeur.com/help/autoposing) | [![](https://cascadeur.com/images/category/2023/03/01/de7c525afefd3378e4e82e5580bc291b.png)](https://cascadeur.com/help/category/18) |
| **View Mode** only shows the model itself with no controllers. | [**AutoPosing**](https://cascadeur.com/help/autoposing) mode is used for automated pose generation | [**Point Controller**](https://cascadeur.com/help/category/18) mode is the main mode for editing poses |

|     |     |     |
| --- | --- | --- |
| [![](https://cascadeur.com/images/category/2023/03/01/126d093aa12ef643bdae4dbd760e79de.png)](https://cascadeur.com/help/category/19) | [![](https://cascadeur.com/images/category/2023/03/01/9b2da9b898cbab2374eee999829bbf1f.png)](https://cascadeur.com/help/category/20) | [![](https://cascadeur.com/images/category/2023/03/01/417643bc934e32e4e17fb68c888c45d4.png)](https://cascadeur.com/help/category/26) |
| [**Box Controller**](https://cascadeur.com/help/category/19) mode is used for adjusting fine details such as fingers or cloth parts | [**Joint Mode**](https://cascadeur.com/help/category/20) shows character armature | **Mesh Mode** is used for working with [meshes](http://cascadeur.com/help/category/26) |
| [![](https://cascadeur.com/images/category/2023/03/01/ab8757cd55772970f85dcc5f3ef636b7.png)](https://cascadeur.com/help/category/45) |  |  |
| **Rigging view Mode** displays [**character rigs**](https://cascadeur.com/help/category/45) |  |  |

## Customizing Edit Modes

By default, every edit mode has its own preset of elements available for editing. These presets, however, can be fully customized by using the **Visible** (which defines what types of objects are visible) and **Selectable** (defines object types available for editing) menus.

To access these menus, **right-click** the **Edit Mode** indicator below the Toolbar:

![](https://cascadeur.com/images/category/2023/03/01/7261fde5ff0883232b8aef101d3aabba.png)

**Visible Menu**

This menu lists every object type that can be present in a scene:

These elements are:

|     |     |     |
| --- | --- | --- |
| [Box Controllers](https://cascadeur.com/help/category/19) | [Center of Mass](https://cascadeur.com/help/category/39) | [Joints](https://cascadeur.com/help/category/20) |
| [Point Controllers](https://cascadeur.com/help/category/18) | [Ballistic Trajectories](https://cascadeur.com/help/category/42) | [Shaded Meshes](https://cascadeur.com/help/category/26) |
| [Edges](https://cascadeur.com/help/category/50) | [Object Trajectories](https://cascadeur.com/help/trajectories) | [Wireframe Meshes](https://cascadeur.com/help/category/26#meshes_wireframe) |
| [AutoPosing Controllers](https://cascadeur.com/help/autoposing) | [Angular Momentums](https://cascadeur.com/help/category/40) | [Textures](https://cascadeur.com/help/category/26#mesh_mode_textures) |
| [Rigid Bodies](https://cascadeur.com/help/category/25) | [Angular Momentum Ghosts](https://cascadeur.com/help/category/40#angmom_ghosts) | [Camera Objects](https://cascadeur.com/help/category/29#camera_objects) |
| [Prototype Objects](https://cascadeur.com/help/prototype_objects) |

By checking items on this list you can enable rendering of corresponding object types in the [**Viewport** window](https://cascadeur.com/help/interface/viewport).

The menu also includes the **X-Ray** feature. When it is enabled, Prototype Objects are always visible, even if they are obscured by meshes and other objects. This feature is used on the rigging stage.

#### **Selectable Menu**

This menu allows you to define which types of objects in the scene can be made selectable in the **Viewport**.

It contains the same list of objects as the **Visible** menu. Checking items on this list marks object types as _selectable_, i.e. ones that you can [select](https://cascadeur.com/help/category/54) in the Viewport.

_**Note:** Even if an object is not marked as selectable, it can still be selected in the [**Outliner**](https://cascadeur.com/help/category/56) window._

Using these two menus allows you to completely change the appearance of the Viewport window and the set of objects to work with.

All changes made to the visible and selecteble lists can be reverted by selecting **Reset all to factory settings** from the [**Settings** menu](https://cascadeur.com/help/interface/main_menu/settings_menu).

## See Also

[Rig Structure](https://cascadeur.com/help/category/17)

[Scenes](https://cascadeur.com/help/category/29)

[Manipulators](https://cascadeur.com/help/category/27)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

6

[No](https://cascadeur.com/help/rest/add-mark "No")

3

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)