---
source_url: https://cascadeur.com/python-api/_generate/csc.model.BehaviourEditor.html
html_file: df4669b4ca27a47dba96f33d977a19ef.html
module: csc.model.BehaviourEditor
---

# csc.model.BehaviourEditor[??](#csc-model-behavioureditor "Permalink to this heading")

*class* csc.model.BehaviourEditor[??](#csc.model.BehaviourEditor "Permalink to this definition")
:   BehaviourEditor class

    This class allows editing of scene behaviours and their properties.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourEditor.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.BehaviourEditor.__init__ "csc.model.BehaviourEditor.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_behaviour`](../csc.html#csc.model.BehaviourEditor.add_behaviour "csc.model.BehaviourEditor.add_behaviour")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`add_behaviour_asset_to_range`](../csc.html#csc.model.BehaviourEditor.add_behaviour_asset_to_range "csc.model.BehaviourEditor.add_behaviour_asset_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | asset\_id : csc.domain.AssetId |
    | [`add_behaviour_data_to_range`](../csc.html#csc.model.BehaviourEditor.add_behaviour_data_to_range "csc.model.BehaviourEditor.add_behaviour_data_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | data\_id : csc.model.DataId |
    | [`add_behaviour_model_object_to_range`](../csc.html#csc.model.BehaviourEditor.add_behaviour_model_object_to_range "csc.model.BehaviourEditor.add_behaviour_model_object_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId |
    | [`add_behaviour_reference_to_range`](../csc.html#csc.model.BehaviourEditor.add_behaviour_reference_to_range "csc.model.BehaviourEditor.add_behaviour_reference_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId |
    | [`add_behaviour_setting_to_range`](../csc.html#csc.model.BehaviourEditor.add_behaviour_setting_to_range "csc.model.BehaviourEditor.add_behaviour_setting_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId |
    | [`delete_behaviour`](../csc.html#csc.model.BehaviourEditor.delete_behaviour "csc.model.BehaviourEditor.delete_behaviour")(self,??behaviour\_id) | behaviour\_id : csc.model.BehaviourId |
    | [`delete_behaviours`](../csc.html#csc.model.BehaviourEditor.delete_behaviours "csc.model.BehaviourEditor.delete_behaviours")(self,??objects\_id) | objectsId : {csc.model.ObjectId} |
    | [`erase_behaviour_data_from_range`](../csc.html#csc.model.BehaviourEditor.erase_behaviour_data_from_range "csc.model.BehaviourEditor.erase_behaviour_data_from_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | data\_id : csc.model.DataId |
    | [`erase_behaviour_model_object_from_range`](../csc.html#csc.model.BehaviourEditor.erase_behaviour_model_object_from_range "csc.model.BehaviourEditor.erase_behaviour_model_object_from_range")(...) | behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId |
    | [`erase_behaviour_reference_from_range`](../csc.html#csc.model.BehaviourEditor.erase_behaviour_reference_from_range "csc.model.BehaviourEditor.erase_behaviour_reference_from_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId |
    | [`erase_behaviour_setting_from_range`](../csc.html#csc.model.BehaviourEditor.erase_behaviour_setting_from_range "csc.model.BehaviourEditor.erase_behaviour_setting_from_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId |
    | [`get_viewer`](../csc.html#csc.model.BehaviourEditor.get_viewer "csc.model.BehaviourEditor.get_viewer")(self) |  |
    | [`hide_behaviour`](../csc.html#csc.model.BehaviourEditor.hide_behaviour "csc.model.BehaviourEditor.hide_behaviour")(self,??behaviour\_id[,??hidden]) | behaviour\_id : csc.model.BehaviourId | hidden : bool(true) -> bool |
    | [`set_behaviour_asset`](../csc.html#csc.model.BehaviourEditor.set_behaviour_asset "csc.model.BehaviourEditor.set_behaviour_asset")(self,??behaviour\_id,??...) | behaviour\_id : csc.model.BehaviourId | name : string | asset\_id : csc.domain.AssetId |
    | [`set_behaviour_data`](../csc.html#csc.model.BehaviourEditor.set_behaviour_data "csc.model.BehaviourEditor.set_behaviour_data")(self,??behaviour\_id,??name,??...) | behaviour\_id : csc.model.BehaviourId | name : string | dataId : csc.model.DataId |
    | [`set_behaviour_data_to_range`](../csc.html#csc.model.BehaviourEditor.set_behaviour_data_to_range "csc.model.BehaviourEditor.set_behaviour_data_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.DataId |
    | [`set_behaviour_field_value`](../csc.html#csc.model.BehaviourEditor.set_behaviour_field_value "csc.model.BehaviourEditor.set_behaviour_field_value")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | name\_value : string |
    | [`set_behaviour_model_object`](../csc.html#csc.model.BehaviourEditor.set_behaviour_model_object "csc.model.BehaviourEditor.set_behaviour_model_object")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId |
    | [`set_behaviour_model_objects_to_range`](../csc.html#csc.model.BehaviourEditor.set_behaviour_model_objects_to_range "csc.model.BehaviourEditor.set_behaviour_model_objects_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.ObjectId[] |
    | [`set_behaviour_reference`](../csc.html#csc.model.BehaviourEditor.set_behaviour_reference "csc.model.BehaviourEditor.set_behaviour_reference")(self,??behaviour\_id,??...) | behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId |
    | [`set_behaviour_references_to_range`](../csc.html#csc.model.BehaviourEditor.set_behaviour_references_to_range "csc.model.BehaviourEditor.set_behaviour_references_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.BehaviourId[] |
    | [`set_behaviour_setting`](../csc.html#csc.model.BehaviourEditor.set_behaviour_setting "csc.model.BehaviourEditor.set_behaviour_setting")(self,??behaviour\_id,??...) | behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId |
    | [`set_behaviour_settings_to_range`](../csc.html#csc.model.BehaviourEditor.set_behaviour_settings_to_range "csc.model.BehaviourEditor.set_behaviour_settings_to_range")(self,??...) | behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.SettingId[] |
    | [`set_behaviour_string`](../csc.html#csc.model.BehaviourEditor.set_behaviour_string "csc.model.BehaviourEditor.set_behaviour_string")(self,??behaviour\_id,??...) | behaviour\_id : csc.model.BehaviourId | name : string | str : string |

    \_\_annotations\_\_ *= {}*[??](#csc.model.BehaviourEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.BehaviourEditor.__module__ "Permalink to this definition")

    add\_behaviour(*\*args*, *\*\*kwargs*)[??](#csc.model.BehaviourEditor.add_behaviour "Permalink to this definition")
    :   Overloaded function.

        1. add\_behaviour(self: csc.model.BehaviourEditor, arg0: csc.model.ObjectId, arg1: str) -> csc.model.BehaviourId

           > object\_id : csc.model.ObjectId | behaviour\_type : string | -> csc.model.BehaviourId
        2. add\_behaviour(self: csc.model.BehaviourEditor, object\_id: csc.model.ObjectId, behaviour\_type: str, behaviour\_id: csc.model.BehaviourId) -> csc.model.BehaviourId

           > object\_id : csc.model.ObjectId | behaviour\_type : string | behaviour\_id : csc.model.BehaviourId | -> csc.model.BehaviourId

    add\_behaviour\_asset\_to\_range(*self: csc.model.BehaviourEditor*, *behaviour\_id: csc.model.BehaviourId*, *name: str*, *asset\_id: common::GenericId<domain::scene::assets::Asset>*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_asset_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | asset\_id : csc.domain.AssetId

    add\_behaviour\_data\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *data\_id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_data_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | data\_id : csc.model.DataId

    add\_behaviour\_model\_object\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *mo\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_model_object_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId

    add\_behaviour\_reference\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *beh\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_reference_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId

    add\_behaviour\_setting\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *setting\_id: [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.add_behaviour_setting_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId

    delete\_behaviour(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.BehaviourEditor.delete_behaviour "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId

    delete\_behaviours(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *objects\_id: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.BehaviourEditor.delete_behaviours "Permalink to this definition")
    :   objectsId : {csc.model.ObjectId}

    erase\_behaviour\_data\_from\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *data\_id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_data_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | data\_id : csc.model.DataId

    erase\_behaviour\_model\_object\_from\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *mo\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_model_object_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId

    erase\_behaviour\_reference\_from\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *beh\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_reference_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId

    erase\_behaviour\_setting\_from\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *setting\_id: [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.erase_behaviour_setting_from_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId

    get\_viewer(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*)  [csc.model.BehaviourViewer](../csc.html#csc.model.BehaviourViewer "csc.model.BehaviourViewer")[??](#csc.model.BehaviourEditor.get_viewer "Permalink to this definition")

    hide\_behaviour(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *hidden: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = True*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.hide_behaviour "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | hidden : bool(true) -> bool

    set\_behaviour\_asset(*self: csc.model.BehaviourEditor*, *behaviour\_id: csc.model.BehaviourId*, *name: str*, *asset\_id: common::GenericId<domain::scene::assets::Asset>*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_asset "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | asset\_id : csc.domain.AssetId

    set\_behaviour\_data(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *data\_id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_data "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | dataId : csc.model.DataId

    set\_behaviour\_data\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_data_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.DataId

    set\_behaviour\_field\_value(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *name\_value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_field_value "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | name\_value : string

    set\_behaviour\_model\_object(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *mo\_id: [csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_model_object "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | mo\_id : csc.model.ObjectId

    set\_behaviour\_model\_objects\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ObjectId](../csc.html#csc.model.ObjectId "csc.model.ObjectId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_model_objects_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.ObjectId[]

    set\_behaviour\_reference(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *beh\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_reference "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | beh\_id : csc.model.BehaviourId

    set\_behaviour\_references\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_references_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.BehaviourId[]

    set\_behaviour\_setting(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *setting\_id: [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_setting "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | setting\_id : csc.model.SettingId

    set\_behaviour\_settings\_to\_range(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId")]*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_settings_to_range "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | inserted\_ids : csc.model.SettingId[]

    set\_behaviour\_string(*self: [csc.model.BehaviourEditor](../csc.html#csc.model.BehaviourEditor "csc.model.BehaviourEditor")*, *behaviour\_id: [csc.model.BehaviourId](../csc.html#csc.model.BehaviourId "csc.model.BehaviourId")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *str: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.model.BehaviourEditor.set_behaviour_string "Permalink to this definition")
    :   behaviour\_id : csc.model.BehaviourId | name : string | str : string