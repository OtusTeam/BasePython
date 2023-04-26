import os

from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from models import db
from views.items import items_app
from views.products import products_app


config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
app.register_blueprint(items_app)
app.register_blueprint(products_app)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.cli.command("create-all")
def command_create_all():
    with app.app_context():
        db.create_all()


@app.get("/")
def index_view():
    # return "<h1>Hello Index!!</h1>"
    features = ["Items", "Products (WIP)", "Hello views"]
    return render_template("index.html", features=features)


def print_request_info():
    print(request)


# @app.get("/hello-plain/")
# def hello_plain_view():
#     name = "World!"
#     return f"Hello {name}"


@app.get("/hello-plain/")
@app.get("/hello/")
def hello_view():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"

    flash("Hello was flashed!")
    # return f"<h1>Hello {name}!</h1>"
    return render_template("hello.html", name=name)


@app.get("/images/")
@app.get("/images/<path:img_dir>/")
def get_image(img_dir: str = "default/images/path"):
    return {
        "data": {
            "image": "todo load",
            "path": img_dir,
        },
    }


if __name__ == "__main__":
    app.run()
