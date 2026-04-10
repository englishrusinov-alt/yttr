from dataclasses import dataclass
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class SimpleConfig(BaseSettings):
    app_port: int
    database_url: str
    secret_key: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    app_env: str = 'local'

@dataclass
class AppConfig():
    app_port: int
    app_env: str = 'local'
@dataclass
class DatabaseConfig():
    database_url: str
@lru_cache
def get_settings()->SimpleConfig:
    return SimpleConfig()
@dataclass
class SecurityConfig():
    secret_key: str


def build_app_config(raw: SimpleConfig) -> AppConfig:
    return AppConfig(
        app_env=raw.app_env,
        app_port=raw.app_port,
    )


def build_database_config(raw: SimpleConfig) -> DatabaseConfig:
    return DatabaseConfig(
        database_url=raw.database_url,
    )


def build_security_config(raw: SimpleConfig) -> SecurityConfig:
    return SecurityConfig(
        secret_key=raw.secret_key,
    )

