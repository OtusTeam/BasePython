from os import getenv

from flask import Flask, request, render_template
from flask_migrate import Migrate

from models import db
from views.items import items_app
from views.products import products_app


app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///project.db")
config_name = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")

db.init_app(app=app)
migrate = Migrate(app=app, db=db)

app.register_blueprint(items_app)
app.register_blueprint(products_app)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


@app.get("/hello/")
def handle_hello():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello {name}!"}


@app.get("/hello/<name>/")
def handle_hello_name(name: str):
    return {"message": f"Hello {name}!"}
