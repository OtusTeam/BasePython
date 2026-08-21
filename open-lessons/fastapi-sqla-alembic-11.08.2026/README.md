# FastAPI + sync SQLAlchemy: старт вебинара

Стартовый проект для вебинара «Работа с SQLAlchemy и Alembic в FastAPI».
Каркас приложения уже собран, но слой запросов и миграции намеренно предстоит
реализовать на занятии.

## Что уже подготовлено

- FastAPI с обычными `def`-обработчиками;
- синхронные SQLAlchemy 2.x и Psycopg 3;
- PostgreSQL 18 в Docker Compose или Podman;
- `Engine`, фабрика сессий и FastAPI dependency для `Session`;
- ORM-модели `Author` и `Book` со связью один-ко-многим;
- Pydantic-схемы, маршруты, service layer и доменные исключения;
- временное создание таблиц через `Base.metadata.create_all()` при старте;
- пакет Alembic, установленный для занятия, но ещё не настроенный.

Методы в `app/repositories/` пока являются учебными заглушками. В каждом из них
есть `TODO` с контрактом запроса, который нужно написать на вебинаре.

## Что работает в стартовой версии

- приложение запускается и показывает Swagger;
- `GET /` возвращает информацию о сервисе;
- `GET /health` проверяет только само приложение и возвращает
  `database: not_checked`;
- модели создают таблицы при первом запуске.

CRUD-маршруты уже подключены, но валидный запрос до реализации repositories
намеренно завершается `NotImplementedError`. Это не готовая персистентность, а
точка старта упражнения.

## Запуск

Установите [uv](https://docs.astral.sh/uv/getting-started/installation/), затем:

```bash
cp .env.example .env
uv python install 3.14
uv sync --locked
docker compose up -d --wait
uv run uvicorn app.main:app --reload
```

Откройте:

- API: <http://127.0.0.1:8000>
- Swagger: <http://127.0.0.1:8000/docs>
- healthcheck: <http://127.0.0.1:8000/health>

Если локальный PostgreSQL уже занимает порт `5432`, добавьте в `.env`:

```dotenv
FASTAPI_DEMO__DATABASE__POSTGRES__PORT=55432
```

Одна переменная изменит и опубликованный Compose-порт, и адрес подключения
приложения.

## Настройки

Базовая конфигурация находится в
[`app/config/yaml/default.yaml`](app/config/yaml/default.yaml). Секреты и
локальные переопределения — в `.env`, вложенность задаётся двойным
подчёркиванием:

```dotenv
FASTAPI_DEMO__APP__DEBUG=true
FASTAPI_DEMO__DATABASE__POSTGRES__PASSWORD=app
FASTAPI_DEMO__DATABASE__SQLALCHEMY__POOL_SIZE=5
```

Порядок приоритета: аргументы `Settings` → переменные окружения → `.env` → YAML.

## API

```text
GET  /
GET  /health
POST /api/v1/authors
GET  /api/v1/authors
GET  /api/v1/authors/{author_id}
POST /api/v1/authors/{author_id}/books
GET  /api/v1/books
GET  /api/v1/books/{book_id}
```

Views, ORM-модели, Pydantic-схемы и repositories разделены по ресурсам в
`app/api/routes/`, `app/models/`, `app/schemas/` и `app/repositories/`.

## План работы на занятии

1. Разобрать конфигурацию `Engine`, `SessionFactory` и session dependency.
2. Реализовать SQLAlchemy-запросы по `TODO` в repositories.
3. Проверить создание, чтение, пагинацию и загрузку связанных книг.
4. Убрать временный вызов `Base.metadata.create_all()`.
5. Инициализировать Alembic командой `uv run alembic init migrations`.
6. Подключить URL БД и `Base.metadata` в `migrations/env.py`, а каталог
   `migrations` вернуть в `project-includes` для Pyrefly.
7. Сгенерировать, проверить и применить первую миграцию.

### Важно перед первой миграцией

`create_all()` уже создаёт таблицы. Если запустить
`alembic revision --autogenerate` на этой же схеме, первая миграция получится
пустой. Перед этапом с Alembic остановите приложение, удалите вызов
`create_all()` и пересоздайте учебную БД.

Следующая команда удаляет локальные данные этого Compose-проекта:

```bash
docker compose down -v
docker compose up -d --wait
```

После этого можно генерировать и применять начальную миграцию.

## Проверки стартового проекта

Тесты не требуют PostgreSQL и проверяют настройки, модели, ограничения и
создание схемы через `Base.metadata.create_all()`:

```bash
uv run pytest -q
uv run ruff check .
uv run pyrefly check
uv run prek run --all-files
```

После реализации repositories к проекту можно добавить интеграционные тесты
CRUD с отдельной тестовой БД.

## Целевой поток запроса

```text
route → CatalogService → Repository → SQLAlchemy Session → PostgreSQL
                            ↓
                  domain exception
                            ↓
                  FastAPI error handler
```

Session dependency выдаёт сессию, откатывает её при исключении и всегда
закрывает. Изменяющие методы сервиса вызывают `commit()`; запросы только на
чтение не коммитятся.
