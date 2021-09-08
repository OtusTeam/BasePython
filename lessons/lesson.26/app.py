from flask import Flask, request
from flask_migrate import Migrate

from models.database import db
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")

app.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///./products.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    # return "Hello, World!"
    return "<p>Hello, World!</p>"


@app.route("/hello/")
def hello_name():
    name = request.args.get("name", "World")
    return {
        "message": f"Hello {name}!"
    }


@app.route("/item/")
@app.route("/item/<int:item_id>/")
def get_item(item_id: int = 42):
    return {"item_id": item_id}


@app.route("/calc/")
def calc_numbers():
    a = 1
    b = "2"
    # b = 2
    return str(a + b)
