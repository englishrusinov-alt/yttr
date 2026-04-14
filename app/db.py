from sqlalchemy.orm import DeclarativeBase, session, sessionmaker

from app.config import get_settings
from app.exceptions import ConfigError
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

def create_db_engine(database_url: str):
    if not database_url:
        raise ConfigError("database_url is required")
    return create_engine(database_url)



def get_session():
    settings = get_settings()
    engine = create_db_engine(settings.database_url)
    SessionLocal = sessionmaker(engine)
    with SessionLocal() as session:
        yield session
