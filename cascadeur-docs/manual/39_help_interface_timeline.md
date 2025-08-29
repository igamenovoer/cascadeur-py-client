# Untitled

Source: https://cascadeur.com/help/interface/timeline

- [Home](https://cascadeur.com/help)
- [Interface](https://cascadeur.com/help/interface)
- Timeline

EN

# Timeline

![](https://cascadeur.com/images/category/2025/02/19/bd10019bcc862302c49d8a9dcf852b4c.png)

**1.** Create / Delete a [**keyframe**](https://cascadeur.com/help/category/34).

**2\.** Change kinematics on the selected keys or the current frame.

**3.** IK / FK frame modes switch.

**4.** [Mark / Unmark](https://cascadeur.com/help/category/36) a selected keyframe.

Creates a label that makes the frame

**5.** Change [**interpolation**](https://cascadeur.com/help/category/21) on interval.

**6.** [**Interpolation modes**](https://cascadeur.com/help/category/21#types_of_interpolation) selection.

**7.** [IK / FK interpolation](https://cascadeur.com/help/interpolation#ik_and_fk_interpolation) mode switch.

**8.** [**Animation playback**](https://cascadeur.com/help/category/38) controls.

**9.** Loop animation playback.

If this is enabled, animation will be played continuously.

**10.** Play only keyframes.

If this is enabled, only keyframe poses will be shown when animation is played.

**11.** [**Timeline settings**](https://cascadeur.com/help/category/199).

**12.** The number of the first frame of the available part of the timeline.

By default, it is set to zero. Increasing this number excludes all frames that come before it.

The excluded frames are **not** deleted.

**13.** [**Keyframe**](http://cascadeur.com/help/category/34) (marked by a deeper shade of blue).

These frames store all data regarding the character's pose.

**14.** Frame with **interpolation**.

On these frames, the pose is calculated automatically on the basis of the neares Keyframes.

How exactly it is calculated depends on the [type of interpolation](https://cascadeur.com/help/tools/timeline_tools/interpolation#types_of_interpolation) used.

**15.** The part of the Timeline available for editing (and playback).

Drag the corners of this bar (or directly enter the numbers) to change the length of the available part.

**16.** The **current frame indicator**.

Can be dragged to select a specific frame.

**17.** The last frame of the timeline.

Change this number to change the overall length of the Timeline.

**18.** [**Interval edit mode**](https://cascadeur.com/help/interval_edit_mode).

**19.** [**Fixing interpolation on change**](https://cascadeur.com/help/interval_edit_mode#fixing_interpolation_on_change).

**20.** [**Animation Cycles**](https://cascadeur.com/help/animation_cycles).

**21.** **Invert frame indicator hotkeys**.

When this is set to **F**, the next/previous frame hotkeys ( **A** and **D** by default) would move the current frame indicator to the next or previous frame.

When set to **K**, they would move the indicator to the next/previous _keyframe_.

**22.** Current frame time.

**23.** [**Animation Tracks**](https://cascadeur.com/help/tools/timeline_tools/animation_tracks).

**24.** Tools for managing Animation Tracks.

**25.** [**Track Stretching Mode**](https://cascadeur.com/help/tools/timeline_tools/track_stretching_mode).

**26.** **Auto Interpolation**.

**27.** The number of the last Keyframe on the Timeline.

Clicking this sets the end of the availabe part of the Timeline to this last keyframe.

All Timeline controls are also available in the [**Timeline** menu](https://cascadeur.com/help/category/11#menu_timeline).

# Navigation

**Move through the timeline** by pressing the **![A](https://cascadeur.com/images/category/2019/06/047a18eea99d2f0391412c25f5dc861a38.png)** and **![D](https://cascadeur.com/images/category/2019/06/04875d91b785a0c7a9399cbbbd4ee468aa.png)** hotkeys or by moving the red pointer to the frame you need.

**Move between keyframes** by pressing **Shift** \+ **A** and **Shift** \+ **B**.

**Play** animation by using the [**Animation playback**](https://cascadeur.com/help/category/38) controls at the right side of the Timeline.

Alternatively, press **X** or **Space** on the keyboard.

To instantly go to the **first** frame on the Timeline, press **Z**.

**Left-click** a frame to select it. A selected frame is marked with a black border.

**Right-click** a frame to select it on all [**Animation Tracks**](https://cascadeur.com/help/category/15) at the same time.

**Select a group of frames** by selecting one frame and then moving the black border left or right while holding **![Left Mouse Button](https://cascadeur.com/images/category/2019/06/04705eec8d7b79b302d32eba008a192f92.png)**.

Hold **Ctrl** and press either **Left Arrow** or **Right Arrow** to expand the selection on either left or right side.

**Add** or **remove** frames by pressing the **![+](https://cascadeur.com/images/category/2019/06/0455e9a22cb7c305ee484238f22a46c20e.png)** or **![-](https://cascadeur.com/images/category/2019/06/04535dd6234d2fdb2a3e7b6843347746ad.png)** keys. New frames will be added (or removed) at the right of the selected frame

# [Keyframes](https://cascadeur.com/help/tools/timeline_tools/keyframes)

**Keyframes** ( **keys** for short) store character poses and positions. If you edit a pose in a regular frame, the changes made will not be recorded. To adjust a pose, you have to create a keyframe for it.

**Create a new key** by selecting a frame and pressing the _Add or remove frame_ button (or the **![F](https://cascadeur.com/images/category/2019/06/049742a6e8486bc5bfad3400116b71e785.png)** hotkey).

**Create several keys** by selecting a group of frames and pressing **![Alt](https://cascadeur.com/images/category/2019/06/042f0eb6ef388167ff923ac76922e0704d.png) + ![F](https://cascadeur.com/images/category/2019/06/0436595e8d398df9b116627d8c7ac7ccae.png)**.

If the **Auto Key** feature (the small 'A' sign near the keyfarme button) is enabled, a keyframe is automatically created on the current frame when any changes are applied to the object/character.

**Jump between keyframes** by pressing **![A](https://cascadeur.com/images/category/2019/06/0460063bbab5fc03c0c91d5cb028cf3ff9.png)** or **![D](https://cascadeur.com/images/category/2019/06/044c16c74b1f2ed42fc5335732efcdfee4.png)** while holding **![Shift](https://cascadeur.com/images/category/2019/06/04cfe0776123e21bfe6d7baa27f673d252.png).**

You can also set the Inver Frame Indicator to **K** to get the same effect.

**Move** a key (or a group of keys) to a different place on the timeline by selecting and dragging it while holding **![Middle Mouse Button](https://cascadeur.com/images/category/2019/06/04eef31650d9587e41cf7df4d9294ba9c9.png)**

**![](https://cascadeur.com/images/category/2023/01/16/7ad2bc6268acb3dbcc1c8da6f8a9e457.gif)**

Note #1

If you move a key to a frame that already has another key, this another key will be deleted and replaced by the one you have moved.

Note #2

The first key in the timeline cannot be moved. If you try to move it, its copy will be created instead (this is because a timeline should start with a keyframe).

**Copy** a key (or a group of keys) by selecting and dragging it to a new frame while holding **![Shift](https://cascadeur.com/images/category/2019/06/04cfe0776123e21bfe6d7baa27f673d252.png) +** **![Middle Mouse Button](https://cascadeur.com/images/category/2019/06/04eef31650d9587e41cf7df4d9294ba9c9.png):**

**![](https://cascadeur.com/images/category/2023/01/16/c25f23ad02149c71e7a995048a596c9d.gif)**

**Expand** or **shrink** intervals between keys by adding or removing frames

![](https://cascadeur.com/images/category/2023/01/16/a2b07b99256f437cdc3dd5b1e7e7b691.gif)

# [Tracks](https://cascadeur.com/help/tools/timeline_tools/animation_tracks)

The timeline can be split into [**Animation Tracks**](https://cascadeur.com/help/category/15) for a more convenient workflow.

## See Also

[Timeline Menu](https://cascadeur.com/help/interface/main_menu/timeline_menu)

[Edit Menu](https://cascadeur.com/help/interface/main_menu/edit_menu)

[Interpolation Menu](https://cascadeur.com/help/interface/main_menu/interpolation_menu)

[Timeline Tools](https://cascadeur.com/help/category/33)

[Keyframes](https://cascadeur.com/help/category/34)

[Animation Tracks](https://cascadeur.com/help/category/15)

[Interpolation](https://cascadeur.com/help/category/21)

[Timeline Settings](https://cascadeur.com/help/category/199)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

6

[No](https://cascadeur.com/help/rest/add-mark "No")

3

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)