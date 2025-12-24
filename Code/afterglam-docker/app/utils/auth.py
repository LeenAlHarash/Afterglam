import re
import bcrypt
from datetime import datetime
from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError
from app.config.env import settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "THISISASECRETKEY"
bearer_scheme = HTTPBearer()


def valider_courriel(courriel: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" #valider le courriel
    return re.match(pattern, courriel) is not None


def valider_telephone(telephone: str) -> bool:
    return telephone.isdigit() and 10 <= len(telephone) <= 15


def format_nom_complet(nom: str, prenom: str) -> str:
    if not nom and not prenom:
        return "Inconnu"
    return f"{prenom.strip().capitalize()} {nom.strip().upper()}"


def format_date(date_value) -> str:
    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d %H:%M")
    return str(date_value)


def hasher_mdp(mdp: str) -> str:
    if not mdp:
        raise ValueError("Le mot de passe ne peut pas être vide.")
    hashed = bcrypt.hashpw(mdp.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8") #retourne hasher

    
    #comparer avec le mdp hasher
def verifier_mdp(mdp: str, mdp_hash) -> bool:
    if not mdp or not mdp_hash:
        return False

    if isinstance(mdp_hash, str):
        mdp_hash = mdp_hash.encode("utf-8")

    return bcrypt.checkpw(mdp.encode("utf-8"), mdp_hash)


def authentifier_utilisateur(utilisateur: dict, mdp: str) -> bool:
    if not utilisateur or "mdp" not in utilisateur:
        return False
    return verifier_mdp(mdp, utilisateur["mdp"])


def admin_required(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError as e:
        print("JWT ERROR:", e)
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")