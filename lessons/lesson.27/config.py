from os import getenv

db_url = "sqlite:///./blog.db"

# всегда False
db_echo = False

# только по переменной окружения можем включить
if getenv("DB_ECHO") == "1":
    db_echo = True
