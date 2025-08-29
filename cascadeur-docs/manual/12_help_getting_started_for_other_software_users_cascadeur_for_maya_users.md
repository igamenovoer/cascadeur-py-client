# Untitled

Source: https://cascadeur.com/help/getting_started/for_other_software_users/cascadeur_for_maya_users

- [Home](https://cascadeur.com/help)
- [Getting Started](https://cascadeur.com/help/getting_started)
- [For Other Software Users](https://cascadeur.com/help/getting_started/for_other_software_users)
- Cascadeur for Maya Users

EN

# Cascadeur for Maya Users

This page provides an introduction to Cascadeur from the viewpoint of a Maya user. Its purpose is to help you to translate your existing Maya experience into Cascadeur.

# The Basics

Cascadeur is **not** a general-purpose 3D solution. You cannot create 3D models, nor can you skin it to joints/bones. Characters should be prepared for animation beforehand, in other programs.

Animation in Cascadeur is created in the same manner as it is in Maya. You only need to create [**keyframes**](https://cascadeur.com/help/keyframes) and set character poses for them, and the software will do the rest.

However, there are some differences:

|     |     |
| --- | --- |
| #### **Maya** | #### **Cascadeur** |
| You need to set the pose first, then you can add a keyframe | You need to add a keyframe and then set a pose for it |
| Keyframes can be set separately for translation, rotation etc. | A keyframe always contains every motion parameter |

Character poses and positions in Cascadeur are defined by keyframes.

Because of this, at least _one_ keyframe is always present in the scene.

Every frame in Cascadeur, including non-key ones, stores animation data. This means that regular frames can be moved, copied etc., much like keyframes.

By default, all keyframes in Cascadeur are placed on the same [**Animation Track**](https://cascadeur.com/help/animation_tracks) and thus contain animation data for **every** scene object. If you need to animate only some of the scene objects, - or a specific part of your character - create a separate track for this part and place keyframes on that track.

The timeline in Cascadeur is discreet. It always includes an integer number of frames, and there’s no way to place keyframes in the subframe space.

However, you still have full control over animation and can stretch, retime and alter it in other ways.

[**Graph Editor**](https://cascadeur.com/help/tools/animation_tools/graph_editor) is present in Cascadeur. However, the standard Cascadeur control rig isn’t designed to be controlled via Graph Editor as it has no exposed Euler transforms (translation/rotation/scale).

You can attempt to control the rig via Point Controllers with parameters such as Swing, Twist, Vector Length, and IK Direction. However, compared to the standard Graph Editor usage, you will probably find such an approach cumbersome and unappealing.

Instead, the Cascadeur users are encouraged to refine their animation using the tools for tracking and editing the animation directly in the Viewport. These include:

- [Frame ghosts](https://cascadeur.com/help/ghosts)
- [Trajectory editing](https://cascadeur.com/help/trajectories)
- [Filters](https://cascadeur.com/help/filters) for fixing animation errors
- Tools for [mirroring poses](https://cascadeur.com/help/mirror_tools)

...and more.

Another feature of Cascadeur is its [**Physics Tools**](https://cascadeur.com/help/physics_tools). This set of instruments can be used for easily creating physically accurate motions, as well as for improving the quality of the existing animations.

# Interface

![](https://cascadeur.com/images/category/2021/01/21/ca194a36dd0df02f87b7b7218f92819e.png)

_User interface in Maya_

![](https://cascadeur.com/images/category/2023/02/20/bb80471d12f3c86338425acc4248d700.png)

_User interface in Cascadeur_

**1** \- Viewport/View Panel

**2** \- Timeline/Time Slider

**3** \- Toolbar/Menu Sets

**4** \- Object settings

# Quick Glossary

|     |     |
| --- | --- |
| #### **Maya** | #### **Cascadeur** |
| Joint | Joint |
| View panel | Viewport |
| Menu Sets | Toolbar |
| Time Slider / Time Editor | Timeline |
| Interpolation | Interpolation |
| Menus | Main Menu |

# Controls

|     |     |     |
| --- | --- | --- |
| #### **Action** | #### **Maya** | #### **Cascadeur** |
| **Camera Actions** |
| Rotate Camera | Alt + LMB | Alt + LMB |
| Zoom Camera | Alt + RMB | Alt + RMB |
| Pan Camera | Alt + Mouse Wheel | Alt + Mouse Wheel |
| **Selecting Objects** |
| Select an object | LMB | LMB |
| Border Select | Hold LMB and drag | Hold LMB and drag |
| **Manipulators** |
| Translate an object | W | W |
| Rotate an object | E | E |
| Hide an object | Ctrl + H | V |
| Focus on an object | F | T |
| **Frames and Animation** |
| Add Keyframe | S | F |

# Example

Cascadeur to Autodesk Maya \| Bridge Plugin Workflow Tutorial - YouTube

[Photo image of Cascadeur — Reinventing Animation](https://www.youtube.com/channel/UCwF6yYbIFJmB5ynAkzq9Psg?embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

Cascadeur — Reinventing Animation

64.4K subscribers

[Cascadeur to Autodesk Maya \| Bridge Plugin Workflow Tutorial](https://www.youtube.com/watch?v=tiTGzay7Xto)

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

[Watch on](https://www.youtube.com/watch?v=tiTGzay7Xto&embeds_referring_euri=https%3A%2F%2Fcascadeur.com%2F)

0:00

0:00 / 4:41
•Live

•

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

19

[No](https://cascadeur.com/help/rest/add-mark "No")

17

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)