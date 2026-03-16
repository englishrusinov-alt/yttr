def validate_config_key(key: str) -> bool:
    return key.startswith("APP_") and key.isupper()
