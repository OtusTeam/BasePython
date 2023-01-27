from flask import Flask
from flask import jsonify
from flask import request
from flask import flash
from flask import render_template
from flask import redirect

from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.exc import DatabaseError

from models import db

from werkzeug.exceptions import NotFound

from views.products import products_app

app = Flask(
    __name__,
)
app.register_blueprint(products_app, url_prefix="/products")

app.config.update(
    ENV="development",
    SECRET_KEY="sfgsdgsdhshjwrywgxhsetsdfxg",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://demouser:demopass@postgres:5432/blog",
    # SQLALCHEMY_ECHO=True,
)

csft = CSRFProtect(app)

db.init_app(app)
# migrate = Migrate(app, db, compare_type=True)
migrate = Migrate(app, db)


@app.cli.command("db-create-all")
def db_create_all():
    print(db.metadata.tables)
    # db.create_all()


def print_request():
    print("request:", request)
    print("headers", request.headers)


@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello_world(name: str = None):
    if name is None:
        name = request.args.get("name", "world")
    return f"<h2>Hello {name}!</h2>"


@app.get("/items/")
def get_items():
    return jsonify(
        {
            "items": [
                {"id": 1},
                {"id": 2},
            ],
        },
        # spam="eggs",
    )


@app.get("/items/<int:item_id>/")
def get_item(item_id: int):
    return {"item": {"id": item_id}}


@app.get("/items/<item_id>/")
def get_item_as_string(item_id: str):
    return {"item_id": item_id.upper()}


@app.errorhandler(DatabaseError)
def handle_database_error(error):
    flash("oops! no db connection!", "danger")
    return redirect("/")

# @app.errorhandler(404)
# def handle_404(error):
#     if isinstance(error, NotFound) and error.description != NotFound.description:
#         return error
#     # return f"<h1>eroror: {error}</h1>", 404
#     return render_template("404.html"), 404
