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