from pydantic import BaseModel

class MaisonFuneraille(BaseModel):
    id: int
    nom: str
    telephone: str
    adresse: str
    code_postal: str

    def __eq__(self, other):
        if not isinstance(other, MaisonFuneraille):
            return notImplemented
        return self.id == other.id