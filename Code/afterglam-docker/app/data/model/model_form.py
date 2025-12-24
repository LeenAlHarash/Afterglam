from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class StatutEnum(str, Enum):
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    PEND = 'PEND'

class Form(BaseModel):
    id: int
    date_creation: datetime
    statut: StatutEnum
    date_collecte: datetime
    client_id: int # Clé étrangère pour le client
    admin_id: int # Clé étrangère pour l'administrateur
    maison_id: int # Clé étrangère pour la maison funéraire

    def __eq__(self, other):
        if not isinstance(other, Form):
            return notImplemented
        return self.id == other.id

