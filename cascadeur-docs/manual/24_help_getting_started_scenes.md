# Untitled

Source: https://cascadeur.com/help/getting_started/scenes

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- Scenes

EN

# Scenes

**On this page:**

- [Creating a New Scene](https://cascadeur.com/help/getting_started/scenes#start_new_scene)
- [Opening an Existing Scene](https://cascadeur.com/help/getting_started/scenes#start_open_file)
- [Scene Contents](https://cascadeur.com/help/getting_started/scenes#about_scenes)
  - [Models and Character](https://cascadeur.com/help/getting_started/scenes#about_characters)
  - [Camera Objects](https://cascadeur.com/help/getting_started/scenes#camera_objects)
  - [Helper Objects](https://cascadeur.com/help/getting_started/scenes#helper_objects)
- [Sample Scenes](https://cascadeur.com/help/getting_started/scenes#start_sample_scenes)
- [Migrating Scenes](https://cascadeur.com/help/getting_started/scenes#scenes_migrating)
- [Scenes With Multiple Characters](https://cascadeur.com/help/getting_started/scenes#scenes_multiple_characters)

![](https://cascadeur.com/images/category/2023/02/27/86dcd297cc9d4668825416285f167868.png)

_A standart scene with one character in the **Viewport** window_

Animation in Cascadeur is created within **Scenes**.  A scene is, in essence, a set of objects all of which are available for editing at the same time. A scene can be saved to a _.casc_ file, and a previously saved scene can be restored from a file.

Scenes are primarily viewed through the [Viewport](https://cascadeur.com/help/category/10) window. You can open multiple scenes at the same time, with each one occupying a separate tab in the Viewport.

To learn about controlling the scene, see [**Main Controls**](https://cascadeur.com/help/category/74)

## Creating a New Scene

Working on an animation project should start with creating a new scene. There are two ways to do this.

**First**, you can click the **New Scene** button on the [splash screen](https://cascadeur.com/help/interface/splash_window) that appears when you run Cascadeur:

![](https://cascadeur.com/images/category/2023/02/27/cfcaf43c1261051325794c36b6c933ff.png)

**Second**, you can select **New Scene** from the [**File** menu](https://cascadeur.com/help/interface/main_menu/file_menu):

![](https://cascadeur.com/images/category/2023/02/27/d6a42d61aa0f474f9db7858ecf6f465c.png)

Either way, this will create a new empty scene:

![](https://cascadeur.com/images/category/2023/02/27/71262c4727135302c92da42c4b8a6ec1.png)

_A newly created scene in the Viewport window_

## Opening an Existing Scene

Alternatively, you can load a pre-existing scene to use it as a base for your work. As with creating a new file, this can be done in two ways:

**First**, you can select **Open...** from the **File** menu:

![](https://cascadeur.com/images/category/2023/02/27/0d2d33945db0d510512aa4bec87f8efa.png)

A standard Open File dialogue will appear. Use it to specify the file you need to open.

**Second**, you can open a folder that contains the file you need in any file manager and double-click the name of the file:

![](https://cascadeur.com/images/category/2019/06/057799bb16c88b7765ebbd4fbb1854c6a9.jpg)

Either way, the file you've chosen will be loaded to Cascadeur and shown in the **Viewport** window:

![](https://cascadeur.com/images/category/2023/02/27/6c523679fa0b59c7be32cd11a1b60bb4.png)

_The **cube.casc** (included in the installation package) file opened in the program_

## Scene Contents

A scene can include the following types of objects:

- Characters
- Camera objects
- Helper objects

#### **Models and Characters**

Cascadeur works with _3d models_, or _meshes_: 3d objects that represent an object or a character.

These models can be animated on their own, but this method of animation is very limited. You’ll only be able to move and scale objects, but not to deform them - which is often necessary for more complex animations. Moreover, you won’t be able to use most of the functionality Cascadeur provides.

Because of this, a better way to animate 3d models is to use a skeleton.

A skeleton is a set of [**Joints**](https://cascadeur.com/help/rig/rig_structure/rig_elements/joints) (bones) that is attached to the mesh and then used for controlling it. Each joint is linked to a part of the mesh, allowing you to move the character’s skeleton to position the character.

![](https://cascadeur.com/images/category/2023/02/27/f880cd44e68c4cc6e2f96cea2be60308.png)

_Character mesh (left) and character skeleton (right) as seen in Cascadeur viewport._

3d models with skeletons attached are often referred to as _characters_.

Meshes and joints are both brought to Cascadeur through the process of [import](https://cascadeur.com/help/getting_started/import_fbxdae).

Links between joints and meshes are created through _skinning_.

Skinning establishes the influence joints have on the parts of the mesh.

The image below shows a character in Blender (a popular 3d software). Here, you can see several of the joints with the amount of influence each one of them has on the parts of the mesh:

![](https://cascadeur.com/images/category/2022/03/24/e28a4e1b32c70f8d91073585e419f7ea.gif)

_Red color means maximum influence, blue means no influence._

These values are used to deform the mesh when joints move:

![](https://cascadeur.com/images/category/2022/03/24/5ae47018710100898bf98687a92ef802.gif)

_A skinned mesh would deform in accordance to the skeleton attached to it._

Currently, skinning **cannot** be done in Cascadeur. You need to import your models with their meshes already skinned to the joints. This can be done in most of the 3d software solutions.

When you don’t have access to such software, you might consider online solutions such as [Mixamo](https://www.mixamo.com/). Using them, you can upload a 3d model and attach it to a standard humanoid skeleton; skinning values will be generated automatically.

This approach will obviously only work with human-shaped characters, but if your characters are indeed human-shaped, this might be enough.

If you are not sure if you character already has skinning, there’s an easy way to find out:

**1.** Switch to the [**Joint Mode**](https://cascadeur.com/help/getting_started/edit_modes):

![](https://cascadeur.com/images/category/2023/02/27/a3d38abd8e4709657ed7c7e2bd095343.png)

**2.** Select one (or several) of the joints.

![](https://cascadeur.com/images/category/2023/02/27/d42efb112042f2f31e622235d90bcaf3.png)

_Joints you’ve selected will be colored yellow in the Viewport window._

**3.** Go to the **Mesh mode**:

![](https://cascadeur.com/images/category/2023/02/27/d4000019430dbe879c7e3dd4bd4d7cf9.png)

**4.** Select the [**Rotate** manipulator](https://cascadeur.com/help/tools/animation_tools/manipulators#rig_rotate_manipulator):

![](https://cascadeur.com/images/category/2023/02/27/e399a822619432b5d747a6ec9c1be341.png)

**5.** Try to rotate the joint you’ve selected.

If the mesh moves after the joint, then it is already skinned to the skeleton.

If it doesn’t, there is either no skinning data or something has gone wrong during import.

#### **Camera Objects**

If you need to view your scene from a pre-defined angle, this can be achieved by adding a **Camera** object to the scene. To do this, select **Camera** from the **Objects** menu.

After you created a new Camera, select it by clicking its name in the **Outliner** window at the right:

![](https://cascadeur.com/images/category/2023/02/27/26cc0c50d3e5e593f132d275182b29f1.png)

Note

A camera object is only visible when it is selected.

Camera objects cannot be adjusted using general controls described above. The only way to change their positions and spatial orientation is by applying manipulators.

To see the scene through an additional camera, press the **Align to Camera** button in the Toolbar.

#### **Helper Objects**

This type of objects is used for improving animation, creatig physically accurate motions and such.

Available helper objects include:

- [**Ghosts**](https://cascadeur.com/help/category/22)
- [**Trajectories**](https://cascadeur.com/help/category/23)
- [**Angular Momentum**](https://cascadeur.com/help/category/40) visualizer
- [**Ballistic Curves**](https://cascadeur.com/help/category/42)

## Sample Scenes

Cascadeur installation package includes several example files that you can use as templates or as means to learn about software's features. These examples are located in the **.../cascadeur/scenes** folder. Character models in these files are fully rigged and ready for animation.

- **Backflip\_animation.casc** \- a complex animation of a character performing a backflip. Makes use of Cascadeur's physical tools such as [Ballistic Trajectory](https://cascadeur.com/help/category/42).
- **Cascy.casc** - a scene with the standard Cascadeur character model.
- **Cascy\_sabers.casc** - a  scene with a standard character with two sabred attached.
- **Cascy\_sword.casc** - a scene with a standard character with a giant sword attached.
- **Cube.casc** \- a simple scene including one cube.
- **Dracorex.casc** \- a rigged model of a dinosaur.
- **Dracorex\_walk\_cycle.casc** \- the same model performing a walking animation.
- **Move\_AI.casc** \- a sample model for [Move AI](https://www.move.ai/).
- **MVN\_Puppet.casc** \- a sample model for the [Movella](https://www.movella.com/) motion capture solution.
- **Rokoko.casc** \- a sample model for the [Rokoko](https://www.rokoko.com/) motion capture system.
- **Sabertooth.casc** \- a model of a sabertooth cat.
- **UE4\_Mannequin.casc** \- a scene with a standard Unreal Engine 4 character.
- **UE4\_Mannequin\_Female.casc** \- a scene with the same rig. but a different character model.
- **UE5\_Manny.casc** \- a scene with a standard Unreal Engine 5 character.
- **UE5\_Quinn.casc** \- a scene with another standard Unreal Engine 5 character.
- **UEFN\_Mannequin.casc** \- a scene with a model for Unreal Editor for Fortnite.

## Migrating Scenes

There are some incompatibilities between the closed Beta and the current Open Beta versions of Cascadeur. These incompatibilities prevent scenes from the older version to properly work in the newer one.

So if you want to use an outdated scene, you'll need to **migrate** it to the new version.

See [**Migrating Outdated Scenes**](https://cascadeur.com/help/category/100) to learn how to do it.

## Scenes With Multiple Character

Sometimes you might need a scene with several characters in it. For this, there is a dedicated page: [**Scenes With Multiple Characters**](https://cascadeur.com/help/getting_started/scenes/scenes_with_multiple_characters).

However, do keep in mind that incresing the number of characters also increases the computation power required to properly run the scene. If your machine struggles with a complex scene, you might consider using [**Scene Linking Tool**](https://cascadeur.com/help/tools/animation_tools/scene_linking_tool) instead of one scene with multiple characters.

## See Also

[Main Controls](https://cascadeur.com/help/category/74)

[Edit Modes](https://cascadeur.com/help/category/53)

[Rig Structure](https://cascadeur.com/help/category/17)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

11

[No](https://cascadeur.com/help/rest/add-mark "No")

0

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)