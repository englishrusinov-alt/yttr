# YTTER: Backend Framework

Проект на базе [antifragile спецификации](docs/antifragile_python_backend_master_prompt_2026_v2_ru.md).  
Цель: прокачка hardcore-навыков Python Backend Engineering (FastAPI, SQLAlchemy, Alembic, Docker) через deliberate practice.

---

## 🛠 Зависимости (Prerequisites)
- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/) (Пакетный менеджер)
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/) (Для инфраструктуры)

---

## 🚀 Быстрый старт (Local Development)

1. **Клонируем репозиторий и переходим в папку:**
   ```bash
   git clone <your-repo-url> ytter
   cd ytter
   ```

2. **Создаем локальную конфигурацию:**
   ```bash
   cp .env.example .env
   ```

3. **Устанавливаем зависимости Python:**
   ```bash
   poetry install
   ```

4. **Поднимаем инфраструктуру (База данных):**
   ```bash
   docker compose up -d db
   ```

5. **Запускаем приложение (Development Mode):**
   ```bash
   poetry run fastapi dev app/main.py
   # Или через скрипт:
   # ./scripts/setup.sh
   ```

---

## 🧪 Разработка и тестирование (Commands)

Все команды выполняются через `poetry run`, чтобы гарантировать изоляцию окружения.

- **Запуск тестов:**
  ```bash
  poetry run pytest
  ```

- **Проверка синтаксиса и стиля (Linting):**
  ```bash
  poetry run ruff check .
  ```

- **Автоформатирование кода:**
  ```bash
  poetry run ruff format .
  ```

---

## 🐳 Запуск всего стека в Docker (Production-like)
Если нужно поднять приложение и базу в изолированных контейнерах:
```bash
cp .env.example .env
docker compose up --build
```
