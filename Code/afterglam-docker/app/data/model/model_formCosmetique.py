from pydantic import BaseModel

class FormCosmetique(BaseModel):
    id: int
    form_id: int
    cosmetique_id: int