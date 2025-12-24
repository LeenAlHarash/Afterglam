from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.responses import JSONResponse
from app.utils.auth import admin_required
from app.db import afterglam
from app.interface.model_view.view_maisonFuneraire import MaisonView
from app.services.services_maisonFuneraire import (list_maisonFuneraires, get_maison_by_id, get_maison_by_name, create_maison_db, update_maison_db, delete_maison_db)

router = APIRouter(prefix="/maisons", tags=["maisons"])

@router.get("/", response_model=list[MaisonView])
def get_maisons():
    return list_maisonFuneraires()

@router.get("/id/{maison_id}", response_model=MaisonView)
def get_maison(maison_id: int, admin=Depends(admin_required)):
    maison = get_maison_by_id(maison_id)
    if not maison:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La maison funéraire n'existe pas.")
    return maison

@router.get("/name/{maison_name}", response_model=MaisonView)
def get_maison_by_nom(maison_name: str):
    maison = get_maison_by_name(maison_name)
    if not maison:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La maison funéraire n'existe pas.")
    return maison

@router.post("/", response_model=MaisonView, status_code=status.HTTP_201_CREATED)
def create_maison(maison: MaisonView):
    try:
        return create_maison_db(maison)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="La maison funéraire n'a pas été crée avec succès")

@router.put("/{maison_id}", response_model=MaisonView)
def replace_maison(maison_id: int, nouveau_maison: MaisonView):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La modification d'une maison funéraire via l'API est interdite."
    )

@router.delete("/{maison_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_maison_by_id(maison_id: int):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="La suppresion d'une maison funéraire via l'API est interdite."
    )