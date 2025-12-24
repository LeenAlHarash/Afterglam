from pydantic import BaseModel

class RefreshTokenView(BaseModel):
    id: int
    status: str