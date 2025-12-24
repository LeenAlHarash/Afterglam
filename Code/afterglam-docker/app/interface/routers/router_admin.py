from fastapi import APIRouter, HTTPException, Request, Form, Depends
from starlette import status
from starlette.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
import requests
from app.utils.auth import admin_required
from app.db import afterglam
from app.interface.model_view.model_view_token import TokenView
from app.interface.model_view.view_admin import AdminView
from app.services.services_admin import (list_admins, get_admin_by_id, create_admin_db, update_admin_db, delete_admin_db)
from app.services.services_auth import authenticate_and_issue_token, refresh_token_flow

router = APIRouter(prefix="/admins", tags=["admins"])

@router.post("/login", summary="Login an admin")
def login_admin(form_data: OAuth2PasswordRequestForm = Depends()) -> TokenView:
    return authenticate_and_issue_token(email=form_data.username, password=form_data.password)

@router.post("/refresh")
def refresh(refresh_token: str = Form(...)) -> TokenView:
    return refresh_token_flow(refresh_token)


@router.get("/", response_model=list[AdminView])
def get_admins(admin=Depends(admin_required)):
    return list_admins()

@router.get("/{admin_id}", response_model=AdminView)
def get_admin_route(admin_id: int, admin=Depends(admin_required)):
    admin = get_admin_by_id(admin_id)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="L'administrateur n'existe pas.")

    return admin


@router.post("/", response_model=AdminView, status_code=status.HTTP_201_CREATED)
def create_admin(admin: AdminView):
    try:
        return create_admin_db(admin)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="L'administrateur n'a pas été crée avec succès")


@router.put("/{admin_id}", response_model=AdminView)
def replace_admin(admin_id: int, nouveau_admin: AdminView):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La modification d'un administrateur via l'API est interdite."
    )


@router.delete("/{admin_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_admin_by_id(admin_id: int):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La suppression d'un administrateur via l'API est interdite."
    )