---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.Scene.html
html_file: 2d3f6ceaa81bd61222f21c0264293550.html
module: csc.domain.Scene
---

# csc.domain.Scene 

Scene class 
Root class that represents a scene and its methods for modifying or observing it. Modify scene by func modify:
- name – Name of the modifier
- func – Modify functor void(modelEditor, updateEditor, scene)

name – Name of the modifier func – Modify functor void(modelEditor, updateEditor, scene) Modify scene by func modify_update:
- name – Name of the modifier
- func – Modify functor void(modelEditor, updateEditor, sceneUpdater)

name – Name of the modifier func – Modify functor void(modelEditor, updateEditor, sceneUpdater) Methods __init__ (self) assets_manager (self) -> AssetsManager behaviour_viewer (self) -> csc.model.BehaviourViewer data_viewer (self) -> csc.model.DataViewer error (self, arg0) get_current_frame (self[, clamp_animation]) get_event_log_or_null (self) get_layers_selector (self) -> csc.layers.Selector info (self, arg0) layers_viewer (self) -> csc.layers.Viewer model_viewer (self) -> csc.model.ModelViewer modify (self, arg0, arg1) -> bool modify_update (self, arg0, arg1) -> bool modify_update_with_session (self, arg0, arg1) -> bool modify_with_session (self, arg0, arg1) -> bool selector (self) -> Selector set_current_frame (self, frame) set_event_log (self, message_handler) success (self, arg0) warning (self, arg0) -> AssetsManager -> csc.model.BehaviourViewer -> csc.model.DataViewer -> csc.layers.Selector -> csc.layers.Viewer -> csc.model.ModelViewer -> bool -> bool -> bool -> bool -> Selector