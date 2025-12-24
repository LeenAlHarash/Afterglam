from typing import List, Optional
import mysql.connector

from app.db import afterglam
from app.data.model.model_client import Client

def get_all_clients() -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Client;")  
    results = cursor.fetchall()
    cursor.close()
    return results

def get_a_client(client_id: int) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Client WHERE id=%s;", (client_id,))  
    result = cursor.fetchone()
    cursor.close()
    return result

def create_client_in_db(client: Client) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Client WHERE id=%s", (client.id,))
    if cursor.fetchone():
        cursor.close()
        raise ValueError("Un client avec cet identifiant existe déjà.")
    
    cursor.execute(
        "INSERT INTO Client (id, nom, prenom, telephone, courriel, adresse, code_postal) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (client.id, client.nom, client.prenom, client.telephone, client.courriel, client.adresse, client.code_postal)
    )
    afterglam.commit()
    cursor.close()
    return client

def update_client_in_db(client_id: int, client: Client) -> Optional[dict]:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Client WHERE id=%s", (client_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return None
    
    cursor.execute(
        "UPDATE Client SET nom=%s, prenom=%s, telephone=%s, courriel=%s, adresse=%s, code_postal=%s WHERE id=%s",
        (client.nom, client.prenom, client.telephone, client.courriel, client.adresse, client.code_postal, client_id)
    )
    afterglam.commit()
    cursor.close()
    client.id = client_id
    return client


def delete_client_in_db(client_id: int) -> bool:
    cursor = afterglam.cursor()
    cursor.execute("SELECT id FROM Client WHERE id=%s", (client_id,))
    if cursor.fetchone() is None:
        cursor.close()
        return False
    cursor.execute("DELETE FROM Client WHERE id=%s", (client_id,))
    afterglam.commit()
    cursor.close()
    return True