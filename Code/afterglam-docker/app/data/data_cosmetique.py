from typing import List, Optional
import mysql.connector

from app.db import afterglam
from app.data.model.model_cosmetique import Cosmetique

def get_all_cosmetiques() -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cosmetique;")  
    results = cursor.fetchall()
    cursor.close()
    return results

def get_a_cosmetique(cosmetique_id: int) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cosmetique WHERE id=%s;", (cosmetique_id,))  
    result = cursor.fetchone()
    cursor.close()
    return result
    
def get_cosmetique_by_nom(nom: str) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT id, nom FROM Cosmetique WHERE nom=%s;", (nom,))
    result = cursor.fetchone()
    cursor.close()
    return result

def create_cosmetique_in_db(cosmetique: Cosmetique) -> Optional[dict]:
    cursor = afterglam.cursor()
    if cosmetique.id:
        cursor.execute("SELECT id FROM Cosmetique WHERE id=%s;", (cosmetique.id,))
        if cursor.fetchone():
            cursor.close()
            raise ValueError("Un cosmetique avec cet identifiant existe déjà.")

    cursor.execute(
        "INSERT INTO Cosmetique (id, nom) VALUES (%s, %s);",
        (cosmetique.id, cosmetique.nom)
    )
    afterglam.commit()
    cursor.close()
    return cosmetique


def update_cosmetique_in_db(cosmetique_id: int, cosmetique: Cosmetique) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Cosmetique WHERE id=%s;", (cosmetique_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return None

    cursor.execute(
        "UPDATE Cosmetique SET nom=%s WHERE id=%s;",
        (cosmetique.nom, cosmetique_id)
    )
    afterglam.commit()
    cursor.close()
    cosmetique.id = cosmetique_id
    return cosmetique


def delete_cosmetique_in_db(cosmetique_id: int) -> bool:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Cosmetique WHERE id=%s;", (cosmetique_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return False

    cursor.execute("DELETE FROM Cosmetique WHERE id=%s;", (cosmetique_id,))
    afterglam.commit()
    cursor.close()
    return True