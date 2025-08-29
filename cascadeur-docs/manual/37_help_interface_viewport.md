# Untitled

Source: https://cascadeur.com/help/interface/viewport

- [Home](https://cascadeur.com/help)
- [Interface](https://cascadeur.com/help/interface)
- Viewport

EN

# Viewport

**On this page**

- [Parts of the Viewport](https://cascadeur.com/help/interface/viewport#viewport_parts)
  - [Viewport Window](https://cascadeur.com/help/interface/viewport#viewport_viewport)
  - [Camera (View Cube)](https://cascadeur.com/help/interface/viewport#viewport_cube)
  - [Edit Mode Switch](https://cascadeur.com/help/interface/viewport#viewport_edit_modes)
  - [Align to camera](https://cascadeur.com/help/interface/viewport#viewport_align_to_camera)
  - [Camera Textures](https://cascadeur.com/help/interface/viewport#viewport_camera_textures)
  - [Visible and Selectable Menus](https://cascadeur.com/help/interface/viewport#viewport_visible_selectable)
- [Customizing Viewport](https://cascadeur.com/help/interface/viewport#viewport_customizing)
- [Detaching Viewport](https://cascadeur.com/help/interface/viewport#viewport_detaching)
- [Viewport Hot Keys](https://cascadeur.com/help/interface/viewport#viewport_hotkeys)

![](https://cascadeur.com/images/category/2024/10/17/f7f72425fe79d55ade581303e79ec3d9.png)

# Parts of the Viewport

Viewport in Cascadeur includes a number of parts:

## (1) Viewport Window

The main program window. It shows the loaded scene, which you can edit using any tool the program gives you.

By default, Viewport includes one window. This window can be split into **two** smaller ones by pressing **Shift+Spacebar** and into **four** by presing **Shift+Alt+Spacebar.**

Each one of these smaller windows can be maximized by selecting it with  **![](https://cascadeur.com/images/category/2019/06/04e916212cae20c3898819cd7986b9ccb9.png)**  and pressing **Shift+Spacebar** or **Shift+Alt+Spacebar** again **.** This way you can also restore Viewport to its initial state.

## (2) Camera (View Cube)

A scene is viewed through a virtual camera

![](https://cascadeur.com/images/category/2022/12/14/ef5486fa77ddf6dbf96b571b7efc8fd0.png)

The **Viewcube** shows the spatial orientation of the camera and can be used to quickly switch between pre-defined views.

Clicking one of the cones switches the camera to one of the six orthogonal perspectives:

**Red \- the X axis**( **front and back** for standard scenes included in Cascadeur)

**Blue \- the Z axis**( **right and left** for standard scenes)

**Green \- the Y axis**( **top and bottom**)

Clicking the cube itself switches projection modes between **perspective** and **isometric**.

If you hold **Ctrl**, moving the mouse over the View Cube would highlight its edges and vertices.

Clicking these edges and vertices would then set the camera to the corresponding perspective:

![](https://cascadeur.com/images/category/2025/06/10/7dbf13501a954595c42b370abc9f9150.gif)

The **lock symbol** locks the camera to the current position so it won't move if you try to rotate.

The locked camera can still be panned and switched between six standard perspectives.

## (3) Edit Mode Switch

This item is used for switching between [**Edit Modes**](https://cascadeur.com/help/edit_modes).

Clicking the switch enables the next Edit Mode:

![](https://cascadeur.com/images/category/2022/09/19/263c6d1c8db901cb55f69f852a248a3c.gif)

Clicking the sign at the right of the switch opens the list of all available Edit Modes:

![](https://cascadeur.com/images/category/2022/09/19/53a5e9260d0a16b47f3dacecb0ad4d61.gif)

## (4) Align to camera

This item is used for aligning the Viewport to the currently selected [Camera Object](https://cascadeur.com/help/tools/camera_tools).

Clicking the triangle icon at the right side of it opens a drop-down menu:

![](https://cascadeur.com/images/category/2023/05/24/b1fc7f8a573b50ed7c74e14b25b11d7c.png)

**Add camera**

Creates a new Camera Object.

## Camera Textures

Another common use case is adding reference images to the camera. This is different from regular [references](https://cascadeur.com/help/animation_pipeline/reference) in that such images are attached directly to the camera - not to an object in the scene - and cover the entire field of view.

This cannot be done with the default Viewport camera - but can be done with user-added [**Camera Objects**](https://cascadeur.com/help/tools/camera_tools).

See the [**Camera Textures** section](https://cascadeur.com/help/tools/camera_tools#camera_texture) (on the Camera Tools page) to learn how to do this.

## Visible and Selectable Menus

Right-clicking the Edit Mode Switch opens **Visible** and **Selectable** menus:

![](https://cascadeur.com/images/category/2022/12/14/6ed8c0310e2c2b380cb8e2a358ab846c.png)

By editing this menus, you can change what types of scene elements you can see and use in each Edit Mode.

These menus are described in greater detail on the [**Edit Modes** page](https://cascadeur.com/help/edit_modes#edit_modes_custom).

# Customizing Viewport

The characters - and any other 3d objects too - in the Viewport are lit with a set of light sources. These light sources cannot be moved, but their other parameters can be customized.

For the intensity of the lights, there  is a set of settings in the [**Settings Window**](https://cascadeur.com/help/interface/main_menu/settings_window), called [**Lights**](https://cascadeur.com/help/category/244):

![](https://cascadeur.com/images/category/2025/06/10/9c2489e9e6eacf62892388aa946ede34.png)

**Ambient Intensity**

The power of the environment light in the scene (sets the background lighting in the scene).

Set to **0.5** by default.

**Camera Intensity**

The powers of the ‘front’ light (lights the model from the camera POV).

Set to **0.3** by default.

**Ground Light Intensity**

The power of the ground light (the source that lights the model from below).

Set to **0.3** by default.

**Sky Light Intensity**

The power of the sky light (the source that lights the model from above)

Set to **0.7** by default.

There are also settings for the color of the Viewport background. These settings are not combined into a single group and can be found in the [**Visualizers**](https://cascadeur.com/help/category/257) section instead.

The ‘sky’ - the upper part of the Viewport background - is rendered as a gradient defined by two colors:

**Sky Color Light**

The lighter component of the sky gradient.

**Sky Color Dark**

The darker component of the sky gradient.

The ‘ground’, i.e. the lower part of the background, is also a gradient, and it too is defined by two colors:

**Earth Surface Color Light**

The lighter component of the ‘ground’ gradient (i.e. the lower part of the Viewport background).

**Earth Surface Color Dark**

The darker component of the ‘ground’ gradient.

**Earth Surface Color**

(TODO)

# Detaching Viewport

![](https://cascadeur.com/images/category/2024/03/19/20a33a8f6795ca96f3572abe55c4ee90.png)

There is also an option to create a separate Viewport window.

This window is independent from the main Cascadeur window, and can be useful if you, for example, work with a multi-monitor configuration.

This is done by selecting the **Viewport** option from the [**Window** menu](https://cascadeur.com/help/interface/main_menu/window_menu):

![](https://cascadeur.com/images/category/2024/03/19/5a74581919600b80edf3dd1c35d161fa.png)

# Viewport Hot Keys​

The camera can be controlled by holding the **![](https://cascadeur.com/images/category/2019/06/0490ff226511767f992bf7a3efe077d145.png)** key:

- **![](https://cascadeur.com/images/category/2019/06/0428a159c572de5f939cdd6c1504f90527.png)**  rotates the camera
- **![](https://cascadeur.com/images/category/2019/06/04026cb4d59d6c52068db3403efb6c0eac.png)**  zooms the camera in and out; this can also be done by holding **![](https://cascadeur.com/images/category/2019/06/047e29fc279ae0e0acaa54eb617ce47bac.png)** and rotating  **![](https://cascadeur.com/images/category/2019/06/04914e08b1cc6b363f9c84637f14256fef.png)**
- **![](https://cascadeur.com/images/category/2019/06/048bd5349cc122aeb00bb5a678a612da73.png)**  pans the camera
- **![](https://cascadeur.com/images/category/2019/06/04c2e6c14191ccb8eba72eaeda33248116.png)** switches camera view to the nearest orthogonal projection
- ![](https://cascadeur.com/images/category/2019/06/04143d7303caa97e14891fd16148a67630.png), ![](https://cascadeur.com/images/category/2019/06/04b7b3bc54a7dfced7e054c8721ad06034.png) and  ![](https://cascadeur.com/images/category/2019/06/04e916212cae20c3898819cd7986b9ccb9.png)  switches the plane when you move the mouse
- ![](https://cascadeur.com/images/category/2019/06/042001c533574264e44ebf97f2de8026bf.png) focuses camera on the selected object

Edit Mode hotkeys:

- **![](https://cascadeur.com/images/category/2021/02/26/87b754b3f0760f6c0e5281ffab9cc6ec.png)** toggles **View Mode**
- **![](https://cascadeur.com/images/category/2019/06/04cfe0776123e21bfe6d7baa27f673d252.png) + ![](https://cascadeur.com/images/category/2021/02/26/87b754b3f0760f6c0e5281ffab9cc6ec.png)** switches between **Point** and **Box Controller** modes
- **![](https://cascadeur.com/images/category/2019/06/04cfe0776123e21bfe6d7baa27f673d252.png) + ![](https://cascadeur.com/images/category/2021/02/26/f80735e01ea1bd576fd8d7a798e6d770.png)** separates the Viewport window in two parts
- **![](https://cascadeur.com/images/category/2019/06/04cfe0776123e21bfe6d7baa27f673d252.png) + ![](https://cascadeur.com/images/category/2019/06/04b7b3bc54a7dfced7e054c8721ad06034.png) + ![](https://cascadeur.com/images/category/2021/02/26/f80735e01ea1bd576fd8d7a798e6d770.png)** separates the Viewport window in four parts

# See Also

[Camera Tools](https://cascadeur.com/help/camera_tools)

[Main Menu](https://cascadeur.com/help/category/11)

[Toolbar](https://cascadeur.com/help/category/12)

[Selecting Objects](https://cascadeur.com/help/category/54)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

8

[No](https://cascadeur.com/help/rest/add-mark "No")

6

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)