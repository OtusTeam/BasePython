DB_FILENAME = "blog.db"
DB_URL = f"sqlite:///{DB_FILENAME}"
# DB_ECHO = ("some-env" in os.environ) or True  # временно вкл. всегда выкл!
DB_ECHO = False
if 1:  # временно!
    DB_ECHO = True
