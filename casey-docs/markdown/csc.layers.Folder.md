---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Folder.html
html_file: 18676cfb1da24ecc2317a553278bcb61.html
module: csc.layers.Folder
---

# csc.layers.Folder[??](#csc-layers-folder "Permalink to this heading")

*class* csc.layers.Folder[??](#csc.layers.Folder "Permalink to this definition")
:   Folder class

    Implements the parent folder properties of children layers and sub folders items

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Folder.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.Folder.__init__ "csc.layers.Folder.__init__")(\*args,??\*\*kwargs) |  |
    | [`child_by_id`](../csc.html#csc.layers.Folder.child_by_id "csc.layers.Folder.child_by_id")(self,??id) | -> ItemId |
    | [`child_by_pos`](../csc.html#csc.layers.Folder.child_by_pos "csc.layers.Folder.child_by_pos")(self,??pos) | pos : int -> ItemId |
    | [`child_pos`](../csc.html#csc.layers.Folder.child_pos "csc.layers.Folder.child_pos")(self,??id) | id : ItemId | -> int |
    | [`children_cnt`](../csc.html#csc.layers.Folder.children_cnt "csc.layers.Folder.children_cnt")(self) | -> int |
    | [`children_ids`](../csc.html#csc.layers.Folder.children_ids "csc.layers.Folder.children_ids")(self) | -> ItemId[] |
    | [`children_ordered`](../csc.html#csc.layers.Folder.children_ordered "csc.layers.Folder.children_ordered")(self) | -> ItemId[] |
    | [`has_child`](../csc.html#csc.layers.Folder.has_child "csc.layers.Folder.has_child")(self,??id) |  |
    | [`is_empty`](../csc.html#csc.layers.Folder.is_empty "csc.layers.Folder.is_empty")(self) |  |

    
**Attributes:**

    |  |  |
    | --- | --- |
    | [`header`](../csc.html#csc.layers.Folder.header "csc.layers.Folder.header") | -> Header |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Folder.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Folder.__module__ "Permalink to this definition")

    child\_by\_id(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.Folder.child_by_id "Permalink to this definition")
    :   -> ItemId

    child\_by\_pos(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [csc.Guid](../csc.html#csc.Guid "csc.Guid")[??](#csc.layers.Folder.child_by_pos "Permalink to this definition")
    :   pos : int
        -> ItemId

    child\_pos(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Folder.child_pos "Permalink to this definition")
    :   id : ItemId | -> int

    children\_cnt(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Folder.children_cnt "Permalink to this definition")
    :   -> int

    children\_ids(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](../csc.html#csc.Guid "csc.Guid")][??](#csc.layers.Folder.children_ids "Permalink to this definition")
    :   -> ItemId[]

    children\_ordered(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.Guid](../csc.html#csc.Guid "csc.Guid")][??](#csc.layers.Folder.children_ordered "Permalink to this definition")
    :   -> ItemId[]

    has\_child(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*, *id: [csc.Guid](../csc.html#csc.Guid "csc.Guid")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Folder.has_child "Permalink to this definition")

    *property* header[??](#csc.layers.Folder.header "Permalink to this definition")
    :   -> Header

    is\_empty(*self: [csc.layers.Folder](../csc.html#csc.layers.Folder "csc.layers.Folder")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Folder.is_empty "Permalink to this definition")