from fastapi import APIRouter, HTTPException, Request, Depends
from starlette import status
from starlette.responses import JSONResponse
from app.db import afterglam
from app.interface.model_view.view_client import ClientView
from app.services.services_client import (list_clients, get_client_by_id, create_client_db, update_client_db, delete_client_db)
from app.utils.auth import admin_required

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/", response_model=list[ClientView])
def get_clients(admin=Depends(admin_required)):
    return list_clients()

@router.get("/{client_id}", response_model=ClientView)
def get_client(client_id: int, admin=Depends(admin_required)):
    client = get_client_by_id(client_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le client n'existe pas.")
    return client

@router.post("/", response_model=ClientView, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientView):
    try:
        return create_client_db(client)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Le client n'a pas été crée avec succès")

@router.put("/{client_id}", response_model=ClientView)
def replace_client(client_id: int, nouveau_client: ClientView):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La modification d'un client via l'API est interdite."
    )

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_client_by_id(client_id: int):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La suppression d'un client via l'API est interdite."
    )