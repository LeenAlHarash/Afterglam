import datetime
from typing import List
from fastapi import HTTPException, status
from jose import jwt
from app.data.data_admin import get_admin_by_email
from auth.interface.model_view.model_view_token import TokenView
from auth.interface.model_view.model_view_token_decoded import TokenViewDecoded
from auth.interface.model_view.model_view_refresh_token import RefreshTokenView
from auth.data.data_refresh_token import (
    get_all_refresh_tokens,
    save_refresh_token,
    get_refresh_token,
    invalidate_refresh_token,
)
from auth.config.env import settings


def convert_tokens_to_view(row: dict) -> RefreshTokenView:
    return RefreshTokenView(
        id=row["id"],
        status=row["status"]
    )


def list_refresh_tokens() -> List[RefreshTokenView]:
    tokens = get_all_refresh_tokens()
    return [convert_tokens_to_view(t) for t in tokens]


def issue_token(username: str) -> TokenView:
    access_token = create_access_token(username)
    new_id = save_refresh_token("valid")
    refresh_token = create_refresh_token(username, new_id)

    return TokenView(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )
    

def create_access_token(username: str) -> str:
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"sub": username, "exp": expire}
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def create_refresh_token(username: str, token_id: int) -> str:
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )
    to_encode = {"sub": username, "exp": expire, "jti": str(token_id)}
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def validate_token(token: str) -> TokenViewDecoded:
    decode_result = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    token_decoded = TokenViewDecoded(**decode_result)

    exp = token_decoded.exp
    if isinstance(exp, (int, float)):
        exp = datetime.datetime.fromtimestamp(exp, tz=datetime.timezone.utc)

    if exp < datetime.datetime.now(datetime.timezone.utc):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expiré")

    return token_decoded


def require_admin(token_decoded: TokenViewDecoded):
    admin = get_admin_by_email(token_decoded.sub)

    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Accès pour les admins seulement"
        )