# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.Folder.html

# csc.layers.Folder [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html\#csc-layers-folder "Permalink to this heading")

_class_ csc.layers.Folder [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder "Permalink to this definition")

Folder class

Implements the parent folder properties of children layers and sub folders items

\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.__init__ "csc.layers.Folder.__init__")(\*args, \*\*kwargs) |  |
| [`child_by_id`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.child_by_id "csc.layers.Folder.child_by_id")(self, id) | -\> ItemId |
| [`child_by_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.child_by_pos "csc.layers.Folder.child_by_pos")(self, pos) | pos : int -> ItemId |
| [`child_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.child_pos "csc.layers.Folder.child_pos")(self, id) | id : ItemId \| -> int |
| [`children_cnt`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.children_cnt "csc.layers.Folder.children_cnt")(self) | -\> int |
| [`children_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.children_ids "csc.layers.Folder.children_ids")(self) | -\> ItemId\[\] |
| [`children_ordered`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.children_ordered "csc.layers.Folder.children_ordered")(self) | -\> ItemId\[\] |
| [`has_child`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.has_child "csc.layers.Folder.has_child")(self, id) |  |
| [`is_empty`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.is_empty "csc.layers.Folder.is_empty")(self) |  |

Attributes

|     |     |
| --- | --- |
| [`header`](https://cascadeur.com/python-api/csc.html#csc.layers.Folder.header "csc.layers.Folder.header") | -\> Header |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.__module__ "Permalink to this definition")child\_by\_id( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.child_by_id "Permalink to this definition")

-\> ItemId

child\_by\_pos( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.child_by_pos "Permalink to this definition")

pos : int
-\> ItemId

child\_pos( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.child_pos "Permalink to this definition")

id : ItemId \| -> int

children\_cnt( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.children_cnt "Permalink to this definition")

-\> int

children\_ids( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.children_ids "Permalink to this definition")

-\> ItemId\[\]

children\_ordered( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")\[ [csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")\] [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.children_ordered "Permalink to this definition")

-\> ItemId\[\]

has\_child( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_, _id:[csc.Guid](https://cascadeur.com/python-api/csc.html#csc.Guid "csc.Guid")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.has_child "Permalink to this definition")_property_ header [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.header "Permalink to this definition")

-\> Header

is\_empty( _self:[csc.layers.Folder](https://cascadeur.com/python-api/csc.html#csc.layers.Folder "csc.layers.Folder")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Folder.html#csc.layers.Folder.is_empty "Permalink to this definition")