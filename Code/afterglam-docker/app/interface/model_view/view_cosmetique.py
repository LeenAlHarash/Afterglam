from app.data.model.model_cosmetique import Cosmetique


class CosmetiqueView(Cosmetique):

    def __eq__(self, other):
        if not isinstance(other, CosmetiqueView):
            return NotImplemented
        return super().__eq__(other) and self.nb_cosmetiques_disponibles == other.nb_cosmetiques_disponibles