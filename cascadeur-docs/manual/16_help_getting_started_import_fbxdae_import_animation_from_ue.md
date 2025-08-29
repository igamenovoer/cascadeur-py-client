# Untitled

Source: https://cascadeur.com/help/getting_started/import_fbxdae/import_animation_from_ue

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Import FBX/DAE](https://cascadeur.com/help/getting_started/import_fbxdae)
- Import Animation from UE

EN

# Import Animation from UE

![](https://cascadeur.com/images/category/2020/04/22/fad32fa508a39fbf2de3b41ad5c49e3e.jpg)

If this is what happens when you try to export animation from Unreal Engine to Cascadeur, follow these steps to fix it:

Note

You can also learn about this topic in the [**Unreal Engine documentation**](https://docs.unrealengine.com/en-US/WorkingWithContent/Importing/FBX/HowTo/ImportingAnimations/index.html).

**1.** In the **Content Browser**, open the animation asset:

![](https://cascadeur.com/images/category/2020/04/22/371fc8ce75b954bcdc262f7292f840d0.jpg)

**2\. Animation Editor** window will appear

![](https://cascadeur.com/images/category/2020/04/22/189abc0b66c43368eecce1e7ad50456f.jpg)

In it, you need to **record** the animation:

**3.** Stop the animation by clicking **Pause**

![](https://cascadeur.com/images/category/2020/04/22/c4e3065e4b6ddaec3e0c8264ad6707b8.png)

**4.** Click **To front** to set the animation to the first frame

![](https://cascadeur.com/images/category/2020/04/22/2c76052a8fbf03734828929ab1e8dbfc.png)

**5\.** Click the **Record** button to begin recording

![](https://cascadeur.com/images/category/2020/04/22/236be829c9ec7639bbece36e4cafb942.png)

**6.** Click **Play** to restart the animation

![](https://cascadeur.com/images/category/2020/04/22/60d8c1b595b5dc8740834e5bbce093ee.png)

**7\.** Wait until the animation is played at least once

**8\.** Click the **Stop** button

![](https://cascadeur.com/images/category/2020/04/22/2752b1d07d515762212f51016a602a05.png)

**9.** A new animation asset will be created

![](https://cascadeur.com/images/category/2020/04/22/4e37d20ae36cad538c76b26933488721.jpg)

**10.** Open this new asset

We need to cut the animation to the original length.

**11.** On the timeline, select the frame where the motion starts

![](https://cascadeur.com/images/category/2020/04/22/85a38588a3ee37a76b76fa4589108949.jpg)

Note

You can use **To Previous** and **To Next** buttons to position the frame marker.

![](https://cascadeur.com/images/category/2020/04/22/5e378dfc270cce3c17bae8e97c56bf2d.png)

**12.** Right-click the selected frame and select **Remove frame 0 to (the selected frame)**

**![](https://cascadeur.com/images/category/2020/04/22/993205d6bf344ea43aa178a5f60b1ca5.png)**

This will delete the beginning part of the animation

**13\.** Then, select the last frame of the animation

For example, if the initial animation was 30 frames long, you should select frame 30.

**14.** Right-click the selected frame. This time, select **Remove from (the selected frame) to (the last frame)**

**![](https://cascadeur.com/images/category/2020/04/22/3c53a880ca3de1c8860440c586535e92.png)**

This will delete the ending part of the animation

**15.** Save the animation

![](https://cascadeur.com/images/category/2020/04/22/6190b09d25210c779362c07da2acfb13.png)

**16.** Export the animation

![](https://cascadeur.com/images/category/2020/04/22/bca2a501f1e6b47fa71a72fa6acb5c08.jpg)

Now, the animation should be ready for importing to Cascadeur.

However: as animation exported from UE has a different hierarchical structure than the standard models in Cascadeur, you'll need to use the **Animation to selected objects** option. This is the only import option that uses relative paths insead of absolute ones.

To do this:

**17.** Open your model in Cascadeur.

**18.** Switch to the **Joint Mode** in the [**Viewport**](https://cascadeur.com/help/interface/viewport) window:

![](https://cascadeur.com/images/category/2021/12/30/bd67e3da2ed152bf79bf0d14a2552945.png)

**19.** Select **every** joi nt in the model.

**20.** Select **Animation to selected objects** from the **File → Import Fbx/Dae** menu:

![](https://cascadeur.com/images/category/2021/12/30/c6728a86f5e53045d226bdbb091a0d6c.png)

**21.** Select the file containing the animation you've exported.

Now, animation should be imported without issues:

![](https://cascadeur.com/images/category/2020/04/22/93c10cdd98f5844af2b36e2bd51bfde8.jpg)

## How to Fix Incorrect Rotation

![](https://cascadeur.com/images/category/2020/04/22/ad92fd3a0d3fad2e66ba19b1d1278b75.jpg)

Sometimes, animations are imported to Cascadeur incorrectly rotated. To fix this:

**1.** Select **every** joint in the character skeleton

**2.** Select **every** frame of the animation

**3.** Enable [**Interval edit mode**](https://cascadeur.com/help/category/27#manipulators_interval_edit)

![](https://cascadeur.com/images/category/2021/02/16/24f9f59d5df3268b0dc98bda28ffc5a6.png)

**4.** In the [**Settings**](https://cascadeur.com/help/category/55) panel, enable **Fix angle** and set it to **90**

![](https://cascadeur.com/images/category/2020/04/22/927a3484b96bd69af5b359aba1b132a5.png)

**5.** Rotate the character

![](https://cascadeur.com/images/category/2020/04/22/6b02908bae84bdd884a0b0f2f6a48de7.gif)

Don’t forget to disable **Fix angle** and **Interval edit mode** afterwards.

## See Also

[Import](https://cascadeur.com/help/category/75)

[Export to Unreal Engine](https://cascadeur.com/help/category/79)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

12

[No](https://cascadeur.com/help/rest/add-mark "No")

17

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)