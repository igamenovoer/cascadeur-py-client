[CLEAN]

# csc.model.ClusterViewer

## Overview
ClusterViewer provides read access to scene data clusters. It lets you enumerate clusters, resolve a cluster from a data identifier, list data items within a cluster, and query cluster names and bindings. Type details for ClusterId and DataId come from Cascadeur’s API and are not expanded here.

## Class Definition
```python
class csc.model.ClusterViewer
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor; parameters are undocumented.

**Parameters:**
- *args: undocumented – undocumented
- **kwargs: undocumented – undocumented

## Methods

### `cluster_by_data(self, data_id: csc.model.DataId) -> ClusterId`
Returns the cluster identifier associated with a given data identifier.

**Parameters:**
- data_id: csc.model.DataId – undocumented

**Returns:**
- ClusterId – undocumented

### `cluster_datas(self, cluster_id: ClusterId) -> csc.model.DataId[]`
Lists data identifiers that belong to a specified cluster.

**Parameters:**
- cluster_id: ClusterId – undocumented

**Returns:**
- csc.model.DataId[] – undocumented

### `cluster_name(self, cluster_id: ClusterId) -> string`
Gets the name of a cluster.

**Parameters:**
- cluster_id: ClusterId – undocumented

**Returns:**
- string – undocumented

### `clusters(self) -> ClusterId[]`
Returns all cluster identifiers in the scene.

**Returns:**
- ClusterId[] – undocumented

### `clusters_bindings(self) -> (ClusterId, ClusterId)[]`
Returns a list of cluster bindings as pairs.

**Returns:**
- (ClusterId, ClusterId)[] – undocumented

**Notes:**
- The semantics of the binding pairs are undocumented.

## Usage Notes
- The exact structure and behavior of ClusterId and DataId are defined by Cascadeur’s API and are not detailed here.
- Method return values and parameter semantics are minimally documented in this excerpt.

