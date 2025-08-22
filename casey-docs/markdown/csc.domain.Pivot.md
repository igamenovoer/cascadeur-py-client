---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.Pivot.html
html_file: 5ab5d82b64a60c64dbbd12f879d67e5b.html
module: csc.domain.Pivot
---

# csc.domain.Pivot 

Pivot class Represents basic Pivot methods.
- position – overridden method by … || int (frame) || int, StatePivot (pivot)
- rotation – overridden method by … || int (frame) || int, StatePivot (pivot)

position – overridden method by … || int (frame) || int, StatePivot (pivot) rotation – overridden method by … || int (frame) || int, StatePivot (pivot) Methods __init__ (*args, **kwargs) center_of_top_objects (self, arg0) position (*args, **kwargs) Overloaded function. rotation (*args, **kwargs) Overloaded function. select (self, entity_id) Overloaded function.
1. position(self: csc.domain.Pivot) -> numpy.ndarray[numpy.float32[3, 1]]
2. position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray[numpy.float32[3, 1]]
3. position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]]

position(self: csc.domain.Pivot) -> numpy.ndarray[numpy.float32[3, 1]] position(self: csc.domain.Pivot, frame: int) -> numpy.ndarray[numpy.float32[3, 1]] position(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> numpy.ndarray[numpy.float32[3, 1]] Overloaded function.
1. rotation(self: csc.domain.Pivot) -> csc.math.Quaternion
2. rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion
3. rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion

rotation(self: csc.domain.Pivot) -> csc.math.Quaternion rotation(self: csc.domain.Pivot, frame: int) -> csc.math.Quaternion rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) -> csc.math.Quaternion