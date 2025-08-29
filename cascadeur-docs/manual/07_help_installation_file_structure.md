# Untitled

Source: https://cascadeur.com/help/installation/file_structure

- [Home](https://cascadeur.com/help)
- [Installation](https://cascadeur.com/help/installation)
- File Structure

EN

# File Structure

This page describes file structure of the Cascadeur application

## Main Program Folder

By default, the main program folder is named **Cascadeur** across all platforms

_**Note:** During installation, you can specify another name for the main folder; in this case, that name will be used instead of the default one_

The **scenes** folder at the root of the main folder contains the [sample scenes](https://cascadeur.com/help/scenes#start_sample_scenes).

## Application Data

Program data is stored in a dedicated folder at the following location:

- **Windows:** C:\\Users\\<user\_name>\\AppData\\Local\\Nekki Limited\\Cascadeur
- **Ubuntu**: /home/<user\_name>/.local/share/Nekki Limited\\Cascadeur

All of the program settings are stored in several _.ini_ files placed in this directory:

- _Cascadeur.ini_ contains parameters available for editing through the [Settings Window](https://cascadeur.com/help/interface/main_menu/settings_window).
- _Cascadeur\_service.ini_ contains internal settings that are normally not available for editing (such as windows' positions, last use files etc.).
- _Hotkey\_settings.ini_ contains the list of [hotkeys](https://cascadeur.com/help/interface/hotkey_editor) used in the program.
- _Cascadeur\_tools.ini_ contains settings available on the [Scene Settings](https://cascadeur.com/help/interface/scene_settings) panel.

This directory also includes a number of subfolders:

- **autosave** stores backup save files for recently used scenes. Autosaving is performed automatically, its frequency can be adjusted in Cascadeur's [**Settings** window](https://cascadeur.com/help/category/94).


The files in this folder can be accessed by selecting **Open autosave file** from the [**File** menu](https://cascadeur.com/help/interface/main_menu/file_menu).
- **cache** stores cache files.
- **file\_preview** contains _.png_ images depicting recently used scenes (these images are seen on the splash screen under the **Recent Files** tab).
- **logs** contain program log in the form of a text file.

Note

If these files are deleted, all user settings will be reset (missing files are recreated on starting up the program, but with default settings).

## Resources

Resources used by the software, such as scripts or shaders, are stored in the main Cascadeur directory, in the _Resouces_ folder:

![](https://cascadeur.com/images/category/2022/04/26/681ccf11453b91007563947040ba18d6.png)

This folder, in turn, includes several subfolders:

![](https://cascadeur.com/images/category/2022/04/26/e42974693938c073cd676a1406230faf.png)

- **autorig\_templates** is used for the [Quick Rigging Tool](https://cascadeur.com/help/rig/rig_mode/quick_rigging_tool).
- **scripts** is the default folder for storing [Python scripts](https://cascadeur.com/help/tools/animation_tools/python_scripting_in_cascadeur).
- **shaders** contains shaders used by the software.

Finally, the **settings.ini** file contains the _ScriptsDir_ parameter which sets the folder for storing Python scripts.

By default, its value is empty; this means that the aforementioned _scripts_ folder is used.

If you'd like to use a different folder, set a custom value for this parameter.

## Crash Dumps

The location of Cascadeur crash dumps depends on your system settings.

By default, the following directory is used:

- **C:\\Users\\<user\_name>\\AppData\\Local\\CrashDumps**

If you are using **Windows**, and crash dumps are not generated, you'll need to enable them manually.

To do this, open Windows Power Shell and run the following commands:

_New-Item -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting" -Name "LocalDumps"_

_New-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting\\LocalDumps" -Name "DumpFolder" -Value "%LOCALAPPDATA%\\CrashDumps" -PropertyType "ExpandString"_

The commands should be executed as an Administrator.

## See Also

[Installation](https://cascadeur.com/help/category/68)

Was this article useful to you?

[Yes](https://cascadeur.com/help/rest/add-mark "Yes")

14

[No](https://cascadeur.com/help/rest/add-mark "No")

2

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)