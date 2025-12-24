from pydantic import BaseModel

class TokenView(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"