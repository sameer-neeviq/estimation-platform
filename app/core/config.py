from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "Estimation Platform"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "postgresql://admin:APass@localhost:5432/estimator-dev"
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALLOWED_HOSTS: List[str] = ["*"]
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
