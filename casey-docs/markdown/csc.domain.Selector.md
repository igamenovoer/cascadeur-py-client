---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.Selector.html
html_file: b70bbb639b79b50f4d0524a69fb6d1eb.html
module: csc.domain.Selector
---

# csc.domain.Selector[??](#csc-domain-selector "Permalink to this heading")

*class* csc.domain.Selector[??](#csc.domain.Selector "Permalink to this definition")
:   Selector class

    Contains basic methods and properties to operate current selected scene objects

    Variables:
    :   * **ids** ??? Get (csc.model.ObjectId or csc.scene.Tool\_object\_id){}
        * **select** ??? overridden method by Select || Entity3d\_id{}, Entity3d\_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#csc.domain.Selector.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.domain.Selector.__init__ "csc.domain.Selector.__init__")(\*args,??\*\*kwargs) |  |
    | [`pivot`](../csc.html#csc.domain.Selector.pivot "csc.domain.Selector.pivot")(self) | -> Pivot |
    | [`select`](../csc.html#csc.domain.Selector.select "csc.domain.Selector.select")(\*args,??\*\*kwargs) | Overloaded function. |
    | [`selected`](../csc.html#csc.domain.Selector.selected "csc.domain.Selector.selected")(self) | -> Selection |

    \_\_annotations\_\_ *= {}*[??](#csc.domain.Selector.__annotations__ "Permalink to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[??](#id0 "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.Selector.__module__ "Permalink to this definition")

    pivot(*self: [csc.domain.Selector](../csc.html#csc.domain.Selector "csc.domain.Selector")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Selector.pivot "Permalink to this definition")
    :   -> Pivot

    select(*\*args*, *\*\*kwargs*)[??](#csc.domain.Selector.select "Permalink to this definition")
    :   Overloaded function.

        1. select(self: csc.domain.Selector, select: csc.domain.Select) -> None
        2. select(self: csc.domain.Selector, ids: set[Union[csc.model.ObjectId, csc.domain.Tool\_object\_id]], id: Union[csc.model.ObjectId, csc.domain.Tool\_object\_id] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type\_filter: set[str] = set(), auto\_pivot: bool = False) -> None

    selected(*self: [csc.domain.Selector](../csc.html#csc.domain.Selector "csc.domain.Selector")*)  [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")[??](#csc.domain.Selector.selected "Permalink to this definition")
    :   -> Selection