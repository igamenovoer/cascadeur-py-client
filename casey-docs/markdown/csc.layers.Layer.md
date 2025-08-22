---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Layer.html
html_file: 1538044fb3a1570e77d83177f97c2680.html
module: csc.layers.Layer
---

# csc.layers.Layer 

Layer class The Layer is the basic element that implements intervals and sections to set
interpolation properties of scene objects
- header – Get Header
- is_locked – Get bool
- is_visible – Get bool
- obj_ids – Get csc.Guid{}
- sections – Get std::map<Pos, Section>

header – Get Header is_locked – Get bool is_visible – Get bool obj_ids – Get csc.Guid{} sections – Get std::map<Pos, Section> Methods __init__ (*args, **kwargs) actual_key (self, pos) -> Key actual_key_pos (self, pos) -> int actual_section (self, pos) -> Section actual_section_pos (self, pos) -> int find_section (self, pos) pos : int | -> Section interval (self, pos) -> Interval is_key (self, pos) is_key_or_fixed (self, pos) key (self, pos) -> Key key_frame_indices (self) -> FramesIndices last_key_pos (self) -> int section (self, pos) -> Section Attributes header is_locked is_visible obj_ids -> csc.model.ObjectId{} sections -> std::map<Pos, Section> -> Key -> int -> Section -> int pos : int | -> Section -> Interval -> Key -> FramesIndices -> int -> csc.model.ObjectId{} -> Section -> std::map<Pos, Section>