---
source_url: https://cascadeur.com/python-api/_generate/csc.update.ActivityAttribute.html
html_file: 87d315a7a178289e648498f7bd4e7852.html
module: csc.update.ActivityAttribute
---

# csc.update.ActivityAttribute[??](#csc-update-activityattribute "Permalink to this heading")

*class* csc.update.ActivityAttribute[??](#csc.update.ActivityAttribute "Permalink to this definition")
:   ActivityAttribute represents the activity of the data function.
    It should be bool.
    If true - function is active, if false - inactive. If not set - always active.
    It is an input-only attribute.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.update.ActivityAttribute.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.update.ActivityAttribute.__init__ "csc.update.ActivityAttribute.__init__")(\*args,??\*\*kwargs) |  |
    | `connect`(self,??attribute) | attribute: NodeAttribute |
    | `connected_attributes`(self) | -> NodeAttribute[] |
    | `connected_leaves`(self[,??get\_only\_first]) | -> NodeAttribute[] |
    | `connected_leaves_in_undirected_graph`(self) |  |
    | `direction`(self) | -> csc.DirectionValue |
    | `disconnect`(\*args,??\*\*kwargs) | Overloaded function. |
    | `id`(self) | -> AttributeId |
    | `is_active`(self) |  |
    | `name`(self) |  |
    | `node`(self) | -> Node |

    \_\_annotations\_\_ *= {}*[??](#csc.update.ActivityAttribute.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.update'*[??](#csc.update.ActivityAttribute.__module__ "Permalink to this definition")