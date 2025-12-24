from typing import Optional, List
from app.db import afterglam

def save_refresh_token(status: str = "valid") -> int:
    cursor = afterglam.cursor()
    cursor.execute(
        "INSERT INTO refresh_tokens (status) VALUES (%s)",
        (status,)
    )
    afterglam.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def invalidate_refresh_token(token_id: int) -> None:
    cursor = afterglam.cursor()

    cursor.execute(
        "UPDATE refresh_tokens SET status = 'invalid' WHERE id = %s",
        (token_id,)
    )

    cursor.execute(
        "DELETE FROM refresh_tokens WHERE id = %s",
        (token_id,)
    )
    afterglam.commit()
    cursor.close()

def get_refresh_token(token_id: int) -> Optional[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM refresh_tokens WHERE id = %s", (token_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_all_refresh_tokens() -> List[dict]:
    cursor = afterglam.cursor(dictionary=True)
    cursor.execute("SELECT * FROM refresh_tokens;")
    results = cursor.fetchall()
    cursor.close()
    return results