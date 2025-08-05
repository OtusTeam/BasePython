# Таблицы

## Пользователь

Я хочу хранить информацию о пользователях приложения.
Пользователи могут входить по `username` или `email`.

Необходимо сделать следующие колонки:
- `id` - уникальный идентификатор, автоматическое поле. Первичный ключ.
- `name` - Имя пользователя в свободной форме. Ограничение 100 символов. По умолчанию пустая строчка
- `username` - никнейм пользователя. Уникальный, не пустой (обязательный). Длина до 32 символов
- `email` - эл. почта пользователя. Уникальное значение, может быть пустым. До 150 символов
- `created_at` - дата и время добавления пользователя - значение должно устанавливаться автоматически


## Посты пользователей

Посты - это публикации, которые пользователи могут оставлять в нашем сервисе.
Каждый пост завязан на пользователя, который этот пост завёл.
Не может существовать поста без автора.

У поста должны быть следующие свойства:
- `id` - уникальный идентификатор, автоматическое поле. Первичный ключ.
- `title` - заголовок, ограничение до 120 символов, не уникальный, не пустой
- `body` - тело поста - текст публикации. много букв. не пустой
- `user_id` - ссылка на пользователя - обязательное не пустое поле, не уникальное


# Передача миграций

```shell
alembic upgrade --sql base:2ab2
```

Дорогой девопс, примени пожалуйста миграции на проде:

```sql
BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- INFO  [alembic.runtime.migration] Running upgrade  -> 2ab278d05356, create users table
-- Running upgrade  -> 2ab278d05356

CREATE TABLE users (
    id SERIAL NOT NULL, 
    name VARCHAR(100) DEFAULT '' NOT NULL, 
    username VARCHAR(32) NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
    CONSTRAINT pk_users PRIMARY KEY (id), 
    CONSTRAINT uq_users_username UNIQUE (username)
);

INSERT INTO alembic_version (version_num) VALUES ('2ab278d05356') RETURNING alembic_version.version_num;

COMMIT;
```

и ещё одну:

```sql
BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 2ab278d05356 -> 43ce78fc9340, add col email to users table
-- Running upgrade 2ab278d05356 -> 43ce78fc9340

ALTER TABLE users ADD COLUMN email VARCHAR(150);

ALTER TABLE users ADD CONSTRAINT uq_users_email UNIQUE (email);

UPDATE alembic_version SET version_num='43ce78fc9340' WHERE alembic_version.version_num = '2ab278d05356';

COMMIT;

```


Или две вместе:

```sql
BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 2ab278d05356 -> 43ce78fc9340, add col email to users table
-- Running upgrade 2ab278d05356 -> 43ce78fc9340

ALTER TABLE users ADD COLUMN email VARCHAR(150);

ALTER TABLE users ADD CONSTRAINT uq_users_email UNIQUE (email);

UPDATE alembic_version SET version_num='43ce78fc9340' WHERE alembic_version.version_num = '2ab278d05356';

-- INFO  [alembic.runtime.migration] Running upgrade 43ce78fc9340 -> afe5f2bb7d8a, create posts table
-- Running upgrade 43ce78fc9340 -> afe5f2bb7d8a

CREATE TABLE posts (
    id SERIAL NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    body TEXT DEFAULT '' NOT NULL, 
    user_id INTEGER NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
    CONSTRAINT pk_posts PRIMARY KEY (id), 
    CONSTRAINT fk_posts_user_id_users FOREIGN KEY(user_id) REFERENCES users (id)
);

UPDATE alembic_version SET version_num='afe5f2bb7d8a' WHERE alembic_version.version_num = '43ce78fc9340';

COMMIT;
```


пример с оффлайн миграцией с обновлением данных в колонке:

```sql
BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade afe5f2bb7d8a -> b0eea4ddd07e, require users email
-- Running upgrade afe5f2bb7d8a -> b0eea4ddd07e

UPDATE users 
SET email=(users.username || '@invalid.email')
WHERE users.email IS NULL;

ALTER TABLE users ALTER COLUMN email SET NOT NULL;

UPDATE alembic_version SET version_num='b0eea4ddd07e' WHERE alembic_version.version_num = 'afe5f2bb7d8a';

COMMIT;
```



---

### Запуск

```shell
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
