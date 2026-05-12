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

T010:

WELL:
1) Изменил файл config.py , добавив поля APP_ENV и APP_PORT
2) Создал тест test_config_validation_fails(monkeypatch): ,
   где изменил значение порта на строку , pydantic поругал

[BAD] 2) Fact: Закоммитил инструкцию `cp .env.example .env` в README, но сам `.env.example` содержал неправильные поля (`PORT` вместо `APP_PORT`).
[BAD]    Taxonomy: [2. Modeling error], [10. Serialization or contract error]
[BAD]    Why: забыл о контракте
[BAD]    Rule for next time: проверять конфиги на контракты всегда перед разработкой

[BAD] 3) Fact: Оставил глобальную инициализацию `settings = SimpleConfig()` на уровне модуля, что роняло сборку тестов `pytest` еще до их запуска из-за отсутствия переменных окружения.
[BAD]    Taxonomy: [5. State management error], [11. Testing blindness]
[BAD]    Why: не знал что там синглтон ставится
[BAD]    Rule for next time: ставить lru cache где нужно тестить и вызывать с Dependency Injection

[BAD] 4) Fact: Написал незаконченный тест `test_config_validation_fails`, где остановился на `monkeypatch.setenv`, не вызвав сам код и не проверив отлов исключений через `with pytest.raises(ValidationError)`.
[BAD]    Taxonomy: [11. Testing blindness], [15. Ложная уверенность, вызванная отсутствием верификации]
[BAD]    Why: Не знал что надо ловить исключения через with
[BAD]    Rule for next time: юзать with для отлова исключений в тестах

T011
WELL:
Я перестал делать внутренние config-классы наследниками SimpleConfig и перевёл их в отдельные dataclass-структуры: AppConfig, DatabaseConfig, SecurityConfig. Это был правильный сдвиг от “всё читает env” к “есть raw loader и есть внутренние формы данных”.
Я выделил SimpleConfig как единственную точку входа для внешней среды через BaseSettings, а затем добавил builder-функции build_app_config, build_database_config, build_security_config. Это уже соответствует идее transformation raw -> internal shape, а не inheritance.
Я не остановился на happy path и добавил проверки:
success/fail тесты для SimpleConfig,
success-тесты для builder-логики на T011 через заранее собранный SimpleConfig(...).
Это значит, что я уже начал отделять boundary validation от внутреннего mapping-а.
Я дошёл до правильной рабочей модели без готового решения с нуля: SimpleConfig читает env, а внутренние конфиги не читают env напрямую. Для новичкового уровня это важный conceptual breakthrough, а не просто синтаксическая правка.
STRUGGLE:
Fact: Сначала я пытался сделать AppConfig, DatabaseConfig, SecurityConfig наследниками SimpleConfig, как будто внутренние модели — это “подтипы” env-loader’а.
Taxonomy: [2. Modeling error]
Why: Я не различал два слоя: внешний источник конфигурации и внутреннее представление конфигурации в приложении. Мне казалось, что если поля одинаковые, то inheritance “естественен”, хотя по смыслу роли у классов разные.
Evidence: Только после перехода к отдельным dataclass-моделям и builder-функциям структура стала правильной: SimpleConfig остался BaseSettings, а внутренние модели перестали читать env.
Rule for next time: Если один класс читает внешний мир, а другой просто хранит уже нормализованные данные, я сначала проверяю отношение “is-a” против “built-from”. Для boundary-объектов и internal-shape-объектов по умолчанию выбирать transformation, а не inheritance.
Fact: Я несколько раз путал обычные классы с аннотациями, @dataclass и BaseSettings, из-за чего создавал либо пустые оболочки без конструктора, либо классы, которые вели себя не так, как я ожидал.
Taxonomy: [1. Syntax or API memory error], [12. Operational blindness]
Why: У меня не было автоматизма на том, что Python-класс с одними аннотациями — это ещё не полноценная runtime-модель, и что BaseSettings сам по себе уже решает другую задачу, чем dataclass.
Evidence: Builder-функции начали иметь смысл только после того, как внутренние модели стали dataclass’ами с реальными полями, а не пустыми оболочками.
Rule for next time: Перед созданием нового типа явно писать себе роль: “читает env”, “валидирует API payload”, “просто хранит внутренние данные”. Под каждую роль выбирать один инструмент: BaseSettings, BaseModel или @dataclass, а не смешивать их вслепую.
Fact: Я долго держал тесты в старой ментальной модели и пытался инстанцировать AppConfig(), DatabaseConfig(), SecurityConfig() так, будто они сами читают env и валидируют окружение.
Taxonomy: [11. Testing blindness], [2. Modeling error]
Why: Я изменил архитектуру кода, но не перестроил сразу модель тестирования. В голове всё ещё жил старый паттерн: “любой config-класс читает env”.
Evidence: Ошибки TypeError: __init__() missing required positional argument и переход к тестам через raw = SimpleConfig(...) показали, что builder-тесты надо писать на transformation, а env-тесты оставлять только для SimpleConfig.
Rule for next time: После любого архитектурного изменения я отдельно спрашиваю себя: “Что теперь является boundary under test?” Если env читает только один класс, то только он и должен иметь env-driven negative tests.
Fact: Я путал проблемы текущего тикета с красными тестами из других частей проекта и тратил внимание на шум вокруг health и dashboard, хотя они не были частью T011.
Taxonomy: [12. Operational blindness]
Why: Под усталостью я переставал чётко разделять scope тикета и начинал воспринимать “всё красное” как одну проблему.
Evidence: Даже после того как T011 уже встал на правильные рельсы, в сводке оставались unrelated падения, не относящиеся к конфиг-моделям.
Rule for next time: При красном тест-ране я сначала группирую падения по подсистемам: config, health, logging, db. Я не позволяю несвязанным красным тестам диктовать оценку текущего тикета.
Fact: В negative-тестах T011 я всё ещё частично проверял падение SimpleConfig() вместо отдельной логики builder-слоя, поэтому T011 закрыт честно, но не идеально отполирован.
Taxonomy: [11. Testing blindness]
Why: Мне было проще продолжать бить по входному слою, чем придумать действительно отдельный негативный случай именно для transformation-уровня.
Evidence: В текущих T011-тестах success-path уже идёт через SimpleConfig(...) -> build_*, но failure-path по сути ещё завязан на невозможность собрать SimpleConfig().
Rule for next time: Для многошаговой архитектуры я должен иметь хотя бы по одному тесту на каждый слой: boundary validation отдельно, transformation отдельно, consumer usage отдельно.

TO12: 

WELL:

Реализовал utility module с helper-функциями для safe time, UUID и hash.
Добавил success и failure тесты.
Удержал scope маленьким и не начал строить лишние классы.

STRUGGLE:

Fact: Сначала не понимал, как правильно работать с UTC datetime и чем aware datetime отличается от naive.
Taxonomy: [12. Operational blindness]
Why: Не было ментальной модели безопасной работы со временем в Python.
Rule for next time: Для времени сначала проверять, timezone-aware ли объект, и по умолчанию выбирать UTC.
Fact: В тесте на sha256 я написал tuple внутри assert вместо реального сравнения.
Taxonomy: [1. Syntax or API memory error], [11. Testing blindness]
Why: Я знал, что хочу сравнить два значения, но ошибся в форме assert-выражения.
Rule for next time: В каждом assert явно проверять, что там есть булево условие, а не просто набор значений.
Fact: UUID-тест сначала проверял только тип str, а не реальную валидность UUID.
Taxonomy: [11. Testing blindness]
Why: Я проверил поверхностный признак, а не сам контракт helper-функции.
Rule for next time: Для utility-функций проверять не только тип результата, но и семантическую валидность значения.


T014

WELL:

Реализовал helper’ы для санитаризации имени файла и сборки безопасного пути.
Написал success и failure тесты на happy path, path stripping и пустое имя.
Удержал scope тикета маленьким: не полез в upload endpoint, MIME и storage.

STRUGGLE:

Fact: Все 4 теста упали с TypeError: issubclass() arg 1 must be a class.
Taxonomy: [1. Syntax or API memory error]
Why: Я, скорее всего, перепутал issubclass(...) и isinstance(...). В boundary-helper’ах я проверял не класс, а обычное значение вроде строки или Path-объекта.
Rule for next time: Если я валидирую входное значение, по умолчанию сначала думаю про isinstance(value, Type). issubclass использовать только когда у меня реально класс, а не объект.
Fact: Я написал тест с ожиданием конкретной формы очищенного имени файла, но не до конца сверил это с реальной логикой regex-замены.
Taxonomy: [10. Serialization or contract error], [11. Testing blindness]
Why: Я зафиксировал ожидаемый output раньше, чем чётко определил контракт sanitize-функции для символов перед расширением файла.
Rule for next time: Перед тестом на string transformation я сначала выписываю точный контракт преобразования на 2–3 примерах, и только потом фиксирую assert.
Fact: Тикет в целом рабочий по идее, но я всё ещё делаю ошибки на уровне маленьких API-деталей Python.
Taxonomy: [12. Operational blindness]
Why: Паттерн boundary control я уже понял, но инструментальный слой (Path, regex, isinstance/issubclass`) пока не автоматизирован.
Rule for next time: После новой концепции я отдельно добиваю микрослой API-инструментов, чтобы не терять время на мелких runtime-ошибках.


T015

WELL:

Создал собственную иерархию доменных ошибок с базовым DomainError и узкими наследниками для типовых сценариев.
Не оставил exception hierarchy “декоративной”, а реально встроил её в file_utils, где sanitize_upload_filename() поднимает InvalidFilenameError на плохом входе.
Добил тикет до рабочего состояния и проверил его через тесты; финальный test run полностью зелёный.

STRUGGLE:

Fact: Сначала я попытался сделать raise ("filename is empty or invalid"), из-за чего Python упал с TypeError: exceptions must derive from BaseException.
Taxonomy: [1. Syntax or API memory error]
Why: Я смешал “сообщение об ошибке” и “объект исключения”. В голове была идея ошибки, но не был автоматизирован правильный Python-способ её поднятия.
Rule for next time: В Python я всегда поднимаю либо класс исключения, либо его экземпляр, например raise InvalidFilenameError("..."), а не строку.
Fact: Изначально у меня не было уверенной модели, чем Python exception hierarchy отличается от более Java-подобного layer-based exception style.
Taxonomy: [2. Modeling error], [12. Operational blindness]
Why: Я искал аналог DAO/service-style исключений, хотя задача была не про инфраструктурный слой, а про доменные ошибки и error modeling.
Rule for next time: Для Python-сервисов сначала строю исключения вокруг доменного смысла (InvalidFilenameError, EntityNotFoundError), а не вокруг технических слоёв вроде DAO.
Fact: Я закрыл тикет не с первого раза, а через маленький runtime-bug и последующую коррекцию.
Taxonomy: [11. Testing blindness]
Why: Только тесты и реальный прогон показали, что формально “похоже на exception” ещё не значит “это действительно корректно поднимается как исключение”.
Rule for next time: После добавления custom exception я сразу делаю минимальный тест на pytest.raises(...), чтобы проверить не только дизайн класса, но и реальное raise-поведение.

T016

WELL:

Понял, что задача не про json, jq или regex-движок, а про маленькую утилиту, которая берёт сырой dict с filter params и приводит его к нормальной форме. Это правильно совпало с целью тикета: parsing and normalization.
Смог удержать маленький scope: limit, offset, status, sort_order, без ухода в универсальный query engine, ORM-магии и лишнюю архитектуру. Это хороший проход для tiny module.
Использовал уже созданный InvalidFilterError, то есть связал новый тикет с предыдущим и не стал плодить случайные ошибки без общей иерархии.

STRUGGLE:

Fact: Я сначала вообще не мог придумать логику реализации и застрял, потому что в голове задача расплывалась в что-то слишком общее и абстрактное.
Taxonomy: [2. Modeling error], [12. Operational blindness]
Why: Я не увидел минимальную форму задачи и пытался представить “фильтрацию вообще”, а не конкретную нормализацию нескольких параметров.
Rule for next time: Если задача кажется туманной, я сначала сужаю её до 3–4 конкретных полей и пишу, что приходит на вход и что должно выйти на выходе.
Fact: Я пытался думать через regex и общий проход по всем элементам, хотя для limit, offset, status, sort_order это не нужно.
Taxonomy: [12. Operational blindness]
Why: Я инстинктивно искал “техничный” способ решения до того, как построил простую ментальную модель данных.
Rule for next time: Для parsing/normalization задач я сначала проверяю, можно ли решить их через явную логику по полям без regex, и только потом думаю о более общих техниках.
Fact: Я не решил задачу полностью сам с нуля и в итоге переписал предложенное решение после собственной попытки подумать.
Taxonomy: [15. AI-induced false confidence]
Why: Моя самостоятельная попытка упёрлась в отсутствие ментальной модели, и без внешнего каркаса я не мог собрать решение в цельный модуль.
Rule for next time: Если я беру помощь после честной попытки, я должен помечать это как assisted solve, а не как autonomous solve, и потом вернуться к паттерну позже в delayed recall без подсказок.
Fact: Главная трудность была не в синтаксисе Python, а в том, чтобы понять, какие именно boundary rules должны существовать и где давать default, а где бросать InvalidFilterError.
Taxonomy: [4. Boundary and validation error], [2. Modeling error]
Why: Я ещё не автоматизировал паттерн “грязный вход → нормализованный выход → ошибка на плохом значении”.
Rule for next time: Для каждого filter param я отдельно выписываю: тип, default, допустимые значения, и условие, при котором нужно кидать custom exception.

T020

WELL:

Реализовал базовый SQLAlchemy-каркас для работы с БД: дошёл до идеи Base, engine и session management, а не застрял на абстрактной теории ORM. Это соответствует цели тикета: Create the SQLAlchemy base, engine, and session management.
Добавил тест на создание engine и negative case на пустой database_url, то есть не ограничился happy path и реально проверил boundary для DB-конфигурации. Твой конфиг уже содержал database_url как обязательное поле, и ты использовал его как источник для T020.
Правильно встроил современный PostgreSQL driver через psycopg в Poetry-зависимости проекта, а не начал обходить проблему случайными костылями. До этого в pyproject.toml у тебя драйвера Postgres не было.
Главную архитектурную проблему ты в итоге исправил правильно: убрал создание settings/engine/session с верхнего уровня модуля и засунул это внутрь функций, после чего тесты перестали падать на этапе import/test collection. Это был правильный фикс по lifecycle, а не случайное “затыкание” ошибки.

STRUGGLE:

Fact: Я сначала разместил get_settings() и создание engine/session на верхнем уровне app/db.py, из-за чего pytest падал ещё во время импорта модуля с ValidationError на отсутствующие app_port, database_url, secret_key.
Taxonomy: [5. State management error], [12. Operational blindness]
Why: Я не учёл жизненный цикл модуля Python: код на module level выполняется сразу при импорте, а не “позже, когда понадобится”. Из-за этого boundary конфигурации сработал слишком рано.
Rule for next time: Всё, что зависит от окружения, подключения к БД или runtime initialization, я не выношу на top-level без очень явной причины. Сначала спрашиваю: “это definition-time или runtime?”
Fact: Я думал, что проблема может быть “в полях” или в PostgreSQL URL, хотя реальная причина была в import-time side effect внутри db.py.
Taxonomy: [12. Operational blindness]
Why: Я видел красный traceback на SimpleConfig, но сначала не выделил, что он возник не в тестовой логике, а из-за импорта модуля.
Rule for next time: Если ошибка случается в test collection или прямо на import, я первым делом проверяю, какой код выполняется на верхнем уровне модуля.
Fact: Я добавил Postgres driver и URL через postgresql+psycopg://..., но не сразу понимал, нужен ли это временный костыль или нормальный продовый путь.
Taxonomy: [25. Dependency judgment], [12. Operational blindness]
Why: У меня не было устойчивой модели различия между “PostgreSQL как СУБД” и “DBAPI driver как Python-адаптер для SQLAlchemy”.
Rule for next time: Для работы SQLAlchemy с конкретной БД я отдельно проверяю: что является диалектом БД, а что является драйвером Python. Не путать postgresql и psycopg.
Fact: Тест на engine я начал писать без ясного понимания, что именно нужно проверять: реальное подключение, URL, тип engine или поведение драйвера.
Taxonomy: [11. Testing blindness], [12. Operational blindness]
Why: Я ещё не автоматизировал правило, что unit test на create_engine() должен в первую очередь проверять корректную сборку Engine, а не обязательно живую доступность БД.
Rule for next time: Для инфраструктурных factory-функций сначала тестирую shape/contract результата (Engine, URL parts, negative case), а интеграционное подключение отделяю в другой тест.


T021

WELL:

Я реально довёл Alembic wiring до рабочего состояния: initial migration создалась, значит контур alembic -> env.py -> metadata -> database connection у меня в итоге заработал. Это уже не теория, а рабочий артефакт тикета. До этого в шаблоне Alembic у меня был target_metadata = None и фейковый sqlalchemy.url, то есть wiring из коробки не был реально подключён к проекту.
Я разобрался, что Alembic нельзя запускать через системный apt-пакет, а нужно запускать через Poetry из корня проекта, чтобы использовать проектное окружение и зависимости. Это было правильное operational решение, потому что alembic уже был в зависимостях проекта.
Я починил несколько разных слоёв проблем подряд:
сначала config wiring,
потом драйвер и URL,
потом запуск Docker Postgres,
потом .env.
То есть я не бросил тикет на первой operational ошибке, а реально довёл его до результата.
Я на практике понял одну из главных идей schema evolution: миграции живут не сами по себе, а зависят от корректного lifecycle-и окружения — metadata, URL, driver, доступности БД и валидного config source. Это как раз и есть полезная часть T021, а не просто команда alembic revision.

STRUGGLE:

Fact: Изначально Alembic-окружение было только шаблонно и не было реально связано с моим приложением: в alembic/env.py стоял target_metadata = None, а в alembic.ini — заглушечный driver://user:pass@localhost/dbname.
Taxonomy: [3. Schema design error], [12. Operational blindness]
Why: Я ещё не видел, что Alembic нужно не “просто установить”, а реально привязать к Base.metadata и рабочему database URL.
Rule for next time: Когда беру migration tool, я первым делом проверяю две вещи: откуда он берёт metadata и откуда он берёт реальный DB URL.
Fact: Я сначала заставил alembic/env.py тянуть get_settings().database_url, но этим же потянул весь SimpleConfig, из-за чего Alembic падал на обязательных полях конфига, которые вообще не нужны миграциям, включая secret_key. Это видно по ошибке ValidationError на app_port, database_url, secret_key, а потом отдельно на одном secret_key.
Taxonomy: [12. Operational blindness], [5. State management error]
Why: Я связал Alembic со всем приложением слишком сильно. Вместо “Alembic нужен только URL БД” я дал ему зависимость от полного runtime-config приложения.
Rule for next time: Для migration tooling я подключаю только минимально необходимый config, а не весь application settings object.
Fact: После создания реального .env у меня сломались старые negative-тесты на SimpleConfig, потому что BaseSettings начал находить значения из файла, даже когда я удалял env-переменные через monkeypatch.delenv(). Это проявилось в тестах, где ожидался ValidationError, но он больше не происходил.
Taxonomy: [11. Testing blindness], [12. Operational blindness]
Why: Я не учёл, что появление .env меняет модель тестирования BaseSettings: удаление env-переменной уже не гарантирует отсутствие значения.
Rule for next time: Если у BaseSettings есть env_file, negative-тесты я пишу либо с _env_file=None, либо через явную инициализацию с пропущенным полем, а не воюю с внешней средой.
Fact: Я несколько раз упирался в operational ошибки подключения к Postgres:
сначала Alembic лез в 127.0.0.1:5432 и получал password authentication failed,
хотя в compose у меня раньше был проброс 5433:5432,
потом у меня была сломанная строка в .env, из-за которой имя БД склеилось с SECRET_KEY,
только после этого initial migration реально сгенерировалась.
Taxonomy: [12. Operational blindness], [25. Dependency judgment]
Why: Я ещё не автоматизировал различие между:
host-context vs docker-context,
внутренним портом контейнера vs внешним портом хоста,
DB dialect vs DBAPI driver,
корректной .env строкой vs сломанной конфигурацией файла.
Rule for next time: Если инфраструктурная команда падает, я первым делом проверяю 4 вещи: host, port, credentials, формат config-файла — до того, как начинаю подозревать библиотеку.
Fact: Я сначала воспринимал ошибки Alembic как “что-то не так с Alembic”, хотя по факту большая часть проблем была не в самом migration tool, а в lifecycle проекта: settings, Docker, Postgres URL, driver и доступность базы.
Taxonomy: [12. Operational blindness]
Why: У меня ещё не было устойчивой mental model, что migration tool просто обнажает все слабые места project wiring.
Rule for next time: Если migration tool падает, я не обвиняю сразу сам tool; я проверяю весь путь config -> URL -> driver -> DB availability -> metadata.

T022

WELL:

Я реально довёл первую ORM-сущность до рабочего состояния: определил User с нужным смысловым минимумом — email, timestamps и is_active. Это соответствует задаче тикета: Define the User model with timestamps and activation fields.
Я не остановился на одном классе, а дотащил связанный контур до конца: модель загрузилась, тесты прошли, и Alembic autogenerate в итоге увидел новую таблицу users и создал миграцию add user table. Это уже не декоративная модель, а реально включённая в schema evolution сущность.
Я поймал и исправил проблему с duplicate table registration: сначала не понимал, что наследование от Base уже автоматически добавляет модель в Base.metadata, а потом разобрался и убрал ручное дублирование. Это важное понимание ORM lifecycle, а не просто синтаксическая правка.
Я отделил то, что должно тестироваться на уровне Python-объекта, от того, что реально живёт на уровне БД и ORM metadata. Это помогло не требовать от модели того, что SQLAlchemy не обязан делать при простом User(...).

STRUGGLE:

Fact: Я сначала ожидал, что is_active будет сразу True на простом User(email="..."), но в текущем стиле SQLAlchemy ORM объект создавался с None, и тест падал.
Taxonomy: [2. Modeling error], [11. Testing blindness]
Why: Я смешал Python-конструктор объекта и database/ORM defaults. У меня ещё не было устойчивой модели, когда значение появляется сразу в объекте, а когда только при INSERT или flush.
Rule for next time: Для ORM-моделей я отдельно различаю constructor-time behavior и database-time defaults. Если хочу тестировать default, сначала проверяю: это Python-level default или DB/ORM insert-time default?
Fact: Я сначала сделал negative test, который ожидал TypeError на обычном User(email="test@example.com"), хотя это был тот же happy path, и он не должен был падать.
Taxonomy: [11. Testing blindness]
Why: Я ещё не выделил чётко, где у модели реально есть Python-level валидация, а где есть только DB-level constraints вроде nullable=False и unique=True.
Rule for next time: Перед написанием negative test я сначала отвечаю себе: “на каком уровне вообще должен происходить fail — Python object creation, ORM flush, DB commit или constraint inspection?”
Fact: У меня была маленькая, но блокирующая опечатка в поле nullable, из-за которой тесты падали ещё во время импорта модели.
Taxonomy: [1. Syntax or API memory error]
Why: При новой ORM-форме я ещё не автоматизировал точный API mapped_column(), и мелкая ошибка в keyword argument полностью ломала импорт.
Rule for next time: После написания новой ORM-модели я сразу делаю короткий import smoke check или test collection run, чтобы быстро поймать API-level опечатки.
Fact: При попытке сделать миграцию я получил ValueError: Duplicate table keys across multiple MetaData objects: "users", потому что добавил User в metadata отдельно, не понимая, что через наследование от Base он уже регистрируется автоматически. Потом, когда убрал дублирование, Alembic увидел Detected added table 'users' и сгенерировал миграцию.
Taxonomy: [5. State management error], [12. Operational blindness]
Why: Я ещё не до конца понимал, как работает declarative registration и что Base.metadata — единый реестр таблиц, а не место, куда нужно вручную “добавлять” модель после объявления класса.
Rule for next time: Если модель наследуется от Base, я предполагаю, что она уже зарегистрирована в metadata автоматически, и сначала проверяю текущее состояние metadata, прежде чем что-то добавлять руками.
Fact: Мне потребовалось время, чтобы понять, что для T022 negative case можно делать не только через runtime exception, но и через проверку shape/constraint модели, например nullable=False или unique=True, если я ещё не строю полноценный DB insert test.
Taxonomy: [11. Testing blindness], [2. Modeling error]
Why: Я слишком узко понимал negative case как “должно прямо упасть при создании объекта”, хотя у ORM-моделей часть негативных условий выражается через schema contract, а не через конструктор Python-класса.
Rule for next time: Для entity design задач я отдельно выбираю, что именно проверяю: object shape, metadata constraints, migration diff или реальное DB behavior.



T023 Postmortem — модели Track и Lesson + Alembic migration

Что я пытался сделать:
Мне нужно было определить модели Track и Lesson с полями ordering, publish-флагами, timestamps и связью lessons.track_id -> tracks.id.

Что получилось:
Модели Track и Lesson уже были определены в app/models.py.
Alembic autogenerate корректно увидел две новые таблицы: tracks и lessons.
После команды alembic upgrade head таблицы реально появились в PostgreSQL.
Я вручную проверил схему через \dt, \d tracks и \d lessons.
Я также проверил, что lessons.track_id имеет foreign key на tracks.id.

Что пошло не так / где я запутался:
Сначала я попытался создать новую миграцию, когда база данных ещё не была обновлена до последней существующей миграции.
Alembic выдал ошибку: "Target database is not up to date."
Ошибка была в том, что я перепутал существование migration-файлов с реальным состоянием базы данных.

Вторая путаница:
После команды alembic revision --autogenerate я сразу зашёл в PostgreSQL и ожидал увидеть таблицы tracks и lessons.
Но revision --autogenerate только создаёт файл миграции.
Он не применяет миграцию к базе.
Таблицы появились только после команды alembic upgrade head.

Категория ошибки:
Ошибка schema evolution.
Непонимание migration workflow.
Путаница между состоянием кода, состоянием migration-файлов и состоянием реальной базы данных.

Правильная ментальная модель:
SQLAlchemy models описывают желаемую Python-side схему.
Alembic revision --autogenerate создаёт migration-файл на основе изменений в моделях.
Alembic upgrade head применяет migration-файлы к реальной базе данных.
PostgreSQL меняется только после upgrade, а не после revision generation.

Что я проверил:
1. Успешно запустил alembic upgrade head.
2. Проверил таблицы в PostgreSQL через \dt.
3. Убедился, что users, tracks и lessons существуют.
4. Проверил структуру таблиц через \d tracks и \d lessons.
5. Убедился, что lessons.track_id ссылается на tracks.id.
6. Проверил failure case: попытка вставить lesson с несуществующим track_id упала с foreign key error.
7. Проверил happy path: создал track, потом создал lesson, привязанный к этому track.

Правило на следующий раз:
Перед созданием новой autogenerate-миграции всегда проверять, что база догнана до последней миграции:

poetry run alembic current
poetry run alembic heads
poetry run alembic upgrade head

Потом создавать миграцию:

poetry run alembic revision --autogenerate -m "message"

Потом вручную открыть и проверить migration-файл.

Потом применить миграцию:

poetry run alembic upgrade head

Главный урок:
Изменение модели — это ещё не изменение базы.
Изменение базы происходит только после цепочки:
model change -> migration file -> alembic upgrade head.

T023 можно считать закрытым, потому что модели есть, миграция создана, миграция применена, схема проверена, foreign key работает, happy path и failure case проверены.


T024 Postmortem — Task model + migration + schema verification

Что я пытался сделать:
Мне нужно было определить модель Task с типом задачи, сложностью, metadata-полем и связью с Lesson.
Цель T024 была не просто написать модель, а провести полный schema workflow:
model -> migration -> upgrade -> manual DB verification -> failure case -> happy path.

Что получилось:
Я создал модель Task и связал её с Lesson через lesson_id.
Финальная модель Task содержит поля:
- id
- lesson_id
- title
- description
- task_type
- difficulty
- metadata
- sort_order
- is_published
- created_at
- updated_at

Я проверил, что SQLAlchemy правильно видит колонки модели через:

poetry run python -c "from app.models import User, Track, Lesson, Task; print(Task.__table__.columns.keys())"

Ожидаемый результат был получен:

['id', 'lesson_id', 'title', 'description', 'task_type', 'difficulty', 'metadata', 'sort_order', 'is_published', 'created_at', 'updated_at']

После этого я сбросил локальную dev-базу через:

docker compose down -v
docker compose up -d db

Затем создал новую чистую миграцию:

poetry run alembic revision --autogenerate -m "initial schema"

Alembic увидел таблицы:
- tracks
- users
- lessons
- tasks

Потом я применил миграцию:

poetry run alembic upgrade head

В PostgreSQL я проверил таблицы через:

\dt

И увидел:
- alembic_version
- users
- tracks
- lessons
- tasks

Failure case:
Я попытался вставить task с lesson_id, которого не существует:

INSERT INTO tasks (
    lesson_id,
    title,
    description,
    task_type,
    difficulty,
    metadata,
    sort_order,
    is_published
)
VALUES (
    999999,
    'Broken task',
    'Should fail',
    'text',
    3,
    NULL,
    0,
    false
);

Ожидаемо получил ошибку foreign key:

ERROR: insert or update on table "tasks" violates foreign key constraint "tasks_lesson_id_fkey"
DETAIL: Key (lesson_id)=(999999) is not present in table "lessons".

Это подтвердило, что база не разрешает создать task без существующего lesson.

Happy path:
Я создал track:

INSERT INTO tracks (title, description, sort_order, is_published)
VALUES ('Python Backend', 'Main backend track', 0, false)
RETURNING id;

Потом создал lesson, привязанный к этому track:

INSERT INTO lessons (track_id, title, content, sort_order, is_published)
VALUES (1, 'SQLAlchemy models', 'Intro lesson', 0, false)
RETURNING id;

Потом создал task, привязанный к этому lesson:

INSERT INTO tasks (
    lesson_id,
    title,
    description,
    task_type,
    difficulty,
    metadata,
    sort_order,
    is_published
)
VALUES (
    1,
    'Define a SQLAlchemy model',
    'Create model and explain fields.',
    'text',
    3,
    NULL,
    0,
    false
);

Insert прошёл успешно.

Что пошло не так:
Сначала я сделал ошибку в модели Task:
после mapped_column у task_type стояла лишняя запятая.

Из-за этого Python превратил поле task_type в tuple, а SQLAlchemy проигнорировал его как колонку.
Раньше в логе было предупреждение:

SAWarning: Ignoring declarative-like tuple value of attribute 'task_type'

Также у меня была typo в названии поля:

sort_oder

вместо:

sort_order

Из-за этих ошибок Alembic создал неправильную миграцию: таблица tasks появилась без task_type и с неправильной колонкой sort_oder.

Категория ошибки:
Schema modeling error.
Python syntax trap.
Migration workflow error.
Недостаточная проверка autogenerate migration перед применением.

Правильная ментальная модель:
SQLAlchemy видит только корректно объявленные mapped_column поля.
Лишняя запятая после mapped_column превращает колонку в tuple, и ORM её не маппит.
Alembic autogenerate не понимает мои намерения — он просто сравнивает то, что реально видит SQLAlchemy.
Если модель неправильная, Alembic честно создаст неправильную миграцию.

Главный урок:
Перед созданием миграции надо проверять не только код глазами, но и реальный SQLAlchemy mapping:

poetry run python -c "from app.models import Task; print(Task.__table__.columns.keys())"

Если в этом списке нет нужной колонки, миграцию создавать рано.

Ещё один урок:
Миграцию нельзя применять вслепую.
После alembic revision --autogenerate надо открыть migration-файл и проверить:
- правильные имена колонок;
- наличие foreign key;
- отсутствие typo;
- nullable / not nullable;
- порядок создания таблиц.

Что я сделал для исправления:
Так как это локальный dev-проект и данные не были важны, я сбросил dev-базу и пересоздал чистую initial schema миграцию.
Это допустимо в учебной локальной среде.
В production/shared-среде так делать нельзя: там надо было бы писать новую corrective migration вперёд.

Правило на следующий раз:
1. Сначала исправить модель.
2. Проверить SQLAlchemy mapping:

poetry run python -c "from app.models import Task; print(Task.__table__.columns.keys())"

3. Проверить, что база на актуальном head:

poetry run alembic current
poetry run alembic heads
poetry run alembic upgrade head

4. Создать миграцию:

poetry run alembic revision --autogenerate -m "message"

5. Открыть migration-файл глазами.
6. Только потом применить:

poetry run alembic upgrade head

7. Проверить схему в psql.
8. Проверить failure case.
9. Проверить happy path.

T024 считается закрытым, потому что:
- модель Task создана;
- Task связан с Lesson через foreign key;
- task_type есть и сохраняется в базе;
- difficulty есть;
- metadata есть;
- sort_order исправлен;
- миграция создана и применена;
- таблица tasks существует;
- foreign key работает;
- failure case с неправильным lesson_id падает;
- happy path track -> lesson -> task проходит.
T025 Postmortem — модели Attempt и Review + workflow state design

Что я пытался сделать:
Мне нужно было определить модели Attempt и Review.
Цель T025 была не просто создать две таблицы, а смоделировать workflow:
пользователь отправляет попытку решения task, а reviewer потом создаёт review с оценкой и feedback.

Главная доменная модель:
Task -> Attempt -> Review

Attempt = попытка пользователя решить конкретный task.
Review = результат проверки конкретной attempt.

Что получилось:
Я создал таблицы attempts и reviews.
После миграции PostgreSQL показал таблицы:

- users
- tracks
- lessons
- tasks
- attempts
- reviews
- alembic_version

Это подтвердило, что миграция была применена к базе.

Модель Attempt:
- id
- task_id
- user_id
- answer_text
- status
- metadata
- submitted_at
- created_at
- updated_at

Модель Review:
- id
- attempt_id
- reviewer_id
- score
- feedback
- created_at
- updated_at

Почему status не boolean:
Сначала была идея думать через true/false, но для Attempt это плохая модель.
Attempt — это workflow entity, а не простой флаг.

Boolean может выразить только:
true / false

Но попытка может иметь несколько состояний:
submitted
in_review
reviewed
rejected

Поэтому status лучше хранить как controlled string с CheckConstraint, а не как is_reviewed boolean.

Какие constraints нужны и зачем:
ForeignKey на attempts.task_id нужен, чтобы attempt не мог ссылаться на task, которого нет.
ForeignKey на attempts.user_id нужен, чтобы attempt не мог принадлежать несуществующему user.
ForeignKey на reviews.attempt_id нужен, чтобы review не мог ссылаться на attempt, которого нет.
ForeignKey на reviews.reviewer_id нужен, чтобы review не мог быть создан от имени несуществующего reviewer.

UniqueConstraint на reviews.attempt_id нужен не для связи, а для другого инварианта:
один attempt может иметь только один final review.

CheckConstraint на Attempt.status нужен, чтобы база не принимала мусорные статусы вроде done_bro.
CheckConstraint на Review.score нужен, чтобы база не принимала score вне диапазона 0–100.

Что пошло не так:
Сначала в модели Review я снова допустил Python syntax trap:
после mapped_column у id стояла лишняя запятая.

Из-за этого SQLAlchemy воспринял id не как колонку, а как tuple.
Лог показал предупреждение:

SAWarning: Ignoring declarative-like tuple value of attribute 'id'

Потом SQLAlchemy упал с ошибкой:

Mapper Mapper[Review(reviews)] could not assemble any primary key columns for mapped table 'reviews'

Причина:
Review оказался без primary key, потому что id был проигнорирован.

Категория ошибки:
Python syntax trap.
ORM mapping error.
Schema modeling error.
Недостаточная предварительная проверка модели перед Alembic autogenerate.

Как я исправил:
Я убрал лишнюю запятую после mapped_column(primary_key=True).
После этого проверил SQLAlchemy mapping перед миграцией.

Правильная проверка перед Alembic:

poetry run python -c "from app.models import Attempt, Review; print(Attempt.__table__.columns.keys()); print(Review.__table__.columns.keys())"

Главный урок:
Перед созданием миграции нужно проверять, что SQLAlchemy реально видит все колонки.
Если ORM mapping неправильный, Alembic создаст неправильную миграцию или упадёт до её создания.

Что я проверил после миграции:
1. Проверил, что таблицы attempts и reviews появились в PostgreSQL.
2. Проверил failure case: attempt с несуществующим task_id падает по foreign key.
3. Проверил failure case: attempt с несуществующим user_id должен падать по foreign key.
4. Проверил, что invalid status надо тестировать только с валидными task_id и user_id.
5. Проверил happy path: существующий task + существующий user -> attempt.
6. Проверил happy path: существующий attempt + reviewer -> review.
7. Проверил, что если использовать неправильный task_id, база падает раньше, чем доходит до проверки status.

Важная ошибка во время проверки:
Я пытался создать attempt с task_id = 1, но в базе существующий task имел id = 2.

PostgreSQL правильно вернул:

Key (task_id)=(1) is not present in table "tasks".

Это не ошибка модели.
Это означало, что я использовал несуществующий task_id.
После SELECT id, title FROM tasks; я увидел реальный task_id и использовал его.

Правило для проверки failure cases:
Когда я проверяю один конкретный failure case, все остальные поля должны быть валидными.

Например:
Если я проверяю invalid status, то task_id и user_id должны существовать.
Иначе база сначала упадёт по foreign key, и я не проверю status constraint.

Правильная ментальная модель:
ForeignKey защищает существование связанной строки.
UniqueConstraint защищает уникальность бизнес-отношения.
CheckConstraint защищает допустимый диапазон или набор значений.
nullable=False защищает от отсутствия значения, но не защищает от мусорного значения.

Пример:
score INTEGER NOT NULL запрещает NULL, но разрешает 999.
score INTEGER + CheckConstraint(score BETWEEN 0 AND 100) запрещает 999.

Что я должен делать в следующих schema tickets:
1. Сначала вывести инварианты домена.
2. Потом определить поля.
3. Потом решить nullable / not nullable.
4. Потом добавить FK, unique и check constraints.
5. Потом проверить ORM mapping.
6. Потом создать Alembic migration.
7. Потом открыть migration-файл глазами.
8. Потом применить migration.
9. Потом проверить схему в psql.
10. Потом проверить failure cases и happy path.

T025 считается закрытым, потому что:
- Attempt model создан.
- Review model создан.
- attempts и reviews появились в базе.
- Attempt связан с Task и User.
- Review связан с Attempt и reviewer User.
- Workflow status смоделирован не через boolean, а через state.
- Foreign key failure cases проверены.
- Happy path attempt -> review прошёл.
- Ошибка с лишней запятой была найдена, понята и исправлена.

Да, **в идеале это пишется тестами**.

Но сейчас у тебя этап **schema modeling / migration verification**, поэтому ручной SQL — это временный smoke-check:

```text
модель -> миграция -> база реально защищает инварианты
```

Позже, когда дойдёшь до repositories / test fixtures, эти проверки надо перенести в pytest/integration tests. То есть:

```text
Сейчас:
ручной SQL в psql = быстрая проверка схемы

Позже:
pytest + real test DB = автоматическая проверка
```

Строго по DoD: T026 у тебя закрыт по **model/migration/schema/failure cases**, но automated test ещё pending. Это нормально на текущем этапе, но не надо забывать. В backlog acceptance для тикетов действительно требует test/postmortem, так что позже эти SQL checks надо превратить в тесты. 

Копируй postmortem:


T026 Postmortem — Progress and Notification models + derived state design

Что я пытался сделать:
Мне нужно было определить модели Progress и Notification.
Цель T026 была не просто добавить две таблицы, а смоделировать derived state:
Progress хранит вычисляемое состояние пользователя по lesson, а Notification хранит сообщения для пользователя.

Главная доменная модель:
Progress = состояние пользователя по конкретному lesson.
Notification = уведомление, адресованное конкретному user.

Что получилось:
Я создал модели Progress и Notification.
После миграции PostgreSQL показал новые таблицы:
- progress
- notifications

Это подтвердило, что миграция была применена к базе.

Модель Progress:
- id
- user_id
- lesson_id
- status
- completion_percent
- mastery_score
- last_activity_at
- completed_at
- metadata
- created_at
- updated_at

Модель Notification:
- id
- user_id
- kind
- title
- body
- payload
- is_read
- read_at
- created_at
- updated_at

Почему Progress не стал XP/rank/achievements:
Сначала я думал о progress как об XP, rank, achievements и gamification.
Но для T026 правильнее сузить Progress до derived state:
user + lesson -> status / completion_percent / mastery_score.

XP, rank, achievements, streaks и level — это отдельный gamification layer, который надо добавлять позже.
Сейчас Progress должен быть простой материализованной сводкой по прохождению lesson.

Почему Progress связан с Lesson, а не Track:
Progress по Track можно позже посчитать из lesson progress.
Если сразу делать progress по Track, Lesson и Task одновременно, схема станет сложнее раньше времени.
Поэтому на T026 выбран минимальный полезный уровень:
User + Lesson.

Какие constraints были добавлены:
1. UniqueConstraint(user_id, lesson_id)
   Один пользователь не должен иметь две progress-записи на один lesson.

2. CheckConstraint на status:
   status должен быть только одним из:
   not_started
   in_progress
   completed

3. CheckConstraint на completion_percent:
   completion_percent должен быть от 0 до 100.

4. CheckConstraint на mastery_score:
   mastery_score должен быть от 0 до 100.

5. CheckConstraint на notification kind:
   kind должен быть только одним из:
   review_completed
   progress_updated
   system

Почему composite unique, а не отдельные unique:
Сначала можно ошибочно сделать UniqueConstraint только на user_id или только на lesson_id.
Но это неправильно.

Unique(user_id) означал бы:
один user может иметь только одну progress-запись вообще.

Unique(lesson_id) означал бы:
один lesson может иметь только одну progress-запись вообще.

Правильный инвариант:
один user может иметь только один progress на один конкретный lesson.

Поэтому нужен:
UniqueConstraint("user_id", "lesson_id")

Почему completed_at nullable:
completed_at не должен автоматически заполняться при создании progress.
Если progress ещё не completed, completed_at должен быть NULL.
Иначе система будет считать lesson завершённым сразу после создания progress.

Почему Notification.payload сделан JSON:
payload хранит структурированные данные, например:
attempt_id
lesson_id
score

Это не просто текст, поэтому JSON лучше Text.

Что я проверил:
1. Проверил, что таблицы progress и notifications появились через \dt.
2. Проверил структуру progress через \d progress.
3. Проверил структуру notifications через \d notifications.
4. Проверил happy path для progress.
5. Проверил failure case для progress с несуществующим user_id.
6. Проверил failure case для progress с несуществующим lesson_id.
7. Проверил failure case для invalid progress status.
8. Проверил failure case для completion_percent вне диапазона 0–100.
9. Проверил failure case для mastery_score вне диапазона 0–100.
10. Проверил duplicate progress на тот же user_id + lesson_id.
11. Проверил happy path для notification.
12. Проверил failure case для notification с несуществующим user_id.
13. Проверил failure case для invalid notification kind.

Что пошло не так / что было важно понять:
Я сначала думал о Progress слишком широко — как об XP, ranks и achievements.
Но это было бы преждевременное расширение.
Правильное решение для T026 — хранить минимальный derived state по lesson.

Также важно было не спутать разные типы constraints:
ForeignKey защищает существование связанной строки.
UniqueConstraint защищает уникальность бизнес-отношения.
CheckConstraint защищает допустимые значения.
nullable=False защищает от отсутствия значения, но не от мусорного значения.

Категория ошибки / риска:
Derived state design risk.
Premature gamification risk.
Schema constraint modeling risk.
Риск усложнить модель раньше времени.

Правильная ментальная модель:
Progress не является source of truth.
Source of truth — это tasks, attempts и reviews.
Progress — это derived/materialized state, который позже будет обновляться через ProgressService.

Notification тоже пока не workflow engine.
Это простая таблица сообщений для пользователя.
Background jobs, delivery status, retries и notification service будут позже.

Что отложено:
- XP
- rank
- achievements
- streaks
- level system
- ProgressService
- NotificationService
- background jobs
- frontend notification UI
- автоматический recalculation progress
- notification enqueue logic

Test status:
На этом этапе я сделал manual SQL verification через psql.
Это проверило, что база реально применяет foreign keys, unique constraints и check constraints.

Но полноценный automated pytest test ещё не написан.
Позже, когда появятся repository layer и test DB fixtures, эти SQL checks надо перенести в integration tests.

Правило на следующий раз:
1. Сначала понять, является ли таблица source of truth или derived state.
2. Не добавлять gamification раньше времени.
3. Для progress выбирать минимальный уровень агрегации.
4. Для уникальности бизнес-отношений использовать composite unique.
5. Перед миграцией проверять ORM mapping.
6. После миграции проверять \d table.
7. Для каждого constraint делать отдельный failure case.
8. Когда появится test harness, переносить ручные SQL checks в pytest.

T026 считается закрытым по schema/migration/manual verification, потому что:
- Progress model создан.
- Notification model создан.
- progress и notifications появились в базе.
- Progress связан с User и Lesson.
- Notification связан с User.
- Progress имеет status, completion_percent и mastery_score constraints.
- Progress имеет unique constraint на user_id + lesson_id.
- Notification имеет kind constraint.
- Happy paths проверены.
- Failure cases проверены.
- Automated pytest test помечен как pending для repository/test-fixture этапа.


T027 Postmortem — AuditLog and IdempotencyKey models + operational state design

Что я пытался сделать:
Мне нужно было определить модели AuditLog и IdempotencyKey.
Цель T027 была не просто добавить две таблицы, а смоделировать operational state:
AuditLog хранит историю важных действий в системе.
IdempotencyKey защищает систему от повторного выполнения одной и той же операции.

Главная доменная идея:
AuditLog = кто, что, когда сделал и над какой сущностью.
IdempotencyKey = ключ, который не даёт повторному request создать дубликат операции.

Что получилось:
Я создал модели AuditLog и IdempotencyKey.
После миграции PostgreSQL показал новые таблицы:
- audit_logs
- idempotency_keys

Это подтвердило, что миграция была применена к базе.

Модель AuditLog:
- id
- actor_user_id
- action
- entity_type
- entity_id
- metadata
- created_at

Модель IdempotencyKey:
- id
- user_id
- key
- operation
- status
- response_body
- created_at
- updated_at
- expires_at

Почему AuditLog не является обычным app log:
Обычные application logs нужны для debugging и observability.
AuditLog нужен для бизнес- и security-истории:
кто сделал важное действие, когда сделал, над какой сущностью и с какими данными.

Почему actor_user_id nullable:
Не каждое событие создаётся пользователем.
Некоторые события могут быть системными:
- system.progress_recalculated
- background job created notification
- cleanup expired idempotency keys

Поэтому actor_user_id должен быть nullable.
AuditLog с actor_user_id = NULL — это валидный system event.

Почему action NOT NULL:
AuditLog без action бесполезен.
Если неизвестно, что произошло, запись не имеет смысла.
Поэтому action должен быть обязательным.

Почему entity_type и entity_id nullable:
Не каждое audit-событие обязательно привязано к конкретной бизнес-сущности.
Но когда привязка есть, можно хранить:
entity_type = "attempt"
entity_id = 12

или:
entity_type = "user"
entity_id = 5

Почему IdempotencyKey нужен:
Если клиент повторит один и тот же request из-за сетевого лага, retry или двойного клика, система может случайно создать дубликат.
Например:
один submit attempt может создать две attempts.

IdempotencyKey защищает от этого:
один user + один key + одна operation должны выполняться только один раз.

Почему unique constraint именно на user_id + key + operation:
Просто key сам по себе может совпасть у разных пользователей.
operation тоже важна, потому что один и тот же key может теоретически использоваться для разных типов операций.

Правильный инвариант:
один пользователь не может повторно использовать тот же key для той же operation.

Поэтому нужен:
UniqueConstraint("user_id", "key", "operation")

Почему status не boolean:
IdempotencyKey — это маленький workflow.
У него больше двух состояний:
- processing
- completed
- failed

Boolean не выразил бы это нормально.
Поэтому status хранится как controlled string с CheckConstraint.

Какие constraints были добавлены:
1. ForeignKey на audit_logs.actor_user_id -> users.id
   AuditLog не может ссылаться на несуществующего actor user.

2. NOT NULL на audit_logs.action
   AuditLog без action запрещён.

3. ForeignKey на idempotency_keys.user_id -> users.id
   IdempotencyKey не может принадлежать несуществующему user.

4. UniqueConstraint на idempotency_keys(user_id, key, operation)
   Один и тот же пользователь не может повторить тот же idempotency key для той же operation.

5. CheckConstraint на idempotency_keys.status
   status может быть только:
   processing
   completed
   failed

Что я проверил:
1. Проверил, что таблицы audit_logs и idempotency_keys появились через \dt.
2. Проверил структуру audit_logs через \d audit_logs.
3. Проверил структуру idempotency_keys через \d idempotency_keys.
4. Проверил AuditLog happy path: system event с actor_user_id = NULL проходит.
5. Проверил AuditLog failure case: actor_user_id с несуществующим user_id падает по foreign key.
6. Проверил AuditLog failure case: action = NULL падает по NOT NULL.
7. Проверил IdempotencyKey happy path: валидный key создаётся.
8. Проверил IdempotencyKey failure case: duplicate user_id + key + operation падает по unique constraint.
9. Проверил IdempotencyKey failure case: invalid status падает по check constraint.
10. Проверил IdempotencyKey failure case: несуществующий user_id падает по foreign key.

Что пошло не так / что было важно понять:
Сначала я воспринимал AuditLog как обычные логи для моделей.
Но AuditLog — это не Python logging и не structlog.
Это отдельная таблица для важных бизнес/безопасность событий.

Также важно было понять, что IdempotencyKey — это не просто random key.
Это operational protection от duplicate submit / retry / повторного выполнения операции.

Категория риска:
Operational state design risk.
Duplicate operation risk.
Auditability risk.
Workflow state modeling risk.

Правильная ментальная модель:
AuditLog отвечает на вопросы:
- кто сделал?
- что сделал?
- над чем сделал?
- когда сделал?
- какие дополнительные данные были?

IdempotencyKey отвечает на вопрос:
- выполнялась ли уже эта операция с этим ключом для этого пользователя?

Что отложено:
- AuditService
- автоматическая запись audit events
- request IP / user-agent
- middleware для idempotency key
- actual duplicate-submit logic
- retry behavior
- cleanup expired idempotency keys
- связывание idempotency key с HTTP headers
- полноценные repository/service tests

Test status:
На этом этапе я сделал manual SQL verification через psql.
Это подтвердило, что база реально применяет foreign keys, unique constraint, check constraint и NOT NULL.

Automated pytest integration tests пока не написаны.
Позже, когда появятся repository layer и test DB fixtures, эти SQL checks надо перенести в pytest.

Правило на следующий раз:
1. Сначала определить: это domain state или operational state.
2. Для audit log не путать application logs и persistent audit history.
3. Для idempotency всегда определить scope уникальности.
4. Для workflow status не использовать boolean, если состояний больше двух.
5. Перед миграцией проверять ORM mapping.
6. После миграции проверять \d table.
7. Для каждого constraint делать отдельный failure case.
8. Когда появится test harness, переносить ручные SQL checks в pytest.

T027 считается закрытым по schema/migration/manual verification, потому что:
- AuditLog model создан.
- IdempotencyKey model создан.
- audit_logs и idempotency_keys появились в базе.
- AuditLog поддерживает system events через actor_user_id = NULL.
- AuditLog action защищён NOT NULL.
- IdempotencyKey связан с User.
- IdempotencyKey имеет unique constraint на user_id + key + operation.
- IdempotencyKey имеет status constraint.
- Happy paths проверены.
- Failure cases проверены.
- Automated pytest test помечен как pending для repository/test-fixture этапа.

T030 Postmortem — UserRepository + PostgreSQL integration tests

Что я пытался сделать:
Мне нужно было написать UserRepository с методами:
- get_by_id
- get_by_email
- create
- update

Цель T030 была не просто сделать функции для User, а впервые отделить слой работы с БД от ORM-модели.
Model описывает таблицу.
Repository описывает операции чтения и записи через SQLAlchemy Session.

Главная архитектурная идея:
User model = структура таблицы users.
UserRepository = слой доступа к данным для users.

Что получилось:
Я создал отдельный repository layer, а не стал писать методы прямо в models.py.
Для UserRepository были реализованы методы:
- get_by_id(user_id)
- get_by_email(email)
- create(email, is_active)
- update(user, **fields)

Repository принимает SQLAlchemy Session через constructor.
Это правильно, потому что session lifecycle должен контролироваться снаружи: service layer, use case или test.

Почему repository не должен делать commit:
Repository должен делать DB-операцию, но не должен решать границы транзакции.
Внутри repository допустимы:
- session.add(...)
- session.flush()
- session.refresh(...)

Но commit должен быть снаружи.

Причина:
Позже одна бизнес-операция может включать несколько действий:
- create attempt
- update progress
- create notification
- write audit log

И всё это должно коммититься одной транзакцией.
Если каждый repository сам делает commit, транзакционная целостность развалится.

Что я проверил:
Я написал PostgreSQL integration tests для UserRepository.
Тесты проверили:
1. create user
2. get user by id
3. get user by email
4. get_by_id возвращает None для несуществующего user
5. get_by_email возвращает None для несуществующего email
6. update user
7. update запрещает неизвестное поле

Negative cases:
1. get_by_id для missing id возвращает None.
2. get_by_email для missing email возвращает None.
3. update с неизвестным полем, например password_hash, падает с ValueError.

Почему я выбрал PostgreSQL, а не SQLite:
SQLite in-memory проще, но он не полностью повторяет PostgreSQL.
Так как проект реально использует PostgreSQL, repository tests лучше гонять на настоящей test database.
Это ближе к production behavior и ловит больше реальных проблем.

Что было сделано для test DB:
Я создал отдельную базу:
ytter_test_db

И добавил TEST_DATABASE_URL только для тестового запуска.
Важное правило:
TEST_DATABASE_URL не должен лежать в обычном .env как runtime app config.
Это test-only config.

Что пошло не так:
После добавления TEST_DATABASE_URL сломались старые config-тесты.
SimpleConfig начал видеть test_database_url и падал с ошибкой:

Extra inputs are not permitted

Причина:
Я смешал runtime application config и test-only config.
SimpleConfig не должен знать про TEST_DATABASE_URL, потому что это не настройка приложения, а настройка test harness.

Как я исправил:
Я вынес TEST_DATABASE_URL из обычного .env / runtime config.
Для запуска тестов начал экспортировать его через shell или setup.sh.
Также config tests были изолированы от .env через _env_file=None, чтобы тесты не зависели от внешнего окружения.

Вторая проблема:
Repository tests сначала падали, потому что TEST_DATABASE_URL не был задан.
Ошибка была в fixture test_database_url.

Правильное поведение:
Если TEST_DATABASE_URL не задан, тест должен явно сказать:
TEST_DATABASE_URL is not set

Это лучше, чем молчаливый fail.

Третья проблема:
После фикса repository tests и config tests остались 2 падения в tests/test_models.py.

Тесты проверяли:

User.__table__.c.track_sort_order
User.__table__.c.lesson_track_id

Но это неправильная модель.
У User не должно быть track_sort_order или lesson_track_id.
sort_order принадлежит Track.
track_id принадлежит Lesson.

Правильные проверки:
Track.__table__.c.sort_order.nullable is False
Lesson.__table__.c.track_id.nullable is False

Это была ошибка старого теста, а не ошибка моделей.

Категории ошибок:
1. Config boundary error.
2. Test environment pollution.
3. Runtime config vs test-only config confusion.
4. Stale tests after schema changes.
5. Repository abstraction learning.
6. Transaction boundary design.

Правильная ментальная модель:
Runtime app config — это то, что нужно приложению для запуска.
Test-only config — это то, что нужно test harness.
Их нельзя бездумно смешивать.

Repository не владеет транзакцией.
Repository работает внутри переданной Session.
Service/use case/test решает, когда commit или rollback.

PostgreSQL integration tests должны использовать отдельную test database.
Нельзя гонять destructive tests против dev/prod database.

Что я сделал хорошо:
1. Не положил repository в models.py.
2. Создал отдельный слой app/repositories.
3. Сделал UserRepository с явным Session dependency.
4. Не стал делать commit внутри repository.
5. Написал integration tests на реальном PostgreSQL.
6. Добавил negative cases.
7. Починил конфликт runtime config и test config.
8. Починил устаревшие model tests.
9. Довёл полный test run до зелёного состояния.

Что отложено:
- service layer
- transaction orchestration на уровне use case
- generic BaseRepository
- pagination
- soft delete
- domain-specific UserService
- auth/password logic
- PostgreSQL test database lifecycle automation
- CI test database setup

Что я должен делать дальше:
1. Для каждого repository писать tests на real PostgreSQL test DB.
2. Не использовать SQLite, если нужно проверить реальное DB behavior.
3. Не класть test-only переменные в runtime .env.
4. Не делать commit внутри repository.
5. После schema/model changes проверять, не устарели ли старые tests.
6. Перед full test run разделять ошибки по классам:
   - config
   - repository
   - model tests
   - DB connection
   - migration
7. Постепенно переносить manual SQL checks из прошлых тикетов в automated pytest integration tests.

T030 считается закрытым, потому что:
- UserRepository создан.
- get_by_id работает.
- get_by_email работает.
- create работает.
- update работает.
- negative cases проверены.
- PostgreSQL integration tests написаны.
- test DB используется отдельно от dev DB.
- полный test run стал зелёным.

T031 — TrackRepository и LessonRepository basics

WELL:

Я реализовал базовые repository-методы для Track и Lesson: create, get by id, get by title, update.
Я исправил copy-paste ошибку из UserRepository и начал работать с правильными ORM-моделями.
Я добавил happy-path и negative-path тесты: missing entity возвращает None, неизвестное поле в update даёт ValueError.
Я понял, что Lesson не существует отдельно от Track, и начал передавать track_id при создании lesson.

STRUGGLE:

Fact: Сначала я пытался создавать Lesson без track_id.
Taxonomy: [3. Schema design error], [4. Boundary and validation error]
Why: Я воспринимал Lesson как самостоятельную сущность, хотя по схеме это дочерняя запись, завязанная на Track.
Rule for next time: Перед написанием repository для модели я сначала проверяю её обязательные foreign keys и только потом пишу create() contract.
Fact: В update() я сначала делал setattr(Track/Lesson, field_name, value) вместо изменения конкретного объекта.
Taxonomy: [5. State management error], [1. Syntax/API memory error]
Why: Я перепутал ORM-класс и ORM-instance.
Rule for next time: В repository update всегда мутируется переданный объект (track, lesson, user), а не класс модели (Track, Lesson, User).
Fact: Часть тестов я обновил не сразу после изменения сигнатуры LessonRepository.create(track_id, ...).
Taxonomy: [11. Testing blindness], [10. Serialization or contract error]
Why: Я изменил production contract, но не синхронизировал все тесты с новым контрактом.
Rule for next time: После изменения сигнатуры метода я прохожу поиском по всем вызовам этого метода и обновляю каждый тестовый сценарий.