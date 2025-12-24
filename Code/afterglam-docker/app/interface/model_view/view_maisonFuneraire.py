from app.data.model.model_maisonFuneraire import MaisonFuneraille


class MaisonView(MaisonFuneraille):

    def __eq__(self, other):
        if not isinstance(other, MaisonView):
            return NotImplemented
        return super().__eq__(other) and self.nb_maisons_disponibles == other.nb_maisons_disponibles