import mysql.connector
import bcrypt

conn = mysql.connector.connect(
    host="db",
    user="root",
    password="root"
)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS afterglam")
cursor.execute("CREATE DATABASE afterglam")

cursor.close()
conn.close()

afterglam = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="afterglam"
)
cursor = afterglam.cursor()

with open("afterglam-db.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

statements = sql_script.split(";")
for statement in statements:
    if statement.strip():
        cursor.execute(statement)

cursor.close()
afterglam.commit()

def rehash_admin_passwords():
    afterglam = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="afterglam"
    )
    cursor = afterglam.cursor()
    cursor.execute("SELECT id, courriel, mdp FROM Admin")
    admins = cursor.fetchall()

    for admin_id, email, pwd in admins:
        if not pwd:
            continue

        # Ensure pwd is a string
        if isinstance(pwd, bytes):
            pwd = pwd.decode("utf-8")

        if not pwd.startswith("$2b$"):
            plain_pwd = f"admin{admin_id}"
            hashed_pwd = bcrypt.hashpw(
                plain_pwd.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")
            cursor.execute(
                "UPDATE Admin SET mdp = %s WHERE id = %s",
                (hashed_pwd, admin_id)
            )

    afterglam.commit()
    cursor.close()
    afterglam.close()

rehash_admin_passwords()