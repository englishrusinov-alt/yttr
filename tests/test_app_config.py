import pytest
from pydantic import ValidationError

import app.config
from app.config import AppConfig, SimpleConfig


def test_get_settings_success(monkeypatch):
    # Этап 1: Подменяем переменные окружения (monkeypatch.setenv)
    # Нам нужно замокать ВСЕ обязательные поля, чтобы класс собрался.
    # ВАЖНО: monkeypatch работает со строками, поэтому порт передаем как "8080"

    raw = SimpleConfig(app_port=8080, database_url=
        "postgresql://user:pass@localhost:5432/mydb" , secret_key=
                       "change_this_in_production"
                       )
    settings = app.config.build_app_config(raw)

    assert settings.app_port == 8080

def test_config_validation_fails(monkeypatch):
    monkeypatch.setenv("APP_PORT","Martell")
    with pytest.raises(expected_exception = ValidationError):
        raw = SimpleConfig()
        app.config.build_app_config(raw)


