from pydantic import BaseModel

class Admin(BaseModel):
    id: int
    nom: str
    prenom: str
    telephone: str
    courriel: str
    mdp: str

    def __eq__(self, other):
        if not isinstance(other, Admin):
            return notImplemented
        return self.id == other.id