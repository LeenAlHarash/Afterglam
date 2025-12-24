from typing import List, Optional

from app.db import afterglam
from app.data.data_cosmetique import get_all_cosmetiques, get_a_cosmetique, get_cosmetique_by_nom, create_cosmetique_in_db, update_cosmetique_in_db, delete_cosmetique_in_db
from app.interface.model_view.view_cosmetique import CosmetiqueView
from app.data.model.model_cosmetique import Cosmetique

def convert_cosmetiques_to_view(cosmetique: dict) -> CosmetiqueView:
    if isinstance(cosmetique, dict):
        return CosmetiqueView(
            id=cosmetique["id"],
            nom=cosmetique["nom"]
        )
    else:
        return CosmetiqueView(
            id=cosmetique.id,
            nom=cosmetique.nom
        )

def list_cosmetiques() -> List[CosmetiqueView]:
    cosmetiques = get_all_cosmetiques()
    return [convert_cosmetiques_to_view(c) for c in cosmetiques]

def get_cosmetique_by_id(cosmetique_id: int) -> Optional[CosmetiqueView]:
    cosmetique = get_a_cosmetique(cosmetique_id)
    if cosmetique:
        return convert_cosmetiques_to_view(cosmetique)
    return None

def get_cosmetique_by_name(nom: str) -> Optional[CosmetiqueView]:
    cosmetique = get_cosmetique_by_nom(nom)
    if cosmetique:
        return convert_cosmetiques_to_view(cosmetique)
    return None

def create_cosmetique_db(cosmetique: Cosmetique) -> CosmetiqueView:
    cosmetique = create_cosmetique_in_db(cosmetique)
    if cosmetique:
        return convert_cosmetiques_to_view(cosmetique)
    return None


def update_cosmetique_db(cosmetique_id: int, cosmetique: CosmetiqueView) -> Optional[CosmetiqueView]:
    cosmetique = update_cosmetique_in_db(cosmetique_id, cosmetique)
    if cosmetique:
        return convert_cosmetiques_to_view(cosmetique)
    return None

def delete_cosmetique_db(cosmetique_id: int) -> bool:
    cosmetique = delete_cosmetique_in_db(cosmetique_id)
    if cosmetique:
        return True
    return False