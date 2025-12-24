from fastapi import FastAPI
from auth.config.env import settings
from auth.interface.routers import router_auth

app = FastAPI(
    title=settings.AUTH_PROJECT_NAME,
    version=settings.AUTH_API_VERSION
)

@app.get("/")
def root():
    return {"message": "Bonjour, AUTH!"}

app.include_router(router_auth.router)