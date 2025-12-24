import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.db import afterglam
from app.services.services_cosmetique import create_cosmetique_db, update_cosmetique_db, delete_cosmetique_db
from app.interface.model_view.view_cosmetique import CosmetiqueView

def test_create_cosmetique_in_db():
    # Créer un cosmetique avec CosmetiqueView
    cosmetique = CosmetiqueView(
        id=11,
        nom="Illuminateur"
    )

    create_cosmetique_db(cosmetique)

    # Verify the cosmetique was added correctly
    cursor = afterglam.cursor()
    cursor.execute("SELECT nom FROM Cosmetique WHERE id=%s", (cosmetique.id,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Illuminateur"

    afterglam.commit()
    cursor.close()

def test_update_cosmetique_in_db():
    # Créer un cosmetique dans la base de données
    initial_cosmetique = CosmetiqueView(
        id=12,
        nom="Poudre bronzante"
    )
    
    # Ajouter ce cosmetique à la base de données
    create_cosmetique_db(initial_cosmetique)

    # Mise à jour du cosmetique
    updated_cosmetique = CosmetiqueView(
        id=12,
        nom="Poudre"
    )

    # Exécuter l'action qui fait la mise à jour du cosmetique
    update_cosmetique_db(12, updated_cosmetique)

    cursor = afterglam.cursor()
    cursor.execute("SELECT nom FROM Cosmetique WHERE id=%s", (12,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Poudre"

    afterglam.commit()
    cursor.close()

def test_delete_cosmetique_in_db():
    # Créer un cosmetique dans la base de données
    cosmetique_to_delete = CosmetiqueView(
        id=13,
        nom="Base de maquillage"
    )
    
    create_cosmetique_db(cosmetique_to_delete)

    # Exécuter l'action qui fait la suppression du cosmetique
    result = delete_cosmetique_db(13)

    assert result is True

    # Validation de la suppression
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Cosmetique WHERE id=%s", (13,))
    row = cursor.fetchone()

    assert row is None

    cursor.close()