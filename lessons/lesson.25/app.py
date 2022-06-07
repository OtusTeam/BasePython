from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.products import products_app
from models.database import db

app = Flask(__name__)
app.config.update(
    ENV="development",
    SECRET_KEY="qwertytrewsupersecret",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://username:passwd!@localhost:5432/blog",
)

app.register_blueprint(products_app, url_prefix="/products")

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
# db.app = app
# with app.app_context():
#     # db.create_all()
#     db.drop_all()


# @app.route("/")
# def hello_world():
#     # print_request()
#     return "<h1>Hello, World!</h1>"


@app.route("/")
def index_page():
    print(request.path)
    print(vars(request.url_rule))
    print(vars(request))
    return render_template("index.html")


# def print_request():
#     print(request)


@app.get("/hello/")
def hello_name():
    # print_request()

    # name = "World"
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello, {name}!"}


@app.get("/items/<int:item_id>/")
def get_item(item_id: int):
    return {
        "item": {"id": item_id},
    }


@app.get("/items/<item_id>/")
def get_item_str(item_id: str):
    return {
        "item_id": item_id.upper(),
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
