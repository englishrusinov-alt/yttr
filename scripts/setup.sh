cd /home/qarrooak/Documents/YTTER/
export TEST_DATABASE_URL="postgresql+psycopg://user:password@localhost:5433/ytter_test_db"
poetry run python3 app/logic.py
poetry run pytest tests/