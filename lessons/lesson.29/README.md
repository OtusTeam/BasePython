
## Таблицы

### Авторы
У меня будет таблица авторов.

У каждого автора должны быть следующие свойства:
- `id` - первичный ключ, числовой
- `username` - имя пользователя. уникально. не пустое. лимит 32 символа
- `bio` - сюда пользователь может написать что угодно о себе. лимит 200 символов
- `email` - почта. опицонально. лимит 120 символов.
- `full_name` - ФИО / Имя + Фамилия пользователя. до 100 символов

### Публикации
У меня будет таблица публикаций, написанных авторами.
- `id` - первичный ключ, числовой
- `author_id` - ссылка на автора, внешний ключ. автор публикации.
- `title` - заголовок публикации. 120 символов
- `body` - текст. большой текст
- `published_at` - датавремя



```python
s = "Current month: %(month).2d"
line = "val: %s"
line % 'abc'
'val: abc'
line % 42
'val: 42'
line = "val: %r"
line % 'abc'
"val: 'abc'"
repr('abc')
"'abc'"
line = "number: %d"
line % 42
'number: 42'
line % 'a'
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: %d format: a real number is required, not str
line = "number: %(num)d"
line % 42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: format requires a mapping
line % {'num': 42}
'number: 42'
line = "number %.2d"
line % 42
'number 42'
line % 7
'number 07'
line % 123
'number 123'
s % {'month': 3}
'Current month: 03'
num = 7
f"number: {num:.2d}"
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# ValueError: Precision not allowed in integer format specifier
f"number: {num:2d}"
'number:  7'
f"number: {num:02d}"
'number: 07'
"number: {num:02d}".format(num=num)
'number: 07'

```


```shell
(.venv) suren@MacBookPro sql-project-demo % alembic upgrade --sql b39b:f8a0                              
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Generating static SQL
INFO  [alembic.runtime.migration] Will assume transactional DDL.
BEGIN;

INFO  [alembic.runtime.migration] Running upgrade b39bb783280d -> e770c0edaaa8, add col full_name to users
-- Running upgrade b39bb783280d -> e770c0edaaa8

ALTER TABLE users ADD COLUMN full_name VARCHAR(100) DEFAULT '' NOT NULL;

UPDATE alembic_version SET version_num='e770c0edaaa8' WHERE alembic_version.version_num = 'b39bb783280d';

INFO  [alembic.runtime.migration] Running upgrade e770c0edaaa8 -> f8a06c1f7697, add col body to articles
-- Running upgrade e770c0edaaa8 -> f8a06c1f7697

ALTER TABLE articles ADD COLUMN body TEXT DEFAULT '' NOT NULL;

UPDATE alembic_version SET version_num='f8a06c1f7697' WHERE alembic_version.version_num = 'e770c0edaaa8';

COMMIT;

```