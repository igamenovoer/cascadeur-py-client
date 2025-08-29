# Untitled

Source: https://cascadeur.com/help/category/280

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Export FBX/DAE](https://cascadeur.com/help/getting_started/export_fbxdae)
- Export to Roblox Studio

EN

# Export to Roblox Studio

# Exporting the Animation

After you finish animating your Roblox character, you can export the animation back to Roblox Studio.

This can be done with the following steps:

**1.** On the [**Timeline**](https://cascadeur.com/help/interface/timeline), select an interval with your animation.

**2.** In the scenes’s [**Viewport**](https://cascadeur.com/help/interface/viewport), select one object belonging to your character’s control rig (e.g. a [**Center of Mass**](https://cascadeur.com/help/tools/physics_tools/center_of_mass)).

**3.** Select the **Export to Roblox** command from the [**Commands** menu](https://cascadeur.com/help/interface/main_menu/commands_menu):

![](https://cascadeur.com/images/category/2025/04/03/b75afd2c80422a847abdaee594af246f.png)

**4.** In the appeared dialog message, click either **Export with mesh** or **Export without mesh**.

Some Roblox models can import and use the animations without the meshes, while others require a skinned character model present in the imported animation. If you’re not sure which one works best for you, you can try both and see which one imports correctly.

![](https://cascadeur.com/images/category/2025/04/03/5b9be89915deafc801d0f616944af5e9.png)

The **Export to Roblox** command does the following:

1\. Bakes the selected timeline interval, filling it with keyframes

2\. Removes the control rig, leaving just the joints and the character mesh

3\. Scales the found root object (Armature or Root) to the scale of 1-1-1.

Note

The **Export to Roblox** command works only on the Roblox characters with the generated Cascadeur control rig. You can’t use this command on the unrigged model with just the skeleton.

# Importing Animation to Roblox Studio

Once you have successfully exported your animated Roblox character from Cascadeur, you can import the animation to Roblox Studio:

**1.** Open Roblox Studio.

**2.** Open a world where you want to import your animations. An empty **Classic Baseplate** should be fine.

**3.** In the “Avatar” tab, click on **Rig Builder**. In the appeared window, select your Rig Type (R6 or R15) and click **My Avatar**.

Alternatively, add your target R6 or R15 model to the scene with your preferred choice of plugins and tools:

![](https://cascadeur.com/images/category/2025/04/03/1607c2692ff1394d445164699e7ba288.png)

**4.** Move the appeared model wherever you like or reset its Position in the model’s Properties window.

**5.** Select your model and in the same **Avatar** tab open the **Animation Editor**.

**6.** Press the **3-dot** button to the right of the name of your animation. Then, press **Import -> From FBX Animation**:

![](https://cascadeur.com/images/category/2025/04/03/3a224126ee0cd4eb55c9e6d9732fa415.png)

Note

Roblox Studio’s Animation Editor tends to cut out the pose in the last frame of the imported animation.

If you wish to preserve all poses in your animations, adding an additional keyframe at the end of your Cascadeur animation is recommended.

Warning

The Animation Editor is very sensitive to the contents of the imported scene, such as:

\- the correct bone orientations in the imported R6/R15 model

\- the presence or lack of the character mesh

\- the presence or lack of additional bones, such as Handle bones for props

\- the character mesh not having the same name as one of the character bones

If any of these aren’t accounted for, the imported animation may look broken.

**7.** Press the **3-dot** button to the right of the name of your animation. Then, press **Publish to Roblox** to save your animation as an animation clip.

After you’ve published your animation, you can continue implementing it into your project.

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

2

[No](https://cascadeur.com/help/rest/add-mark "No")

3

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)