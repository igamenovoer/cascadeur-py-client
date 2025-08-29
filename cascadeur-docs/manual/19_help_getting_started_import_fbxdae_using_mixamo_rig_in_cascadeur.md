# Untitled

Source: https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Import FBX/DAE](https://cascadeur.com/help/getting_started/import_fbxdae)
- Using Mixamo Rig in Cascadeur

EN

# Using Mixamo Rig in Cascadeur

**On this page:**

- [Model Import](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_model_import)
  - [Preparing the Arms](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_arms)
- [Rigging](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_rigging)
  - [Direction Controllers](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_direction_controllers)
  - [Finalizing the Rig](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_finalizing)
- [Animation](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_animation)
- [Example](https://cascadeur.com/help/getting_started/import_fbxdae/using_mixamo_rig_in_cascadeur#mixamo_example)

Warning

This page is intended for users who already have some experience with rigging in Cascadeur.

To learn the basics of creating rigs, check out our [tutorials](https://cascadeur.com/learn).

To learn more about rigging and rigs in general, see the [**Rig**](https://cascadeur.com/help/rig) section of the manual.

Mixamo models (both stock and custom) use standardised skeleton that can be rigged to be used in Cascadeur.

# Model Import

Start with exporting your model from Mixamo.

We recommend using either binary FBX, ASCII FBX or Collada formats. Either should work fine.

![](https://cascadeur.com/images/category/2021/05/21/518a3bf30c13597c37660e5b3f5d36d4.png)

After this, import the model to Cascadeur.

To do this, select either **Import FBX/DAE → Scene** or **Import FBX/DAE → Model** from the [**File** menu](https://cascadeur.com/help/file_menu).

![](https://cascadeur.com/images/category/2023/04/10/326d41ccc31e3d86f36a00f76f2c0293.png)

You should end up with something like this.

### Preparing the Arms

By default, character arms in Mixamo skeleton form a straight line:

![](https://cascadeur.com/images/category/2023/04/10/37837e9346649b98751c901fd64ffa58.png)

This might lead to incorrect bending in the finalized rig (see [here](https://cascadeur.com/help/hinge_connections) to learn more about it).

To prevent this from happening, you’ll need to manually fold the limbs before rigging:

**1.** Switch to the [**Joint Mode**](https://cascadeur.com/help/edit_modes).

**2.** Select the joints after the elbow.

**3.** Go to the [**Scene Settings**](https://cascadeur.com/help/scene_settings) panel.

**4.** On the **Manipulators** tab, enable the **Fix rotation step** parameter:

![](https://cascadeur.com/images/category/2023/04/10/33793a25193ccb6a3c77c1060c33042e.png)

**5.** Set the value for Fix angle ( **5**, for example).

**6.** On the **Toolbar**, set the **Local Mode** for the manipulators:

![](https://cascadeur.com/images/category/2023/04/10/c3a5aba033370ada32d6594fb8691da6.png)

**7.** Use [**Rotate**](https://cascadeur.com/help/manipulators#rig_rotate_manipulator) manipulator to bend the arm.

**8.** Do the same for the other arm.

After this, everything should be ready for rigging.

# Rigging

The base of the rig can be created using [**Quick Rigging Tool**](https://cascadeur.com/help/quick_rigging_tool).

However, it is recommended to then use the regular [**Rigging Tool**](https://cascadeur.com/help/rigging_tool) for making refinements to the prototype rig.

As usual, your goal is to create sets of [**Prototype objects**](https://cascadeur.com/help/prototype_objects) for the joints associated with your character.

### Joints

Character skeleton in Mixamo is structured similarly to the one used by standard Cascadeur models, but its structure is a bit more complex, and some of the joint names are different.

The following tables list the main joints in the Cascadeur skeleton and their counterparts in Mixamo skeleton.

|     |     |
| --- | --- |
| **Cascadeur** | **Mixamo** |
| pelvis | mixamorig:Hips |
| stomach | mixamorig:Spine |
| chest | mixamorig:Spine2 |
| neck | mixamorig:Neck |
| head | mixamorig:Head |
| clavicle\_r | mixamorig:RightShoulder |
| arm\_r | mixamorig:RightArm |
| forearm\_r | mixamorig:RightForeArm |
| hand\_r | mixamorig:RightHand |
| thigh\_r | mixamorig:RightUpLeg |
| calf\_r | mixamorig:RightLeg |
| foot\_r | mixamorig:RightFoot |
| toe\_r | mixamorig:RightToeBase |

If a joint has two or more counterparts in the Mixamo skeleton, we recommend rigging all of these joints with one set of prototypes. See [**Rigging Complex Skeletons**](https://cascadeur.com/help/rigging_complex_skeletons).

### Direction Controllers

![](https://cascadeur.com/images/category/2023/04/10/5dfe5a29c32081a6737bf8f0df6e29e2.png)

[**Direction Controllers**](https://cascadeur.com/help/direction_controllers) in elbows should face backwards for the arms to bend properly. In the case one of them faces the opposite direction:

**1.** Select the prototype [**Point Controller**](https://cascadeur.com/help/point_controllers) in the corresponding elbow.

**2.** In the [**Outliner**](https://cascadeur.com/help/outliner), open the **Hinge settings** behavior tab.

**3.** Disable **Direction controller is right**:

![](https://cascadeur.com/images/category/2023/04/10/4384122f6640df76569f2068d7213cde.png)

After this both controllers will be facing the right direction:

![](https://cascadeur.com/images/category/2023/04/10/44446c7fa91c4d93c9b662db73001ea8.png)

### Finalizing the Rig

Once everything is set, click **Generate rig**:

![](https://cascadeur.com/images/category/2023/02/20/d90cc0b762a3e814641a5982bde625d4.png)

Then wait a bit, and your character should be fully rigged and ready for animation.

# Animation

To add animation to a Mixamo character:

**1.** Select **File → Import Fbx/Dae → Animation**:

![](https://cascadeur.com/images/category/2023/02/20/55b490736526d3cc4b18ff96b81d242b.png)

**2.** Specify the file (in FBX or Collada format) containing the animation.

After this, the animation should be imported and applied to the character.

To learn more about importing animation see [here](https://cascadeur.com/help/import_fbxdae#import_animations).

# Example

Mixamo to Cascadeur - Using Custom Characters - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[Mixamo to Cascadeur - Using Custom Characters](https://www.youtube.com/watch?v=SZHVubEDifk)

Cascadeur — Reinventing Animation

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=SZHVubEDifk&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 7:24
•Live

•

## See Also

[Import FBX/DAE](https://cascadeur.com/help/import_fbxdae)

[Rig](https://cascadeur.com/help/rig)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

9

[No](https://cascadeur.com/help/rest/add-mark "No")

2

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)