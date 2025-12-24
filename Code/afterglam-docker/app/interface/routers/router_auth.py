from typing import List
from fastapi import APIRouter

from app.interface.model_view.model_view_refresh_token import RefreshTokenView
from app.services.services_auth import get_refresh_tokens

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/refreshTokens", response_model=List[RefreshTokenView])
def get_list_refresh_tokens():
    return get_refresh_tokens()