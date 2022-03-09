from flask import Flask
from flask_migrate import Migrate

from models.database import db
from views.products import products_app

app = Flask(__name__)

app.config.update(
    SECRET_KEY="\xe4X\xb2\xd6\xf2\x94\xca\xd3m\xccMM\x07l",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://app:password@localhost/shop",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(products_app, url_prefix="/products")


# @app.route("/")
@app.get("/")
def hello_world():
    return "<p>Hello, World!!! (again)</p>"


@app.route("/items/<int:item_id>/")
def get_item(item_id):
    return {"item_id": item_id}


@app.get("/hello/")
# @app.get("/hello/<string:name>/")
@app.get("/hello/<name>/")
def hello_user(name="World"):
    return {"message": f"Hello {name}!"}


# @app.get("/authors/<int:author_id>/books/")
@app.get("/authors/<int:author_id>/books/<int:book_id>/")
def get_authors_book_by_id(author_id: int, book_id: int):
    # res = author_id / book_id
    return {
        "author_id": author_id,
        "book_id": book_id,
        # "div": res,
    }
