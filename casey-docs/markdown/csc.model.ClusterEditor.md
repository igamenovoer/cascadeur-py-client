---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ClusterEditor.html
html_file: 3abc023119537a0e71a2e506b0be5426.html
module: csc.model.ClusterEditor
---

# csc.model.ClusterEditor[??](#csc-model-clustereditor "Permalink to this heading")

*class* csc.model.ClusterEditor[??](#csc.model.ClusterEditor "Permalink to this definition")
:   ClusterEditor class

    This class lets edit scene data clusters.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ClusterEditor.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.ClusterEditor.__init__ "csc.model.ClusterEditor.__init__")(\*args,??\*\*kwargs) |  |
    | [`add_cluster`](../csc.html#csc.model.ClusterEditor.add_cluster "csc.model.ClusterEditor.add_cluster")(self,??inserted\_ids,??name) | insertedIds : csc.model.DataId[] | name : string ("") | -> ClusterId |
    | [`add_data_to_cluster`](../csc.html#csc.model.ClusterEditor.add_data_to_cluster "csc.model.ClusterEditor.add_data_to_cluster")(self,??cluster\_index,??...) | cluster\_index : ClusterId | insertedIds : csc.model.DataId[] |
    | [`bind_clusters`](../csc.html#csc.model.ClusterEditor.bind_clusters "csc.model.ClusterEditor.bind_clusters")(self,??cluster\_id\_first,??...) | cluster\_id\_first : ClusterId | cluster\_id\_second : ClusterId |
    | [`remove_cluster`](../csc.html#csc.model.ClusterEditor.remove_cluster "csc.model.ClusterEditor.remove_cluster")(self,??cluster\_id) | cluster\_id : ClusterId |
    | [`remove_data_from_cluster`](../csc.html#csc.model.ClusterEditor.remove_data_from_cluster "csc.model.ClusterEditor.remove_data_from_cluster")(self,??data\_id) | data\_id : csc.model.DataId |
    | [`set_cluster_name`](../csc.html#csc.model.ClusterEditor.set_cluster_name "csc.model.ClusterEditor.set_cluster_name")(self,??cluster\_id,??name) | cluster\_id : ClusterId | name : string |
    | [`unbind_cluster`](../csc.html#csc.model.ClusterEditor.unbind_cluster "csc.model.ClusterEditor.unbind_cluster")(self,??cluster\_id) | cluster\_id : ClusterId |
    | [`unbind_clusters`](../csc.html#csc.model.ClusterEditor.unbind_clusters "csc.model.ClusterEditor.unbind_clusters")(self,??cluster\_id\_first,??...) | cluster\_id\_first : ClusterId | cluster\_id\_second : ClusterId |

    \_\_annotations\_\_ *= {}*[??](#csc.model.ClusterEditor.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ClusterEditor.__module__ "Permalink to this definition")

    add\_cluster(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.ClusterEditor.add_cluster "Permalink to this definition")
    :   insertedIds : csc.model.DataId[] | name : string (??????) | -> ClusterId

    add\_data\_to\_cluster(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *inserted\_ids: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")]*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.add_data_to_cluster "Permalink to this definition")
    :   cluster\_index : ClusterId | insertedIds : csc.model.DataId[]

    bind\_clusters(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id\_first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *cluster\_id\_second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.bind_clusters "Permalink to this definition")
    :   cluster\_id\_first : ClusterId | cluster\_id\_second : ClusterId

    remove\_cluster(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.remove_cluster "Permalink to this definition")
    :   cluster\_id : ClusterId

    remove\_data\_from\_cluster(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *data\_id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.remove_data_from_cluster "Permalink to this definition")
    :   data\_id : csc.model.DataId

    set\_cluster\_name(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.set_cluster_name "Permalink to this definition")
    :   cluster\_id : ClusterId | name : string

    unbind\_cluster(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.unbind_cluster "Permalink to this definition")
    :   cluster\_id : ClusterId

    unbind\_clusters(*self: [csc.model.ClusterEditor](../csc.html#csc.model.ClusterEditor "csc.model.ClusterEditor")*, *cluster\_id\_first: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *cluster\_id\_second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.model.ClusterEditor.unbind_clusters "Permalink to this definition")
    :   cluster\_id\_first : ClusterId | cluster\_id\_second : ClusterId