# Untitled

Source: https://cascadeur.com/help/getting_started/export_fbxdae/export_to_unity

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [Export FBX/DAE](https://cascadeur.com/help/getting_started/export_fbxdae)
- Export to Unity

EN

# Export to Unity

## Import Model

To import a Cascadeur model to Unity:

**1.** Select **Import New Asset…** from the **Assets** menu

![](https://cascadeur.com/images/category/2020/10/23/386a79b7941f0054665e8c6452efcf4e.png)

**2.** Select the file

Alternatively, you can drag the model file to the **Assets** folder or to the **Project** window.

**3.** Wait until the model is imported

By default, importing a model will also create an empty animation asset. If you don’t need it:

**1.** Go to the **Animation** tab

**2.** Uncheck **Import Animation**

![](https://cascadeur.com/images/category/2020/10/23/122bbb82c7dfdf9d11009ae2017c3fbe.png)

**3.** Click **Apply**

## Import Model with Animation

If you try to import a file that contains a model and animation data for it,

**1.** Select **Import New Asset…** from the **Assets** menu

![](https://cascadeur.com/images/category/2020/10/23/386a79b7941f0054665e8c6452efcf4e.png)

**2.** Select the file

(Both FBX and Collada formats are supported)

**3.** A new collection will be created:

![](https://cascadeur.com/images/category/2020/10/23/478671b042f5e83c1acf9227cd149b52.png)

This collection will include the model itself, the skeleton for it, a material, and an animation

## Import Animation Clips

To import an animation clip:

**1.** Import the animation ( **Assets → Import New Asset…**)

**2.** Select the animation asset

**3.** Open the **Model** tab:

![](https://cascadeur.com/images/category/2020/10/23/6a35a813229df48d8e8a769b2c6e10ee.png)

**4.** Enable **Preserve Hierarchy**:

![](https://cascadeur.com/images/category/2020/10/23/0bbff20ae1cd6dfea2c5bbc6f3a1b882.png)

**5.** Click **Apply**:

![](https://cascadeur.com/images/category/2020/10/23/275c3ab7c12a9bd12dda4b0fb95f28ac.png)

**6.** Now you can open the **Animation** tab and see if the animation works as it should

Alternatively, you can import an animated model and then make clips from this animation:

**1.** Import the model the usual way

**2.** Open the imported asset in the **Inspector** window:

![](https://cascadeur.com/images/category/2020/10/23/004e857be6d30e7823cfc741e5243077.gif)

**3.** Select the animation asset:

![](https://cascadeur.com/images/category/2020/10/23/3d2d1ee1bef1f97df3ec824568e9cbaa.png)

**4.** Open the **Rig** tab

**5.** Select **Animation Type**.

- Select **Humanoid** if you're plan to use the default Unity rig.
- For other cases, select **Generic**.

**6.** Set **Avatar Definition** for your animation.

- If you plan to use the skeleton from this model, select **Create From This Model**.
- If you plan to use a skeleton from a different model, select **Copy From Other Avatar**. In the **Source** field, select the avatar from that model.

**7.** Click **Apply** to save the changes.

**8.** Duplicate the animation ( **Edit → Duplicate**). A separate animation asset will be created

![](https://cascadeur.com/images/category/2020/10/23/a670dd834dbd4a2c11e38b2e9cecc5ba.png)

**9.** Now you can delete the imported model

It is not advised to use this process as the main method of importing animations, but in some cases, it can be used as well.

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

8

[No](https://cascadeur.com/help/rest/add-mark "No")

5

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)