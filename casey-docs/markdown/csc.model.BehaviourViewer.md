---
source_url: https://cascadeur.com/python-api/_generate/csc.model.BehaviourViewer.html
html_file: be9ab243b7070ca4aec36922171e15b3.html
module: csc.model.BehaviourViewer
---

# csc.model.BehaviourViewer[??](#csc-model-behaviourviewer "Permalink to this heading")

*class* csc.model.BehaviourViewer[??](#csc.model.BehaviourViewer "Permalink to this definition")
:   BehaviourViewer class

    This class allows viewing of scene behaviours and their properties.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourViewer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.BehaviourViewer.__init__ "csc.model.BehaviourViewer.__init__")(\*args,??\*\*kwargs) |  |
    | [`behaviour_id`](../csc.html#csc.model.BehaviourViewer.behaviour_id "csc.model.BehaviourViewer.behaviour_id")(self,??object\_id,??behaviour\_name) | objectId : csc.model.ObjectId | behaviour\_name : string | -> csc.model.BehaviourId |
    | [`get_behaviour_asset`](../csc.html#csc.model.BehaviourViewer.get_behaviour_asset "csc.model.BehaviourViewer.get_behaviour_asset")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId |
    | [`get_behaviour_asset_range`](../csc.html#csc.model.BehaviourViewer.get_behaviour_asset_range "csc.model.BehaviourViewer.get_behaviour_asset_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[] |
    | [`get_behaviour_by_name`](../csc.html#csc.model.BehaviourViewer.get_behaviour_by_name "csc.model.BehaviourViewer.get_behaviour_by_name")(self,??object\_id,??...) | objectId : csc.model.ObjectId | behaviour\_name : string | -> csc.model.BehaviourId |
    | [`get_behaviour_data`](../csc.html#csc.model.BehaviourViewer.get_behaviour_data "csc.model.BehaviourViewer.get_behaviour_data")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.DataId |
    | [`get_behaviour_data_range`](../csc.html#csc.model.BehaviourViewer.get_behaviour_data_range "csc.model.BehaviourViewer.get_behaviour_data_range")(self,??behaviour\_id,??...) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.DataId[] |
    | [`get_behaviour_name`](../csc.html#csc.model.BehaviourViewer.get_behaviour_name "csc.model.BehaviourViewer.get_behaviour_name")(self,??behaviour\_id) | behaviour\_id : csc.model.BehaviourId | -> string |
    | [`get_behaviour_object`](../csc.html#csc.model.BehaviourViewer.get_behaviour_object "csc.model.BehaviourViewer.get_behaviour_object")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId |
    | [`get_behaviour_objects_range`](../csc.html#csc.model.BehaviourViewer.get_behaviour_objects_range "csc.model.BehaviourViewer.get_behaviour_objects_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId[] |
    | [`get_behaviour_owner`](../csc.html#csc.model.BehaviourViewer.get_behaviour_owner "csc.model.BehaviourViewer.get_behaviour_owner")(self,??behaviour\_id) | behaviour\_id : csc.model.BehaviourId | -> csc.model.ObjectId |
    | [`get_behaviour_property_names`](../csc.html#csc.model.BehaviourViewer.get_behaviour_property_names "csc.model.BehaviourViewer.get_behaviour_property_names")(self,??behaviour\_id) | -> string[] |
    | [`get_behaviour_reference`](../csc.html#csc.model.BehaviourViewer.get_behaviour_reference "csc.model.BehaviourViewer.get_behaviour_reference")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId |
    | [`get_behaviour_reference_range`](../csc.html#csc.model.BehaviourViewer.get_behaviour_reference_range "csc.model.BehaviourViewer.get_behaviour_reference_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[] |
    | [`get_behaviour_setting`](../csc.html#csc.model.BehaviourViewer.get_behaviour_setting "csc.model.BehaviourViewer.get_behaviour_setting")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId |
    | [`get_behaviour_settings_range`](../csc.html#csc.model.BehaviourViewer.get_behaviour_settings_range "csc.model.BehaviourViewer.get_behaviour_settings_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId[] |
    | [`get_behaviour_string`](../csc.html#csc.model.BehaviourViewer.get_behaviour_string "csc.model.BehaviourViewer.get_behaviour_string")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> string |
    | [`get_behaviours`](../csc.html#csc.model.BehaviourViewer.get_behaviours "csc.model.BehaviourViewer.get_behaviours")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`get_children`](../csc.html#csc.model.BehaviourViewer.get_children "csc.model.BehaviourViewer.get_children")(self,??object\_id) | -> Children behs ids |
    | [`get_property_type`](../csc.html#csc.model.BehaviourViewer.get_property_type "csc.model.BehaviourViewer.get_property_type")(self,??behaviour\_id,??name) | behaviour\_id : csc.model.BehaviourId | name : string | -> Type[] |
    | [`is_hidden`](../csc.html#csc.model.BehaviourViewer.is_hidden "csc.model.BehaviourViewer.is_hidden")(self,??behaviour\_id) | -> bool |
    | [`is_valid_behaviour_type`](../csc.html#csc.model.BehaviourViewer.is_valid_behaviour_type "csc.model.BehaviourViewer.is_valid_behaviour_type")(self,??behaviour\_name) | behaviour\_name : string | -> bool |

    \_\_annotations\_\_ *= {}*[??](#csc.model.BehaviourViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.BehaviourViewer.__module__ "Permalink to this definition")

    behaviour\_id(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *object\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *behaviour\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourViewer.behaviour_id "Permalink to this definition")
    :   objectId : csc.model.ObjectId | behaviour\_name : string | -> csc.model.BehaviourId

    get\_behaviour\_asset(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  common::GenericId<domain::scene::assets::Asset>[??](#csc.model.BehaviourViewer.get_behaviour_asset "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId

    get\_behaviour\_asset\_range(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  list[common::GenericId<domain::scene::assets::Asset>][??](#csc.model.BehaviourViewer.get_behaviour_asset_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[]

    get\_behaviour\_by\_name(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *object\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*, *behaviour\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourViewer.get_behaviour_by_name "Permalink to this definition")
    :   objectId : csc.model.ObjectId | behaviour\_name : string | -> csc.model.BehaviourId

    get\_behaviour\_data(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")[??](#csc.model.BehaviourViewer.get_behaviour_data "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.DataId

    get\_behaviour\_data\_range(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")][??](#csc.model.BehaviourViewer.get_behaviour_data_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.DataId[]

    get\_behaviour\_name(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.BehaviourViewer.get_behaviour_name "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | -> string

    get\_behaviour\_object(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.model.BehaviourViewer.get_behaviour_object "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId

    get\_behaviour\_objects\_range(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")][??](#csc.model.BehaviourViewer.get_behaviour_objects_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.ObjectId[]

    get\_behaviour\_owner(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")[??](#csc.model.BehaviourViewer.get_behaviour_owner "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | -> csc.model.ObjectId

    get\_behaviour\_property\_names(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][??](#csc.model.BehaviourViewer.get_behaviour_property_names "Permalink to this definition")
    :   -> string[]

    get\_behaviour\_reference(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")[??](#csc.model.BehaviourViewer.get_behaviour_reference "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId

    get\_behaviour\_reference\_range(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")][??](#csc.model.BehaviourViewer.get_behaviour_reference_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.BehaviourId[]

    get\_behaviour\_setting(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")[??](#csc.model.BehaviourViewer.get_behaviour_setting "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId

    get\_behaviour\_settings\_range(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")][??](#csc.model.BehaviourViewer.get_behaviour_settings_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> csc.model.SettingId[]

    get\_behaviour\_string(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.BehaviourViewer.get_behaviour_string "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> string

    get\_behaviours(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourViewer.get_behaviours "Permalink to this definition")
    :   Overloaded function.

        1. get\_behaviours(self: csc.model.BehaviourViewer, type\_name: str) -> list[csc.model.BehaviourId]

           > typeName : string | -> csc.model.BehaviourId[]
        2. get\_behaviours(self: csc.model.BehaviourViewer, object\_id: csc.model.ObjectId) -> list[csc.model.BehaviourId]

           > objectId : csc.model.ObjectId | -> csc.model.BehaviourId[]

    get\_children(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *object\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")][??](#csc.model.BehaviourViewer.get_children "Permalink to this definition")
    :   -> Children behs ids

    get\_property\_type(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [csc.model.PropertyType](../csc.html#csc.model.PropertyType "csc.model.PropertyType")[??](#csc.model.BehaviourViewer.get_property_type "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | -> Type[]

    is\_hidden(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourViewer.is_hidden "Permalink to this definition")
    :   -> bool

    is\_valid\_behaviour\_type(*self: [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")*, *behaviour\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourViewer.is_valid_behaviour_type "Permalink to this definition")
    :   behaviour\_name : string | -> bool