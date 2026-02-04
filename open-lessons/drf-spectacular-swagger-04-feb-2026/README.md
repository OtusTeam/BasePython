Этот код на Django + Django REST Framework

Как альтернатива тому, что мы делали на FastAPI-JSON:API в другом репо:
https://github.com/mahenzon/fastapi-jsonapi-example-movies-catalog


## Таблицы

### Фильм

Поля:

- `id` - bigint pk
- `title` - str, CI (если PG), not null, index - для поиска
- `description` - описание фильма - not null, default `""`
- `release_date` - старт проката - `date`, nullable
- `duration` - продолжительность фильма в минутах - uint, nullable
- `age_rating` - возрастной рейтинг, ссылка на сущность, nullable

### Жанр фильма

Поля:

- `id` - int pk
- `name` - str, CI (если PG), unique, not null
- `description` - - not null, default `""`

### Фильм <-> Жанр

Поля:

- `id` - int pk
- `movie_id` - ссылка на pk movie.id
- `genre_id` - ссылка на pk genre.id


### Возрастной рейтинг фильма

Свойства:

- `name` - название рейтинга - уникально, первичный ключ
- `description` - описание. например: "только с детьми"
