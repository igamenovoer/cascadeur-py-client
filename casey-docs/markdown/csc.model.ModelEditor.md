---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ModelEditor.html
html_file: dbc6362aebe211be60307113c12bfeaa.html
module: csc.model.ModelEditor
---

# csc.model.ModelEditor[??](#csc-model-modeleditor "Permalink to this heading")

*class* csc.model.ModelEditor[??](#csc.model.ModelEditor "Permalink to this definition")
:   ModelEditor class

    Represents basic methods to edit the scene model

    Variables:
    :   **add\_object** ??? overridden method by GroupId -> csc.model.ObjectId

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelEditor.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.ModelEditor.__init__ "csc.model.ModelEditor.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_object`](../csc.html#csc.model.ModelEditor.add_object "csc.model.ModelEditor.add_object")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`behaviour_editor`](../csc.html#csc.model.ModelEditor.behaviour_editor "csc.model.ModelEditor.behaviour_editor")(self) | -> BehaviourEditor |
    | [`data_editor`](../csc.html#csc.model.ModelEditor.data_editor "csc.model.ModelEditor.data_editor")(self) | -> DataEditor |
    | [`delete_objects`](../csc.html#csc.model.ModelEditor.delete_objects "csc.model.ModelEditor.delete_objects")(self,??ids[,??close\_connections]) |  |
    | [`fit_animation_size_by_layers`](../csc.html#csc.model.ModelEditor.fit_animation_size_by_layers "csc.model.ModelEditor.fit_animation_size_by_layers")(self) |  |
    | [`get_viewer`](../csc.html#csc.model.ModelEditor.get_viewer "csc.model.ModelEditor.get_viewer")(self) |  |
    | [`init_default_constants`](../csc.html#csc.model.ModelEditor.init_default_constants "csc.model.ModelEditor.init_default_constants")(self) |  |
    | [`layers`](../csc.html#csc.model.ModelEditor.layers "csc.model.ModelEditor.layers")(self) | -> csc.layers.Layers |
    | [`layers_editor`](../csc.html#csc.model.ModelEditor.layers_editor "csc.model.ModelEditor.layers_editor")(self) | -> csc.layers.Editor |
    | [`layers_selector`](../csc.html#csc.model.ModelEditor.layers_selector "csc.model.ModelEditor.layers_selector")(self) | -> csc.layers.Selector |
    | [`move_obj_ids_in_layers`](../csc.html#csc.model.ModelEditor.move_obj_ids_in_layers "csc.model.ModelEditor.move_obj_ids_in_layers")(self[,??objIds]) |  |
    | [`move_objects_to_layer`](../csc.html#csc.model.ModelEditor.move_objects_to_layer "csc.model.ModelEditor.move_objects_to_layer")(self,??ids,??target\_layer\_id) |  |
    | [`set_fixed_interpolation_if_need`](../csc.html#csc.model.ModelEditor.set_fixed_interpolation_if_need "csc.model.ModelEditor.set_fixed_interpolation_if_need")(self,??...[,??...]) |  |
    | [`set_object_name`](../csc.html#csc.model.ModelEditor.set_object_name "csc.model.ModelEditor.set_object_name")(self,??id,??name) |  |
    | [`set_object_type_name`](../csc.html#csc.model.ModelEditor.set_object_type_name "csc.model.ModelEditor.set_object_type_name")(self,??id,??name) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.model.ModelEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ModelEditor.__module__ "Permalink to this definition")

    add\_object(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelEditor.add_object "Permalink to this definition")
    :   Overloaded function.

        1. add\_object(self: csc.model.ModelEditor) -> csc.model.ObjectId
        2. add\_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) -> csc.model.ObjectId

    behaviour\_editor(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")[??](#csc.model.ModelEditor.behaviour_editor "Permalink to this definition")
    :   -> BehaviourEditor

    data\_editor(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.model.DataEditor](../csc.html#csc.model.DataEditor "csc.model.DataEditor")[??](#csc.model.ModelEditor.data_editor "Permalink to this definition")
    :   -> DataEditor

    delete\_objects(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *ids: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]*, *close\_connections: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.delete_objects "Permalink to this definition")

    fit\_animation\_size\_by\_layers(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.fit_animation_size_by_layers "Permalink to this definition")

    get\_viewer(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.model.ModelViewer](../csc.html#csc.model.ModelViewer "csc.model.ModelViewer")[??](#csc.model.ModelEditor.get_viewer "Permalink to this definition")

    init\_default\_constants(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.init_default_constants "Permalink to this definition")

    layers(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.model.ModelEditor.layers "Permalink to this definition")
    :   -> csc.layers.Layers

    layers\_editor(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.layers.Editor](../csc.html#csc.layers.Editor "csc.layers.Editor")[??](#csc.model.ModelEditor.layers_editor "Permalink to this definition")
    :   -> csc.layers.Editor

    layers\_selector(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.model.ModelEditor.layers_selector "Permalink to this definition")
    :   -> csc.layers.Selector

    move\_obj\_ids\_in\_layers(*self: csc.model.ModelEditor, objIds = csc.model.ObjectId[]: list[csc.model.ObjectId], layer\_id: csc.Guid*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.move_obj_ids_in_layers "Permalink to this definition")

    move\_objects\_to\_layer(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]*, *target\_layer\_id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.move_objects_to_layer "Permalink to this definition")

    set\_fixed\_interpolation\_if\_need(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *actuals: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")]*, *frame: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *ignore\_locked: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = False*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.set_fixed_interpolation_if_need "Permalink to this definition")

    set\_object\_name(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.set_object_name "Permalink to this definition")

    set\_object\_type\_name(*self: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ModelEditor.set_object_type_name "Permalink to this definition")