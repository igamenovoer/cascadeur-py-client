# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html

# csc.layers.Viewer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html\#csc-layers-viewer "Permalink to this heading")

_class_ csc.layers.Viewer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer "Permalink to this definition")

Viewer class

This class contains all methods and properties that describe the structure of scene objects’ interpolation properties.
The structure is represented in the hierarchy of layers divided by folders.

Variables:

- **top\_layer\_id** – overridden method by ItemId \|\| ItemId\[\]

- **merged\_layer** – overridden method like static and member LayerId\[\]

- **last\_key\_pos** – overridden method by LayerId\[\], -> Layer

- **frames\_count** – overridden method by LayerId\[\], -> int

- **significant\_frames** – overridden method by LayerId{}, -> int{}


\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.__init__ "csc.layers.Viewer.__init__")(\*args, \*\*kwargs) |  |
| [`actual_key_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.actual_key_pos "csc.layers.Viewer.actual_key_pos")(self, pos) |  |
| [`all_child_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_child_ids "csc.layers.Viewer.all_child_ids")(self, id) | -\> ItemId\[\] |
| [`all_included_layer_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_included_layer_ids "csc.layers.Viewer.all_included_layer_ids")(self, items\[, ...\]) | items : ItemId\[\] \| ignoreLocked : bool (false) \| -> LayerId\[\] |
| [`all_layer_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_layer_ids "csc.layers.Viewer.all_layer_ids")(self) | -\> LayerId\[\] |
| [`all_parent_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.all_parent_ids "csc.layers.Viewer.all_parent_ids")(self, id) | -\> FolderId\[\] |
| [`default_layer_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.default_layer_id "csc.layers.Viewer.default_layer_id")(self) | -\> LayerId |
| [`find_folder`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.find_folder "csc.layers.Viewer.find_folder")(self, id) | id : FolderId \| -> Folder |
| [`find_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.find_layer "csc.layers.Viewer.find_layer")(self, id) | id : LayerId \| -> Layer |
| [`folder`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.folder "csc.layers.Viewer.folder")(self, id) | id : FolderId \| -> Folder |
| [`folders_map`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.folders_map "csc.layers.Viewer.folders_map")(self) | -\> <FolderId, Folder>{} |
| [`for_all_ordered_items`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.for_all_ordered_items "csc.layers.Viewer.for_all_ordered_items")(self, arg0) |  |
| [`frames_count`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.frames_count "csc.layers.Viewer.frames_count")(\*args, \*\*kwargs) | Overloaded function. |
| [`has_item`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.has_item "csc.layers.Viewer.has_item")(self, id) | -\> bool |
| [`header`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.header "csc.layers.Viewer.header")(self, id) | id : ItemId \| -> Header |
| [`is_deep_child`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.is_deep_child "csc.layers.Viewer.is_deep_child")(self, item\_id, folder\_id) | -\> bool |
| [`item`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.item "csc.layers.Viewer.item")(self, id) | id : ItemId \| -> ItemVariant |
| [`last_key_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.last_key_pos "csc.layers.Viewer.last_key_pos")(\*args, \*\*kwargs) | Overloaded function. |
| [`layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer "csc.layers.Viewer.layer")(self, id) | id : LayerId \| -> Layer |
| [`layer_id_by_obj_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer_id_by_obj_id "csc.layers.Viewer.layer_id_by_obj_id")(self, id) | id : csc.model.ObjectId \| -> LayerId |
| [`layer_id_by_obj_id_or_null`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer_id_by_obj_id_or_null "csc.layers.Viewer.layer_id_by_obj_id_or_null")(self, id) | id : csc.model.ObjectId \| -> LayerId |
| [`layer_ids_by_obj_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layer_ids_by_obj_ids "csc.layers.Viewer.layer_ids_by_obj_ids")(self, ids) | ids : csc.model.ObjectId\[\] \| -> LayerId{} |
| [`layers_indices`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layers_indices "csc.layers.Viewer.layers_indices")(self, id\_arr, ignore\_locked) | -\> IndicesContainer |
| [`layers_map`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.layers_map "csc.layers.Viewer.layers_map")(self) | -\> <LayerId, Layer>{} |
| [`merged_layer`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.merged_layer "csc.layers.Viewer.merged_layer")(self, scene, ids, normalize) |  |
| [`obj_ids_by_layer_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.obj_ids_by_layer_ids "csc.layers.Viewer.obj_ids_by_layer_ids")(self, id\_arr) | -\> LayerId\[\] |
| [`pos_in_parent`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.pos_in_parent "csc.layers.Viewer.pos_in_parent")(self, id) | -\> int |
| [`root_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.root_id "csc.layers.Viewer.root_id")(self) | -\> FolderId |
| [`significant_frames`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.significant_frames "csc.layers.Viewer.significant_frames")(\*args, \*\*kwargs) | Overloaded function. |
| [`top_layer_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.top_layer_id "csc.layers.Viewer.top_layer_id")(\*args, \*\*kwargs) | Overloaded function. |
| [`unlocked_layer_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer.unlocked_layer_ids "csc.layers.Viewer.unlocked_layer_ids")(self, id\_arr) | -\> LayerId\[\] |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.__module__ "Permalink to this definition")actual\_key\_pos( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.actual_key_pos "Permalink to this definition")all\_child\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.all_child_ids "Permalink to this definition")

-\> ItemId\[\]

all\_included\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _items:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_, _ignore\_locked:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")=False_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.all_included_layer_ids "Permalink to this definition")

items : ItemId\[\] \| ignoreLocked : bool (false) \| -> LayerId\[\]

all\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.all_layer_ids "Permalink to this definition")

-\> LayerId\[\]

all\_parent\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.all_parent_ids "Permalink to this definition")

-\> FolderId\[\]

default\_layer\_id( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.default_layer_id "Permalink to this definition")

-\> LayerId

find\_folder( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.find_folder "Permalink to this definition")

id : FolderId \| -> Folder

find\_layer( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.find_layer "Permalink to this definition")

id : LayerId \| -> Layer

folder( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.folder "Permalink to this definition")

id : FolderId \| -> Folder

folders\_map( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid"), [csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.folders_map "Permalink to this definition")

-\> <FolderId, Folder>{}

for\_all\_ordered\_items( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _arg0:Callable\[\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")\]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.for_all_ordered_items "Permalink to this definition")frames\_count( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.frames_count "Permalink to this definition")

Overloaded function.

1. frames\_count(self: csc.layers.Viewer) -> int

2. frames\_count(self: csc.layers.Viewer, id\_arr: list\[csc.Guid\]) -> int


has\_item( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.has_item "Permalink to this definition")

-\> bool

header( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.header "Permalink to this definition")

id : ItemId \| -> Header

is\_deep\_child( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _item\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_, _folder\_id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.is_deep_child "Permalink to this definition")

-\> bool

item( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[csc.layers.ItemVariant](https://cascadeur.com/python-api/csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.item "Permalink to this definition")

id : ItemId \| -> ItemVariant

last\_key\_pos( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.last_key_pos "Permalink to this definition")

Overloaded function.

1. last\_key\_pos(self: csc.layers.Viewer) -> int

2. last\_key\_pos(self: csc.layers.Viewer, id\_arr: list\[csc.Guid\]) -> int


layer( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.layer "Permalink to this definition")

id : LayerId \| -> Layer

layer\_id\_by\_obj\_id( _self:csc.layers.Viewer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.layer_id_by_obj_id "Permalink to this definition")

id : csc.model.ObjectId \| -> LayerId

layer\_id\_by\_obj\_id\_or\_null( _self:csc.layers.Viewer_, _id:common::GenericId<domain::scene::model::ModelObject>_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.layer_id_by_obj_id_or_null "Permalink to this definition")

id : csc.model.ObjectId \| -> LayerId

layer\_ids\_by\_obj\_ids( _self:csc.layers.Viewer,ids:list\[common::GenericId<domain::scene::model::ModelObject>\]_)→[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.layer_ids_by_obj_ids "Permalink to this definition")

ids : csc.model.ObjectId\[\] \| -> LayerId{}

layers\_indices( _self:csc.layers.Viewer_, _id\_arr:domain::scene::layers::index::IndicesContainer_, _ignore\_locked:bool=False_)→domain::scene::layers::index::IndicesContainer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.layers_indices "Permalink to this definition")

-\> IndicesContainer

layers\_map( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid"), [csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.layers_map "Permalink to this definition")

-\> <LayerId, Layer>{}

merged\_layer( _self:csc.layers.Viewer,scene:domain::scene::Scene,ids:list\[csc.Guid\],normalize:bool=True_)→[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.merged_layer "Permalink to this definition")obj\_ids\_by\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id\_arr:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_)→list\[common::GenericId<domain::scene::model::ModelObject>\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.obj_ids_by_layer_ids "Permalink to this definition")

-\> LayerId\[\]

pos\_in\_parent( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.pos_in_parent "Permalink to this definition")

-\> int

root\_id( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.root_id "Permalink to this definition")

-\> FolderId

significant\_frames( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.significant_frames "Permalink to this definition")

Overloaded function.

1. significant\_frames(self: csc.layers.Viewer) -> domain::scene::layers::index::FramesIndices

2. significant\_frames(self: csc.layers.Viewer, id\_arr: set\[csc.Guid\]) -> domain::scene::layers::index::FramesIndices


top\_layer\_id( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.top_layer_id "Permalink to this definition")

Overloaded function.

1. top\_layer\_id(self: csc.layers.Viewer, id: csc.Guid) -> csc.Guid

2. top\_layer\_id(self: csc.layers.Viewer, id\_arr: list\[csc.Guid\]) -> csc.Guid


unlocked\_layer\_ids( _self:[csc.layers.Viewer](https://cascadeur.com/python-api/csc.html#csc.layers.Viewer "csc.layers.Viewer")_, _id\_arr:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\]_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Viewer.html#csc.layers.Viewer.unlocked_layer_ids "Permalink to this definition")

-\> LayerId\[\]