import pytest
from sqlalchemy.orm import Session

from app.repositories.track_repository import TrackRepository


def test_create_track(db_session: Session)->None:
    repo = TrackRepository(db_session)

    track = repo.create(
        title="Python loops basics",
        description="Use while , for loops and solve problem",
    )

    db_session.commit()

    assert track.id is not None
    assert track.title == "Python loops basics"
    assert track.description == "Use while , for loops and solve problem"
    assert track.sort_order == 0
    assert track.is_published == False

def test_get_track_by_id(db_session: Session)->None:
    repo = TrackRepository(db_session)
    track = repo.create(
        title="Python",
        description="Use while , for loops and solve problem",
    )
    db_session.commit()

    found = repo.get_by_id(track.id)

    assert found is not None
    assert found.id == track.id
    assert found.title == "Python"
    assert found.description == "Use while , for loops and solve problem"


def test_get_track_by_title(db_session: Session) -> None:
    repo = TrackRepository(db_session)

    track = repo.create(
        title="Python",
        description="Use while , for loops and solve problem",
    )
    db_session.commit()

    found = repo.get_by_title("Python")

    assert found is not None
    assert found.id == track.id
    assert found.title == "Python"

def test_get_by_id_returns_none_for_missing_track(db_session: Session) -> None:
    repo = TrackRepository(db_session)

    found = repo.get_by_id(999999)

    assert found is None

def test_get_by_title_returns_none_for_missing_track(db_session: Session) -> None:
    repo = TrackRepository(db_session)

    found = repo.get_by_title("Data Science ")

    assert found is None

def test_update_track(db_session: Session) -> None:
    repo = TrackRepository(db_session)

    track = repo.create(
        title="Python",
        description="Use while , for loops and solve problem",
    )
    db_session.commit()

    updated = repo.update(
        track,
        title="Java",
        description="Use only one loop and dividing symbol",
    )
    db_session.commit()

    assert updated.id == track.id
    assert updated.title == "Java"
    assert updated.description == "Use only one loop and dividing symbol"
def test_update_rejects_unknown_field(db_session: Session) -> None:
    repo = TrackRepository(db_session)

    track = repo.create(
        title="Python",
        description="Use while , for loops and solve problem",
    )
    db_session.commit()

    with pytest.raises(ValueError):
        repo.update(track, password_hash="hack")