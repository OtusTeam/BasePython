# Примеры с подгрузкой связей в SQLAlchemy

## Сущности

### User

Поля:

- `id`
- `username`
- `created_at`

### Profile

Связь 1к1 с `User`

Поля:

- `id`
- `about`
- `site`
- `created_at`
- `user_id` - fk

### Article

Связь с `User` "ко многим". У одного пользователя любое количество публикаций

Поля:

- `id`
- `title`
- `text`
- `created_at`
- `user_id` - fk
