import pytest
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository


def test_create_user(db_session: Session)->None:
    repo = UserRepository(db_session)

    user = repo.create(
        email="created@example.com",
        is_active=True,
    )

    db_session.commit()

    assert user.id is not None
    assert user.email is not None
    assert user.is_active is True

def test_get_user_by_id(db_session: Session)->None:
    repo = UserRepository(db_session)
    user = repo.create(
        email="by-id@example.com",
        is_active=True,
    )
    db_session.commit()

    found = repo.get_by_id(user.id)

    assert found is not None
    assert found.id == user.id
    assert found.email == "by-id@example.com"

def test_get_user_by_email(db_session: Session) -> None:
    repo = UserRepository(db_session)

    user = repo.create(
        email="by-email@example.com",
        is_active=True,
    )
    db_session.commit()

    found = repo.get_by_email("by-email@example.com")

    assert found is not None
    assert found.id == user.id
    assert found.email == "by-email@example.com"

def test_get_by_id_returns_none_for_missing_user(db_session: Session) -> None:
    repo = UserRepository(db_session)

    found = repo.get_by_id(999999)

    assert found is None

def test_get_by_email_returns_none_for_missing_user(db_session: Session) -> None:
    repo = UserRepository(db_session)

    found = repo.get_by_email("missing@example.com")

    assert found is None

def test_update_user(db_session: Session) -> None:
    repo = UserRepository(db_session)

    user = repo.create(
        email="old@example.com",
        is_active=True,
    )
    db_session.commit()

    updated = repo.update(
        user,
        email="new@example.com",
        is_active=False,
    )
    db_session.commit()

    assert updated.id == user.id
    assert updated.email == "new@example.com"
    assert updated.is_active is False
def test_update_rejects_unknown_field(db_session: Session) -> None:
    repo = UserRepository(db_session)

    user = repo.create(
        email="safe@example.com",
        is_active=True,
    )
    db_session.commit()

    with pytest.raises(ValueError):
        repo.update(user, password_hash="hack")