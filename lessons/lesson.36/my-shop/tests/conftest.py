from pytest import fixture


@fixture(scope="session", autouse=True)
def migrate_db():
    from app import app
    from flask_migrate import upgrade

    with app.app_context():
        upgrade()
