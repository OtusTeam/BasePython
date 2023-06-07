from os import getenv

from flask import Flask
from flask import request
from flask import render_template

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db
from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(items_app, url_prefix="/items")
app.register_blueprint(products_app)

config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
config_object = f"config.{config_class_name}"
app.config.from_object(config_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.get("/", endpoint="index")
def hello_root():
    return render_template("index.html")


@app.get("/loading/")
def loading_page():
    return render_template("loading.html")


@app.get("/hello/")
@app.get("/hello/<name>/")
def hello_path(name: str | None = None):
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
