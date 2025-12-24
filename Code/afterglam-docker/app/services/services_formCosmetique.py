from typing import List, Optional

from app.data.data_formCosmetique import insert_form_cosmetique, get_form_cosmetiques
from app.data.data_cosmetique import get_cosmetique_by_nom
from app.data.model.model_formCosmetique import FormCosmetique
from app.interface.model_view.view_formCosmetique import FormCosmetiqueView

def convert_formcosmetique_to_view(fc: dict) -> FormCosmetiqueView:
    if isinstance(fc, dict):
        return FormCosmetiqueView(
            id=fc["id"],
            form_id=fc["form_id"],
            cosmetique_id=fc["cosmetique_id"]
        )
    else:
        return FormCosmetiqueView(
            id=fc.id,
            form_id=fc.form_id,
            cosmetique_id=fc.cosmetique_id
        )

def add_formcosmetiques_by_name(form_id: int, cosmetique_noms: List[str]) -> List[FormCosmetiqueView]:
    views: List[FormCosmetiqueView] = []
    for nom in cosmetique_noms:
        cosmetique = get_cosmetique_by_nom(nom)
        if not cosmetique:
            raise ValueError(f"Cosmétique '{nom}' introuvable")
        fc_id = insert_form_cosmetique(form_id, cosmetique["id"])
        views.append(FormCosmetiqueView(id=fc_id, form_id=form_id, cosmetique_id=cosmetique["id"]))
    return views

def get_formcosmetiques_by_form(form_id: int) -> Optional[List[FormCosmetiqueView]]:
    fcs = get_form_cosmetiques(form_id)
    if fcs:
        return [convert_formcosmetique_to_view(fc) for fc in fcs]
    return None