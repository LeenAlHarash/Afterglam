from typing import List, Optional
import mysql.connector

from app.db import afterglam
from app.data.model.model_form import Form

def get_all_forms() -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Form;")  
    results = cursor.fetchall()
    cursor.close()
    return results

def get_a_form(form_id: int) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Form WHERE id=%s;", (form_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_a_form_from_client(client_id: int) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Form WHERE client_id=%s;", (client_id,))  
    result = cursor.fetchall()
    cursor.close()
    return result

# Jointure
def get_forms_from_client_nom(form_client_id: int) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT Form.*, Client.nom AS nom, Client.prenom AS prenom FROM Form JOIN Client ON Client.id = Form.client_id WHERE Form.client_id=%s;", (form_client_id,))  
    result = cursor.fetchall()
    cursor.close()
    return result

def get_forms_from_client_email(client_email: str) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    
    cursor.execute("SELECT id FROM Client WHERE courriel=%s;", (client_email,))
    client = cursor.fetchone()
    
    if not client:
        cursor.close()
        return []
    
    client_id = client["id"]
    
    cursor.execute("""
        SELECT Form.*, Client.nom AS nom, Client.prenom AS prenom
        FROM Form
        JOIN Client ON Client.id = Form.client_id
        WHERE Form.client_id=%s;
    """, (client_id,))
    
    result = cursor.fetchall()
    cursor.close()
    return result

def get_forms_from_admin(form_admin_id: int) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Form WHERE admin_id=%s;", (form_admin_id,))  
    result = cursor.fetchall()
    cursor.close()
    return result

# Jointure
def get_forms_from_admin_nom(form_admin_id: int) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT Form.*, Admin.nom AS nom, Admin.prenom AS prenom FROM Form JOIN Admin ON Admin.id = Form.admin_id WHERE Form.admin_id=%s;", (form_admin_id,))  
    result = cursor.fetchall()
    cursor.close()
    return result

def get_forms_from_maison(form_maison_id: int) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Form WHERE maison_id=%s;", (form_maison_id,))  
    result = cursor.fetchall()
    cursor.close()
    return result

# Jointure
def get_forms_from_maison_nom(form_maison_id: int) -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT Form.*, MaisonFuneraille.nom AS nom FROM Form JOIN MaisonFuneraille ON MaisonFuneraille.id = Form.maison_id WHERE Form.maison_id=%s;", (form_maison_id,))  
    result = cursor.fetchall()
    cursor.close()
    return result

def create_form_in_db(form: Form) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Form WHERE id=%s", (form.id,))
    if cursor.fetchone():
        cursor.close()
        raise ValueError("Un formulaire avec cet identifiant existe déjà.")

    cursor.execute(
        "INSERT INTO Form (id, date_creation, statut, date_collecte, client_id, admin_id, maison_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (form.id, form.date_creation, form.statut, form.date_collecte, form.client_id, form.admin_id, form.maison_id)
    )

    afterglam.commit()
    cursor.close()
    return form

def update_form_in_db(form_id: int, form: Form) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Form WHERE id=%s;", (form_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return None

    cursor.execute(
        "UPDATE Form SET date_creation=%s, statut=%s, date_collecte=%s, client_id=%s, admin_id=%s, maison_id=%s WHERE id=%s",
        (form.date_creation, form.statut, form.date_collecte, form.client_id, form.admin_id, form.maison_id, form_id)
    )

    afterglam.commit()
    cursor.close()
    return form

def delete_form_in_db(form_id: int) -> bool:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Form WHERE id=%s;", (form_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return False

    cursor.execute("DELETE FROM Form WHERE id=%s;", (form_id,))
    afterglam.commit()
    cursor.close()
    return True