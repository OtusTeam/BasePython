# Шпаргалка: `venv`, `pip`, Poetry и `uv`

## 📦 PyPI — каталог Python-пакетов

### Открыть официальный каталог Python-пакетов

```text
https://pypi.org/
```

На PyPI можно:

* искать Python-библиотеки;
* смотреть доступные версии;
* читать инструкции по установке;
* изучать зависимости и документацию пакетов.

---

# 🐍 Виртуальное окружение `venv`

## Создание виртуального окружения

### Создать виртуальное окружение через команду `python`

```bash
python -m venv ./myvenv
```

### Создать виртуальное окружение через команду `python3`

```bash
python3 -m venv ./myvenv
```

Обозначения:

* `python3` — используемый интерпретатор Python;
* `-m venv` — запуск встроенного модуля `venv`;
* `./myvenv` — директория виртуального окружения.

После выполнения команды появится директория:

```text
myvenv/
```

В ней находятся:

* отдельный интерпретатор Python;
* отдельный `pip`;
* установленные зависимости проекта;
* скрипты активации окружения.

---

## Активация виртуального окружения

### Активировать окружение в Linux или macOS

```bash
source ./myvenv/bin/activate
```

После активации в начале строки терминала обычно появляется название окружения:

```text
(myvenv)
```

### Активировать окружение в Windows CMD

```cmd
.\myvenv\Scripts\activate
```

### Активировать окружение в Windows PowerShell

```powershell
.\myvenv\Scripts\Activate.ps1
```

---

## Деактивация виртуального окружения

### Выйти из виртуального окружения

```bash
deactivate
```

После этого команды `python` и `pip` снова будут использовать системное окружение.

---

# 📥 Менеджер пакетов `pip`

## Проверка `pip`

### Показать версию `pip`

```bash
pip --version
```

Команда показывает:

* версию `pip`;
* путь установки;
* используемую версию Python.

### Показать установленные пакеты

```bash
pip list
```

---

## Установка пакетов

### Установить последнюю доступную версию `requests`

```bash
pip install requests
```

### Установить конкретную версию `requests`

```bash
pip install requests==2.26
```

Конструкция `==` фиксирует точную версию пакета.

---

## Удаление и обновление пакетов

### Удалить пакет `requests`

```bash
pip uninstall requests
```

Перед удалением `pip` запросит подтверждение.

### Обновить пакет `requests`

```bash
pip install --upgrade requests
```

Флаг `--upgrade` обновляет пакет до последней доступной версии.

---

## Работа с `requirements.txt`

### Сохранить установленные зависимости

```bash
pip freeze > requirements.txt
```

Команда:

1. получает список установленных пакетов;
2. фиксирует их версии;
3. записывает результат в `requirements.txt`.

Пример содержимого:

```text
requests==2.26.0
urllib3==1.26.20
```

### Установить зависимости из файла

```bash
pip install -r requirements.txt
```

Обозначения:

* `-r` — прочитать зависимости из файла;
* `requirements.txt` — файл с пакетами и версиями.

---

# 📝 Poetry

## Официальная документация Poetry

### Открыть инструкцию по установке Poetry

```text
https://python-poetry.org/docs/#installing-with-the-official-installer
```

---

## Установка Poetry

### Установить Poetry в Linux или macOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Команда скачивает и запускает официальный установочный скрипт Poetry.

### Установить Poetry в Windows PowerShell

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Проверить установку Poetry

```bash
poetry --version
```

---

## Создание проекта

### Создать новый проект Poetry

```bash
poetry new poetry_project
```

Poetry создаст приблизительно такую структуру:

```text
poetry_project/
├── pyproject.toml
├── README.md
├── tests/
└── poetry_project/
    └── __init__.py
```

Файл `pyproject.toml` содержит:

* информацию о проекте;
* версию Python;
* основные зависимости;
* группы дополнительных зависимостей.

---

## Добавление зависимостей

### Добавить FastAPI

```bash
poetry add fastapi
```

Poetry:

1. добавит пакет в `pyproject.toml`;
2. установит пакет;
3. обновит файл `poetry.lock`.

### Добавить Black в группу `lint`

```bash
poetry add black --group lint
```

Группы позволяют разделять зависимости:

* основные;
* тестовые;
* инструменты форматирования;
* инструменты разработки.

### Добавить конкретную версию `requests`

```bash
poetry add requests==2.26
```

---

## Удаление зависимостей

### Удалить FastAPI

```bash
poetry remove fastapi
```

Poetry удалит пакет из проекта и обновит файл блокировки.

---

## Обновление зависимостей

### Обновить только пакет `requests`

```bash
poetry update requests
```

### Обновить все зависимости проекта

```bash
poetry update
```

Обновление выполняется в пределах ограничений, указанных в `pyproject.toml`.

---

## Просмотр зависимостей

### Показать все зависимости

```bash
poetry show
```

### Показать информацию о пакете `requests`

```bash
poetry show requests
```

### Показать дерево зависимостей

```bash
poetry show --tree
```

Дерево показывает:

* прямые зависимости;
* транзитивные зависимости;
* какие библиотеки установлены другими пакетами.

---

## Установка зависимостей проекта

### Установить зависимости из проекта

```bash
poetry install
```

Команда использует:

```text
pyproject.toml
poetry.lock
```

Если `poetry.lock` существует, Poetry устанавливает зафиксированные в нём версии.

---

## Информация о виртуальном окружении

### Показать информацию об окружении Poetry

```bash
poetry env info
```

Команда показывает:

* путь к виртуальному окружению;
* версию Python;
* путь к интерпретатору;
* системную информацию.

---

## Синхронизация окружения

### Синхронизировать окружение с файлом блокировки

```bash
poetry sync
```

Команда:

* устанавливает нужные зависимости;
* удаляет лишние зависимости;
* приводит окружение в соответствие с `poetry.lock`.

---

## Удаление виртуального окружения

### Показать доступные окружения

```bash
poetry env list
```

### Удалить конкретное окружение

```bash
poetry env remove <имя_или_путь_интерпретатора>
```

Например:

```bash
poetry env remove python3.13
```

### Удалить все окружения проекта

```bash
poetry env remove --all
```

---

## Проверка конфигурации проекта

### Проверить файл `pyproject.toml`

```bash
poetry check
```

Команда проверяет корректность конфигурации проекта Poetry.

---

# ⚡ Менеджер проектов и зависимостей `uv`

## Официальная документация `uv`

### Открыть документацию по возможностям `uv`

```text
https://docs.astral.sh/uv/getting-started/features/
```

---

## Установка `uv`

### Установить `uv` в Linux или macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Проверить установку `uv`

```bash
uv --version
```

---

## Работа с версиями Python

### Показать доступные и установленные версии Python

```bash
uv python list
```

Команда показывает:

* установленные версии Python;
* доступные для установки версии;
* пути к интерпретаторам.

### Найти установленный Python версии 3.14

```bash
uv python find 3.14
```

Команда ищет подходящий интерпретатор Python и выводит путь к нему.

### Установить Python 3.13

```bash
uv python install 3.13
```

`uv` скачает и установит подходящую версию Python.

---

# 🧭 Краткий порядок работы с `venv` и `pip`

```bash
# Создать виртуальное окружение
python3 -m venv ./myvenv

# Активировать его в Linux
source ./myvenv/bin/activate

# Проверить pip
pip --version

# Установить зависимость
pip install requests

# Сохранить зависимости
pip freeze > requirements.txt

# Выйти из окружения
deactivate

# Восстановить зависимости
pip install -r requirements.txt
```

---

# 🧭 Краткий порядок работы с Poetry

```bash
# Создать проект
poetry new poetry_project

# Перейти в проект
cd poetry_project

# Добавить зависимость
poetry add fastapi

# Добавить инструмент разработки
poetry add black --group lint

# Посмотреть зависимости
poetry show --tree

# Установить зависимости
poetry install

# Проверить окружение
poetry env info

# Синхронизировать окружение
poetry sync

# Проверить конфигурацию
poetry check
```

---

# 🧭 Краткий порядок работы с `uv`

```bash
# Проверить uv
uv --version

# Посмотреть версии Python
uv python list

# Найти установленный Python
uv python find 3.14

# Установить Python
uv python install 3.13
```
