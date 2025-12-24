from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.responses import JSONResponse
from app.utils.auth import admin_required
from app.db import afterglam
from app.interface.model_view.view_form import FormView
from app.services.services_form import (list_forms, get_form_by_id, get_form_by_client_id, get_client_name_by_form_id,
get_form_by_admin_id, get_admin_name_by_form_id, get_form_by_maison_id, get_maison_name_by_form_id, create_form_db, update_form_db, delete_form_db,
get_form_by_client_email)

router = APIRouter(prefix="/forms", tags=["forms"])

@router.get("/", response_model=list[FormView])
def get_forms(admin=Depends(admin_required)):
    return list_forms()

@router.get("/{form_id}", response_model=FormView)
def get_form(form_id: int, admin=Depends(admin_required)):
    form = get_form_by_id(form_id)
    if not form:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le formulaire n'existe pas.")
    return form

# Tests pour les jointures
@router.get("/clientForm/{client_id}", response_model=list[FormView])
def get_form_client_id(client_id: int, admin=Depends(admin_required)):
    form = get_form_by_client_id(client_id)
    if not form:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le formulaire n'existe pas.")
    return form

@router.get("/clientFormEmail/{client_email}", response_model=list[FormView])
def get_form_client_email(client_email: str):
    form = get_form_by_client_email(client_email)
    if not form:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le formulaire n'existe pas.")
    return form

@router.get("/adminForm/{admin_id}", response_model=list[FormView])
def get_form_admin_id(admin_id: int, admin=Depends(admin_required)):
    form = get_form_by_admin_id(admin_id)
    if not form:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le formulaire n'existe pas.")
    return form

@router.get("/maisonForm/{maison_id}", response_model=list[FormView])
def get_form_maison_id(maison_id: int, admin=Depends(admin_required)):
    form = get_form_by_maison_id(maison_id)
    if not form:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le formulaire n'existe pas.")
    return form

@router.get("/maisonFormNom/{maison_id}", response_model=list[FormView])
def get_form_maison_show_name(maison_id: int):
    form = get_maison_name_by_form_id(maison_id)
    if not form:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le formulaire n'existe pas.")
    return form

@router.post("/", response_model=FormView, status_code=status.HTTP_201_CREATED)
def create_form(form: FormView):
    try:
        return create_form_db(form)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Le formulaire n'a pas été crée avec succès")

@router.put("/{form_id}", response_model=FormView)
def replace_form(form_id: int, nouveau_form: FormView):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La modification d'un formulaire via l'API est interdite."
    )

@router.delete("/{form_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_form_by_id(form_id: int):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La suppression des formulaires via l'API est interdite."
    )