from typing import List, Optional

from app.db import afterglam
from app.data.data_maisonFuneraire import get_all_maisons, get_a_maisonFuneraire, get_a_maisonFuneraire_by_name, create_maison_in_db, update_maison_in_db, delete_maison_in_db
from app.interface.model_view.view_maisonFuneraire import MaisonView
from app.data.model.model_maisonFuneraire import MaisonFuneraille
from app.utils.auth import valider_telephone

def convert_maisonFuneraires_to_view(maisonFuneraire: dict) -> MaisonView:
    if isinstance(maisonFuneraire, dict):
        return MaisonView(
            id=maisonFuneraire["id"],
            nom=maisonFuneraire["nom"],
            telephone=maisonFuneraire["telephone"],
            adresse=maisonFuneraire["adresse"],
            code_postal=maisonFuneraire["code_postal"]
        )
    else:
        return MaisonView(
            id=maisonFuneraire.id,
            nom=maisonFuneraire.nom,
            telephone=maisonFuneraire.telephone,
            adresse=maisonFuneraire.adresse,
            code_postal=maisonFuneraire.code_postal
        )

def list_maisonFuneraires() -> List[MaisonView]:
    maisonFuneraires = get_all_maisons()
    return [convert_maisonFuneraires_to_view(m) for m in maisonFuneraires]


def get_maison_by_id(maison_id: int) -> Optional[MaisonView]:
    maison = get_a_maisonFuneraire(maison_id)
    if maison:
        return convert_maisonFuneraires_to_view(maison)
    return None

def get_maison_by_name(maison_name: str) -> Optional[MaisonView]:
    maison = get_a_maisonFuneraire_by_name(maison_name)
    if maison:
        return convert_maisonFuneraires_to_view(maison)
    return None

def create_maison_db(maison: MaisonView) -> MaisonView:
    maison = create_maison_in_db(maison)
    if maison:
        return convert_maisonFuneraires_to_view(maison)
    return None

def update_maison_db(maison_id: int, maison: MaisonView) -> Optional[MaisonView]:
    maison = update_maison_in_db(maison_id, maison)
    if maison:
        return convert_maisonFuneraires_to_view(maison)
    return None

def delete_maison_db(maison_id: int) -> bool:
    maison = delete_maison_in_db(maison_id)
    if maison:
        return True
    return False