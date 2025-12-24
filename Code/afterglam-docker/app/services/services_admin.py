from typing import List, Optional
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import bcrypt
from app.db import afterglam
from app.data.data_admin import get_all_admins, get_an_admin, create_admin_in_db, update_admin_in_db, delete_admin_in_db, get_admin_by_email
from app.interface.model_view.view_admin import AdminView
from app.data.model.model_admin import Admin
from app.utils.auth import hasher_mdp, valider_courriel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admins/login")

def convert_admins_to_view(admin: dict) -> AdminView:
    if isinstance(admin, dict):
        return AdminView(
            id=admin["id"],
            nom=admin["nom"],
            prenom=admin["prenom"],
            telephone=admin["telephone"],
            courriel=admin["courriel"]
        )
    else:
        return AdminView(
            id=admin.id,
            nom=admin.nom,
            prenom=admin.prenom,
            telephone=admin.telephone,
            courriel=admin.courriel,
            mdp=admin.mdp
        )

def list_admins() -> List[AdminView]:
    admins = get_all_admins()
    return [convert_admins_to_view(a) for a in admins]


def get_admin_by_id(admin_id: int) -> Optional[AdminView]:
    admin = get_an_admin(admin_id)
    if admin:
        return convert_admins_to_view(admin)
    return None


def create_admin_db(admin: AdminView) -> AdminView:
    admin = create_admin_in_db(admin)
    if admin:
        return convert_admins_to_view(admin)
    return None


def update_admin_db(admin_id: int, admin: AdminView) -> Optional[AdminView]:
    admin = update_admin_in_db(admin_id, admin)
    if admin:
        return convert_admins_to_view(admin)
    return None


def delete_admin_db(admin_id: int) -> bool:
    admin = delete_admin_in_db(admin_id)
    if admin:
        return True
    return False