# Untitled

Source: https://cascadeur.com/help/getting_started/scenes/scenes_with_multiple_characters

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Scenes](https://cascadeur.com/help/getting_started/scenes)
- Scenes with Multiple Characters

EN

# Scenes with Multiple Characters

**On this page**

- [Getting Started](https://cascadeur.com/help/getting_started/scenes/scenes_with_multiple_characters#multiple_charactrs_getting)
- [Importing Characters](https://cascadeur.com/help/getting_started/scenes/scenes_with_multiple_characters#multiple_characters_importing)
- [Namespaces](https://cascadeur.com/help/getting_started/scenes/scenes_with_multiple_characters#multiple_characters_namespaces)
- [Example](https://cascadeur.com/help/getting_started/scenes/scenes_with_multiple_characters#multiple_characters_example)

Sometimes you might need more than one character in your scene. This page describes how this can be achieved.

# Getting Started

Start with opening a scene containing one character:

![](https://cascadeur.com/images/category/2023/04/10/ef8ffbafcb9baa1e84cc2c7394f3b229.png)

Here we are using the _Standard\_model\_male.casc_ file from the standard Cascadeur package as an example.

# Importing Characters

Now you can add the second character.

**1.** Select **Import → Import Fbx/Dae** from the [**File**](https://cascadeur.com/help/file_menu) menu:

![](https://cascadeur.com/images/category/2025/02/17/e55a567dc1817a5605768040e517ca82.png)

**2.** Select the _.casc_ file containing the second character.

Now the second character should appear in the scene.

![](https://cascadeur.com/images/category/2025/02/17/a87a90be534a4bafaa1ad1f3366d9b59.png)

But as you can see, the imported character appears at the center of the scene: the place already occupied by the first character.

To move a character:

**3.** Switch to the [**Point Controller** Mode](https://cascadeur.com/help/edit_modes).

**4.** Select every the character's [**Center of Mass**](https://cascadeur.com/help/tools/physics_tools/center_of_mass).

**5.** Use the [**Translate** manipulator](https://cascadeur.com/help/manipulators#rig_translate_manipulator) to move the character.

![](https://cascadeur.com/images/category/2025/02/17/e4cc4bc7ebf1b82ceaccc4bd8106b122.gif)

Repeat these steps for every character you’d like to add to the scene.

# Namespaces

Imported characters are automatically assigned namespaces: the first imported character gets _character\_1_ namespace, the second is _character\_2_ and so on.

This is done to avoid naming conflicts. In a Cascadeur scene, you can use one name for several objects without issues; however, if you try to export such a scene into FBX or Collada format, this will lead to conflicts.

Note

These namespaces do not take into account the character or characters that are in the scene from the start.

You can manually change namespace for any odject. To do this:

**1.** Select an object.

**2.** Use the **Change namespace** option from the [**Commands** menu](https://cascadeur.com/help/interface/main_menu/commands_menu):

![](https://cascadeur.com/images/category/2023/04/10/de0c6be7a9dd2d90ed330a9dbfd9be3b.png)

**3.** Set the new namespace for the object you've selected.

And this is all there is to know about setting up scenes with multiple characters.

**However:** keep in mind that populating the scene with a large number of characters may cause slowdowns.

If your system is unable to process as many characters as you need, you might try to use [**Scene Linking Tool**](https://cascadeur.com/help/scene_linking_tool).

# Example

How to Animate 2 Characters in Cascadeur \| Contact Pair Animation - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[How to Animate 2 Characters in Cascadeur \| Contact Pair Animation](https://www.youtube.com/watch?v=gumcvLfNnDM)

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

[Watch on](https://www.youtube.com/watch?v=gumcvLfNnDM&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 19:30
•Live

•

## See Also

[Scenes](https://cascadeur.com/help/scenes)

[Animation Tracks](https://cascadeur.com/help/animation_tracks)

[Scene Linking Tool](https://cascadeur.com/help/scene_linking_tool)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

12

[No](https://cascadeur.com/help/rest/add-mark "No")

0

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)