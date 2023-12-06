from os import getenv

from flask import Flask, request, render_template
from flask_migrate import (
    Migrate,
    migrate as migrate_command,
    upgrade as upgrade_command,
)
from views.products.views import products_app
from models import db


app = Flask(__name__)
app.register_blueprint(products_app)

CONFIG_NAME = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")

db.init_app(app)
migrate = Migrate(app, db)


def create_migration():
    with app.app_context():
        migrate_command()
        # with app.request_context():
        #     pass


@app.cli.command("apply-migrations")
def run_migration():
    with app.app_context():
        upgrade_command()


@app.route("/", endpoint="index")
def root():
    words = ["foo", "bar", "spam", "eggs"]
    return render_template("index.html", words=words)


@app.get("/hello/")
def hello_view():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    ids = request.args.getlist("id")
    return {"message": f"Hello {name}!", "ids": ids}


@app.get("/hello/<name>/")
def hello_path_view(name):
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
