---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ClusterViewer.html
html_file: 24a252a4503aeac8d3fefbef3dec51e4.html
module: csc.model.ClusterViewer
---

# csc.model.ClusterViewer 

ClusterViewer class 
This class lets read scene data clusters. Methods __init__ (*args, **kwargs) cluster_by_data (self, data_id) data_id : csc.model.DataId | -> ClusterId cluster_datas (self, cluster_id) cluster_id : ClusterId | -> csc.model.DataId[] cluster_name (self, cluster_id) cluster_id : ClusterId | -> string clusters (self) -> ClusterId[] clusters_bindings (self) -> (ClusterId,ClusterId)[] data_id : csc.model.DataId | -> ClusterId cluster_id : ClusterId | -> csc.model.DataId[] cluster_id : ClusterId | -> string -> ClusterId[] -> (ClusterId,ClusterId)[]