import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.db import afterglam
from app.services.services_maisonFuneraire import create_maison_db, update_maison_db, delete_maison_db
from app.interface.model_view.view_maisonFuneraire import MaisonView

def test_create_maison_in_db():
    # Créer un maison avec maisonView
    maison = MaisonView(
        id=4,
        nom="Complexe Funéraire Mont-Royal",
        telephone="514-095-0893",
        adresse="28e avenue",
        code_postal="H1X 7H9"
    )

    create_maison_db(maison)

    # Verify the maison was added correctly
    cursor = afterglam.cursor()
    cursor.execute("SELECT nom, telephone, adresse, code_postal FROM MaisonFuneraille WHERE id=%s", (maison.id,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Complexe Funéraire Mont-Royal"
    assert row[1] == "514-095-0893"
    assert row[2] == "28e avenue"
    assert row[3] == "H1X 7H9"

    afterglam.commit()
    cursor.close()

def test_update_maison_in_db():
    # Créer un maison dans la base de données
    initial_maison = MaisonView(
        id=5,
        nom="Maison Funéraire Desjardins & Fils", 
        telephone="123-456-7890",
        adresse="4372 13e avenue",
        code_postal="H9H 1O1"
    )
    
    # Ajouter ce maison à la base de données
    create_maison_db(initial_maison)

    # Mise à jour du maison
    updated_maison = MaisonView(
        id=5,
        nom="Maison Funéraire Desjardins",
        telephone="514-528-6985",
        adresse="4372 13e avenue",
        code_postal="H9H 1O1"
    )

    # Exécuter l'action qui fait la mise à jour du maison
    update_maison_db(5, updated_maison)

    cursor = afterglam.cursor()
    cursor.execute("SELECT nom, telephone, adresse, code_postal FROM MaisonFuneraille WHERE id=%s", (5,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Maison Funéraire Desjardins"
    assert row[1] == "514-528-6985" 
    assert row[2] == "4372 13e avenue"
    assert row[3] == "H9H 1O1"

    afterglam.commit()
    cursor.close()

def test_delete_maison_in_db():
    # Créer un maison dans la base de données
    maison_to_delete = MaisonView(
        id=6,
        nom="Maison Funéraire du Repos Éternel",
        telephone="555-555-5555",
        adresse="19e avenue",
        code_postal="D0D 0D0"
    )
    
    create_maison_db(maison_to_delete)

    # Exécuter l'action qui fait la suppression du maison
    result = delete_maison_db(6)

    assert result is True

    # Validation de la suppression
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM MaisonFuneraille WHERE id=%s", (6,))
    row = cursor.fetchone()

    assert row is None

    cursor.close()