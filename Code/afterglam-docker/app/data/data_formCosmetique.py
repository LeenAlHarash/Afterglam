from typing import List, Optional
import mysql.connector

from app.db import afterglam
from app.data.model.model_formCosmetique import FormCosmetique

def insert_form_cosmetique(form_id: int, cosmetique_id: int) -> int:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO FormCosmetique (form_id, cosmetique_id) VALUES (%s, %s);",
        (form_id, cosmetique_id)
    )
    fc_id = cursor.lastrowid
    afterglam.commit()
    cursor.close()
    return fc_id

def get_form_cosmetiques(form_id: int) -> list[dict]:
    cursor = afterglam.cursor(dictionary=True)
    query = """
        SELECT FC.id, FC.form_id, FC.cosmetique_id, C.nom AS cosmetique_nom
        FROM FormCosmetique FC
        JOIN Cosmetique C ON C.id = FC.cosmetique_id
        WHERE FC.form_id=%s;
    """
    cursor.execute(query, (form_id,))
    result = cursor.fetchall()
    cursor.close()
    return result