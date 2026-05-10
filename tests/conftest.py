import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from app.db import Base


@pytest.fixture(scope="session")
def test_database_url()->str:
    database_url = os.getenv("TEST_DATABASE_URL")

    if not database_url:
        pytest.fail()
    if "test" not in database_url:
        raise RuntimeError(
            "Refusing to run tests against a non-test database. "
        )
    return database_url
@pytest.fixture(scope="session")
def engine(test_database_url:str):
    engine = create_engine(test_database_url)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield engine

    Base.metadata.drop_all(engine)
    engine.dispose()

@pytest.fixture()
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()

    session = Session(
        bind=connection,
        join_transaction_mode="create_savepoint"
    )
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
        