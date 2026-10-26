# Книжная полка: тестирование FastAPI с pytest

Самостоятельное маленькое API для вебинара на **38 минут**. Одна таблица книг,
четыре маршрута, локальная SQLite. Python 3.14, FastAPI, SQLAlchemy 2.1,
pytest и синхронный `TestClient`.

Откройте [сценарий вебинара](docs/WEBINAR.md): тайминг, порядок написания тестов
и команды для каждого шага. Готовое решение содержит 22 тестовых случая.

## Запуск за две команды

Нужен [uv](https://docs.astral.sh/uv/getting-started/installation/).
Python 3.14 `uv` установит при необходимости.

```bash
uv sync --locked
uv run --locked fastapi dev bookshelf/main.py
# Открыть http://127.0.0.1:8000/docs
```

`just setup`, `just dev`, `just check`, `just test -v` — короткие аналоги;
`just` необязателен для запуска. Все команды выполняются из корня этого проекта.
База `bookshelf.db` создаётся при старте и сохраняет книги между запусками.

## Что делает API

| Метод | Путь | Результат |
| --- | --- | --- |
| GET | `/health` | `200`, `{"status": "ok"}` |
| GET | `/books` | `200`, список книг |
| POST | `/books` | `201`, созданная книга |
| PATCH | `/books/{book_id}/read` | `200`, книга отмечена прочитанной; `404`, если её нет |

Тело POST: `{"title": "Чистый Python", "pages": 300}`.
Ответ: `{"id": "<UUID>", "title": "Чистый Python", "pages": 300, "is_read": false}`.
Название очищается от пробелов по краям и содержит 1–100 символов.
Число страниц — целое от 1 до 10000: строки и `true` не принимаются.
Неверные данные или UUID дают `422`.

```bash
curl -i http://127.0.0.1:8000/books \
  -H 'Content-Type: application/json' \
  -d '{"title":"Чистый Python","pages":300}'
curl -i http://127.0.0.1:8000/books
```

Swagger `/docs` — готовый интерфейс для ручной проверки перед автоматизацией.
Отдельного frontend нет.

## Откуда начинать писать тесты

`codex/fastapi-pytest-start` (`9d2f5db`) указывает на готовое приложение **без тестов**.
Зависимости, настройки pytest и coverage уже подготовлены.
`codex/fastapi-pytest-demo` содержит второй коммит с решением и сценарием занятия.
Обе ветки имеют самостоятельную историю: код и коммиты Вече сюда не входят.

Из чистой рабочей папки создайте личную ветку для занятия:

```bash
git switch -c workshop/pytest codex/fastapi-pytest-start
uv sync --locked
mkdir tests
```

На старте `pytest` ещё не запускают: тестов нет, пустой запуск заканчивается
кодом 5. Сначала создайте `tests/__init__.py`, `tests/conftest.py` и первый
`tests/test_health.py`. В ветке решения:

```bash
uv run --locked pytest -v
uv run --locked pytest -k health --no-cov
```

Переходите к решению через `git switch codex/fastapi-pytest-demo` только после
сохранения своей работы в коммите. Пошаговый сценарий `docs/WEBINAR.md`
появляется во втором коммите.

## Настройки и безопасная тестовая БД

`bookshelf/config/default.yaml` содержит значения по умолчанию;
`dev.yaml` и `test.yaml` — слои окружения. `*Config` разделены по предметам,
главный `Settings` один. Приоритет: аргументы `Settings(...)` → переменные
окружения → выбранный YAML → базовый YAML. Пути YAML привязаны к пакету.
Файл `.env` здесь не загружается: для урока достаточно явных env overrides.

```bash
BOOKSHELF__BOOKS__ALLOW_CREATE=false uv run --locked fastapi dev bookshelf/main.py
```

При таком запуске POST возвращает `503` и
`{"detail": "Adding books is disabled"}`. Это наглядное поведение для проверки
`app.dependency_overrides[settings_dep]`.

Тесты должны передавать `Settings` с `database.path` внутри `tmp_path` в
`create_app(...)` **до** входа в `with TestClient(...)`. Так lifespan сразу
открывает временную БД. Подмена `settings_dep` влияет на HTTP-зависимости,
но не пересоздаёт engine. Для подмены источника данных используют `session_dep`.
Каждый запрос получает отдельную Session; fixture создаёт данные своей Session.

## Правила исходного репозитория

Перенесены из `master` (`f512277`): Python 3.14 без future annotations;
именованный пакет без `src`; `uv` и lockfile; отдельные TOML инструментов;
Ruff ALL с одним import на строку; Pyrefly; native prek; команды `just`;
router → service → models; HTTP-коды через `starlette.status`;
UUIDv7 и отдельный `created_at`; один ORM-класс на файл;
ресурсы внутри отдельного lifespan; конфиги/YAML; fixtures только в conftest.
Import Linter проверяет границы слоёв. `pytest-cov` показывает пробелы покрытия
без требования достичь 100%.

```bash
just check
# Необязательно: установить локальные hooks Git.
uv run --locked prek install
```

Учебные упрощения: синхронные маршруты и SQLite; таблица создаётся через
`create_all`. При изменении схемы понадобятся миграции. Нет авторизации,
пагинации, очередей и production-развёртывания; сервер предназначен для
локальной демонстрации. Список возвращает все книги, поэтому демо рассчитано
на небольшую учебную БД.
