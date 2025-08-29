# Untitled

Source: https://cascadeur.com/help/getting_started/import_fbxdae

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- Import FBX/DAE

EN

# Import FBX/DAE

**On this page**

- [Import FBX/DAE](https://cascadeur.com/help/getting_started/import_fbxdae#import_fbx_dae)
- [Import Textures](https://cascadeur.com/help/getting_started/import_fbxdae#import_textures)
- [Animated Textures](https://cascadeur.com/help/getting_started/import_fbxdae#animated_textures)
- [Import Issues](https://cascadeur.com/help/getting_started/import_fbxdae#import_issues)

Cascadeur works with various file formats that you can import from other software.

The following types of objects can be imported:

- [3d meshes](https://cascadeur.com/help/category/26)
- [Joints](https://cascadeur.com/help/category/20)
- Joint animations
- [Textures (separately)](https://cascadeur.com/help/category/26#mesh_mode_textures)

# Import FBX/DAE

**1.** Select **Import → Fbx/Dae** from the [**File** menu](https://cascadeur.com/help/interface/main_menu/file_menu).

**2.** The **FBX/DAE Import** dialog window will appear:

![](https://cascadeur.com/images/category/2025/05/19/2bdeec459c38c1ce6c86cba9c8b5d64d.png)

In this window, you can set up parameters that define the exact way of how a file should be added to the scene.

#### **Presets**

Here, you can select one of the predefined setting schemes, each one optimized for a particular task.

There are several available variants:

**Animation** is for importing animation data to the skeleton hierarchy present in the Cascadeur scene.

**Animation to selected frames** imports animation data to the skeleton hierarchy present in the Cascadeur scene and applies it to the frames that are currently selected on the [**Timeline**](https://cascadeur.com/help/interface/timeline).

**Animation to selected objects** also imports animation data, but applies it to the currently selected objects in the scene.

**Model** is for importing only the 3d meshes without animation attached to them.

**Scene** imports the entire Casacdeur scene.

## IMPORT

This section contains settings that define how exactly should the model be added to the scene.

**Import to selected joints**

If this option is enabled, the model is applied only to the selected Joints.

Can be used when, for example, you need to use different meshes for several identical skeletons.

**Import to selected interval**

If this option is enabled, the imported animation is applied only to the selected part of the Timeline.

## INCLUDE

This section contains settings that define what parts of the model should be added to the scene.

**Animation**

If this option is enabled, animation data from the imported file is applied to the current scene.

**Meshes**

If this option is enabled, the 3d objects from the imported file are added to the current scene.

**Blenshapes**

If this option is enabled, the blendshape data stored in the imported file is added with the imported 3d objects.

## Settings

**Fbx up axis**

Sets the axis that should be considered the up axis when the FBX file is brought to the scene.

There are two options: **Z** and **Y**. By default, the **Y** axis is selected.

**Adjust axis system on import**

If this option is enabled, Cascadeur converts the coordinate system when a 3D model is imported to the scene: if the model has the **Z** axis pointed upward, the system is changed so the **Y** axis would be up.

There are three possible options for this parameter:

● **Off** means it is ignored and doesn’t affect anything.

● If it is set to **Root**, the axes are adjusted on the basis of the root object, i.e. the object with the highest position in the hierarchy.

● And if it is set to **Deep**, the root object is ignored, and the next object in the hierarchy is used instead. This can be used when, for example, when imported scenes display incorrect rotation.

Root is the default value.

**Triangulate on import**

If this is enabled, the imported model is triangulated: every polygon with more than 3 vertices is divided into a set of triangles.

Disabled by default.

**Fbx compatibility version**

The version of the FBX format used for export.

The default version is **2020**.

**Change start frame**

If this option is enabled, you can specify the first frame of the imported animation. This can be used, for example, when the initial frames are empty (and thus not needed), or when you have multiple animations combined into one sequence.

If it is left unchecked, the animation is imported starting with frame **0**.

Disabled by default.

**Open first take**

If this option is enabled, the first _take_ (animation clip) is applied when the file is imported to the scene (if the file has multiple takes).

If it is disabled, you’ll get a list of all takes in the file and can manually select one of them.

Disabled by default.

**Leave dialog open**

If this is enabled, the import window is left open after the file is imported to the scene. Otherwise, it is closed.

Disabled by default.

Once you’ve finished setting the import options, click the Import button and choose the file you’d like to add into the scene:

![](https://cascadeur.com/images/category/2025/01/24/c391dbd456f50862e43e65396df3d86a.png)

# Import Textures

Warning

By default, the texture tool is **disabled** on the Toolbar.

To make it accessible, open the [**Settings Window**](https://cascadeur.com/help/interface/main_menu/settings_window) and enable the tool in the **Toolbar Visible** section.

Menu options, however, are always available.

To add a texture to a model:

**1.** Switch to the **Mesh Mode**.

![](https://cascadeur.com/images/category/2023/02/20/b0b099ccbd7f1397bb2f6db7f4f3d6ba.png)

**2.** In the **Viewport**, select a mesh

**3.** Click the **Bind texture** button:

![](https://cascadeur.com/images/category/2023/02/20/912fd7f4fd4c34eb165e42c14544365b.png)

...or select **Bind texture** from the [**View** menu](https://cascadeur.com/help/interface/main_menu/view_menu).

**4.** Select the image file containing the texture.

**Png**, **bmp**, **tga** and **jpeg** image formats are supported.

After this, the texture should appear on the model.

To remove a texture from a model:

**1.** Select the mesh.

**2.** Click the **Unbind texture** button

![](https://cascadeur.com/images/category/2023/02/20/d587fa85ddeb885dbd02151ed927873a.png)

...or select **Unbind Texture** from the **View** menu.

After this, the texture should be removed from the model.

# Animated Textures

You can also import animated textures. There are two ways to do this:

First, you can import a video file as a texture.

To do this:

**1.** Select **File → Import → Reference video**.

**2.** Select a video file.

Currently, only the **.mp4** files are supported.

After this, a plane containing the video should appear in the scene.

This option is only intended for setting up animated references. It won't work with character models.

So if you'd like to apply an animated texture to a character, you should follow a different set of steps:

**1.** Prepare a sequence of images named something like this:

**tex\_000.png**, **tex\_001.png**, **tex\_002**.png and so on.

**2.** In Cascadeur, switch to the **Mesh Mode**.

**3.** Select a mesh.

**4.** Click the **Bind texture** button.

**5.** Select every file you want to use for your animated texture.

After this, the texture should be applied to the model. One file of the sequence is equal to one frame of animation

# Common Problems

**Incorrect Scale**

If a model is imported with an incorrect scale, this can be fixed in two ways:

You can scale the model manually, using the **Scale** manipulator

If the model is skinned to a skeleton, you can scale either the first object in the model's whole hierarchy (i.e. an Armature) or the first joint in the model's skeleton hierarchy (i.e. a 'root' joint).

If the model consists of just the mesh, you can scale the mesh object.Alternatively, you can change the selected object's **Local Scale** value, which can be accessed in the **Object properties** window, in the **Transform** behavior.

**Error in pasting animation or timeline data**

Make sure that your imported animation and the model in the scene have the same skeleton hierarchy (the set of joints).

The ' **Animation**', ' **Animation to selected frames**' and ' **Animation to selected objects**' presets import and apply animation data to the exact skeleton hierarchies present in the current scene and the animation file.

The animation may fail to import if the scene skeleton hierarchy’s joint order or naming scheme is significantly different.

If the skeleton in the animation file has the same naming scheme, but different proportions, the animation may get imported incorrectly.

The animation import can fail if the root objects (the first object in the skeleton hierarchy) in the scene and the animation file have different names, even though the rest of the joints are exactly the same. In that case, try selecting just the actual joint hierarchy of your character model and using the ' **Animation to selected objects**' preset.

If the animation import continues to fail, import the animation data with the ' **Scene**' preset into the current or new Cascadeur scene and compare the source and the target skeleton hierarchies. If their joint order, naming scheme or proportions are noticeably different, you may need to use the [**Retargeting**](https://cascadeur.com/help/category/219) tool to transfer animation between two different skeleton hierarchies.

**Incorrect Import from Unreal Engine**

If you are experiencing problems trying to import animation from Unreal Engine to Cascadeur, please consult [**this page**](https://cascadeur.com/help/category/80).

## See Also

[Export FBX/DAE](https://cascadeur.com/help/category/76)

[Import Animation from Unreal Engine](https://cascadeur.com/help/category/80)

[Import from Blender](https://cascadeur.com/help/category/93)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

13

[No](https://cascadeur.com/help/rest/add-mark "No")

18

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)