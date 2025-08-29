# Untitled

Source: https://cascadeur.com/help/category/192

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Export FBX/DAE](https://cascadeur.com/help/getting_started/export_fbxdae)
- Export to Daz Studio

EN

# Export to Daz Studio

Once you’ve finished animating a [Daz Studio character](https://cascadeur.com/help/getting_started/import_fbxdae/import_from_daz_studio), you’d probably want to send this character back to Daz Studio for rendering.

This can be done by following these steps:

**1.** On the [**Timeline**](https://cascadeur.com/help/interface/timeline), select an interval with an animation you'd like to export.

**2.** Select the **Export to DAZ** command from the [**Commands** menu](https://cascadeur.com/help/interface/main_menu/commands_menu):

![](https://cascadeur.com/images/category/2023/02/28/5a820c20f29391c407ed091bce1c0420.png)

**3.** In the appeared dialog message, click on "Export selected frames".

This command will export the joints and animation - if there is any - attached to them. The mesh(es) will be ignored.

The "Export to DAZ" command does the following things:

**1.** Moves ever single point controller of the character's control rig, on each selected frame, by the local position of the Hip joint in the scene's "Base Pose" - the pose that the character was using while in Rig Mode.

**2.** Turns off export for translation and scale channels of all body joints.

**3.** Turns off export for the translation, rotation, and scale channels of all face joints, as well as both Pectoral joints.

Note

The effect of the command can be replicated manually, but doing this is cumbersome and is not recommended.

Warning

If you're using Cascadeur 2024.3.3 or earlier and Daz Studio 4.23+, download the [corrected "Export to DAZ" script](https://drive.google.com/file/d/1RAMsYkF9238btZnHXRksXE9MKvW5gVaz/view)

Put this corrected .py file in **\[Your Cascadeur directoty\]\\resources\\scripts\\python\\commands** folder.

Daz Studio 4.23 uses the "model pose" as a reference pose for its imported FBX animations, which isn't included with the exported skeleton animations in Cascadeur 2024.3.3 and earlier. To mitigate that, Daz animation has to be exported with the character mesh, to allow Daz to extract the "model pose" from the mesh's "bind pose".

# Importing the animation back to Daz Studio

Once you have successfully exported your animated Daz character from Cascadeur, you can import the animation back to Daz studio:

**1.** Open an empty scene in Daz Studio

**2.** Import your animation using the **"File -> Import..."** command

**3.** In the Import options window, turn on the **“Include Animation”** setting and in the dropdown menu below **select the name of the animation take**

**4.** Save the animation as a Pose Preset using the **File -> Save as… -> Pose Preset** command.

![](<Base64-Image-Removed>)

**5.** Create a new empty scene

**6.** Add the character figure that you’ve previously exported from Daz Studio to the scene

**7.** Run the [Daz script "Prepare figure for animation"](https://www.dropbox.com/s/pjojvrnymcdi388/Prepare%20Figure%20For%20Animation.dse?dl=0) by double-clicking the script file while the Daz Studio window is active

Note

This Daz script turns off the Rotation locks and Rotation limits on all joints of the character figure, ensuring that the imported animation plays exactly as it does in Cascadeur

**8.** Switch to the Content Library tab and find the saved Pose Preset in the **“My Library -> Presets -> Poses”** folder.

**9.** Select the figure in the Scene Outliner window, then double-click on the saved Pose Preset to apply the animation to the character figure

**10.** When prompted with the “Preset Exceeds Limits” message, click the **“Leave limits on”** button

If the “Preset Exceeds Limits” message is missing for you, check that you have the "Show the Preset Exceeds Limits dialog" setting turned on

![](<Base64-Image-Removed>)

# Example

Cascadeur to Daz 3D - How to Export Animation - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[Cascadeur to Daz 3D - How to Export Animation](https://www.youtube.com/watch?v=wHiKCx8nj5k)

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

[Watch on](https://www.youtube.com/watch?v=wHiKCx8nj5k&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 1:08
•Live

•

How to Import and Export Animation Between Cascadeur and Daz 3D - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[How to Import and Export Animation Between Cascadeur and Daz 3D](https://www.youtube.com/watch?v=Cs_dL6L_OaA)

Cascadeur — Reinventing Animation

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=Cs_dL6L_OaA&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 8:01
•Live

•

## See Also

[Import FBX/DAE](https://cascadeur.com/help/import_fbxdae)

[Import from Daz Studio](https://cascadeur.com/help/getting_started/import_fbxdae/import_from_daz_studio)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

9

[No](https://cascadeur.com/help/rest/add-mark "No")

0

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)