# Untitled

Source: https://cascadeur.com/help/category/210

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Import FBX/DAE](https://cascadeur.com/help/getting_started/import_fbxdae)
- Working with MetaHumans

EN

# Working with MetaHumans

**On this page**

- [Exporting MetaHuman Characters](https://cascadeur.com/help/category/210#metahuman_export)
  - [Import and Rigging](https://cascadeur.com/help/category/210#metahuman_import)
- [Applying Cascadeur Animations](https://cascadeur.com/help/category/210#metahuman_cas_anim)
- [Common Issues](https://cascadeur.com/help/category/210#metahuman_issues)

Despite their complexity, MetaHuman characters operate on the same basic principles as any other 3D models. However, there are certain nuances you might encounter when you try to use such characters with Cascadeur.

This page describes the ways of dealing with these nuances.

## Exporting MetaHuman Characters

If you’d like to animate MetaHuman characters in Cascadeur, you’ll first need to _export_ them.

The most convenient way to do this is by using **Quixel Bridge**.

**1.** Open Quixel Bridge

At the moment using it is the only way to export MetaHuman characters.

Note

You need the version of Quixel Bridge compatible with the preset you’re using. For example, if you are using a UE5 MetaHuman preset, use Bridge for UE5

**2.** Open your character.

Currently, MetaHuman characters can only be exported to Maya and to Unreal Engine.

If your plan is to use your character(s) for creating animation, you’ll need to use the Maya export option.

**3.** Open **Export Settings**:

![](https://cascadeur.com/images/category/2023/09/20/df662bc74fbaed3f00311065ecf11892.png)

**4.** On the **Export Target** tab, select **Maya**:

![](https://cascadeur.com/images/category/2023/09/20/90b30ab2c3f6762e0b7e75514c4e4b78.png)

**5.** Now go to the **Models** tab and select the level of detail you’d like to export:

![](https://cascadeur.com/images/category/2023/09/20/6c674ad9667624616efd4bb917994fb8.png)

Using **LOD0** is not recommended: it might include objects (such as hair strands) not currently supported by Cascadeur.

**6.** On the same tab, set **MetaHumans** to **Source Asset**:

![](https://cascadeur.com/images/category/2023/09/20/d3dec6dec866d01ba5db759e574cd18e.png)

Now, everything is set.

**7.** Go back to the panel and click **Export**:

![](https://cascadeur.com/images/category/2023/09/20/4ece64197c630c4c26e2988980b32d24.png)

You should get a set of files compatible with Maya.

You can read more about it here:

[https://dev.epicgames.com/documentation/en-us/metahuman/exporting-metahumans-to-maya](https://dev.epicgames.com/documentation/en-us/metahuman/exporting-metahumans-to-maya)

After you get the character to Maya, simply re-export the scene to FBX format and import the file to Cascadeur.

Alternatively, you can try to export your MetaHuman characters directly from **Unreal Engine**.

To do this, you’ll need to manually export several assets that make up a MetaHuman character:

![](https://cascadeur.com/images/category/2023/09/20/412ee6be53bf9335985f0c5f14c39079.png)

**1.** Right-click the asset file.

**2.** Select **Asset Actions → Export…** from the menu:

![](https://cascadeur.com/images/category/2023/09/20/56fd9c31ed296574e6120b432a7f7138.png)

You should get an .fbx file containing the corresponding part of the character.

You'll need to repeat this procedure for every asset that make up the character

MetaHuman characters include several parts: the skeleton and several meshes, with the exact list depending on the level of detail you are using.

#### **Import and Rigging**

Once you have the assets exported, you can get them to a Cascadeur scene.

We recommend to start with importing the skeleton and then applying meshes to it.

To import the skeleton, use **File → Import Fbx/Dae → Scene**. You can import one of the exported skeleton meshes.

The problem with the meshes is that each exported skeleton mesh has a differently named root Transform object. Because of that, the skeleton hierarchies aren’t matching completely, and thus, when you use the **Add model to selected** preset to add the mesh to an existing skeleton hierarchy, a separate hierarchy would be imported instead.

This can be fixed by renaming the root Transform object already imported in the scene, to the name of the root Transform object of the skeleton mesh you want to import.

![](https://cascadeur.com/images/category/2025/02/07/052f1132bf9194ed353b3a3b7c73343e.jpg)

_Example of 2 skeleton meshes from the same Metahuman character._

_Notice the difference between the names of the root Transform objects._

For each of the meshes:

**1.** Import a second skeleton mesh with **Add Fbx/Dae → Scene**.

**2.** Select the second skeleton mesh’s root Transform object.

**3.** Copy its name in the **Object Properties** tab below.

**4.** Undo the import by selecting **Undo** from the **Edit** menu (or by pressing **Ctrl** and **Z**).

**5.** Rename the first skeleton mesh’s root Transform object with the copied name.

**6.** Switch to the **Joint Mode**.

**7.** Select the whole skeleton hierarchy.

**8.** Select **Add Fbx/Dae → Add model to selected** from the **File** menu.

**9.** Pick the same skeleton mesh file that you’ve previously imported.

**10.** Repeat steps **1-9** until the whole character is assembled.

After you do these steps for every part of the character, you should get a functioning 3D model.

Now, you need to add a rig to it.

The MetaHuman skeleton is similar to the one used in the standard UK4 and UK5 models.

You can use the [**Quick Rigging Tool**](https://cascadeur.com/help/rig/rig_mode/quick_rigging_tool) to create the base of the rig.

After the base is complete, however, you can use the regular [**Rigging Tools**](https://cascadeur.com/help/rig/rig_mode/rigging_tools) to make further adjustments - if you need them.

## Applying Cascadeur Animations

Animations created in Cascadeur can be applied to MetaHuman characters.

When you create animations to be used with MetaHuman characters, we’d recommend using models with similar structure: UE4 Mannequin for UE4 MetaHuman template, UE5 Manny/Quinn for UE5.

Once animation is complete, you’ll need to export it, so it could be applied to the character.

Recommended settings:

**FbxUpAxis** to **Z**

**TypeFbxAscii** to **Off**

Both these settings are found in the [**Settings Window**](https://cascadeur.com/help/interface/main_menu/settings_window), under the APP category:

![](https://cascadeur.com/images/category/2023/09/20/bd5a4ed4b5bb8b8fb84bc81124a1492d.png)

To export animation:

**1.** Open the **File** menu.

**2.** Select **Export Fbx/Dae → Without Meshes**:

![](https://cascadeur.com/images/category/2023/09/20/0b1002a69e034ab38b77bdbd0b7b9c99.png)

**3.** In the save file dialog, set the **FBX** format.

What you’ll get is an .fbx file containing the character skeleton and animation associated with it. This file, you can import to the engine and use the animation with your character.

However, the imported animation should be retargeted.

The nuances of retargeting animations for MetaHuman characters are described here:

[https://dev.epicgames.com/documentation/en-us/metahuman/retargeting-animations-to-a-metahuman-in-unreal-engine-5](https://dev.epicgames.com/documentation/en-us/metahuman/retargeting-animations-to-a-metahuman-in-unreal-engine-5)

## Common Issues

Sometimes when you apply animations to a MetaHuman character, a distortion like this occurs:

![](https://cascadeur.com/images/category/2023/09/20/461c25ed41de0595d9a5f588aca7736d.png)

This can be fixed by altering skeleton settings:

**1.** Open the skeleton.

**2.** Go to the **Skeleton Tree** panel.

**3.** Set **root** and **pelvis** to **Animation**.

**4.** Set all other bones to **Skeleton**:

![](https://cascadeur.com/images/category/2023/09/20/8fe1f4ac3ac36f5b783a575f2c90701d.png)

**5.** Save the skeleton.

After this, animations should work without any problems.

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

14

[No](https://cascadeur.com/help/rest/add-mark "No")

10

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)