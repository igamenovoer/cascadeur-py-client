---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html
html_file: bc7e7903a22cd3fbb4c79442878fbddf.html
module: csc.layers.LayersContainer
---

# csc.layers.LayersContainer[??](#csc-layers-layerscontainer "Permalink to this heading")

*class* csc.layers.LayersContainer[??](#csc.layers.LayersContainer "Permalink to this definition")
:   LayersContainer class

    It is the container of layers.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.LayersContainer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.LayersContainer.__init__ "csc.layers.LayersContainer.__init__")(\*args,??\*\*kwargs) |  |
    | [`at`](../csc.html#csc.layers.LayersContainer.at "csc.layers.LayersContainer.at")(self,??arg0) | -> Layer |
    | [`has_any_obj_ids`](../csc.html#csc.layers.LayersContainer.has_any_obj_ids "csc.layers.LayersContainer.has_any_obj_ids")(self) |  |
    | [`has_obj_id`](../csc.html#csc.layers.LayersContainer.has_obj_id "csc.layers.LayersContainer.has_obj_id")(self,??id) |  |
    | [`layer_id_by_obj_id`](../csc.html#csc.layers.LayersContainer.layer_id_by_obj_id "csc.layers.LayersContainer.layer_id_by_obj_id")(self,??id) | -> LayerId |
    | [`layer_id_by_obj_id_or_null`](../csc.html#csc.layers.LayersContainer.layer_id_by_obj_id_or_null "csc.layers.LayersContainer.layer_id_by_obj_id_or_null")(self,??id) | -> LayerId |
    | [`map`](../csc.html#csc.layers.LayersContainer.map "csc.layers.LayersContainer.map")(self) | -> <LayerId, Layer>{} |
    | [`obj_ids`](../csc.html#csc.layers.LayersContainer.obj_ids "csc.layers.LayersContainer.obj_ids")(self) | -> <csc.model.ObjectId, LayerId>{} |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.LayersContainer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.LayersContainer.__module__ "Permalink to this definition")

    at(*self: [csc.layers.LayersContainer](../csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")*, *arg0: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.LayersContainer.at "Permalink to this definition")
    :   -> Layer

    has\_any\_obj\_ids(*self: [csc.layers.LayersContainer](../csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersContainer.has_any_obj_ids "Permalink to this definition")

    has\_obj\_id(*self: csc.layers.LayersContainer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.LayersContainer.has_obj_id "Permalink to this definition")

    layer\_id\_by\_obj\_id(*self: csc.layers.LayersContainer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.LayersContainer.layer_id_by_obj_id "Permalink to this definition")
    :   -> LayerId

    layer\_id\_by\_obj\_id\_or\_null(*self: csc.layers.LayersContainer*, *id: common::GenericId<domain::scene::model::ModelObject>*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.LayersContainer.layer_id_by_obj_id_or_null "Permalink to this definition")
    :   -> LayerId

    map(*self: [csc.layers.LayersContainer](../csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.LayersContainer.map "Permalink to this definition")
    :   -> <LayerId, Layer>{}

    obj\_ids(*self: [csc.layers.LayersContainer](../csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.LayersContainer.obj_ids "Permalink to this definition")
    :   -> <csc.model.ObjectId, LayerId>{}