import pytest
import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.db import afterglam
from app.services.services_form import create_form_db, update_form_db, delete_form_db
from app.interface.model_view.view_form import FormView
from app.data.model.model_form import StatutEnum

def test_create_form_in_db():
    # Créer un formulaire avec FormView
    form = FormView(
        id=7,
        date_creation=datetime(2024, 5, 1, 10, 30),
        statut=StatutEnum.OPEN,
        date_collecte=datetime(2024, 5, 15, 14, 0),
        client_id=1,
        admin_id=1,
        maison_id=1,
        nom="Lévesque",
        prenom="Sophie"
    )

    create_form_db(form)

    # Liaison des id cosmetiques avec le formulaire
    cosmetique_ids = [1, 2]
    cursor = afterglam.cursor()
    for cosmetique_id in cosmetique_ids:
        cursor.execute(
            "INSERT INTO FormCosmetique (form_id, cosmetique_id) VALUES (%s, %s)",
            (form.id, cosmetique_id)
        )

    # Vérifier si le formulaire a été ajouté
    cursor = afterglam.cursor()
    cursor.execute(
        "SELECT date_creation, statut, date_collecte, client_id, admin_id, maison_id FROM Form WHERE id=%s",
        (form.id,)
    )
    row = cursor.fetchone()

    assert row is not None
    assert row[1] == "OPEN"
    assert row[3] == 1
    assert row[4] == 1
    assert row[5] == 1

    # Vérifier si les cosmétiques ont été liés
    cursor.execute(
        "SELECT cosmetique_id FROM FormCosmetique WHERE form_id=%s ORDER BY cosmetique_id",
        (form.id,)
    )
    linked_cosmetiques = [r[0] for r in cursor.fetchall()]
    assert linked_cosmetiques == cosmetique_ids

    afterglam.commit()
    cursor.close()

def test_update_form_in_db():
    # Créer un formulaire initial
    initial_form = FormView(
        id=8,
        date_creation=datetime(2024, 4, 1, 12, 0),
        statut=StatutEnum.PEND,
        date_collecte=datetime(2024, 4, 5, 9, 0),
        client_id=2,
        admin_id=2,
        maison_id=2,
        nom="Nguyen",
        prenom="Marc"
    )

    create_form_db(initial_form)

    # Mise à jour du formulaire
    updated_form = FormView(
        id=8,
        date_creation=initial_form.date_creation,
        statut=StatutEnum.CLOSE,
        date_collecte=datetime(2024, 4, 10, 10, 0),
        client_id=2,
        admin_id=2,
        maison_id=2,
        nom="Nguyen",
        prenom="Marc"
    )

    update_form_db(8, updated_form)
    
    # Liaison des id cosmetiques avec le formulaire
    cosmetique_ids = [1, 2]
    cursor = afterglam.cursor()
    for cosmetique_id in cosmetique_ids:
        cursor.execute(
            "INSERT INTO FormCosmetique (form_id, cosmetique_id) VALUES (%s, %s)",
            (updated_form.id, cosmetique_id)
        )

    cursor = afterglam.cursor()
    cursor.execute("SELECT statut, date_collecte FROM Form WHERE id=%s", (8,))
    row = cursor.fetchone()

    assert row is not None
    assert row[0] == "CLOSE"
    assert str(row[1].date()) == "2024-04-10"
    
    # Vérifier si les cosmétiques ont été liés
    cursor.execute(
        "SELECT cosmetique_id FROM FormCosmetique WHERE form_id=%s ORDER BY cosmetique_id",
        (updated_form.id,)
    )
    linked_cosmetiques = [r[0] for r in cursor.fetchall()]
    assert linked_cosmetiques == cosmetique_ids

    afterglam.commit()
    cursor.close()

def test_delete_form_in_db():
    # Créer un formulaire à supprimer
    form_to_delete = FormView(
        id=9,
        date_creation=datetime(2024, 3, 1, 8, 0),
        statut=StatutEnum.OPEN,
        date_collecte=datetime(2024, 3, 5, 17, 0),
        client_id=3,
        admin_id=3,
        maison_id=3,
        nom="Dubois",
        prenom="Élise"
    )

    create_form_db(form_to_delete)

    # Liaison des id cosmetiques avec le formulaire
    cosmetique_ids = [1, 2]
    cursor = afterglam.cursor()
    for cosmetique_id in cosmetique_ids:
        cursor.execute(
            "INSERT INTO FormCosmetique (form_id, cosmetique_id) VALUES (%s, %s)",
            (form_to_delete.id, cosmetique_id)
        )

    # Supprimer les liens avant de supprimer le formulaire
    cursor.execute("DELETE FROM FormCosmetique WHERE form_id=%s", (form_to_delete.id,))

    # Supprimer le formulaire
    result = delete_form_db(9)
    assert result is True

    # Vérifier la suppression
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Form WHERE id=%s", (9,))
    row = cursor.fetchone()
    assert row is None

    # Vérifier la suppression des liens dans FormCosmetique
    cursor.execute("SELECT * FROM FormCosmetique WHERE form_id=%s", (form_to_delete.id,))
    linked = cursor.fetchall()
    assert linked == []  # Doit être vide si les liens ont été supprimés

    cursor.close()