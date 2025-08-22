---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ClusterViewer.html
html_file: 24a252a4503aeac8d3fefbef3dec51e4.html
module: csc.model.ClusterViewer
---

# csc.model.ClusterViewer[??](#csc-model-clusterviewer "Permalink to this heading")

*class* csc.model.ClusterViewer[??](#csc.model.ClusterViewer "Permalink to this definition")
:   ClusterViewer class

    This class lets read scene data clusters.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.model.ClusterViewer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.model.ClusterViewer.__init__ "csc.model.ClusterViewer.__init__")(\*args,??\*\*kwargs) |  |
    | [`cluster_by_data`](../csc.html#csc.model.ClusterViewer.cluster_by_data "csc.model.ClusterViewer.cluster_by_data")(self,??data\_id) | data\_id : csc.model.DataId | -> ClusterId |
    | [`cluster_datas`](../csc.html#csc.model.ClusterViewer.cluster_datas "csc.model.ClusterViewer.cluster_datas")(self,??cluster\_id) | cluster\_id : ClusterId | -> csc.model.DataId[] |
    | [`cluster_name`](../csc.html#csc.model.ClusterViewer.cluster_name "csc.model.ClusterViewer.cluster_name")(self,??cluster\_id) | cluster\_id : ClusterId | -> string |
    | [`clusters`](../csc.html#csc.model.ClusterViewer.clusters "csc.model.ClusterViewer.clusters")(self) | -> ClusterId[] |
    | [`clusters_bindings`](../csc.html#csc.model.ClusterViewer.clusters_bindings "csc.model.ClusterViewer.clusters_bindings")(self) | -> (ClusterId,ClusterId)[] |

    \_\_annotations\_\_ *= {}*[??](#csc.model.ClusterViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.model'*[??](#csc.model.ClusterViewer.__module__ "Permalink to this definition")

    cluster\_by\_data(*self: [csc.model.ClusterViewer](../csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")*, *data\_id: [csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.model.ClusterViewer.cluster_by_data "Permalink to this definition")
    :   data\_id : csc.model.DataId | -> ClusterId

    cluster\_datas(*self: [csc.model.ClusterViewer](../csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.DataId](../csc.html#csc.model.DataId "csc.model.DataId")][??](#csc.model.ClusterViewer.cluster_datas "Permalink to this definition")
    :   cluster\_id : ClusterId | -> csc.model.DataId[]

    cluster\_name(*self: [csc.model.ClusterViewer](../csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")*, *cluster\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.model.ClusterViewer.cluster_name "Permalink to this definition")
    :   cluster\_id : ClusterId | -> string

    clusters(*self: [csc.model.ClusterViewer](../csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][??](#csc.model.ClusterViewer.clusters "Permalink to this definition")
    :   -> ClusterId[]

    clusters\_bindings(*self: [csc.model.ClusterViewer](../csc.html#csc.model.ClusterViewer "csc.model.ClusterViewer")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.model.ClustersEdge](../csc.html#csc.model.ClustersEdge "csc.model.ClustersEdge")][??](#csc.model.ClusterViewer.clusters_bindings "Permalink to this definition")
    :   -> (ClusterId,ClusterId)[]