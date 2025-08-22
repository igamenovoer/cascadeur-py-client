---
source_url: https://cascadeur.com/python-api/_generate/csc.update.Connection.html
html_file: d836b7c6e06abf0af79e41f0ff04f19a.html
module: csc.update.Connection
---

# csc.update.Connection[??](#csc-update-connection "Permalink to this heading")

*class* csc.update.Connection[??](#csc.update.Connection "Permalink to this definition")
:   Connection class

    Implements the Connection between two attributes

    Variables:
    :   * **source** ??? Get output AttributeId of the source
        * **destination** ??? Get input AttributeId of the destination

    AttributeId = std::variant<RegularFunctionAttributeId, ActivityAttributeId,
    :   RegularDataAttributeId, ActualityAttributeId,
        SettingFunctionAttributeId, SettingDataAttributeId,
        GroupAttributeId, ExternalPropertyAttributeId,
        ConstantDataAttributeId, ConstantSettingAttributeId>

    \_\_init\_\_(*self: [csc.update.Connection](../csc.html#csc.update.Connection "csc.update.Connection")*, *source: [csc.update.RegularFunctionAttributeId](../csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](../csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](../csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](../csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](../csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](../csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](../csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](../csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*, *destination: [csc.update.RegularFunctionAttributeId](../csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](../csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](../csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](../csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](../csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](../csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](../csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](../csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.update.Connection.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.Connection.__init__ "csc.update.Connection.__init__")(self,??source,??destination) |  |

    
**Attributes:**

    |  |  |
    | --- | --- |
    | [`destination`](../csc.html#csc.update.Connection.destination "csc.update.Connection.destination") |  |
    | [`source`](../csc.html#csc.update.Connection.source "csc.update.Connection.source") |  |

    \_\_annotations\_\_ *= {}*[??](#csc.update.Connection.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.update.Connection](../csc.html#csc.update.Connection "csc.update.Connection")*, *source: [csc.update.RegularFunctionAttributeId](../csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](../csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](../csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](../csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](../csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](../csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](../csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](../csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*, *destination: [csc.update.RegularFunctionAttributeId](../csc.html#csc.update.RegularFunctionAttributeId "csc.update.RegularFunctionAttributeId") | [csc.model.HyperedgeId](../csc.html#csc.model.HyperedgeId "csc.model.HyperedgeId") | [csc.update.RegularDataAttributeId](../csc.html#csc.update.RegularDataAttributeId "csc.update.RegularDataAttributeId") | [csc.update.ActualityAttributeId](../csc.html#csc.update.ActualityAttributeId "csc.update.ActualityAttributeId") | [csc.update.SettingFunctionAttributeId](../csc.html#csc.update.SettingFunctionAttributeId "csc.update.SettingFunctionAttributeId") | [csc.model.SettingId](../csc.html#csc.model.SettingId "csc.model.SettingId") | [csc.update.GroupAttributeId](../csc.html#csc.update.GroupAttributeId "csc.update.GroupAttributeId") | [csc.update.ExternalPropertyAttributeId](../csc.html#csc.update.ExternalPropertyAttributeId "csc.update.ExternalPropertyAttributeId") | [csc.update.ConstantDataAttributeId](../csc.html#csc.update.ConstantDataAttributeId "csc.update.ConstantDataAttributeId") | [csc.update.ConstantSettingAttributeId](../csc.html#csc.update.ConstantSettingAttributeId "csc.update.ConstantSettingAttributeId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.Connection.__module__ "Permalink to this definition")

    *property* destination[??](#csc.update.Connection.destination "Permalink to this definition")

    *property* source[??](#csc.update.Connection.source "Permalink to this definition")