---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.CyclesViewer.html
html_file: ac2111ef062a838f0914ac0eb7897ef7.html
module: csc.layers.CyclesViewer
---

# csc.layers.CyclesViewer[??](#csc-layers-cyclesviewer "Permalink to this heading")

*class* csc.layers.CyclesViewer[??](#csc.layers.CyclesViewer "Permalink to this definition")
:   Cycle viewer class

    \_\_init\_\_(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *layer: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.layers.CyclesViewer.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.CyclesViewer.__init__ "csc.layers.CyclesViewer.__init__")(self,??layer) |  |
    | [`any_cycles_exist_in_frames`](../csc.html#csc.layers.CyclesViewer.any_cycles_exist_in_frames "csc.layers.CyclesViewer.any_cycles_exist_in_frames")(self,??arg0,??arg1) |  |
    | [`cycle_contains_frame_index`](../csc.html#csc.layers.CyclesViewer.cycle_contains_frame_index "csc.layers.CyclesViewer.cycle_contains_frame_index")(self,??arg0,??arg1) |  |
    | [`find_cycle`](../csc.html#csc.layers.CyclesViewer.find_cycle "csc.layers.CyclesViewer.find_cycle")(self,??arg0) |  |
    | [`get_active_pos`](../csc.html#csc.layers.CyclesViewer.get_active_pos "csc.layers.CyclesViewer.get_active_pos")(self,??arg0) |  |
    | [`get_active_section_pos`](../csc.html#csc.layers.CyclesViewer.get_active_section_pos "csc.layers.CyclesViewer.get_active_section_pos")(self,??arg0) |  |
    | [`get_cycles_in_frames`](../csc.html#csc.layers.CyclesViewer.get_cycles_in_frames "csc.layers.CyclesViewer.get_cycles_in_frames")(self,??arg0,??arg1) |  |
    | [`get_most_left_and_right_frame_indices_of_cycle`](../csc.html#csc.layers.CyclesViewer.get_most_left_and_right_frame_indices_of_cycle "csc.layers.CyclesViewer.get_most_left_and_right_frame_indices_of_cycle")(...) |  |
    | [`is_pos_in_active_cycle_zone`](../csc.html#csc.layers.CyclesViewer.is_pos_in_active_cycle_zone "csc.layers.CyclesViewer.is_pos_in_active_cycle_zone")(self,??arg0) |  |
    | [`is_pos_in_inactive_cycle_zone`](../csc.html#csc.layers.CyclesViewer.is_pos_in_inactive_cycle_zone "csc.layers.CyclesViewer.is_pos_in_inactive_cycle_zone")(self,??arg0) |  |
    | [`last_pos`](../csc.html#csc.layers.CyclesViewer.last_pos "csc.layers.CyclesViewer.last_pos")(self) |  |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.CyclesViewer.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *layer: [csc.layers.Layer](../csc.html#csc.layers.Layer "csc.layers.Layer")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.CyclesViewer.__module__ "Permalink to this definition")

    any\_cycles\_exist\_in\_frames(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.any_cycles_exist_in_frames "Permalink to this definition")

    cycle\_contains\_frame\_index(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [csc.layers.Cycle](../csc.html#csc.layers.Cycle "csc.layers.Cycle")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.cycle_contains_frame_index "Permalink to this definition")

    find\_cycle(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.layers.CyclesViewer.find_cycle "Permalink to this definition")

    get\_active\_pos(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.CyclesViewer.get_active_pos "Permalink to this definition")

    get\_active\_section\_pos(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.CyclesViewer.get_active_section_pos "Permalink to this definition")

    get\_cycles\_in\_frames(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *arg1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[csc.layers.Cycle](../csc.html#csc.layers.Cycle "csc.layers.Cycle")][??](#csc.layers.CyclesViewer.get_cycles_in_frames "Permalink to this definition")

    get\_most\_left\_and\_right\_frame\_indices\_of\_cycle(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [csc.layers.Cycle](../csc.html#csc.layers.Cycle "csc.layers.Cycle")*)  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")][??](#csc.layers.CyclesViewer.get_most_left_and_right_frame_indices_of_cycle "Permalink to this definition")

    is\_pos\_in\_active\_cycle\_zone(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.is_pos_in_active_cycle_zone "Permalink to this definition")

    is\_pos\_in\_inactive\_cycle\_zone(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*, *arg0: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.CyclesViewer.is_pos_in_inactive_cycle_zone "Permalink to this definition")

    last\_pos(*self: [csc.layers.CyclesViewer](../csc.html#csc.layers.CyclesViewer "csc.layers.CyclesViewer")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.layers.CyclesViewer.last_pos "Permalink to this definition")