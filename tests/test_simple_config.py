import pytest
from pydantic import ValidationError

from app.config import SimpleConfig


def test_get_settings_success(monkeypatch):
    # Этап 1: Подменяем переменные окружения (monkeypatch.setenv)
    # Нам нужно замокать ВСЕ обязательные поля, чтобы класс собрался.
    # ВАЖНО: monkeypatch работает со строками, поэтому порт передаем как "8080"
    monkeypatch.setenv(
        "DATABASE_URL", "postgres://test_user:test_pass@localhost:5432/test_db"
    )
    monkeypatch.setenv("APP_PORT", "8080")
    monkeypatch.setenv("SECRET_KEY", "change_this_in_production")
    # Этап 2: Инстанцируем класс конфигурации.
    # Прямо сейчас он прочитает замоканные переменные из monkeypatch!
    settings = SimpleConfig()

    # Этап 3: Проверяем (assert), что загрузилось то, что мы передали
    assert (
            settings.database_url == "postgres://test_user:test_pass@localhost:5432/test_db"
    )
    # Pydantic сам должен был привести "8080" к числу 8080
    assert settings.app_port == 8080


def test_get_settings_fail_missing_required_url(monkeypatch):
    # Этап 1: Специально УДАЛЯЕМ обязательную переменную из окружения
    monkeypatch.delenv("DATABASE_URL", raising=False)

    # Этап 2: Проверяем, что при попытке создать конфиг будет выброшена ошибка ValidationError
    with pytest.raises(ValidationError):
        SimpleConfig()


def test_config_validation_fails(monkeypatch):
    monkeypatch.setenv("APP_PORT","Martell")
    monkeypatch.setenv("DATABASE_URL", "postgres://test") # заглушка, чтобы не упало из-за отсутствия базы
    monkeypatch.setenv("SECRET_KEY", "change_this_in_production")
    with pytest.raises(expected_exception = ValidationError):
        SimpleConfig()


