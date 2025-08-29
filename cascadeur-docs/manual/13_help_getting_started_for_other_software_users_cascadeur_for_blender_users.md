# Untitled

Source: https://cascadeur.com/help/getting_started/for_other_software_users/cascadeur_for_blender_users

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [For Other Software Users](https://cascadeur.com/help/getting_started/for_other_software_users)
- Cascadeur for Blender Users

EN

# Cascadeur for Blender Users

This page provides an introduction to Cascadeur from the viewpoint of a Blender user. Its purpose is to help you to translate your existing Blender experience into Cascadeur.

## The Basics

Cascadeur is **not** a general-purpose 3D solution. You cannot create 3D models, nor can you skin it to joints/bones. Characters should be prepared for animation beforehand, in other programs.

Animation in Cascadeur is created in the same manner as it is in Blender: by defining keyframes and setting character poses.

However, there are some differences:

|     |     |
| --- | --- |
| #### **Blender** | #### **Cascadeur** |
| You need to set the pose first, then you can add a keyframe | You need to add a keyframe and then set a pose for it |
| Each time you alter a pose, you need to reset the keyframe for it | Poses in keyframes can be altered at any time |
| Keyframes can be set separately for translation, rotation etc. | A keyframe always contains every motion parameter. |

Character poses and positions in Cascadeur are defined by keyframes.

Because of this, at least _one_ keyframe is always present in the scene

Every frame in Cascadeur, including non-key ones, stores animation data. This means that regular frames can be moved, copied etc., much like keyframes.

By default, all keyframes in Cascadeur are placed on the same [**Animation Track**](https://cascadeur.com/help/animation_tracks) and thus contain animation data for **every** scene object. If you need to animate only some of the scene objects, - or a specific part of your character - create a separate track for this part and place keyframes on that track.

The timeline in Cascadeur is discreet. It always includes an integer number of frames, and there’s no way to place keyframes in the subframe space.

However, you still have full control over animation and can stretch, retime and alter it in other ways.

[**Graph Editor**](https://cascadeur.com/help/tools/animation_tools/graph_editor) is present in Cascadeur. However, the standard Cascadeur control rig isn’t designed to be controlled via Graph Editor as it has no exposed Euler transforms (translation/rotation/scale).

You can attempt to control the rig via Point Controllers with parameters such as Swing, Twist, Vector Length, and IK Direction. However, compared to the standard Graph Editor usage, you will probably find such an approach cumbersome and unappealing.

Instead, the Cascadeur users are encouraged to refine their animation using the tools for tracking and editing the animation directly in the Viewport. These include:

- [Frame ghosts](https://cascadeur.com/help/ghosts)
- [Trajectory editing](https://cascadeur.com/help/trajectories)
- [Filters](https://cascadeur.com/help/filters) for fixing animation errors
- Tools for [mirroring poses](https://cascadeur.com/help/mirror_tools)

...and more.

Another feature of Cascadeur is its [**Physics Tools**](https://cascadeur.com/help/physics_tools). This set of instruments can be used for easily creating physically accurate motions, as well as for improving the quality of the existing animations.

## Interface

![](https://cascadeur.com/images/category/2021/01/21/56be3ea80437ddd6f6e156e71929c9b5.png)

_User interface in Blender_

![](https://cascadeur.com/images/category/2023/02/20/153547cbcd9c74c28b04bc99135684bc.png)

_User interface in Cascadeur_

**1** \- Viewport

**2** \- Timeline

**3** \- Toolbar

**4** \- Outliner

**5** \- Object settings

## Quick Glossary

|     |     |
| --- | --- |
| #### **Blender** | #### **Cascadeur** |
| Bone | Joint |
| 3D Viewport | Viewport |
| Toolbar | Toolbar |
| Timeline | Timeline |
| (not present) | Animation Tracks |
| Interpolation | Interpolation |
| Topbar | Main Menu |
| Status bar | (not present) |

## Controls

|     |     |     |
| --- | --- | --- |
| #### **Action** | #### **Blender** | #### **Cascadeur** |
| **Camera Actions** |
| Rotate Camera | Hold Mouse Wheel | Alt + LMB |
| Zoom Camera | Mouse Wheel | Alt + RMB |
| Pan Camera | Shift + Mouse Wheel | Alt + Mouse Wheel |
| **Selecting Objects** |
| Select an object | LMB | LMB |
| Border Select | Hold LMB and drag | Hold LMB and drag |
| **Manipulators** |
| Translate an object | G | W |
| Rotate an object | R | E |
| Hide an object | H | V |
| Make all objects visible | Alt + H | Alt + V |
| **Frames and Animation** |
| Add Keyframe | I | F |

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

66

[No](https://cascadeur.com/help/rest/add-mark "No")

12

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)