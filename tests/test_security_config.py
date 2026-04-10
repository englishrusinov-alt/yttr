import pytest
from pydantic import ValidationError

import app.config
from app.config import SecurityConfig
from app.config import SimpleConfig

def test_get_settings_success(monkeypatch):
    # Этап 1: Подменяем переменные окружения (monkeypatch.setenv)
    # Нам нужно замокать ВСЕ обязательные поля, чтобы класс собрался.
    # ВАЖНО: monkeypatch работает со строками, поэтому порт передаем как "8080"

    raw = SimpleConfig(app_port=8080, database_url=
    "postgresql://user:pass@localhost:5432/mydb", secret_key=
                       "change_this_in_production"
                       )

    settings = app.config.build_security_config(raw)

    # Этап 3: Проверяем (assert), что загрузилось то, что мы передали
    # Pydantic сам должен был привести "8080" к числу 8080
    assert (
            settings.secret_key == "change_this_in_production"
    )


def test_get_settings_fail_missing_required_url(monkeypatch):
    # Этап 1: Специально УДАЛЯЕМ обязательную переменную из окружения
    monkeypatch.delenv("SECRET_KEY", raising=False)

    # Этап 2: Проверяем, что при попытке создать конфиг будет выброшена ошибка ValidationError
    with pytest.raises(ValidationError):
        raw = SimpleConfig()
        app.config.build_security_config(raw)





