import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.db import afterglam
from app.services.services_admin import create_admin_db, update_admin_db, delete_admin_db
from app.interface.model_view.view_admin import AdminView
from app.utils.auth import verifier_mdp

def test_create_admin_in_db():
    # Créer un admin avec AdminView
    admin = AdminView(
        id=5,
        nom="Summers",
        prenom="Dalia",
        telephone="438-985-0125",
        courriel="summersdalia@gmail.com",
        mdp="1234"
    )

    create_admin_db(admin)

    # Verify the admin was added correctly
    cursor = afterglam.cursor()
    cursor.execute("SELECT nom, prenom, telephone, courriel, mdp FROM Admin WHERE id=%s", (admin.id,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Summers"
    assert row[1] == "Dalia"
    assert row[2] == "438-985-0125"
    assert row[3] == "summersdalia@gmail.com"
    assert verifier_mdp("1234", row[4])

    afterglam.commit()
    cursor.close()

def test_update_admin_in_db():
    # Créer un admin dans la base de données
    initial_admin = AdminView(
        id=6,
        nom="Shortcake",
        prenom="Strawberry", 
        telephone="514-520-5206",
        courriel="ss@gmail.com",
        mdp="4567"
    )
    
    # Ajouter ce admin à la base de données
    create_admin_db(initial_admin)

    # Mise à jour du admin
    updated_admin = AdminView(
        id=6,
        nom="Shortcake",
        prenom="Strawberry",
        telephone="514-520-5206", 
        courriel="nouveaucourriel@gmail.com",
        mdp="4567"
    )

    # Exécuter l'action qui fait la mise à jour du admin
    update_admin_db(6, updated_admin)

    cursor = afterglam.cursor()
    cursor.execute("SELECT nom, prenom, telephone, courriel, mdp FROM Admin WHERE id=%s", (6,))
    row = cursor.fetchone()

    # Vérifier si les données sont dans la base de données
    assert row is not None
    assert row[0] == "Shortcake"
    assert row[1] == "Strawberry" 
    assert row[2] == "514-520-5206"
    assert row[3] == "nouveaucourriel@gmail.com"
    assert verifier_mdp("4567", row[4])

    afterglam.commit()
    cursor.close()

def test_delete_admin_in_db():
    # Créer un admin dans la base de données
    admin_to_delete = AdminView(
        id=7,
        nom="Bones",
        prenom="Rocky",
        telephone="438-952-9528",
        courriel="bones@gmail.com",
        mdp="7890"
    )
    
    create_admin_db(admin_to_delete)

    # Exécuter l'action qui fait la suppression du admin
    result = delete_admin_db(7)

    assert result is True

    # Validation de la suppression
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Admin WHERE id=%s", (7,))
    row = cursor.fetchone()

    assert row is None

    cursor.close()