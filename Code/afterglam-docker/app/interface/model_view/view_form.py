from app.data.model.model_form import Form

class FormView(Form):
    nom: str
    prenom: str

    def __eq__(self, other):
        if not isinstance(other, FormView):
            return NotImplemented
        return super().__eq__(other) and self.nb_forms_disponibles == other.nb_forms_disponibles