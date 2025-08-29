# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html

# csc.layers.LayersContainer [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html\#csc-layers-layerscontainer "Permalink to this heading")

_class_ csc.layers.LayersContainer [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer "Permalink to this definition")

LayersContainer class

It is the container of layers.

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.__init__ "csc.layers.LayersContainer.__init__")(\*args, \*\*kwargs) |  |
| [`at`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.at "csc.layers.LayersContainer.at")(self, arg0) | -\> Layer |
| [`has_any_obj_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.has_any_obj_ids "csc.layers.LayersContainer.has_any_obj_ids")(self) |  |
| [`has_obj_id`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.has_obj_id "csc.layers.LayersContainer.has_obj_id")(self, id) |  |
| [`layer_id_by_obj_id`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.layer_id_by_obj_id "csc.layers.LayersContainer.layer_id_by_obj_id")(self, id) | -\> LayerId |
| [`layer_id_by_obj_id_or_null`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.layer_id_by_obj_id_or_null "csc.layers.LayersContainer.layer_id_by_obj_id_or_null")(self, id) | -\> LayerId |
| [`map`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.map "csc.layers.LayersContainer.map")(self) | -\> <LayerId, Layer>{} |
| [`obj_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer.obj_ids "csc.layers.LayersContainer.obj_ids")(self) | -\> <csc.model.ObjectId, LayerId>{} |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.__module__ "Permalink to this definition")at( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_, _arg0:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.at "Permalink to this definition")

-\> Layer

has\_any\_obj\_ids( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.has_any_obj_ids "Permalink to this definition")has\_obj\_id( _self:csc.layers.LayersContainer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.has_obj_id "Permalink to this definition")layer\_id\_by\_obj\_id( _self:csc.layers.LayersContainer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.layer_id_by_obj_id "Permalink to this definition")

-\> LayerId

layer\_id\_by\_obj\_id\_or\_null( _self:csc.layers.LayersContainer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.layer_id_by_obj_id_or_null "Permalink to this definition")

-\> LayerId

map( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.map "Permalink to this definition")

-\> <LayerId, Layer>{}

obj\_ids( _self:[csc.layers.LayersContainer](https://cascadeur.com/python-api/csc.html#csc.layers.LayersContainer "csc.layers.LayersContainer")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.LayersContainer.html#csc.layers.LayersContainer.obj_ids "Permalink to this definition")

-\> <csc.model.ObjectId, LayerId>{}