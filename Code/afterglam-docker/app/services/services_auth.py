import bcrypt
import requests
from fastapi import HTTPException
from starlette import status
from typing import List

from app.config.env import settings
from app.data import data_admin
from app.interface.model_view.model_view_token import TokenView
from app.interface.model_view.model_view_token_decoded import TokenViewDecoded
from app.interface.model_view.model_view_refresh_token import RefreshTokenView

def authenticate_and_issue_token(email: str, password: str) -> TokenView:
    admin = data_admin.get_admin_by_email(email)
    if not admin or not verify_password(password, admin.mdp):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        response = requests.post(
            settings.TOKEN_ENDPOINT,
            data={
                "email": admin.courriel,
                "password": password
            }
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to obtain token from auth service",
        )

    token_data = response.json()
    return TokenView(**token_data)

def refresh_token_flow(refresh_token: str) -> TokenView:
    try:
        response = requests.post(
            settings.REFRESH_ENDPOINT,
            data={"refresh_token": refresh_token}
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to refresh token from auth service",
        )

    token_data = response.json()
    return TokenView(**token_data)

def validate_token(token: str) -> TokenViewDecoded:
    try:
        response = requests.post(
            settings.TOKEN_VALIDATE_ENDPOINT,
            {
                "token": token
            }
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if response.status_code == status.HTTP_403_FORBIDDEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=response.json()["detail"])

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to validate token from auth service",
        )

    token_data = response.json()
    return TokenViewDecoded(**token_data)

def get_refresh_tokens() -> List[RefreshTokenView]:
    try:
        response = requests.get(settings.REFRESH_TOKENS_ENDPOINT)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch refresh tokens from auth service",
        )

    tokens_data = response.json()
    return [RefreshTokenView(**t) for t in tokens_data]

def verify_password(plain_password: str, hashed_password) -> bool:
    if isinstance(hashed_password, str):
        hashed_bytes = hashed_password.encode("utf-8")
    else:
        hashed_bytes = hashed_password  # already bytes
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_bytes)

def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")