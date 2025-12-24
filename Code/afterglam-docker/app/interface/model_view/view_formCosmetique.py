from app.data.model.model_formCosmetique import FormCosmetique

class FormCosmetiqueView(FormCosmetique):
    id: int
    form_id: int
    cosmetique_id: int

    def __eq__(self, other):
        if not isinstance(other, FormCosmetiqueView):
            return NotImplemented