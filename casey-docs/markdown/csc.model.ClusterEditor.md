---
source_url: https://cascadeur.com/python-api/_generate/csc.model.ClusterEditor.html
html_file: 3abc023119537a0e71a2e506b0be5426.html
module: csc.model.ClusterEditor
---

# csc.model.ClusterEditor 

ClusterEditor class 
This class lets edit scene data clusters. Methods __init__ (*args, **kwargs) add_cluster (self, inserted_ids, name) insertedIds : csc.model.DataId[] | name : string ("") | -> ClusterId add_data_to_cluster (self, cluster_index, ...) cluster_index : ClusterId | insertedIds : csc.model.DataId[] bind_clusters (self, cluster_id_first, ...) cluster_id_first : ClusterId | cluster_id_second : ClusterId remove_cluster (self, cluster_id) cluster_id : ClusterId remove_data_from_cluster (self, data_id) data_id : csc.model.DataId set_cluster_name (self, cluster_id, name) cluster_id : ClusterId | name : string unbind_cluster (self, cluster_id) cluster_id : ClusterId unbind_clusters (self, cluster_id_first, ...) cluster_id_first : ClusterId | cluster_id_second : ClusterId insertedIds : csc.model.DataId[] | name : string (ââ) | -> ClusterId cluster_index : ClusterId | insertedIds : csc.model.DataId[] cluster_id_first : ClusterId | cluster_id_second : ClusterId cluster_id : ClusterId data_id : csc.model.DataId cluster_id : ClusterId | name : string cluster_id : ClusterId cluster_id_first : ClusterId | cluster_id_second : ClusterId