from app.models import User


def test_user_model_defaults():
    user = User(email="test@example.com")
    assert user.email == "test@example.com"


def test_user_email_column_unique():
    assert User.__table__.c.email.unique is True


def test_user_email_column_not_nullable():
    assert User.__table__.c.email.nullable is False