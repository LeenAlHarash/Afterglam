from fastapi import FastAPI

from app.config.env import settings
from app.interface.routers import router_client, router_admin, router_cosmetique, router_form, router_maisonFuneraire, router_formCosmetique, router_auth

import mysql.connector

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    docs_url="/docs"
)

# Test qui permet de nous indiquer si le docker container s'exécute
@app.get("/")
def read_root():
    return {"message": "FastAPI fonctionne."}

# Inclusion du router client
app.include_router(router_client.router)

# Inclusion du router admin
app.include_router(router_admin.router)

# Inclusion du router cosmetique
app.include_router(router_cosmetique.router)

# Inclusion du router form
app.include_router(router_form.router)

# Inclusion du router maisonFuneraire
app.include_router(router_maisonFuneraire.router)

# Inclusion du router formCosmetique
app.include_router(router_formCosmetique.router)

# Inclusion du router auth
app.include_router(router_auth.router)