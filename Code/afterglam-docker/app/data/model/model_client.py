from pydantic import BaseModel

class Client(BaseModel):
    id: int
    nom: str
    prenom: str
    telephone: str
    courriel: str
    adresse: str
    code_postal: str

    def __eq__(self, other):
        if not isinstance(other, Client):
            return notImplemented
        return self.id == other.id