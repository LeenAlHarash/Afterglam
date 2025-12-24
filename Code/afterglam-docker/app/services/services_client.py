from typing import List, Optional

from app.db import afterglam
from app.data.data_client import get_all_clients, get_a_client, create_client_in_db, update_client_in_db, delete_client_in_db
from app.interface.model_view.view_client import ClientView
from app.data.model.model_client import Client

def convert_clients_to_view(client: ClientView) -> ClientView:
    if isinstance(client, dict):
        return ClientView(
            id=client["id"],
            nom=client["nom"],
            prenom=client["prenom"],
            telephone=client["telephone"],
            courriel=client["courriel"],
            adresse=client["adresse"],
            code_postal=client["code_postal"]
        )
    else:
        return ClientView(
            id=client.id,
            nom=client.nom,
            prenom=client.prenom,
            telephone=client.telephone,
            courriel=client.courriel,
            adresse=client.adresse,
            code_postal=client.code_postal
        )

def list_clients() -> List[ClientView]:
    clients = get_all_clients()
    return [convert_clients_to_view(c) for c in clients]


def get_client_by_id(client_id: int) -> Optional[ClientView]:
    client = get_a_client(client_id)
    if client:
        return convert_clients_to_view(client)
    return None

def create_client_db(client: ClientView) -> ClientView:
    client = create_client_in_db(client)
    if client:
        return convert_clients_to_view(client)
    return None


def update_client_db(client_id: int, client: ClientView) -> Optional[ClientView]:
    client = update_client_in_db(client_id, client)
    if client:
        return convert_clients_to_view(client)
    return None

# not too sure abt this
def delete_client_db(client_id: int) -> bool:
    client = delete_client_in_db(client_id)
    if client:
        return True
    return False