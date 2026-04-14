import subprocess


def test_alembic_upgrade_head_success():
    result = subprocess.run(
        ["poetry", "run", "alembic", "upgrade", "head"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0


import subprocess


def test_alembic_upgrade_head_failure_with_bad_db_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://bad:bad@localhost:5433/bad_db")

    result = subprocess.run(
        ["poetry", "run", "alembic", "upgrade", "head"],
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0