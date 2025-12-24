from pydantic import BaseModel

class Cosmetique(BaseModel):
    id: int
    nom: str

    def __eq__(self, other):
        if not isinstance(other, Cosmetique):
            return notImplemented
        return self.id == other.id