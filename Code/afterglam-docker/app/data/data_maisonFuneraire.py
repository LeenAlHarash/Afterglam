from typing import List, Optional
import mysql.connector

from app.db import afterglam
from app.data.model.model_maisonFuneraire import MaisonFuneraille

def get_all_maisons() -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MaisonFuneraille;")  
    results = cursor.fetchall()
    cursor.close()
    return results

def get_a_maisonFuneraire(maison_id: int) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MaisonFuneraille WHERE id=%s;", (maison_id,))  
    result = cursor.fetchone()
    cursor.close()
    return result

def get_a_maisonFuneraire_by_name(maison_name: str) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MaisonFuneraille WHERE nom=%s;", (maison_name,))  
    result = cursor.fetchone()
    cursor.close()
    return result

def create_maison_in_db(maison: dict) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM MaisonFuneraille WHERE id=%s", (maison.id,))
    if cursor.fetchone():
        cursor.close()
        raise ValueError("Une maison avec cet identifiant existe déjà.")

    cursor.execute(
        "INSERT INTO MaisonFuneraille (id, nom, telephone, adresse, code_postal) VALUES (%s, %s, %s, %s, %s);",
        (maison.id, maison.nom, maison.telephone, maison.adresse, maison.code_postal)
    )
    afterglam.commit()
    cursor.close()
    return maison

def update_maison_in_db(maison_id: int, maison: MaisonFuneraille) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM MaisonFuneraille WHERE id=%s;", (maison_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return None

    if "telephone" in maison and not valider_telephone(maison["telephone"]):
        raise ValueError("Le numéro de téléphone est invalide.")

    cursor.execute(
        "UPDATE MaisonFuneraille SET nom=%s, telephone=%s, adresse=%s, code_postal=%s WHERE id=%s;",
        (maison.nom, maison.telephone, maison.adresse, maison.code_postal, maison_id)
    )
    afterglam.commit()
    cursor.close()
    maison.id = maison.id
    return maison


def delete_maison_in_db(maison_id: int) -> bool:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM MaisonFuneraille WHERE id=%s;", (maison_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return False

    cursor.execute("DELETE FROM MaisonFuneraille WHERE id=%s;", (maison_id,))
    afterglam.commit()
    cursor.close()
    return True