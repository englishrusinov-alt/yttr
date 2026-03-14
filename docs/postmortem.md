T000:
WELL:
1. I created app-skeleton via terminal , in existing directory , called as "YTTT"
1.1. I added new files , __init__.py , logic.py and test_logic.py to both directories app and tests, added requirements.txt, called venv and
    installation of required libraries , including alembic, sql alchemy, pytest
1.2. I wrote a code with logic of improvised cheking of APP_directory and called function
     in the test_logic.py , where had implemented both negative and positive scenarios for the test

STRUGGLE:
1. I did'nt know how to build app skeleton , thought that it migth be with special settings ,
   but had no idea of the realisation
2. I had used command for activating venv via terminal , source /venv/bin/activate , correct version was with point before venv as a local dir
3. I didn't know what to write in .py files created before , because have no idea about content of such files


correct version::
T000:
WELL:
1. I created app-skeleton via terminal in existing directory called "YTTT".
1.1. I added new files: `__init__.py`, `logic.py` and `test_logic.py` to both directories `app` and `tests`, added `requirements.txt`, created venv and installed required libraries (alembic, sqlalchemy, pytest).
1.2. I successfully wrote a code with logic for improvised checking of APP_directory. I called the function in `test_logic.py`, where I implemented both negative and positive scenarios for the test.

STRUGGLE:

1. Fact: I didn't know how to build the app skeleton and thought it required special hidden settings, feeling lost in the realization.
   Taxonomy: [12. Operational blindness]
   Why: I lacked a clear mental model of a standard Python backend project structure (what goes into `app`, `tests`, `core`, etc.). I was guessing rather than acting on a schema.
   Rule for next time: Before creating any files, I will explicitly draw or write down the target directory tree on paper or in a comment to separate configuration from business logic conceptually.

2. Fact: I failed to activate the virtual environment because I typed `source /venv/bin/activate` instead of the local path without the leading slash.
   Taxonomy: [1. Syntax or API memory error]
   Why: I confused absolute pathing (starting from system root `/`) with relative pathing (starting from the current directory `./` or just `venv/`) in the Unix shell.
   Rule for next time: I will consciously pause and check if I am referencing the system root (`/`) or the current working directory before hitting enter on shell commands.

3. Fact: I created `.py` files (`logic.py`, etc.) but didn't know what to write inside them because I had no idea about their expected content.
   Taxonomy: [2. Modeling error], [11. Testing blindness]
   Why: I created files without a clear objective function or data contract. I was going through the mechanical motions of "making a project" without having a specific slice of behavior to implement.
   Rule for next time: I will never create a logic file empty just to have it. I will write a failing test first (TDD approach), which will dictate exactly what function signature and behavior needs to be written in the logic file.


T001:

WELL:
1) Скачал poetry через команду curl -sSL https://install.python-poetry.org | python3 -
1.2) Следовал инструкциям после скачивания , добавив переменную export PATH ="/home/$USER/.local/bin:$PATH"
1.3) Инициализировал poetry в проекте  через poetry init ,с оздал pyproject.toml , импортировал
     из requirements.txt конфу  cat requirements.txt | xargs poetry add , сделал poetry install
2) Создал в scripts setup.sh , где при запуске переходя в корень запускается сперва
   logic.py , потом уже test_logic, первый через poetry run python3 app/logic.py
   второй через poetry run pytest tests/

3) STRUGGLE:

[BAD] 1) Не знал с чего начать    
[BAD]    Taxonomy: [Modeling error]
[BAD]    Why: Потому что не смог понять смысл требований ,
[BAD]    думая что достаточно requirements переинициализировать
[BAD]    Rule for next time: Раз там указано два варианта библиотек,одна из которых новая для проекта -
[BAD]    эффективней узнать про нее прежде чем делать выводы

[GOOD] 1) Fact: Не знал с чего начать, потому что не понял требования и пытался просто пересоздать requirements.txt без настройки окружения.
[GOOD]    Taxonomy: [12. Operational blindness]
[GOOD]    Why: Я не понял разницу между зависимостями (requirements) и исполняемой сборкой (reproducible setup command).
[GOOD]    Rule for next time: Если в ТЗ есть неизвестный термин или инструмент (Poetry), я не буду угадывать его смысл, а открою официальный 'Getting Started' или введу команду `--help` перед написанием кода.

---

[BAD] 1.2) Не знал как установить poetry в свой проект
[BAD]    Taxonomy: [Modeling error]
[BAD]    Why: Не знаю специфику установки poetry
[BAD]    Rule for next time: найти информаицю про типичные кейсы установки 

[GOOD] 1.2) Fact: Не знал, как правильно установить poetry, и застрял на базовом сетапе инструмента.
[GOOD]    Taxonomy: [19. Linux shell and process mental model]
[GOOD]    Why: Слабо владею привычкой устанавливать CLI-утилиты через официальные изолированные скрипты (`curl ... | sh`), пытался применять опыт стандартного системного пакетирования.
[GOOD]    Rule for next time: При интеграции нового инструмента я буду всегда искать официальный Installation Path (скрипт установки), а не слепо использовать `apt` или `pip` на системном уровне.

---

[BAD] 1.3) Ошибки сборки poetry rrooak-Aspire-A315-59:~/Documents/YTTER$ poetry install
[BAD] Installing dependencies from lock file
[BAD] 
[BAD] No dependencies to install or update
[BAD] 
[BAD] Installing the current project: ytter (0.1.0)
[BAD] Error: The current project could not be installed: No file/folder found for package ytter
[BAD]    Taxonomy: [Syntax error]
[BAD]    Why: Надо было ограничить сборку проекта , поставив свойство [tool.poetry]
[BAD] package-mode = false
[BAD]    Rule for next time: ограничивать сборку всего проекта , если не намерен пушать в PyP как библиотеку

[GOOD] 1.3) Fact: Poetry упал с ошибкой `No file/folder found for package ytter` при попытке сделать `poetry install`.
[GOOD]    Taxonomy: [12. Operational blindness]
[GOOD]    Why: Я не знал, что Poetry по умолчанию пытается собрать саму директорию проекта как переиспользуемую python-библиотеку для публикации в PyPI, а не просто ставит зависимости.
[GOOD]    Rule for next time: Я буду явно отключать режим сборки (`package-mode = false` в `pyproject.toml`), если создаю внутреннее backend-приложение (API), а не публичную библиотеку.

---

[BAD] 2) Ошибки при создании setup.sh: отсутствие перехода в корень и ненахождение venv из - за этого ,
[BAD]    Неправильная команда запуска poetry poetry run python main.py  для тестов,для них есть коробочное решение
[BAD]    poetry run pytest tests/ 
[BAD]    Taxonomy: [Syntax error]
[BAD]    Why: был невнимателен к запуску скрипта не из под корня , плюс не знал про фичу pytest
[BAD]    Rule for next time: проверять с корня ли я запускаю скрипты , также использовать коробчные инстурменты если атковые есть и
[BAD]    использование их обосновано

[GOOD] 2) Fact: Скрипт `setup.sh` падал, потому что не находил окружение из папки `scripts/`. Также тесты падали из-за `ModuleNotFoundError` при попытке запустить их через `python tests/test_logic.py`.
[GOOD]    Taxonomy: [19. Linux shell and process mental model], [40. Generalization across stacks]
[GOOD]    Why: 1) У меня отсутствовала мышечная память на проверку текущей директории перед выполнением команд (`cd ..`); 2) Я не понимал, как Python разрешает пути модулей (PYTHONPATH), и пытался запустить тесты напрямую, а не через специальный раннер `pytest`.
[GOOD]    Rule for next time: 1) В начале любого bash-скрипта я буду прописывать жесткий переход в нужную рабочую директорию (корень). 2) Тесты всегда будут запускаться только через `pytest` (в моем случае `poetry run pytest`), а не прямым вызовом файла интерпретатором.
