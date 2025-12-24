from fastapi import APIRouter, Form, HTTPException, status
from jose import jwt, JWTError
from typing import List

from auth.interface.model_view.model_view_token_decoded import TokenViewDecoded
from auth.interface.model_view.model_view_token import TokenView
from auth.interface.model_view.model_view_refresh_token import RefreshTokenView
from auth.services.services_auth import (issue_token, validate_token, create_access_token, create_refresh_token, list_refresh_tokens)
from auth.data.data_refresh_token import (get_refresh_token, invalidate_refresh_token, save_refresh_token)
from auth.config.env import settings
from app.data.data_admin import get_admin_by_email

router = APIRouter()

@router.post("/token")
def authenticate(email: str = Form(...)):
    return issue_token(email)

@router.post("/token/validate")
def validate(token: str = Form(...)) -> TokenViewDecoded:
    return validate_token(token)

@router.post("/refresh", summary="Refresh access token")
def refresh(refresh_token: str = Form(...)) -> TokenView:
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    username = payload.get("sub")
    token_id = payload.get("jti")

    if not username or not token_id:
        raise HTTPException(status_code=400, detail="Missing claims")

    record = get_refresh_token(int(token_id))
    if not record or record["status"] != "valid":
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    invalidate_refresh_token(int(token_id))

    new_access_token = create_access_token(username)
    new_id = save_refresh_token("valid")
    new_refresh_token = create_refresh_token(username, new_id)

    return TokenView(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
        token_type="bearer"
    )

@router.get("/refreshTokens", response_model=List[RefreshTokenView])
def get_refresh_tokens():
    return list_refresh_tokens()
