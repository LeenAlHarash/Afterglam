from datetime import datetime
from pydantic import BaseModel

class TokenViewDecoded(BaseModel):
    sub: str
    exp: datetime