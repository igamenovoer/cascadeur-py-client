[CLEAN]

# csc.model.ClusterEditor

## Overview
ClusterEditor lets you edit scene data clusters in Cascadeur. It provides operations to create clusters, add or remove data items, rename clusters, and manage bindings between clusters. Type names such as ClusterId and csc.model.DataId appear in the signatures; detailed semantics are undocumented in the provided source.

## Class Definition
```python
class csc.model.ClusterEditor
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a ClusterEditor instance (details undocumented).

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

## Methods

### `add_cluster(self, inserted_ids, name="") -> ClusterId`
Creates a new cluster using the provided data IDs and optional name (details undocumented).

**Parameters:**
- `inserted_ids`: csc.model.DataId[] – undocumented
- `name`: string – optional; default is an empty string

**Returns:**
- `ClusterId` – undocumented

### `add_data_to_cluster(self, cluster_index, inserted_ids)`
Adds data IDs to an existing cluster (details undocumented).

**Parameters:**
- `cluster_index`: ClusterId – undocumented
- `inserted_ids`: csc.model.DataId[] – undocumented

**Returns:**
- undocumented

### `bind_clusters(self, cluster_id_first, cluster_id_second)`
Binds two clusters together (details undocumented).

**Parameters:**
- `cluster_id_first`: ClusterId – undocumented
- `cluster_id_second`: ClusterId – undocumented

**Returns:**
- undocumented

### `remove_cluster(self, cluster_id)`
Removes a cluster (details undocumented).

**Parameters:**
- `cluster_id`: ClusterId – undocumented

**Returns:**
- undocumented

### `remove_data_from_cluster(self, data_id)`
Removes a data item from its cluster (details undocumented).

**Parameters:**
- `data_id`: csc.model.DataId – undocumented

**Returns:**
- undocumented

### `set_cluster_name(self, cluster_id, name)`
Sets the name of the specified cluster (details undocumented).

**Parameters:**
- `cluster_id`: ClusterId – undocumented
- `name`: string – undocumented

**Returns:**
- undocumented

### `unbind_cluster(self, cluster_id)`
Unbinds the specified cluster (details undocumented).

**Parameters:**
- `cluster_id`: ClusterId – undocumented

**Returns:**
- undocumented

### `unbind_clusters(self, cluster_id_first, cluster_id_second)`
Removes a binding between two clusters (details undocumented).

**Parameters:**
- `cluster_id_first`: ClusterId – undocumented
- `cluster_id_second`: ClusterId – undocumented

**Returns:**
- undocumented

## Usage Notes
- Only parameter and type names present in the source were retained; behavior and return values are undocumented here.
- Refer to the official API documentation for authoritative details on semantics and side effects.

