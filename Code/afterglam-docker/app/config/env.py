from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str = "mariadb+pymysql://apiuser:apipassword@db:3306/apidb?charset=utf8mb4"
    JWT_SECRET: str = "SECRET_TO_CHANGE"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    PROJECT_NAME: str = "Default Project Name"
    API_VERSION: str = "0.0.0"
    TOKEN_ENDPOINT: str = "http://auth:8080/token"
    TOKEN_VALIDATE_ENDPOINT : str = "http://auth:8080/token/validate"
    REFRESH_ENDPOINT: str = "http://auth:8080/refresh"
    REFRESH_TOKENS_ENDPOINT: str = "http://auth:8080/refreshTokens"
    
settings = Settings()