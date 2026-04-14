import pytest
from sqlalchemy.engine import Engine

from app.config import SimpleConfig, build_database_config
from app.db import create_db_engine
from app.exceptions import ConfigError


def test_create_db_engine_success():
    raw = SimpleConfig(app_port=8080, database_url=
    "postgresql+psycopg://user:pass@localhost:5432/mydb", secret_key=
                       "change_this_in_production"
                       )

    engine  = create_db_engine(raw.database_url)

    assert isinstance(engine, Engine)
    assert engine.url.drivername == "postgresql+psycopg"
    assert engine.url.host == "localhost"
    assert engine.url.port == 5432
    assert engine.url.database == "mydb"

def test_create_db_engine_failure():
    with pytest.raises(ConfigError):
        create_db_engine("")
