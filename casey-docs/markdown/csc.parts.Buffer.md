---
source_url: https://cascadeur.com/python-api/_generate/csc.parts.Buffer.html
html_file: f839f97a48dfa81ef33cc4fb063ec4c8.html
module: csc.parts.Buffer
---

# csc.parts.Buffer[??](#csc-parts-buffer "Permalink to this heading")

*class* csc.parts.Buffer[??](#csc.parts.Buffer "Permalink to this definition")
:   Buffer class

    Provides methods to operate parts of the scene.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.parts.Buffer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.parts.Buffer.__init__ "csc.parts.Buffer.__init__")(\*args,??\*\*kwargs) |  |
    | [`get`](../csc.html#csc.parts.Buffer.get "csc.parts.Buffer.get")([source\_dir]) |  |
    | [`get_parts_info_by_id`](../csc.html#csc.parts.Buffer.get_parts_info_by_id "csc.parts.Buffer.get_parts_info_by_id")(self) |  |
    | [`get_src_dir`](../csc.html#csc.parts.Buffer.get_src_dir "csc.parts.Buffer.get_src_dir")(self) |  |
    | [`insert_elementary_by_id`](../csc.html#csc.parts.Buffer.insert_elementary_by_id "csc.parts.Buffer.insert_elementary_by_id")(self,??arg0,??arg1,??arg2) |  |
    | [`insert_elementary_by_path`](../csc.html#csc.parts.Buffer.insert_elementary_by_path "csc.parts.Buffer.insert_elementary_by_path")(self,??arg0,??arg1,??arg2) |  |
    | [`insert_object_by_id`](../csc.html#csc.parts.Buffer.insert_object_by_id "csc.parts.Buffer.insert_object_by_id")(self,??arg0,??arg1,??arg2,??arg3) |  |
    | [`insert_object_by_path`](../csc.html#csc.parts.Buffer.insert_object_by_path "csc.parts.Buffer.insert_object_by_path")(self,??arg0,??arg1,??...) |  |
    | [`insert_objects_by_id`](../csc.html#csc.parts.Buffer.insert_objects_by_id "csc.parts.Buffer.insert_objects_by_id")(self,??arg0,??arg1,??arg2,??...) |  |
    | [`insert_objects_by_path`](../csc.html#csc.parts.Buffer.insert_objects_by_path "csc.parts.Buffer.insert_objects_by_path")(self,??arg0,??arg1,??...) |  |
    | [`insert_selected_objects_by_path`](../csc.html#csc.parts.Buffer.insert_selected_objects_by_path "csc.parts.Buffer.insert_selected_objects_by_path")(self,??arg0,??...) |  |
    | [`insert_update_group_by_id`](../csc.html#csc.parts.Buffer.insert_update_group_by_id "csc.parts.Buffer.insert_update_group_by_id")(self,??arg0,??arg1,??arg2) |  |
    | [`insert_update_group_by_path`](../csc.html#csc.parts.Buffer.insert_update_group_by_path "csc.parts.Buffer.insert_update_group_by_path")(self,??arg0,??...) |  |
    | [`refresh`](../csc.html#csc.parts.Buffer.refresh "csc.parts.Buffer.refresh")(self) |  |
    | [`reset_cache`](../csc.html#csc.parts.Buffer.reset_cache "csc.parts.Buffer.reset_cache")(self) |  |
    | [`take_elementary_to_parts`](../csc.html#csc.parts.Buffer.take_elementary_to_parts "csc.parts.Buffer.take_elementary_to_parts")(self,??part\_name,??...) |  |
    | [`take_object_to_parts`](../csc.html#csc.parts.Buffer.take_object_to_parts "csc.parts.Buffer.take_object_to_parts")(self,??part\_name,??from,??...) |  |
    | [`take_objects_to_parts`](../csc.html#csc.parts.Buffer.take_objects_to_parts "csc.parts.Buffer.take_objects_to_parts")(self,??part\_name,??from,??...) |  |
    | [`take_selected_objects_to_parts`](../csc.html#csc.parts.Buffer.take_selected_objects_to_parts "csc.parts.Buffer.take_selected_objects_to_parts")(self,??...) |  |
    | [`take_update_group_to_parts`](../csc.html#csc.parts.Buffer.take_update_group_to_parts "csc.parts.Buffer.take_update_group_to_parts")(self,??part\_name,??...) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.parts.Buffer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.parts'*[??](#csc.parts.Buffer.__module__ "Permalink to this definition")

    *static* get(*source\_dir: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = ''*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.parts.Buffer.get "Permalink to this definition")

    get\_parts\_info\_by\_id(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.parts.Info](../csc.html#csc.parts.Info "csc.parts.Info")][??](#csc.parts.Buffer.get_parts_info_by_id "Permalink to this definition")

    get\_src\_dir(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.parts.Buffer.get_src_dir "Permalink to this definition")

    insert\_elementary\_by\_id(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.parts.GroupInfo](../csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")[??](#csc.parts.Buffer.insert_elementary_by_id "Permalink to this definition")

    insert\_elementary\_by\_path(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [csc.parts.GroupInfo](../csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")[??](#csc.parts.Buffer.insert_elementary_by_path "Permalink to this definition")

    insert\_object\_by\_id(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.parts.Buffer.insert_object_by_id "Permalink to this definition")

    insert\_object\_by\_path(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.parts.Buffer.insert_object_by_path "Permalink to this definition")

    insert\_objects\_by\_id(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")], [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")]][??](#csc.parts.Buffer.insert_objects_by_id "Permalink to this definition")

    insert\_objects\_by\_path(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")], [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")]][??](#csc.parts.Buffer.insert_objects_by_path "Permalink to this definition")

    insert\_selected\_objects\_by\_path(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*, *arg3: [csc.domain.assets.AssetsManager](csc.domain.assets.AssetsManager.html#csc.domain.assets.AssetsManager "csc.domain.assets.AssetsManager")*)  [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.parts.Buffer.insert_selected_objects_by_path "Permalink to this definition")

    insert\_update\_group\_by\_id(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[csc.parts.GroupInfo](../csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId"), [csc.parts.GroupInfo](../csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")]][??](#csc.parts.Buffer.insert_update_group_by_id "Permalink to this definition")

    insert\_update\_group\_by\_path(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*, *arg0: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *arg1: [csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId")*, *arg2: [csc.model.ModelEditor](../csc.html#csc.model.ModelEditor "csc.model.ModelEditor")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[csc.parts.GroupInfo](../csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[csc.update.GroupId](../csc.html#csc.update.GroupId "csc.update.GroupId"), [csc.parts.GroupInfo](../csc.html#csc.parts.GroupInfo "csc.parts.GroupInfo")]][??](#csc.parts.Buffer.insert_update_group_by_path "Permalink to this definition")

    refresh(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.Buffer.refresh "Permalink to this definition")

    reset\_cache(*self: [csc.parts.Buffer](../csc.html#csc.parts.Buffer "csc.parts.Buffer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.parts.Buffer.reset_cache "Permalink to this definition")

    take\_elementary\_to\_parts(*self: csc.parts.Buffer*, *part\_name: str*, *from: csc.domain.Scene*, *object\_id: csc.model.ObjectId*, *parent\_group: csc.update.GroupId*, *elementary: csc.parts.GroupInfo*, *path\_to\_scene\_parts: str*)  [csc.parts.Info](../csc.html#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_elementary_to_parts "Permalink to this definition")

    take\_object\_to\_parts(*self: csc.parts.Buffer*, *part\_name: str*, *from: csc.domain.Scene*, *object\_id: csc.model.ObjectId*, *path\_to\_scene\_parts: str*)  [csc.parts.Info](../csc.html#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_object_to_parts "Permalink to this definition")

    take\_objects\_to\_parts(*self: csc.parts.Buffer, part\_name: str, from: csc.domain.Scene, objects: list[csc.model.ObjectId], objects\_grs: list[csc.update.GroupId], path\_to\_scene\_parts: str*)  [csc.parts.Info](../csc.html#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_objects_to_parts "Permalink to this definition")

    take\_selected\_objects\_to\_parts(*self: csc.parts.Buffer, part\_name: str, from: csc.domain.Scene, selected\_objects: list[csc.model.ObjectId], path\_to\_scene\_parts: str*)  [csc.parts.Info](../csc.html#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_selected_objects_to_parts "Permalink to this definition")

    take\_update\_group\_to\_parts(*self: csc.parts.Buffer, part\_name: str, from: csc.domain.Scene, object\_id: csc.model.ObjectId, parent\_group: csc.update.GroupId, elementary: csc.parts.GroupInfo, sub\_groups: list[csc.update.GroupId], path\_to\_scene\_parts: str*)  [csc.parts.Info](../csc.html#csc.parts.Info "csc.parts.Info")[??](#csc.parts.Buffer.take_update_group_to_parts "Permalink to this definition")