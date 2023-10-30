SELECT users.id, users.username, users.email
FROM users
WHERE users.username ILIKE '%o%';
-- [User(id=1, username='john', email=None), User(id=3, username='bob', email=None)]


UPDATE users
SET email=concat(users.username, '@ya.ru')
WHERE users.username ILIKE '%o%'
RETURNING users.id
