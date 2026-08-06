# Шпаргалка: качество Python-кода - Ruff, Pylint, Flake8, Black, isort и mypy

## 🎯 Назначение инструментов

| Инструмент | Что делает                                                     |
| ---------- | -------------------------------------------------------------- |
| **Ruff**   | Линтинг, автоисправления, сортировка импортов и форматирование |
| **Flake8** | Находит базовые ошибки и нарушения оформления                  |
| **isort**  | Сортирует и группирует импорты                                 |
| **Black**  | Автоматически форматирует Python-код                           |
| **Pylint** | Выполняет более строгий анализ структуры и качества кода       |
| **mypy**   | Проверяет соответствие кода аннотациям типов                   |

Для новых проектов основной вариант:

```text
Ruff
→ линтинг, импорты и форматирование.

mypy
→ отдельная проверка типов.

Pylint
→ дополнительная строгая проверка при необходимости.
```

---

# 🐍 Создание проекта

Проект создаём в PyCharm:

```text
log-analyzer/
├── .venv/
├── main.py
└── pyproject.toml
```

Проверяем активный Python:

```bash
python --version
which python
```

Путь должен вести в окружение проекта:

```text
log-analyzer/.venv/bin/python
```

---

## Подключение Poetry к существующему проекту

```bash
poetry --version
poetry init
poetry check
poetry env info
```

Основные команды:

```text
poetry init
→ создать pyproject.toml в существующем проекте.

poetry check
→ проверить pyproject.toml.

poetry env info
→ показать используемое окружение.
```

Если `.venv` активно, команды запускаем напрямую:

```bash
ruff check .
black --check .
pylint main.py
```

Использовать `poetry run` необязательно.

---

# 📦 Установка инструментов

Добавляем инструменты в отдельную группу `lint`:

```bash
poetry add --group lint ruff pylint flake8 black isort
```

Проверяем версии:

```bash
ruff --version
pylint --version
flake8 --version
black --version
isort --version
```

Проверяем путь к Ruff:

```bash
which ruff
```

Показываем содержимое группы:

```bash
poetry show --only lint --top-level
```

---

# ▶️ Запуск приложения

```bash
python main.py
```

Ожидаемый результат:

```text
Результат анализа логов: INFO - 4, WARNING - 2, ERROR - 2.
```

---

# 🔍 Flake8 - базовый линтер

## Основные команды

```bash
# Проверить весь проект
flake8 .

# Проверить отдельный файл
flake8 main.py
flake8 log_analyzer/report.py

# Проверить несколько целей
flake8 main.py log_analyzer
```

Flake8 только показывает нарушения и не изменяет файлы.

---

## Конфигурация `.flake8`

В корне проекта создаём файл:

```text
.flake8
```

```ini
[flake8]

max-line-length = 88

exclude =
    .venv,
    .git,
    __pycache__

max-complexity = 10
```

---

## Частые ошибки Flake8

| Код    | Сообщение                            | Значение                              |
| ------ | ------------------------------------ | ------------------------------------- |
| `F401` | `imported but unused`                | Импорт не используется                |
| `F841` | `assigned to but never used`         | Переменная не используется            |
| `E225` | `missing whitespace around operator` | Нет пробелов вокруг оператора         |
| `E231` | `missing whitespace after ','`       | Нет пробела после разделителя         |
| `E501` | `line too long`                      | Строка слишком длинная                |
| `E701` | `multiple statements on one line`    | Несколько инструкций в одной строке   |
| `E722` | `do not use bare except`             | Использован `except:` без типа ошибки |
| `W292` | `no newline at end of file`          | Нет перевода строки в конце файла     |
| `W391` | `blank line at end of file`          | Лишняя пустая строка в конце файла    |

Пример `E701`.

Неправильно:

```python
if level in statistics:statistics[level]+=1
```

Правильно:

```python
if level in statistics:
    statistics[level] += 1
```

---

# ↕️ isort — сортировка импортов

## Проверка без изменения файлов

```bash
isort --check-only main.py
isort --check-only main.py log_analyzer
```

## Просмотр изменений

```bash
isort --diff main.py
isort --diff main.py log_analyzer
```

## Применение изменений

```bash
isort main.py log_analyzer
```

---

## Конфигурация isort

В `pyproject.toml`:

```toml
[tool.isort]

profile = "black"
line_length = 88
py_version = 312
known_first_party = ["log_analyzer"]
```

isort:

```text
сортирует импорты;
разделяет стандартные и локальные модули;
не удаляет неиспользуемые импорты.
```

Типичное сообщение:

```text
Imports are incorrectly sorted and/or formatted
```

---

# 🎨 Black - форматирование кода

## Проверить форматирование

```bash
black --check main.py
black --check log_analyzer
black --check main.py log_analyzer
```

## Посмотреть изменения

```bash
black --diff main.py
black --diff log_analyzer
```

## Отформатировать код

```bash
black main.py log_analyzer
```

---

## Конфигурация Black

В `pyproject.toml`:

```toml
[tool.black]

line-length = 88
target-version = ["py312"]
```

Black исправляет:

```text
пробелы;
отступы;
переносы;
оформление словарей и списков;
кавычки.
```

Типичные сообщения:

```text
would reformat main.py
→ файл требует форматирования;

reformatted main.py
→ файл был изменён;

Cannot parse
→ в коде синтаксическая ошибка.
```

---

# 🧐 Pylint - расширенный анализ

## Основные команды

```bash
# Проверить проект
pylint main.py log_analyzer

# Проверить только ошибки
pylint --errors-only main.py log_analyzer

# Показать описание правила
pylint --help-msg=unused-import
pylint --help-msg=E0602
```

Pylint дополнительно проверяет:

```text
docstring;
имена;
порядок импортов;
сложность функций;
количество аргументов;
количество локальных переменных;
потенциальные ошибки.
```

---

## Категории сообщений

```text
F - критическая ошибка проверки;
E - вероятная ошибка программы;
W - предупреждение;
R - рекомендация по рефакторингу;
C - нарушение соглашений;
I - информация.
```

---

## Частые ошибки Pylint

| Код     | Сообщение                    | Значение                            |
| ------- | ---------------------------- | ----------------------------------- |
| `W0611` | `unused-import`              | Импорт не используется              |
| `W0612` | `unused-variable`            | Переменная не используется          |
| `C0103` | `invalid-name`               | Неудачное или неправильное имя      |
| `C0114` | `missing-module-docstring`   | Нет docstring модуля                |
| `C0116` | `missing-function-docstring` | Нет docstring функции               |
| `C0301` | `line-too-long`              | Строка слишком длинная              |
| `C0321` | `multiple-statements`        | Несколько инструкций в одной строке |
| `C0411` | `wrong-import-order`         | Неправильный порядок импортов       |
| `E0602` | `undefined-variable`         | Переменная не определена            |
| `R0913` | `too-many-arguments`         | Слишком много аргументов            |
| `R0914` | `too-many-locals`            | Слишком много локальных переменных  |

---

## Минимальная конфигурация Pylint

```toml
[tool.pylint.main]

py-version = "3.12"
recursive = true
score = true

disable = [
    "missing-module-docstring",
    "missing-function-docstring",
]


[tool.pylint.format]

max-line-length = 88
```

---

# ⚡ Ruff - основной инструмент

## Проверка кода

```bash
ruff check .
```

## Проверка отдельного файла

```bash
ruff check main.py
ruff check log_analyzer/report.py
```

## Показать возможные исправления

```bash
ruff check . --diff
```

## Применить безопасные исправления

```bash
ruff check . --fix
```

## Показать описание правила

```bash
ruff rule F401
ruff rule F841
ruff rule E701
ruff rule I001
```

## Показать статистику

```bash
ruff check . --statistics
```

## Показать настройки

```bash
ruff check . --show-settings
```

---

## Проверка форматирования

```bash
ruff format --check .
```

## Просмотр форматирования

```bash
ruff format --diff .
```

## Форматирование проекта

```bash
ruff format .
```

---

## Конфигурация Ruff

```toml
[tool.ruff]

target-version = "py312"
line-length = 88
extend-exclude = ["data"]


[tool.ruff.lint]

select = [
    "E4",
    "E7",
    "E9",
    "F",
    "I",
    "B",
    "UP",
]

ignore = ["E501"]


[tool.ruff.lint.isort]

known-first-party = ["log_analyzer"]


[tool.ruff.format]

quote-style = "double"
indent-style = "space"
line-ending = "auto"
skip-magic-trailing-comma = false
docstring-code-format = false
```

---

## Частые ошибки Ruff

| Код      | Сообщение                                       | Значение                                   |
| -------- | ----------------------------------------------- | ------------------------------------------ |
| `F401`   | `imported but unused`                           | Неиспользуемый импорт                      |
| `F841`   | `assigned to but never used`                    | Неиспользуемая переменная                  |
| `F821`   | `Undefined name`                                | Неизвестное имя                            |
| `E701`   | `Multiple statements on one line`               | Несколько инструкций в строке              |
| `E722`   | `Do not use bare except`                        | `except:` без типа ошибки                  |
| `I001`   | `Import block is un-sorted`                     | Импорты не отсортированы                   |
| `B006`   | `mutable data structures for argument defaults` | Изменяемое значение параметра по умолчанию |
| `RUF100` | `Unused noqa directive`                         | Лишний комментарий `# noqa`                |

---

# 🧩 mypy - проверка типов

## Установка

```bash
poetry add --group typing mypy
```

## Проверка проекта

```bash
mypy main.py log_analyzer
```

## Показать коды ошибок

```bash
mypy main.py log_analyzer --show-error-codes
```

## Строгий режим

```bash
mypy main.py log_analyzer --strict
```

---

## Частые ошибки mypy

| Код                | Значение                                         |
| ------------------ | ------------------------------------------------ |
| `[arg-type]`       | Передан аргумент неправильного типа              |
| `[assignment]`     | Переменной присвоено значение неправильного типа |
| `[return-value]`   | Функция возвращает неправильный тип              |
| `[attr-defined]`   | У объекта нет указанного атрибута                |
| `[union-attr]`     | Атрибут доступен не у всех возможных типов       |
| `[call-arg]`       | Функция вызвана с неправильными аргументами      |
| `[name-defined]`   | Используется неопределённое имя                  |
| `[operator]`       | Оператор применяется к несовместимым типам       |
| `[no-untyped-def]` | У функции нет аннотаций типов                    |

Пример:

```python
def double(value: int) -> int:
    return value * 2


double("10")
```

Сообщение:

```text
Argument 1 has incompatible type "str";
expected "int"  [arg-type]
```

---

## Конфигурация mypy

```toml
[tool.mypy]

python_version = "3.12"
warn_unused_configs = true
check_untyped_defs = true
show_error_codes = true
```

---

# 🔄 Сравнение инструментов

| Задача                            | Инструмент |
| --------------------------------- | ---------- |
| Базовый линтинг                   | Flake8     |
| Сортировка импортов               | isort      |
| Форматирование                    | Black      |
| Расширенный анализ                | Pylint     |
| Линтинг, импорты и форматирование | Ruff       |
| Проверка типов                    | mypy       |

---

# 🧭 Рекомендуемый набор для нового проекта

```text
Ruff
→ основной линтер, сортировка импортов
  и форматирование.

mypy
→ проверка типов.

Pylint
→ дополнительный строгий анализ
  при необходимости.
```

Flake8, Black и isort полезно знать, поскольку они часто встречаются в существующих проектах.

---

# 🧭 Ежедневный workflow

## Только проверить

```bash
ruff check .
ruff format --check .
```

## Посмотреть изменения

```bash
ruff check . --diff
ruff format --diff .
```

## Исправить и отформатировать

```bash
ruff check . --fix
ruff format .
```

## Финальная проверка

```bash
ruff check .
ruff format --check .
```

## Проверить типы

```bash
mypy main.py log_analyzer
```

## Запустить приложение

```bash
python main.py
```

---

# 📌 Итог

```text
Линтер
→ находит ошибки и нарушения.

Форматтер
→ изменяет внешний вид кода.

Сортировщик импортов
→ группирует и сортирует импорты.

Проверка типов
→ сравнивает код с аннотациями типов.

Разработчик
→ отвечает за смысл, архитектуру
  и бизнес-логику программы.
```
