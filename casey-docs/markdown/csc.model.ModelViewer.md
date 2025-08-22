---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ModelViewer.html
html_file: 2096b4c76202724155cd035882b817f7.html
module: csc.model.ModelViewer
---

# csc.model.ModelViewer[??](#csc-model-modelviewer "Permalink to this heading")

*class* csc.model.ModelViewer[??](#csc.model.ModelViewer "Permalink to this definition")
:   ModelViewer class

    Represents basic methods to view the scene model

    Variables:
    :   **get\_objects** ??? overridden method by string -> csc.model.ObjectId[]

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelViewer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.ModelViewer.__init__ "csc.model.ModelViewer.__init__")(\*args,??\*\*kwargs) |  |
    | [`behaviour_viewer`](../csc.html#csc.model.ModelViewer.behaviour_viewer "csc.model.ModelViewer.behaviour_viewer")(self) | -> BehaviourViewer |
    | [`data_viewer`](../csc.html#csc.model.ModelViewer.data_viewer "csc.model.ModelViewer.data_viewer")(self) | -> DataViewer |
    | [`get_object_name`](../csc.html#csc.model.ModelViewer.get_object_name "csc.model.ModelViewer.get_object_name")(self,??id) |  |
    | [`get_object_type_name`](../csc.html#csc.model.ModelViewer.get_object_type_name "csc.model.ModelViewer.get_object_type_name")(self,??id) |  |
    | [`get_objects`](../csc.html#csc.model.ModelViewer.get_objects "csc.model.ModelViewer.get_objects")(\*args,??\*\*kwargs) | Overloaded function. |

    \_\_annotations\_\_ *= {}*[??](#csc.model.ModelViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ModelViewer.__module__ "Permalink to this definition")

    behaviour\_viewer(*self: [csc.model.ModelViewer](../csc.html#csc.model.ModelViewer "csc.model.ModelViewer")*)  [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")[??](#csc.model.ModelViewer.behaviour_viewer "Permalink to this definition")
    :   -> BehaviourViewer

    data\_viewer(*self: [csc.model.ModelViewer](../csc.html#csc.model.ModelViewer "csc.model.ModelViewer")*)  [csc.model.DataViewer](../csc.html#csc.model.DataViewer "csc.model.DataViewer")[??](#csc.model.ModelViewer.data_viewer "Permalink to this definition")
    :   -> DataViewer

    get\_object\_name(*self: [csc.model.ModelViewer](../csc.html#csc.model.ModelViewer "csc.model.ModelViewer")*, *id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ModelViewer.get_object_name "Permalink to this definition")

    get\_object\_type\_name(*self: [csc.model.ModelViewer](../csc.html#csc.model.ModelViewer "csc.model.ModelViewer")*, *id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ModelViewer.get_object_type_name "Permalink to this definition")

    get\_objects(*\*args*, *\*\*kwargs*)[??](#csc.model.ModelViewer.get_objects "Permalink to this definition")
    :   Overloaded function.

        1. get\_objects(self: csc.model.ModelViewer) -> list[csc.model.ObjectId]
        2. get\_objects(self: csc.model.ModelViewer, name: str) -> list[csc.model.ObjectId]