from flask import (
    Flask,
    request,
    render_template,
)

from flask_migrate import Migrate

from models import db
from views.items import items_app
from views.products import products_app


app = Flask(__name__)
app.config.update(
    SECRET_KEY="616b2180ee260174500b1042c648dff4fe3476137dd0c7b32792a9f8efb1c3b5",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg://user:example@localhost:5432/blog",
    SQLALCHEMY_ECHO=True,
)

app.register_blueprint(items_app)
app.register_blueprint(products_app)

db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="index")
def hello_world():
    return render_template("index.html")


# @app.route("/hello/")
# def hello_from_qs():
#     print("args:", request.args)
#     name = request.args.get("name", "")
#     foo = request.args.getlist("foo")
#     # foo = request.args.get("foo")
#     return {"message": f"Hello, {name}!", "foo": foo}
#
#
# @app.get("/hello/<name>/")
# def hello_name(name):
#     return {"message": f"Hello, {name}!"}


@app.get("/hello/")
@app.get("/hello/<name>/")
def hello_name(name=None):
    if name is None:
        name = request.args.get("name", "")

    name = name.strip() or "World"
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
