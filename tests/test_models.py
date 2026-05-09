from app.models import User


def test_user_model_defaults():
    user = User(email="test@example.com")
    assert user.email == "test@example.com"


def test_user_email_column_unique():
    assert User.__table__.c.email.unique is True


def test_user_email_column_not_nullable():
    assert User.__table__.c.email.nullable is False

def test_user_track_sort_order_column_not_nullable():
    assert User.__table__.c.track_sort_order.nullable is False

def test_user_lesson_track_id_column_not_nullable():
    assert User.__table__.c.lesson_track_id.nullable is False
