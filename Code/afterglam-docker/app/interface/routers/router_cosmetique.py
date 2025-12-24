from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.responses import JSONResponse
from app.utils.auth import admin_required
from app.db import afterglam
from app.interface.model_view.view_cosmetique import CosmetiqueView
from app.services.services_cosmetique import (list_cosmetiques, get_cosmetique_by_id, get_cosmetique_by_name,create_cosmetique_db, update_cosmetique_db, delete_cosmetique_db)

router = APIRouter(prefix="/cosmetiques", tags=["cosmetiques"])

@router.get("/", response_model=list[CosmetiqueView])
def get_comestiques():
    return list_cosmetiques()

@router.get("/id/{cosmetique_id}", response_model=CosmetiqueView)
def get_cosmetique(cosmetique_id: int, admin=Depends(admin_required)):
    cosmetique = get_cosmetique_by_id(cosmetique_id)
    if not cosmetique:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le cosmétique n'existe pas.")
    return cosmetique

@router.get("/name/{cosmetique_nom}", response_model=CosmetiqueView)
def get_cosmetique(cosmetique_nom: str):
    cosmetique = get_cosmetique_by_name(cosmetique_nom)
    if not cosmetique:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Le cosmétique n'existe pas.")
    return cosmetique

@router.post("/", response_model=CosmetiqueView, status_code=status.HTTP_201_CREATED)
def create_cosmetique(cosmetique: CosmetiqueView, admin=Depends(admin_required)):
    try:
        return create_cosmetique_db(cosmetique)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Le cosmétique n'a pas été crée avec succès")

@router.put("/{cosmetique_id}", response_model=CosmetiqueView)
def replace_cosmetique(cosmetique_id: int, nouveau_cosmetique: CosmetiqueView):
    try:
        mise_a_jour_cosmetique = update_cosmetique_db(cosmetique_id, nouveau_cosmetique)
        return JSONResponse(content=mise_a_jour_cosmetique.model_dump(), status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Le cosmétique n'a pas été modifié avec succès")

@router.delete("/{cosmetique_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_cosmetique_by_id(cosmetique_id: int):
    try:
        return delete_cosmetique_db(cosmetique_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Le cosmétique n'a pas été supprimé avec succès")