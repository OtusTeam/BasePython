from flask_migrate import upgrade

from app import app

with app.app_context():
    print("run migrations")
    upgrade()
