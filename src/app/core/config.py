"""Application configuration using pydantic-settings."""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Project metadata
    PROJECT_NAME: str = "AI-Driven FastAPI Template"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "A FastAPI template with AI-driven development workflow"

    # Environment
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = True

    # API Configuration
    API_V1_PREFIX: str = "/api/v1"

    # CORS
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:1212",
        "http://127.0.0.1:1212",
    ]

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 1212
    RELOAD: bool = True


settings = Settings()
