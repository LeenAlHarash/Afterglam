from app.data.model.model_client import Client

class ClientView(Client):

    def __eq__(self, other):
        if not isinstance(other, ClientView):
            return NotImplemented
        return super().__eq__(other) and self.nb_clients_disponibles == other.nb_clients_disponibles