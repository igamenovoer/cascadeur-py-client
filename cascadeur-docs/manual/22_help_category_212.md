# Untitled

Source: https://cascadeur.com/help/category/212

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- Import Usd

EN

# Import Usd

In addition to FBX and Collada formats, Cascadeur also supports loading data from Universal Scene Description (\*.usd) files.

Warning

Currently, USD support in Cascadeur is in its alpha version. Some of the features might work incorrectly.

The following types of objects can be imported:

- [3d meshes](https://cascadeur.com/help/rig/rig_structure/rig_elements/meshes)
- [Joints](https://cascadeur.com/help/rig/rig_structure/rig_elements/joints)
- Animation assigned to joints
- Additional objects (cameras etc.)

## Importing Usd Files

To import a USD file into a Cascadeur scene, select **Import Usd** from the [**File** menu](https://cascadeur.com/help/interface/main_menu/file_menu):

![](https://cascadeur.com/images/category/2023/10/17/b28a87d4273d41b4bb3191dd2aa799a4.png)

There are three options available:

**Animation**

Saves the character skeleton (the set of joints) and animation data into .usd format. Character models are not included.

**Model**

Saves the character model(s) into .usd format. Animation is not included.

**Scene**

Save the whole scene into .usd format, including character models, joints, animation data and additional objects.

## File Formats

When you save USD files, you can specify a particular format to store the scene in. There are several kinds of USD files that can be distinguished by their extensions:

- . **usdc** contains scene data in binary format.
- . **usda** contains the data in ASCII (text) format.
- **.usd** can be either binary or ASCII.
- **.usdz** is a ‘zero-compression’ package file: an unencrypted zip archive that can contain other kinds of usd files, as well as image and sound files.

## See Also

[Import Fbx/Dae](https://cascadeur.com/help/getting_started/import_fbxdae)

[Scenes](https://cascadeur.com/help/getting_started/scenes)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

13

[No](https://cascadeur.com/help/rest/add-mark "No")

0

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)