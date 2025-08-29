# Untitled

Source: https://cascadeur.com/python-api/_generate/csc.layers.Layer.html

# csc.layers.Layer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html\#csc-layers-layer "Permalink to this heading")

_class_ csc.layers.Layer [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer "Permalink to this definition")

Layer class

The Layer is the basic element that implements intervals and sections to set
interpolation properties of scene objects

Variables:

- **header** – Get Header

- **is\_locked** – Get bool

- **is\_visible** – Get bool

- **obj\_ids** – Get csc.Guid{}

- **sections** – Get std::map<Pos, Section>


\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.__init__ "Permalink to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.__init__ "csc.layers.Layer.__init__")(\*args, \*\*kwargs) |  |
| [`actual_key`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_key "csc.layers.Layer.actual_key")(self, pos) | -\> Key |
| [`actual_key_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_key_pos "csc.layers.Layer.actual_key_pos")(self, pos) | -\> int |
| [`actual_section`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_section "csc.layers.Layer.actual_section")(self, pos) | -\> Section |
| [`actual_section_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.actual_section_pos "csc.layers.Layer.actual_section_pos")(self, pos) | -\> int |
| [`find_section`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.find_section "csc.layers.Layer.find_section")(self, pos) | pos : int \| -> Section |
| [`interval`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.interval "csc.layers.Layer.interval")(self, pos) | -\> Interval |
| [`is_key`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_key "csc.layers.Layer.is_key")(self, pos) |  |
| [`is_key_or_fixed`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_key_or_fixed "csc.layers.Layer.is_key_or_fixed")(self, pos) |  |
| [`key`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.key "csc.layers.Layer.key")(self, pos) | -\> Key |
| [`key_frame_indices`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.key_frame_indices "csc.layers.Layer.key_frame_indices")(self) | -\> FramesIndices |
| [`last_key_pos`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.last_key_pos "csc.layers.Layer.last_key_pos")(self) | -\> int |
| [`section`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.section "csc.layers.Layer.section")(self, pos) | -\> Section |

Attributes

|     |     |
| --- | --- |
| [`header`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.header "csc.layers.Layer.header") |  |
| [`is_locked`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_locked "csc.layers.Layer.is_locked") |  |
| [`is_visible`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.is_visible "csc.layers.Layer.is_visible") |  |
| [`obj_ids`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.obj_ids "csc.layers.Layer.obj_ids") | -\> csc.model.ObjectId{} |
| [`sections`](https://cascadeur.com/python-api/csc.html#csc.layers.Layer.sections "csc.layers.Layer.sections") | -\> std::map<Pos, Section> |

\_\_annotations\_\_ _={}_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.__annotations__ "Permalink to this definition")\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#id0 "Permalink to this definition")\_\_module\_\_ _='csc.layers'_ [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.__module__ "Permalink to this definition")actual\_key( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Key [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.actual_key "Permalink to this definition")

-\> Key

actual\_key\_pos( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.actual_key_pos "Permalink to this definition")

-\> int

actual\_section( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Section [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.actual_section "Permalink to this definition")

-\> Section

actual\_section\_pos( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.actual_section_pos "Permalink to this definition")

-\> int

find\_section( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.find_section "Permalink to this definition")

pos : int \| -> Section

_property_ header [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.header "Permalink to this definition")interval( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Interval [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.interval "Permalink to this definition")

-\> Interval

is\_key( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.is_key "Permalink to this definition")is\_key\_or\_fixed( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.is_key_or_fixed "Permalink to this definition")_property_ is\_locked [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.is_locked "Permalink to this definition")_property_ is\_visible [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.is_visible "Permalink to this definition")key( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Key [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.key "Permalink to this definition")

-\> Key

key\_frame\_indices( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_)→domain::scene::layers::index::FramesIndices [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.key_frame_indices "Permalink to this definition")

-\> FramesIndices

last\_key\_pos( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_)→[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.last_key_pos "Permalink to this definition")

-\> int

_property_ obj\_ids [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.obj_ids "Permalink to this definition")

-\> csc.model.ObjectId{}

section( _self:[csc.layers.Layer](https://cascadeur.com/python-api/csc.html#csc.layers.Layer "csc.layers.Layer")_, _pos:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")_)→domain::scene::layers::layer::Section [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.section "Permalink to this definition")

-\> Section

_property_ sections [¶](https://cascadeur.com/python-api/_generate/csc.layers.Layer.html#csc.layers.Layer.sections "Permalink to this definition")

-\> std::map<Pos, Section>