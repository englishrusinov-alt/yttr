import pytest
from sqlalchemy.orm import Session

from app.repositories.lesson_repository import LessonRepository
from app.repositories.track_repository import TrackRepository


def test_create_lesson(db_session: Session)->None:
    track_repo = TrackRepository(db_session)
    track = track_repo.create(
        title="Python",
        description="Python track",
    )
    db_session.commit()
    lesson_repo = LessonRepository(db_session)

    lesson = lesson_repo.create(
        track_id=track.id,
        title="Python loops basics",
        content="Use while , for loops and solve problem",
    )

    db_session.commit()

    assert lesson.id is not None
    assert lesson.track_id == track.id
    assert lesson.title is not None
    assert lesson.content is not None
    assert lesson.sort_order == 0
    assert lesson.is_published == False

def test_get_lesson_by_id(db_session: Session)->None:
    track_repo = TrackRepository(db_session)
    track = track_repo.create(
        title="Python",
        description="Python track",
    )
    db_session.commit()
    repo = LessonRepository(db_session)
    lesson = repo.create(
        track_id=track.id,
        title="Python",
        content="Use while , for loops and solve problem",
    )
    db_session.commit()

    found = repo.get_by_id(lesson.id)

    assert found is not None
    assert found.id == lesson.id
    assert found.track_id == lesson.track_id
    assert found.title == "Python"
    assert found.content == "Use while , for loops and solve problem"


def test_get_lesson_by_title(db_session: Session) -> None:
    track_repo = TrackRepository(db_session)
    track = track_repo.create(
        title="Python",
        description="Python track",
    )
    db_session.commit()
    repo = LessonRepository(db_session)

    lesson = repo.create(
        track_id=track.id,
        title="Python",
        content="Use while , for loops and solve problem",
    )
    db_session.commit()

    found = repo.get_by_title("Python")

    assert found is not None
    assert found.id == lesson.id
    assert found.track_id == lesson.track_id
    assert found.title == "Python"

def test_get_by_id_returns_none_for_missing_lesson(db_session: Session) -> None:
    repo = LessonRepository(db_session)

    found = repo.get_by_id(999999)

    assert found is None

def test_get_by_title_returns_none_for_missing_lesson(db_session: Session) -> None:
    repo = LessonRepository(db_session)

    found = repo.get_by_title("Data Science ")

    assert found is None

def test_update_lesson(db_session: Session) -> None:
    track_repo = TrackRepository(db_session)
    track = track_repo.create(
        title="Python",
        description="Python track",
    )
    db_session.commit()
    repo = LessonRepository(db_session)

    lesson = repo.create(
        track_id=track.id,
        title="Python",
        content="Use while , for loops and solve problem",
    )
    db_session.commit()

    updated = repo.update(
        lesson,
        title="Java",
        content="Use only one loop and dividing symbol",
    )
    db_session.commit()

    assert updated.id == lesson.id
    assert updated.title == "Java"
    assert updated.content == "Use only one loop and dividing symbol"
def test_update_rejects_unknown_field(db_session: Session) -> None:

    track_repo = TrackRepository(db_session)
    track = track_repo.create(
        title="Python",
        description="Python track",
    )
    db_session.commit()
    lesson_repo = LessonRepository(db_session)

    lesson = lesson_repo.create(
        track_id=track.id,
        title="Python loops basics",
        content="Use while , for loops and solve problem",
    )

    db_session.commit()

    with pytest.raises(ValueError):
        lesson_repo.update(lesson, password_hash="hack")