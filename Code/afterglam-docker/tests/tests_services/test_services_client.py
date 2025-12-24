import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.db import afterglam
from app.services.services_client import create_client_db, update_client_db, delete_client_db
from app.interface.model_view.view_client import ClientView

def test_create_client_in_db():
    # Créer un client avec ClientView
    client = ClientView(
        id=7,
        nom="Chevalier",
        prenom="Simon",
        telephone="514-095-0893",
        courriel="monchevalier@gmail.com",
        adresse="28e avenue",
        code_postal="H1X 7H9"
    )

    create_client_db(client)

    # Verify the client was added correctly
    cursor = afterglam.cursor()
    cursor.execute("SELECT nom, prenom, telephone, courriel, adresse, code_postal FROM Client WHERE id=%s", (client.id,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Chevalier"
    assert row[1] == "Simon"
    assert row[2] == "514-095-0893"
    assert row[3] == "monchevalier@gmail.com"
    assert row[4] == "28e avenue"
    assert row[5] == "H1X 7H9"

    afterglam.commit()
    cursor.close()

def test_update_client_in_db():
    # Créer un client dans la base de données
    initial_client = ClientView(
        id=8,
        nom="Old",
        prenom="Name", 
        telephone="123-456-7890",
        courriel="old@example.com",
        adresse="Old Address",
        code_postal="H0H 0H0"
    )
    
    # Ajouter ce client à la base de données
    create_client_db(initial_client)

    # Mise à jour du client
    updated_client = ClientView(
        id=8,
        nom="New",
        prenom="Name",
        telephone="987-654-3210", 
        courriel="new@example.com",
        adresse="New Address",
        code_postal="H1H 1H1"
    )

    # Exécuter l'action qui fait la mise à jour du client
    update_client_db(8, updated_client)

    cursor = afterglam.cursor()
    cursor.execute("SELECT nom, prenom, telephone, courriel, adresse, code_postal FROM Client WHERE id=%s", (8,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "New"
    assert row[1] == "Name" 
    assert row[2] == "987-654-3210"
    assert row[3] == "new@example.com"
    assert row[4] == "New Address"
    assert row[5] == "H1H 1H1"

    afterglam.commit()
    cursor.close()

def test_delete_client_in_db():
    # Créer un client dans la base de données
    client_to_delete = ClientView(
        id=9,
        nom="To",
        prenom="Delete",
        telephone="555-555-5555",
        courriel="del@example.com",
        adresse="Delete Address", 
        code_postal="D0D 0D0"
    )
    
    create_client_db(client_to_delete)

    # Exécuter l'action qui fait la suppression du client
    result = delete_client_db(9)

    assert result is True

    # Validation de la suppression
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Client WHERE id=%s", (9,))
    row = cursor.fetchone()

    assert row is None

    cursor.close()