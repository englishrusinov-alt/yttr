from app.logic import validate_config_key


def test_valid_key_success():
    assert validate_config_key("APP_DATABASE_URL") is True


def test_invalid_key_success():
    assert validate_config_key("lowercased_key") is False
    assert validate_config_key("DATABASE_URL") is False
