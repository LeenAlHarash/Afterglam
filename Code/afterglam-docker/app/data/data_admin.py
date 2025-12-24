from typing import List, Optional
import mysql.connector

from app.db import afterglam
from app.data.model.model_admin import Admin
from app.utils.auth import hasher_mdp, valider_courriel

def get_all_admins() -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Admin;")  
    results = cursor.fetchall()
    cursor.close()
    return results


def get_an_admin(admin_id: int) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Admin WHERE id=%s;", (admin_id,))  
    result = cursor.fetchone()
    cursor.close()
    return result


def create_admin_in_db(admin: Admin) -> Optional[dict]:
    if not valider_courriel(admin.courriel):
        raise ValueError("Format de courriel invalide")

    if get_admin_by_email(admin.courriel) is not None:
        raise ValueError("Un admin avec ce courriel existe déjà.")
        
    admin.mdp = hasher_mdp(admin.mdp)

    #DB
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Admin WHERE id=%s", (admin.id,))
    if cursor.fetchone():
        cursor.close()
        raise ValueError("Un admin avec cet identifiant existe déjà.")

    cursor.execute(
        "INSERT INTO Admin (id, nom, prenom, courriel, telephone, mdp) VALUES (%s, %s, %s, %s, %s, %s)",
        (admin.id, admin.nom, admin.prenom, admin.courriel, admin.telephone, admin.mdp)
    )
    afterglam.commit()
    cursor.close()
    return admin


def update_admin_in_db(admin_id: int, admin: Admin) -> Optional[dict]:
    cursor = afterglam.cursor()

    cursor.execute("SELECT id FROM Admin WHERE id=%s;", (admin_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return None
    
    # Hash
    if admin.mdp:
        admin.mdp = hasher_mdp(admin.mdp)

    cursor.execute(
        "UPDATE Admin SET nom=%s, prenom=%s, telephone=%s, courriel=%s, mdp=%s WHERE id=%s",
        (admin.nom, admin.prenom, admin.telephone, admin.courriel, admin.mdp, admin_id)
    )
    afterglam.commit()
    cursor.close()
    
    admin.id = admin_id
    return admin


def delete_admin_in_db(admin_id: int) -> bool:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Admin WHERE id=%s", (admin_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return False
    cursor.execute("DELETE FROM Admin WHERE id=%s", (admin_id,))
    afterglam.commit()
    cursor.close()
    return True

# Chercher un admin pas son email
def get_admin_by_email(email: str) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute(
        "SELECT id, nom, prenom, telephone, courriel, mdp FROM Admin WHERE courriel=%s",
        (email,)
    )
    row = cursor.fetchone()
    cursor.close()

    if row is None:
        return None

    return Admin(
        id=row[0],
        nom=row[1],
        prenom=row[2],
        telephone=row[3],
        courriel=row[4],
        mdp=row[5]
    )