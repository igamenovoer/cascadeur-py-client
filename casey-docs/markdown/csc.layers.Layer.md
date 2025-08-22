---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.Layer.html
html_file: 1538044fb3a1570e77d83177f97c2680.html
module: csc.layers.Layer
---

# csc.layers.Layer[??](#csc-layers-layer "Permalink to this heading")

*class* csc.layers.Layer[??](#csc.layers.Layer "Permalink to this definition")
:   Layer class

    The Layer is the basic element that implements intervals and sections to set
    interpolation properties of scene objects

    Variables:
    :   * **header** ??? Get Header
        * **is\_locked** ??? Get bool
        * **is\_visible** ??? Get bool
        * **obj\_ids** ??? Get csc.Guid{}
        * **sections** ??? Get std::map<Pos, Section>

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.Layer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.Layer.__init__ "csc.layers.Layer.__init__")(\*args,??\*\*kwargs) |  |
    | [`actual_key`](../csc.html#csc.layers.Layer.actual_key "csc.layers.Layer.actual_key")(self,??pos) | -> Key |
    | [`actual_key_pos`](../csc.html#csc.layers.Layer.actual_key_pos "csc.layers.Layer.actual_key_pos")(self,??pos) | -> int |
    | [`actual_section`](../csc.html#csc.layers.Layer.actual_section "csc.layers.Layer.actual_section")(self,??pos) | -> Section |
    | [`actual_section_pos`](../csc.html#csc.layers.Layer.actual_section_pos "csc.layers.Layer.actual_section_pos")(self,??pos) | -> int |
    | [`find_section`](../csc.html#csc.layers.Layer.find_section "csc.layers.Layer.find_section")(self,??pos) | pos : int | -> Section |
    | [`interval`](../csc.html#csc.layers.Layer.interval "csc.layers.Layer.interval")(self,??pos) | -> Interval |
    | [`is_key`](../csc.html#csc.layers.Layer.is_key "csc.layers.Layer.is_key")(self,??pos) |  |
    | [`is_key_or_fixed`](../csc.html#csc.layers.Layer.is_key_or_fixed "csc.layers.Layer.is_key_or_fixed")(self,??pos) |  |
    | [`key`](../csc.html#csc.layers.Layer.key "csc.layers.Layer.key")(self,??pos) | -> Key |
    | [`key_frame_indices`](../csc.html#csc.layers.Layer.key_frame_indices "csc.layers.Layer.key_frame_indices")(self) | -> FramesIndices |
    | [`last_key_pos`](../csc.html#csc.layers.Layer.last_key_pos "csc.layers.Layer.last_key_pos")(self) | -> int |
    | [`section`](../csc.html#csc.layers.Layer.section "csc.layers.Layer.section")(self,??pos) | -> Section |

    
**Attributes:**

    |  |  |
    | --- | --- |
    | [`header`](../csc.html#csc.layers.Layer.header "csc.layers.Layer.header") |  |
    | [`is_locked`](../csc.html#csc.layers.Layer.is_locked "csc.layers.Layer.is_locked") |  |
    | [`is_visible`](../csc.html#csc.layers.Layer.is_visible "csc.layers.Layer.is_visible") |  |
    | [`obj_ids`](../csc.html#csc.layers.Layer.obj_ids "csc.layers.Layer.obj_ids") | -> csc.model.ObjectId{} |
    | [`sections`](../csc.html#csc.layers.Layer.sections "csc.layers.Layer.sections") | -> std::map<Pos, Section> |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.Layer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.Layer.__module__ "Permalink to this definition")

    actual\_key(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Key[??](#csc.layers.Layer.actual_key "Permalink to this definition")
    :   -> Key

    actual\_key\_pos(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Layer.actual_key_pos "Permalink to this definition")
    :   -> int

    actual\_section(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Section[??](#csc.layers.Layer.actual_section "Permalink to this definition")
    :   -> Section

    actual\_section\_pos(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Layer.actual_section_pos "Permalink to this definition")
    :   -> int

    find\_section(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.Layer.find_section "Permalink to this definition")
    :   pos : int | -> Section

    *property* header[??](#csc.layers.Layer.header "Permalink to this definition")

    interval(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Interval[??](#csc.layers.Layer.interval "Permalink to this definition")
    :   -> Interval

    is\_key(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Layer.is_key "Permalink to this definition")

    is\_key\_or\_fixed(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.Layer.is_key_or_fixed "Permalink to this definition")

    *property* is\_locked[??](#csc.layers.Layer.is_locked "Permalink to this definition")

    *property* is\_visible[??](#csc.layers.Layer.is_visible "Permalink to this definition")

    key(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Key[??](#csc.layers.Layer.key "Permalink to this definition")
    :   -> Key

    key\_frame\_indices(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*)  domain::scene::layers::index::FramesIndices[??](#csc.layers.Layer.key_frame_indices "Permalink to this definition")
    :   -> FramesIndices

    last\_key\_pos(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.Layer.last_key_pos "Permalink to this definition")
    :   -> int

    *property* obj\_ids[??](#csc.layers.Layer.obj_ids "Permalink to this definition")
    :   -> csc.model.ObjectId{}

    section(*self: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*, *pos: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  domain::scene::layers::layer::Section[??](#csc.layers.Layer.section "Permalink to this definition")
    :   -> Section

    *property* sections[??](#csc.layers.Layer.sections "Permalink to this definition")
    :   -> std::map<Pos, Section>