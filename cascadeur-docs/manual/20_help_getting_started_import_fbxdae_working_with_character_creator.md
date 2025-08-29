# Untitled

Source: https://cascadeur.com/help/getting_started/import_fbxdae/working_with_character_creator

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Import FBX/DAE](https://cascadeur.com/help/getting_started/import_fbxdae)
- Working With Character Creator

EN

# Working With Character Creator

Warning

This page is intended for users who already have some experience with rigging in Cascadeur.

To learn the basics of creating rigs, check out our [tutorials](https://cascadeur.com/learn).

To learn more about rigging and rigs in general, see the [**Rig**](https://cascadeur.com/help/rig) section of the manual.

The process of importing Character Creator models to Cascadeur is similar to the regular import process, but with some important differences.

# Model Import

Start with exporting your model from Character Creator to FBX format.

You can use any preset, all of them should work without issues.

If you don’t need animation, we recommend setting the first parameter in the **FBX Options** tab to **Mesh**:

![](https://cascadeur.com/images/category/2021/12/08/634325c960cdc749f4412c9f1aa8b4dc.png)

Note

By default, Character Creator exports animation with 60 fps, while Cascadeur uses 30 fps. To avoid possible inconsistencies, we recommend using one setting for both programs.

• If you are planning to use 30 fps animation, set Frame Rate to 30 during export.

• If you are planning to use 60 fps, set an empty Cascadeur scene to 60 fps before importing the model.

Once you have an FBX file, import it to Cascadeur.To do this, select either **Import FBX/DAE → Scene** or **Import FBX/DAE → Model** from the [**File** menu](https://cascadeur.com/help/file_menu).

The model should appear in the scene:

![](https://cascadeur.com/images/category/2023/02/27/cbda9eaadde5dbf5663ec6104239182e.png)

However, to be able to properly animate the model in Cascadeur, you’ll need to create a rig for it.

# Preparing For Rigging

By default, models from Character Creator have their limbs forming straight lines.

Rigging a model like this would lead to issues with [**Direction Controllers**](https://cascadeur.com/help/direction_controllers). So for the rig to work properly we need to give the limbs a slight bend:

**1.** Switch to the **Joint Mode**.

**2.** Go to the [**Scene settings** panel](https://cascadeur.com/help/scene_settings).

**3.** On the [**Manipulators**](https://cascadeur.com/help/manipulators) tab, enable **Fix rotation step** and set the value to something like **5**:

![](https://cascadeur.com/images/category/2023/02/27/5fb21572a592beeb5eee639315824f33.png)

**4.** Select a limb.

**5.** Use the **Rotate** manipulator to bend it:

![](https://cascadeur.com/images/category/2021/12/08/7baea9c371156eb74a651cfa1569d792.gif)

This should be done for both arms and legs

# Creating the Rig

Now you can proceed to rig the character. The easiest way to do this is to use the [**Quick Rigging Tool**](https://cascadeur.com/help/quick_rigging_tool):

**1.** Turn on the Rig Mode:

![](https://cascadeur.com/images/category/2023/02/27/610d197a951525efb00b76bbf209e388.png)

**2.** The **Rigging Tools** window should appear:

![](https://cascadeur.com/images/category/2023/02/27/342584f3a12f01f228dd61a930b6432f.png)

**3.** There, click the **Quick Rigging Tool** button:

![](https://cascadeur.com/images/category/2023/02/27/d2faaf10b633615adf67a714aa48d041.png)

The **Quick Rigging Tool** window will appear:

![](https://cascadeur.com/images/category/2023/02/27/b853e84cb2e605101b7b7ef15d605c84.png)

In this window, you’ll need to set an appropriate joint for every point/slot.

See the [**Quick Rigging Tool** page](https://cascadeur.com/help/quick_rigging_tool) to learn more about doing this.

If you are using one of the standard Character Creator models, joints will be assigned automatically. If you rig a more customized character, you’ll have to assign them manually.

However, you don’t have to rig every joint. For example:

![](https://cascadeur.com/images/category/2023/02/27/44d1a781f6e48afb03e4a7554b725a42.png)

The Standard Character Creator skeleton starts with a **root joint**. Joints like these are sometimes used for moving the character as a whole, but for Cascadeur rig, they are not necessary. We recommend to ignore the root and start rigging from the next joint in the hierarchy (named **pelvis**).

_**Warning**_

Before you start creating a rig for your character, make sure that the character’s feet touch the ground level. If this is not the case, you should manually position the character on the ground.

When the feet don’t touch the ground in their default position, the AutoPosing feature won’t be able to handle them properly.

# Joints

The structure of the Cascadeur rig is similar to that of the one in Character Creator, but there are some differences.

The following table lists the joints in the Cascadeur rig and their counterparts in the CC:

|     |     |
| --- | --- |
| **Cascadeur** | **Character Creator** |
| pelvis | Hip |
| stomach | Spine01 |
| chest | Spine02 |
| neck | NeckTwist01 |
| head | Head |
| clavicle\_r | R\_Clavicle |
| arm\_r | R\_Upperarm |
| forearm\_r | R\_Forearm |
| hand\_r | R\_Hand |
| thigh\_r | R\_Thigh |
| calf\_r | R\_Calf |
| foot\_r | R\_Foot |
| toe\_r | R\_ToeBase |

Skeletons in Character Creator are symmetrical. This means that you only need to rig the limbs on one side and then simply mirror them for the other.

This is not required, but can greatly speed up the rigging process.

See the [**Quick Rigging Tool** page](https://cascadeur.com/help/quick_rigging_tool) to learn more about limb mirroring.

Once you set all of the joints, click **Add rig elements**:

![](https://cascadeur.com/images/category/2023/02/27/e87a90075d6328603251ee0adb66e8ca.png)

Then close the Quick Rigging Tool window. You should see the character model with sets of prototype objects attached:

![](https://cascadeur.com/images/category/2023/02/27/96eaa6a19ca6ccf2e99d6ec8ccf4868f.png)

Now, the only thing left is to finalize the rig. To do this, click the **Generate rig** button at the bottom of the Rigging tools panel:

![](https://cascadeur.com/images/category/2023/02/27/13cbe08e1e74e2f3d1d76cb703450c35.png)

The end result should be something like this:

![](https://cascadeur.com/images/category/2023/02/27/d1d8baf487cbc8d98844afbf99e33c40.png)

Now your character is properly riggen and can be used in Cascadeur.

# Example

AccuRIG to Cascadeur - How to Rig a Character - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[AccuRIG to Cascadeur - How to Rig a Character](https://www.youtube.com/watch?v=v6q2aqcy9j0)

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

[Watch on](https://www.youtube.com/watch?v=v6q2aqcy9j0&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 2:03
•Live

•

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

12

[No](https://cascadeur.com/help/rest/add-mark "No")

18

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)