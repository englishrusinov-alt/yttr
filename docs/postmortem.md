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



T003:

WELL:
1) Создал .env.example , заполнил "рыбой" , APP_ENV=local и т.д
2) Через poetry скачал pydantic_settings , как лоадер конфы
3) Создал config.py в app , отнаследовал свой класс SimpleConfig от
   BaseSettings , SettingsConfigDict 
4) Создал test_config.py , где через monkeypatch проставлял конфиги APP_PORT И DATABASE_URL НА валидное,
   , сравнивал с целевыми через assert , и failed тест , где удалаял DATABASE_URL , где после запуска с poetry tests все упало


STRUGGLE:
1) Fact: Не знал как создать `.env.example`, чем его заполнить и зачем он вообще нужен.
   Taxonomy: [12. Operational blindness]
   Why: У меня отсутствовала ментальная модель разделения кода (зафиксированного в Git) и конфигурации окружения (которая меняется от сервера к серверу).
   Rule for next time: Если я встречаю неизвестный концептуальный артефакт (например, `.env.example`), я сначала прочитаю про паттерн "12-factor app (Config)", чтобы понять *почему* он существует, прежде чем механически создавать файл.

2) Fact: При создании `SimpleConfig` я импортировал `BaseConfig` из старой `pydantic.v1`, что привело к синтаксическим ошибкам.
   Taxonomy: [25. Dependency judgment], [1. Syntax or API memory error]
   Why: Я скопировал устаревший кусок кода из интернета или по памяти, не проверив актуальную версию библиотеки (Pydantic v2 использует модуль `pydantic-settings`).
   Rule for next time: При добавлении новой зависимости я всегда буду открывать официальную документацию для последней версии, чтобы скопировать актуальный "Hello World" пример импорта, а не доверять случайным старым статьям.

3) Fact: Я не знал, как написать тесты на получение `settings`, потому что модификация `os.environ` внутри теста не давала эффекта.
   Taxonomy: [11. Testing blindness], [5. State management error]
   Why: Я не понимал, что модуль `config` выполняется ровно один раз при импорте, и объект `settings` "замораживает" состояние окружения до начала выполнения самих тестов.
   Rule for next time: При тестировании конфигурации или состояния окружения я никогда не буду импортировать готовый синглтон (`settings`). Я буду импортировать сам класс (`SimpleConfig`), подменять переменные через инструмент `monkeypatch`, и *заново собирать объект* внутри теста.

T003:

WELL:
1) Добавил в poetry fastapi
2) Создал файл health.py , создал гет эндпоинт по url /health, прежде
   подняв app через .FastAPI()
3) Создал тест , который проверяет два кейса ,
   один сравнивает код ответа с успешным 200, другой - делает POST вместо get как failure scenario


STRUGGLE:
1) Fact: Я забыл добавить fastapi перед импортом и не добавил библиотеку через poetry.
   Taxonomy: [25. Dependency judgment]
   Why: Я положился на встроенную функцию автоимпорта в PyCharm (магическое поведение IDE) вместо осознанного управления окружением.
   Rule for next time: Любая новая зависимость в коде должна начинаться с команды `poetry add <packagename>`, а не с автоимпорта IDE. Контроль окружения важнее скорости написания одной строки.

2) Fact: Я не смог написать тест, потому что вызывал `health.health()` как простую функцию, а не тестировал HTTP-поведение приложения.
   Taxonomy: [11. Testing blindness], [4. Boundary and validation error]
   Why: У меня отсутствовала ментальная модель того, что FastAPI эндпоинт — это HTTP-контракт, а не просто функция. Я не проверял роутинг, статус-коды и методы.
   Rule for next time: При тестировании HTTP-эндпоинта, я не буду вызывать функцию напрямую. Я всегда буду использовать `TestClient` и проверять как минимум две вещи: ожидаемый статус-код ответа и структуру (schema) тела ответа.

3) Fact: Мой негативный тест состоял из POST-запроса, но я проверял, что он возвращает статус 200 (ok).
   Taxonomy: [11. Testing blindness]
   Why: Я скопировал позитивный тест и забыл инвертировать ожидаемое поведение (Method Not Allowed).
   Rule for next time: При написании негативного теста я буду явно формулировать: "Какое поведение системы я ожидаю при неправильном использовании?" и проверять именно ошибку (4xx/5xx).

4) Fact: Я изначально проигнорировал создание `lifespan` для тестирования или логирования старта.
   Taxonomy: [12. Operational blindness]
   Why: Я не знал о механизме разделения жизненного цикла (startup/shutdown) от обработки самих HTTP-запросов и не учел требование "startup logging".
   Rule for next time: Любое серьезное приложение должно иметь явные границы старта и завершения. При инициализации сервера я буду всегда прокидывать и логировать `lifespan` (или его аналог), даже если он пока пустой, чтобы зафиксировать границу запуска.


T004:

WELL:
1) Создал Dockerfile , написал команды инициализации poetry и запуска
   сервера через команду unvicorn на порт 8000
2) Создал docker-compose.yml , где поднял постгрес , дефолт логин пароль на 5432
   плюс сбилдил апп + постгрес как зависимость

STRUGGLE:
1) Fact: Я написал `Dockerfile` с синтаксическими ошибками, попытавшись объединить `RUN` и следующую команду `COPY` в один слой через `\`.
   Taxonomy: [12. Operational blindness], [1. Syntax or API memory error]
   Why: Я пытался писать Docker-инструкции как обычный bash-скрипт, не понимая, что в Dockerfile каждое ключевое слово (RUN, COPY, CMD) — это отдельная инструкция, и их нельзя склеивать символом экранирования `\`.
   Rule for next time: При написании Dockerfile я буду помнить, что каждое слово заглавными буквами (RUN, COPY, CMD) начинает новый независимый слой. Символ `\` используется только для переноса длинной bash-команды внутри одной инструкции `RUN`.

2) Fact: В `docker-compose.yml` я сделал значение `DATABASE_URL` вложенным ключом, сломав контракты отступов YAML.
   Taxonomy: [10. Serialization or contract error]
   Why: Я не воспринимал YAML как строгую структуру данных (словарь/мапу), относясь к нему просто как к тексту с произвольными пробелами.
   Rule for next time: Работая с YAML, я буду мысленно мапить отступы в JSON-объекты. Ключ и значение (если это строка) должны быть на одном уровне через пробел после двоеточия.

3) Fact: Команда `sudo docker compose up` падала, потому что у меня была установлена старая версия `docker-compose` (v1) вместо плагина `docker compose` (v2).
   Taxonomy: [19. Linux shell and process mental model]
   Why: Я скопировал команду из туториала/подсказки, не проверив реальное окружение и версию CLI-инструмента на своей Ubuntu.
   Rule for next time: Если базовая команда CLI-утилиты падает с ошибкой "unknown command", мой первый шаг (Block B: Orient) — запуск `<инструмент> --help` или `<инструмент> --version` для проверки того, что именно установлено в моей системе.

T005:

WELL:
1) установил structlog в poetry
2) создал новый файл app/main.py , туда обернул запрос request с uuidv4 , чтобы логи с id шли
3) создал тестовый файл test_dashboard, где проверяю наличие этого ключа


STRUGGLE:
1) Fact: не знал как использовать structlog , зачем он нужен
   Taxonomy: [19. Lack of mental model]
   Why: не знал , что запросы на продах оборачиваются логами для аудита логов
   Rule for next time: Я никогда не буду запускать веб-приложение в продакшене без внедрения Request ID Middleware. Без уникального идентификатора, привязанного к контексту логгера (structlog), отладка конкурентных запросов превращается в слепое угадывание.

T006:

WELL:
1) добавил ruff в poetry
2) запустил ruff check , и он покзаал unused parts of code и т.д
2.1) Добавил конфиг для ruff с flake и syntax checks
3) Проверил и отформатировал через ruff check + ruff format все .py файлы
STRUGGLE:
1) Fact: не знал как использовать ruff , зачем он нужен
   Taxonomy: [19. Lack of mental model]
   Why: не знал , что ruff чекает синтаксис питонских кодов 
   Rule for next time: юзать ruff для быстрой проверки синтакса , в порядке ли .py
2) Fact: неправильно сконфигурировал ruff и запустил
Taxonomy: [19. Lack of mental model]
 Why: не знал , ruff проверяет не только синтакс,но и pyflake , то есть логику и производительность,если указывать в конфе
   Rule for next time: юзать ruff повседневно to prevent issues
   \n\nT007:\n\nWELL:\n1) Услышал критику, понял разницу в подаче мыслей "от себя" и "для оператора системы".\n\nSTRUGGLE:\n1) Fact: Я забыл указать базовые шаги клонирования и создания .env-конфигурации.\n   Taxonomy: [12. Operational blindness], [15. Curse of knowledge]\n   Why: "Проклятие знания" — раз я уже склонировал репозиторий и создал лог-файл, мой мозг воспринимал это как дефолтное состояние мира. Я не мог посмотреть на проект "пустыми глазами" нового сотрудника (или сервера CI/CD).\n   Rule for next time: При написании README или любой инструкции запуска, я буду мысленно или физически удалять папку проекта и проходить путь с \$HOME, фиксируя каждую bash-команду.
