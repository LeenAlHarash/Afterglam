from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from app.utils.auth import admin_required
from app.services.services_formCosmetique import (
    add_formcosmetiques_by_name,
    get_formcosmetiques_by_form,
)
from app.interface.model_view.view_formCosmetique import FormCosmetiqueView

router = APIRouter(prefix="/formcosmetiques", tags=["formCosmetique"])

@router.post("/forms/{form_id}/cosmetiques/by-name", response_model=List[FormCosmetiqueView])
def add_cosmetiques_to_form_by_name(form_id: int, cosmetique_noms: List[str]):
    try:
        result = add_formcosmetiques_by_name(form_id, cosmetique_noms)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors de l'ajout des cosmétiques au formulaire")

@router.get("/forms/{form_id}", response_model=List[FormCosmetiqueView])
def get_cosmetiques_for_form(form_id: int, admin=Depends(admin_required)):
    try:
        result = get_formcosmetiques_by_form(form_id)
        if result:
            return result
        raise HTTPException(status_code=404, detail="Aucun cosmétique trouvé pour ce formulaire")
    except Exception:
        raise HTTPException(status_code=500,
                            detail="Erreur lors de la récupération des cosmétiques")