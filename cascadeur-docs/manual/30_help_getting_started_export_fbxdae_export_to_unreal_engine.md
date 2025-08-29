# Untitled

Source: https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Export FBX/DAE](https://cascadeur.com/help/getting_started/export_fbxdae)
- Export to Unreal Engine

EN

# Export to Unreal Engine

**On this page**

- [Animation for UE Mannequin](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#export_ue4_man)
- [Import Cacscadeur Characters](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#export_ue4_import_casc)
  - [Import Model](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#export_ue4_custom_model)
  - [Import Animation](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#export_ue4_custom_animation)
- [Fixing Incorrect Rotation](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#export_ue4_rotation)
  - [Set necessary rotations during input](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#rotation_import)
  - [Reimport animations with correct rotations](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#rotation_reimport)
- [Example](https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unreal_engine#export_ue4_example)

# Animations for UE Mannequin

Animations created in Cascadeur can be imported to an Unreal Engine project and attached to a skeleton there.

Note

If you are using the default Epic Skeleton in your project, we recommend using _UE5 Manny_ or _UE5 Quinn_ file for creating animations in Cascadeur. [Other models](https://cascadeur.com/help/getting_started/scenes#start_sample_scenes) included in the package have significantly different skeletons, which might lead to compatibility issues.

**1.** Right-click the **Content Browser** window

![](https://cascadeur.com/images/category/2025/03/03/239ebfd6b523be4242612dd7b5ae76ce.png)

**2.** Select **Import to...** from the menu

![](https://cascadeur.com/images/category/2025/03/03/216c2510a030b2b2c7aa692aa400f829.png)

**3.** Select the file containing your model

The file should be in **binary** FBX format. See [here](https://cascadeur.com/help/category/76#fbx_formats) about formats

**4.** The **FBX Import Options** window will appear:

![](https://cascadeur.com/images/category/2025/03/03/4b3b7d1d89d2e8918afcb20fdd973444.png)

**5.** Set **Skeleton** to **SK\_Mannequin**:

![](https://cascadeur.com/images/category/2025/03/03/abd19aa9ecc678ff33b7105fe4b0f2b1.png)

**6.** Make sure that the **Import Only Animations** option is enabled:

![](https://cascadeur.com/images/category/2025/03/03/15b3e61c26da571a3f60bce24a6967f7.png)

**7.** Click the **Import** button

![](https://cascadeur.com/images/category/2025/03/03/fb32dc3638e03cde9eff3de5dfd07634.png)

**9.** An **Animation** asset should be created:

![](https://cascadeur.com/images/category/2025/03/03/eff216232f43c41e883836e9a0e71db9.png)

# Import Cascadeur Characters

To use custom characters, you need to first import the character model and then animations for it.

### Import Model

**1.** Right-click the **Content Browser** window:

![](https://cascadeur.com/images/category/2025/03/03/239ebfd6b523be4242612dd7b5ae76ce.png)

**2.** Select **Import to...** from the menu:

![](https://cascadeur.com/images/category/2025/03/03/216c2510a030b2b2c7aa692aa400f829.png)

**3.** Select the file containing your model

The file should be in **binary** FBX format. See [here](https://cascadeur.com/help/category/76#fbx_formats) about formats

4\. The **FBX Import Options** window will appear:

![](https://cascadeur.com/images/category/2025/03/03/4b3b7d1d89d2e8918afcb20fdd973444.png)

**5.** Set **Skeleton** to **None**

![](https://cascadeur.com/images/category/2025/03/03/dde9109d5dfe44c852f34e2c597ad0e8.png)

**6.** Disable **Import Only Animations**:

![](https://cascadeur.com/images/category/2025/03/04/26dbc678e8f298e7453a80320261ec08.png)

**7.** Disable **Force Front XAxis**

![](https://cascadeur.com/images/category/2020/03/24/fffb5bb9e782bb28c0b2bca2253b8176.png)

**8.** Set **Material Import Method** to **Do Not Create Material** (unless you want the material to be imported with the model)

![](https://cascadeur.com/images/category/2020/03/24/85241e27c8d4e035053cb2fa36143088.png)

**9.** Click the **Import** button:

![](https://cascadeur.com/images/category/2025/03/03/fb32dc3638e03cde9eff3de5dfd07634.png)

**11.** After importing, several assets should be created:

- a **Mesh** asset (contains imported model)
- a **Physics Asset**
- (optional) a **Material** asset (if you decided to import it)

![](https://cascadeur.com/images/category/2020/03/24/1bb07d8881b312d964f52ae67879b8cd.png)

### Import Animation

**1.** Right-click the **Content Browser** window:

![](https://cascadeur.com/images/category/2025/03/03/239ebfd6b523be4242612dd7b5ae76ce.png)

**2.** Select **Import to...** from the menu:

![](https://cascadeur.com/images/category/2025/03/03/216c2510a030b2b2c7aa692aa400f829.png)

**3.** Select the file containing your model

The file should be in **binary** FBX format. See [here](https://cascadeur.com/help/category/76#fbx_formats) about formats

4\. The **FBX Import Options** window will appear:

![](https://cascadeur.com/images/category/2025/03/03/4b3b7d1d89d2e8918afcb20fdd973444.png)

**5.** In the **Skeleton** window, select your custom skeleton

![](https://cascadeur.com/images/category/2020/03/24/df39f3f51ea558d6db7164e9f2afaa71.png)

**6.** Disable **Import Mesh**

![](https://cascadeur.com/images/category/2020/03/24/0a5f492170a310c34284b243a848a6aa.png)

**7.** Disable **Convert Scene**

![](https://cascadeur.com/images/category/2020/03/24/4f7d42e42d14b924d476b00fedc67309.png)

**8.** Disable **Force Front XAxis**

![](https://cascadeur.com/images/category/2020/03/24/66046b777f97a3aaabbfa06121cdc2eb.png)

**9.** Click the **Import** button

![](https://cascadeur.com/images/category/2020/03/24/4605313ecb1b3e6182e4cc6d33969820.png)

**10.** An **Animation** asset should be created

![](https://cascadeur.com/images/category/2020/03/24/416b582f116c7cad0e315c5b2b6e877c.png)

# Fixing Incorrect Rotation

In cases where models and animations are imported with incorrect rotations, there are two ways to fix this:

### Set necessary rotations during import

**1.** In the **Import** window, set the **Import Rotation** values under the **Transform** panel

![](https://cascadeur.com/images/category/2020/03/24/e1c984bfd340212c8f76f120efccb0f8.png)

**2.** Proceed to import the model as described in the **Custom Skeleton** section

Note

There is no way to preview rotations set during import. You might need several attempts to figure out the exact rotations you need.

### Reimport animations with correct rotations

1\. In the content browser, **double-click** the animation in the viewer to open it

2\. Set the necessary rotations

![](https://cascadeur.com/images/category/2020/03/24/1fd84e911b50f52d6c1da92b2a61dfd4.png)

**3.** Save the model/animation

![](https://cascadeur.com/images/category/2020/03/24/89cc8ba25bbdadc4db772755036d512e.png)

**4.** Close the viewer.

**5.** Right-click the model/animation asset and select **Reimport** from the menu

![](https://cascadeur.com/images/category/2020/03/24/f2aa74fac93223b24b8d356987c58d91.jpg)

**6.** After this, the asset will be updated with the new rotations

Rotation axis should be manually chosen in each individual case

![](https://cascadeur.com/images/category/2020/03/24/e047c4b5cd1c0641100adab9e69f49cb.png)

Here, for example, the character should be rotated by **90** degrees across **X-axis**:

![](https://cascadeur.com/images/category/2020/03/24/34781d100083d6a8c6f2c7afd907cdfa.png)

# Example

Cascadeur to UE4 - Custom Character Retargeting - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[Cascadeur to UE4 - Custom Character Retargeting](https://www.youtube.com/watch?v=WrEjKZ5-1qE)

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

[Watch on](https://www.youtube.com/watch?v=WrEjKZ5-1qE&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 27:15
•Live

•

## See Also

[Export](https://cascadeur.com/help/category/76)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

8

[No](https://cascadeur.com/help/rest/add-mark "No")

2

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)