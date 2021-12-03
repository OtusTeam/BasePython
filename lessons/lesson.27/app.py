import os

from flask import Flask
from flask_migrate import Migrate
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import HTTPException

from models import db
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")

CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def root():
    return "<h1>Hello World!</h1>"


@app.route("/items/")
@app.route("/items/<int:item_id>/")
def get_item(item_id=None):
    return {"item_id": item_id}


# @app.before_request
#
# @app.after_request


@app.errorhandler(KeyError)
def handle_key_error(exc):
    return InternalServerError(f"oops, could not find that by key {exc}!")


@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(exc):
    print("exc", exc)
    return InternalServerError("oops, could divide that!")


# @app.errorhandler(Exception)
# def handle_all_exception(exc):
#     if isinstance(exc, HTTPException):
#         return exc
#     print("exc", exc)
#     return InternalServerError("oops, unexpected exception!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
