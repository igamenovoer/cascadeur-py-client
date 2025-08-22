---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.Scene.html
html_file: 2d3f6ceaa81bd61222f21c0264293550.html
module: csc.domain.Scene
---

# csc.domain.Scene[??](#csc-domain-scene "Permalink to this heading")

*class* csc.domain.Scene[??](#csc.domain.Scene "Permalink to this definition")
:   Scene class

    Root class that represents a scene and its methods for modifying or observing it.

    Modify scene by func modify:

    Parameters:
    :   * **name** ??? Name of the modifier
        * **func** ??? Modify functor void(modelEditor, updateEditor, scene)

    Modify scene by func modify\_update:

    Parameters:
    :   * **name** ??? Name of the modifier
        * **func** ??? Modify functor void(modelEditor, updateEditor, sceneUpdater)

    \_\_init\_\_(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.domain.Scene.__init__ "csc.domain.Scene.__init__")(self) |  |
    | [`assets_manager`](../csc.html#csc.domain.Scene.assets_manager "csc.domain.Scene.assets_manager")(self) | -> AssetsManager |
    | [`behaviour_viewer`](../csc.html#csc.domain.Scene.behaviour_viewer "csc.domain.Scene.behaviour_viewer")(self) | -> csc.model.BehaviourViewer |
    | [`data_viewer`](../csc.html#csc.domain.Scene.data_viewer "csc.domain.Scene.data_viewer")(self) | -> csc.model.DataViewer |
    | [`error`](../csc.html#csc.domain.Scene.error "csc.domain.Scene.error")(self,??arg0) |  |
    | [`get_current_frame`](../csc.html#csc.domain.Scene.get_current_frame "csc.domain.Scene.get_current_frame")(self[,??clamp\_animation]) | -> int |
    | [`get_event_log_or_null`](../csc.html#csc.domain.Scene.get_event_log_or_null "csc.domain.Scene.get_event_log_or_null")(self) |  |
    | [`get_layers_selector`](../csc.html#csc.domain.Scene.get_layers_selector "csc.domain.Scene.get_layers_selector")(self) | -> csc.layers.Selector |
    | [`info`](../csc.html#csc.domain.Scene.info "csc.domain.Scene.info")(self,??arg0) |  |
    | [`layers_viewer`](../csc.html#csc.domain.Scene.layers_viewer "csc.domain.Scene.layers_viewer")(self) | -> csc.layers.Viewer |
    | [`model_viewer`](../csc.html#csc.domain.Scene.model_viewer "csc.domain.Scene.model_viewer")(self) | -> csc.model.ModelViewer |
    | [`modify`](../csc.html#csc.domain.Scene.modify "csc.domain.Scene.modify")(self,??arg0,??arg1) | -> bool |
    | [`modify_update`](../csc.html#csc.domain.Scene.modify_update "csc.domain.Scene.modify_update")(self,??arg0,??arg1) | -> bool |
    | [`modify_update_with_session`](../csc.html#csc.domain.Scene.modify_update_with_session "csc.domain.Scene.modify_update_with_session")(self,??arg0,??arg1) | -> bool |
    | [`modify_with_session`](../csc.html#csc.domain.Scene.modify_with_session "csc.domain.Scene.modify_with_session")(self,??arg0,??arg1) | -> bool |
    | [`selector`](../csc.html#csc.domain.Scene.selector "csc.domain.Scene.selector")(self) | -> Selector |
    | [`set_current_frame`](../csc.html#csc.domain.Scene.set_current_frame "csc.domain.Scene.set_current_frame")(self,??frame) |  |
    | [`set_event_log`](../csc.html#csc.domain.Scene.set_event_log "csc.domain.Scene.set_event_log")(self,??message\_handler) |  |
    | [`success`](../csc.html#csc.domain.Scene.success "csc.domain.Scene.success")(self,??arg0) |  |
    | [`warning`](../csc.html#csc.domain.Scene.warning "csc.domain.Scene.warning")(self,??arg0) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Scene.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Scene.__module__ "Permalink to this definition")

    assets\_manager(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  domain::scene::AssetsManager[??](#csc.domain.Scene.assets_manager "Permalink to this definition")
    :   -> AssetsManager

    behaviour\_viewer(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")[??](#csc.domain.Scene.behaviour_viewer "Permalink to this definition")
    :   -> csc.model.BehaviourViewer

    data\_viewer(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")[??](#csc.domain.Scene.data_viewer "Permalink to this definition")
    :   -> csc.model.DataViewer

    error(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.error "Permalink to this definition")

    get\_current\_frame(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *clamp\_animation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.Scene.get_current_frame "Permalink to this definition")
    :   -> int

    get\_event\_log\_or\_null(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Scene.get_event_log_or_null "Permalink to this definition")

    get\_layers\_selector(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Scene.get_layers_selector "Permalink to this definition")
    :   -> csc.layers.Selector

    info(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.info "Permalink to this definition")

    layers\_viewer(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [csc.layers.Viewer](../csc.html#csc.layers.Viewer "csc.layers.Viewer")[??](#csc.domain.Scene.layers_viewer "Permalink to this definition")
    :   -> csc.layers.Viewer

    model\_viewer(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [csc.model.ModelViewer](../csc.html#csc.model.ModelViewer "csc.model.ModelViewer")[??](#csc.domain.Scene.model_viewer "Permalink to this definition")
    :   -> csc.model.ModelViewer

    modify(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify "Permalink to this definition")
    :   -> bool

    modify\_update(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify_update "Permalink to this definition")
    :   -> bool

    modify\_update\_with\_session(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify_update_with_session "Permalink to this definition")
    :   -> bool

    modify\_with\_session(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: Callable*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.Scene.modify_with_session "Permalink to this definition")
    :   -> bool

    selector(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Scene.selector "Permalink to this definition")
    :   -> Selector

    set\_current\_frame(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.set_current_frame "Permalink to this definition")

    set\_event\_log(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *message\_handler: [csc.domain.IMessageHandler](../csc.html#csc.domain.IMessageHandler "csc.domain.IMessageHandler")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.set_event_log "Permalink to this definition")

    success(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.success "Permalink to this definition")

    warning(*self: [csc.domain.Scene](../csc.html#csc.domain.Scene "csc.domain.Scene")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.Scene.warning "Permalink to this definition")