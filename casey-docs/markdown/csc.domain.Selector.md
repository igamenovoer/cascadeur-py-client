---
source_url: https://cascadeur.com/python-api/_generate/csc.domain.Selector.html
html_file: b70bbb639b79b50f4d0524a69fb6d1eb.html
module: csc.domain.Selector
---

# csc.domain.Selector 

Selector class Contains basic methods and properties to operate current selected scene objects
- ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){}
- select – overridden method by Select || Entity3d_id{}, Entity3d_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter)

ids – Get (csc.model.ObjectId or csc.scene.Tool_object_id){} select – overridden method by Select || Entity3d_id{}, Entity3d_id, SelectorFilter (SelectorFilter.Free), SelectorMode (SelectorMode.NewSelection), string{} (typeFilter) Methods __init__ (*args, **kwargs) pivot (self) -> Pivot select (*args, **kwargs) Overloaded function. selected (self) -> Selection -> Pivot Overloaded function.
1. select(self: csc.domain.Selector, select: csc.domain.Select) -> None
2. select(self: csc.domain.Selector, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type_filter: set[str] = set(), auto_pivot: bool = False) -> None

select(self: csc.domain.Selector, select: csc.domain.Select) -> None select(self: csc.domain.Selector, ids: set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id] = <csc.model.ObjectId object at 0x7f3d1b9650b0>, filter: csc.domain.SelectorFilter = <SelectorFilter.Free: 0>, mode: csc.domain.SelectorMode = <SelectorMode.NewSelection: 2>, type_filter: set[str] = set(), auto_pivot: bool = False) -> None -> Selection