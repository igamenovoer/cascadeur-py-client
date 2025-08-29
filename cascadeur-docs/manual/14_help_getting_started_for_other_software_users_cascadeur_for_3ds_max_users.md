# Untitled

Source: https://cascadeur.com/help/getting_started/for_other_software_users/cascadeur_for_3ds_max_users

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [For Other Software Users](https://cascadeur.com/help/getting_started/for_other_software_users)
- Cascadeur for 3ds max users

EN

# Cascadeur for 3ds max users

This page provides an introduction to Cascadeur from the viewpoint of a 3ds max user. Its purpose is to help you to translate your existing experience into Cascadeur.

## The Basics

Cascadeur is **not** a general-purpose 3D solution. It is not designed for creating 3D models or skinning them to joints/bones. Characters should be prepared for animation beforehand, in other programs.

3ds max and Cascadeur use similar approaches to animation. What you need to do is to create [**keyframes**](https://cascadeur.com/help/keyframes) and define character poses for them, while the software will do the rest.

However, there are some differences:

|     |     |
| --- | --- |
| #### **3ds max** | #### **Cascadeur** |
| You need to enable **Set Key** mode before working with keyframes | You can work with keyframes right after the scene is loaded |
| You need to set the pose first, then you can add a keyframe | You need to add a keyframe and then set a pose for it |
| Each time you alter a pose, you need to reset the keyframe for it | Each time you alter a pose, you need to reset the keyframe for it |
| Keyframes can be set separately for translation, rotation etc. | A keyframe always contains every motion parameter |

Character poses and positions in Cascadeur are defined by keyframes.

Because of this, at least _one_ keyframe is always present in the scene

Every frame in Cascadeur - including non-key ones - stores animation data. This means that regular frames can be moved, copied etc., much like keyframes.

By default, all keyframes in Cascadeur are placed on the same **[Animation Track](https://cascadeur.com/help/animation_tracks)** and contain animation data for every object in the scene. However, there is still a way to animate only some of the objects in the scene, or a specific part of your character. Create an separate track for this part or object and place keyframes on that track.

The timeline in Cascadeur is discreet. It always includes an integer number of frames, and keys cannot be placed in the subframe space.

You do, however, still have full control over animation. It can be stretched, retimed and altered in other ways.

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

![](https://cascadeur.com/images/category/2021/02/04/6b961748bf51cf4a2e715ade30c8ec20.png)

_User interface in 3ds Max_

![](https://cascadeur.com/images/category/2023/02/20/375250ac977f87618abd54dc9ac27016.png)

_User interface in Cascadeur_

**1** \- Viewport(s)

**2** \- Timeline/Animation & Time controls

**3** \- Toolbar/Main Toolbar

**4** \- Outliner/Scene Explorer

## Quick Glossary

|     |     |
| --- | --- |
| #### **3ds max** | #### **Cascadeur** |
| Bone | Joint |
| Viewport(s) | Viewport |
| Main Toolbar | Toolbar |
| Animation/Time controls | Timeline |
| Main Menu | Main Menu |

## Controls

|     |     |     |
| --- | --- | --- |
| #### **Action** | #### **3ds max** | #### **Cascadeur** |
| **Camera Actions** |
| Rotate Camera | Ctrl + R | Alt + LMB |
| Zoom Camera | Alt + Z | Alt + RMB |
| Pan Camera | Ctrl + P | Alt + Mouse Wheel |
| **Selecting Objects** |
| Select an object | LMB | LMB |
| Border Select | Hold LMB and drag | Hold LMB and drag |
| **Manipulators** |
| Translate an object | W | W |
| Rotate an object | E | E |
| Hide an object | Ctrl + H | V |
| Make all objects visible | Alt + U | Alt + V |
| **Frames and Animation** |
| Add Keyframe | K | F |

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

17

[No](https://cascadeur.com/help/rest/add-mark "No")

3

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)