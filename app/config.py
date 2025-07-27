from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    APP_NAME: str = "Service"
    APP_VERSION: str = "1.0.0"
    APP_DEBUG: bool = Field(default=True, env="APP_DEBUG")

    MONGODB_URI: str = Field(..., env="MONGODB_URI")
    MONGODB_DB: str = Field(..., env="MONGODB_DB")

    ACCESS_TOKEN: str = Field(..., env="ACCESS_TOKEN")

    SMTP_SERVER: str = Field(..., env="SMTP_SERVER")
    SMTP_PORT: int = Field(default=587, env="SMTP_PORT")
    SMTP_USERNAME: str = Field(..., env="SMTP_USERNAME")
    SMTP_PASSWORD: str = Field(..., env="SMTP_PASSWORD")
    EMAIL_FROM: str = Field(..., env="EMAIL_FROM")
    EMAIL_TO: str = Field(..., env="EMAIL_TO")

    TEMP_DIR: str = "/tmp"
    
    class Config:
        env_file = BASE_DIR / ".env.dev"
        extra = "ignore"


settings = Settings()