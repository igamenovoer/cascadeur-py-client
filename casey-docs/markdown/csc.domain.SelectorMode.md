---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.SelectorMode.html
html_file: 0a4e884a24844882764f526ac0da1a61.html
module: csc.domain.SelectorMode
---

# csc.domain.SelectorMode[??](#csc-domain-selectormode "Permalink to this heading")

*class* csc.domain.SelectorMode[??](#csc.domain.SelectorMode "Permalink to this definition")
:   > SelectorMode enumerable
    >
    > SingleSelection, // Resets if new objects were selected, and nothing changes if already selected ones were selected
    >
    > MultiSelection, // Multiple selections. If not all objects were selected, adds, otherwise subtracts
    >
    > NewSelection, // Resets everything and highlights the selection
    >
    > AdditionSelection, // Adds all selections to selections
    >
    > SubtractionSelection // Subtracts highlighted entities from selections

    Members:

    > SingleSelection
    >
    > MultiSelection
    >
    > NewSelection
    >
    > AdditionSelection
    >
    > SubtractionSelection

    \_\_init\_\_(*self: [csc.domain.SelectorMode](../csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectorMode.__init__ "Permalink to this definition")

    
**Methods:**

    |  |  |
    | --- | --- |
    | [`__init__`](../csc.html#csc.domain.SelectorMode.__init__ "csc.domain.SelectorMode.__init__")(self,??value) |  |

    
**Attributes:**

    |  |  |
    | --- | --- |
    | [`AdditionSelection`](../csc.html#csc.domain.SelectorMode.AdditionSelection "csc.domain.SelectorMode.AdditionSelection") |  |
    | [`MultiSelection`](../csc.html#csc.domain.SelectorMode.MultiSelection "csc.domain.SelectorMode.MultiSelection") |  |
    | [`NewSelection`](../csc.html#csc.domain.SelectorMode.NewSelection "csc.domain.SelectorMode.NewSelection") |  |
    | [`SingleSelection`](../csc.html#csc.domain.SelectorMode.SingleSelection "csc.domain.SelectorMode.SingleSelection") |  |
    | [`SubtractionSelection`](../csc.html#csc.domain.SelectorMode.SubtractionSelection "csc.domain.SelectorMode.SubtractionSelection") |  |
    | [`name`](../csc.html#csc.domain.SelectorMode.name "csc.domain.SelectorMode.name") |  |
    | [`value`](../csc.html#csc.domain.SelectorMode.value "csc.domain.SelectorMode.value") |  |

    AdditionSelection *= <SelectorMode.AdditionSelection: 3>*[??](#csc.domain.SelectorMode.AdditionSelection "Permalink to this definition")

    MultiSelection *= <SelectorMode.MultiSelection: 1>*[??](#csc.domain.SelectorMode.MultiSelection "Permalink to this definition")

    NewSelection *= <SelectorMode.NewSelection: 2>*[??](#csc.domain.SelectorMode.NewSelection "Permalink to this definition")

    SingleSelection *= <SelectorMode.SingleSelection: 0>*[??](#csc.domain.SelectorMode.SingleSelection "Permalink to this definition")

    SubtractionSelection *= <SelectorMode.SubtractionSelection: 4>*[??](#csc.domain.SelectorMode.SubtractionSelection "Permalink to this definition")

    \_\_annotations\_\_ *= {}*[??](#csc.domain.SelectorMode.__annotations__ "Permalink to this definition")

    \_\_eq\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.SelectorMode.__eq__ "Permalink to this definition")

    \_\_getstate\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__getstate__ "Permalink to this definition")

    \_\_hash\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__hash__ "Permalink to this definition")

    \_\_index\_\_(*self: [csc.domain.SelectorMode](../csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__index__ "Permalink to this definition")

    \_\_init\_\_(*self: [csc.domain.SelectorMode](../csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#id0 "Permalink to this definition")

    \_\_int\_\_(*self: [csc.domain.SelectorMode](../csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")*)  [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[??](#csc.domain.SelectorMode.__int__ "Permalink to this definition")

    \_\_members\_\_ *= {'AdditionSelection': <SelectorMode.AdditionSelection: 3>, 'MultiSelection': <SelectorMode.MultiSelection: 1>, 'NewSelection': <SelectorMode.NewSelection: 2>, 'SingleSelection': <SelectorMode.SingleSelection: 0>, 'SubtractionSelection': <SelectorMode.SubtractionSelection: 4>}*[??](#csc.domain.SelectorMode.__members__ "Permalink to this definition")

    \_\_module\_\_ *= 'csc.domain'*[??](#csc.domain.SelectorMode.__module__ "Permalink to this definition")

    \_\_ne\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*, *other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[??](#csc.domain.SelectorMode.__ne__ "Permalink to this definition")

    \_\_repr\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.SelectorMode.__repr__ "Permalink to this definition")

    \_\_setstate\_\_(*self: [csc.domain.SelectorMode](../csc.html#csc.domain.SelectorMode "csc.domain.SelectorMode")*, *state: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)  [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[??](#csc.domain.SelectorMode.__setstate__ "Permalink to this definition")

    \_\_str\_\_(*self: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")*)  [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[??](#csc.domain.SelectorMode.__str__ "Permalink to this definition")

    *property* name[??](#csc.domain.SelectorMode.name "Permalink to this definition")

    *property* value[??](#csc.domain.SelectorMode.value "Permalink to this definition")