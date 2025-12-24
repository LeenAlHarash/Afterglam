from typing import Optional
from app.data.model.model_admin import Admin

class AdminView(Admin):
    id: int
    nom: str
    prenom: str
    telephone: str
    courriel: str
    mdp: Optional[str] = None

    def __eq__(self, other):
        if not isinstance(other, AdminView):
            return NotImplemented
        return super().__eq__(other) and self.nb_admins_disponibles == other.nb_admins_disponibles