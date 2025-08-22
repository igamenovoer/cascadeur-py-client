---
source_url: https://cascadeur.com/python-api/_generate/csc.layers.ItemVariant.html
html_file: ca420901b068b081ff6d24366f47c1d6.html
module: csc.layers.ItemVariant
---

# csc.layers.ItemVariant[??](#csc-layers-itemvariant "Permalink to this heading")

*class* csc.layers.ItemVariant[??](#csc.layers.ItemVariant "Permalink to this definition")
:   ItemVariant class

    Can implement a folder or layer for a header

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.layers.ItemVariant.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.layers.ItemVariant.__init__ "csc.layers.ItemVariant.__init__")(\*args,??\*\*kwargs) |  |
    | [`folder`](../csc.html#csc.layers.ItemVariant.folder "csc.layers.ItemVariant.folder")(self) | -> Folder (if it has folder otherwise none) |
    | [`header`](../csc.html#csc.layers.ItemVariant.header "csc.layers.ItemVariant.header")(self) | -> Header |
    | [`is_folder`](../csc.html#csc.layers.ItemVariant.is_folder "csc.layers.ItemVariant.is_folder")(self) |  |
    | [`is_layer`](../csc.html#csc.layers.ItemVariant.is_layer "csc.layers.ItemVariant.is_layer")(self) |  |
    | [`layer`](../csc.html#csc.layers.ItemVariant.layer "csc.layers.ItemVariant.layer")(self) | -> Layer (if it has layer otherwise none) |

    \_\_annotations\_\_ *= {}*[??](#csc.layers.ItemVariant.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.layers'*[??](#csc.layers.ItemVariant.__module__ "Permalink to this definition")

    folder(*self: [csc.layers.ItemVariant](../csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  domain::scene::layers::Folder[??](#csc.layers.ItemVariant.folder "Permalink to this definition")
    :   -> Folder (if it has folder otherwise none)

    header(*self: [csc.layers.ItemVariant](../csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  [csc.layers.Header](../csc.html#csc.layers.Header "csc.layers.Header")[??](#csc.layers.ItemVariant.header "Permalink to this definition")
    :   -> Header

    is\_folder(*self: [csc.layers.ItemVariant](../csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.ItemVariant.is_folder "Permalink to this definition")

    is\_layer(*self: [csc.layers.ItemVariant](../csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.layers.ItemVariant.is_layer "Permalink to this definition")

    layer(*self: [csc.layers.ItemVariant](../csc.html#csc.layers.ItemVariant "csc.layers.ItemVariant")*)  domain::scene::layers::Layer[??](#csc.layers.ItemVariant.layer "Permalink to this definition")
    :   -> Layer (if it has layer otherwise none)