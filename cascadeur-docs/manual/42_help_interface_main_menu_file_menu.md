# Untitled

Source: https://cascadeur.com/help/interface/main_menu/file_menu

- [Home](https://cascadeur.com/help)
- [Interface](https://cascadeur.com/help/interface)
- [Main Menu](https://cascadeur.com/help/interface/main_menu)
- File Menu

EN

# File Menu

![](https://cascadeur.com/images/category/2025/05/05/4c347c17a511addbef6cf861fad39e33.png)

Contains options for managing files and [Scenes](https://cascadeur.com/help/getting_started/scenes).

**New scene**

Creates an empty scene.

**Open**

Opens an existing scene.

**Open Autosave File...**

Opens an autosave file.

**Save**

Saves the currently open scene.

**Save As...**

Saves the currently open scene under a different name.

**Save As New Version**

Allows you to save the current scene using either an old (.csc) or a new (.casc) file format. Used for migrating scenes between versions.

**Save As... (no assets)**

Saves the scene without the 3d [**Meshes**](https://cascadeur.com/help/rig/rig_structure/rig_elements/meshes).

Can be used to reduce the size of the saved file.

**Recent files**

The list of the recently used scenes.

## Import

![](https://cascadeur.com/images/category/2025/05/05/307ab987361b08f484d8e42bfa198ba1.png)

These options are used for importing 3d models into scenes.

**Import Fbx/Dae**

Opens a [dialog for importing FBX/Collada files](https://cascadeur.com/help/getting_started/import_fbxdae) into the scene.

**Import Usd**

![](https://cascadeur.com/images/category/2025/05/05/32bb2074bdf872be8031c3dbf382ff58.png)

This section contains options for imporing _.usd_ files into Cascadeur scene.

**Import Animation Usd...**

Adds animation to the model(s) in the scene.

3d objects (if present in the file) are ignored.

**Import Model Usd...**

Adds 3d model(s) in the file to the scene.

Animation data is ignored.

**Import Scene Usd...**

Appends the entire content of the file (3d objects and animation) to the currently opened scene.

**Import Scene To Current**

Appends a Cascadeur scene ( _.casc_ file) to the current scene.

**Import Selection Groups**

Imports [**selection groups**](https://cascadeur.com/help/selector_tool#selection_groups) and applies them to the current scene.

The selection groups should be saved as a JSON file beforehand (using **File → Export → Selection groups**).

**Reference video**

Imports a video file and sets it up to be used as a reference for creating animation.

**Audio**

Imports an audio file to the scene.

**Import Glb/Gltf**

Opens a [dialog for importing GLB/GLTF files](https://cascadeur.com/help/category/282) into the scene.

## Export

![](https://cascadeur.com/images/category/2025/05/05/88cea0f7dd685b4dc1ab46ebaa78fade.png)

This is a set of options for exporting Cascadeur scenes to external 3d formats.

**Export Fbx/Dae**

Opens a [dialogue for exporting Cascadeur scenes](https://cascadeur.com/help/getting_started/export_fbxdae) into FBX/Collada files.

**Export Usd**

![](https://cascadeur.com/images/category/2025/05/05/826fb1a4c426eb95ec34f97e78d2080c.png)

A set of options for exporting Cascadeus scenes into _.usd_ format.

**Export Model Usd...**

Saves the character model(s) into .usd format. Animation is not included.

**Export Scene Usd...**

Saves the whole scene into .usd format, including character models, joints, animation data and additional objects.

**Export Video**

Renders the current scene as a video sequence. This feature is described [here](https://cascadeur.com/help/export_fbxdae#export_video) in greater detail.

**Export Selection Groups...**

Saves the [**selection groups**](https://cascadeur.com/help/selector_tool#selection_groups) present in the scene as a JSON file to be used in different scenes.

**Export Glb/Gltf**

Opens a [dialog for exporting Cascadeur scenes](https://cascadeur.com/help/category/283) to GLB/GLTF file format.

**Fix Scene**

Adjusts outdates scenes to properly work with newer versions of Cascadeur.

Makes some adjustments to the scene:

● Changes the object types in accordance with the behaviors associated with them.

● Adds **Is exported**, **Export translate animation**, **Export rotate animation**, **Export scale animation** and **Use namespace** settings to the objects (might be necessary for FBX export).

● Adds **Render layer**, **Is both side**, **Always show textures**, **Ignore joint visibility** and **Is transparent** settings to the Mesh objects.

● Fixes camera by changing the FOV setting to work with degrees (instead of radians).

● Adds Node3d behaviors to the objects that don’t have them.

● Sets the _model pose_ based on the current frame.

However, the recommended way of dealing with such scenes is to regenerate the rig from proto components.

**Home**

Opens the [**Splash Window**](https://cascadeur.com/help/interface/splash_window).

**Exit**

Closes Cascadeur.

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

7

[No](https://cascadeur.com/help/rest/add-mark "No")

2

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)