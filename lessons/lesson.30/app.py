from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.items import items_app
from views.products import products_app

import config
from models import db

app = Flask(__name__)

# python -c 'import secrets; print(secrets.token_hex())'

app.config.update(
    SECRET_KEY="6fc01f2db60feff0f53537060",
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)

app.register_blueprint(
    items_app,
)
app.register_blueprint(
    products_app,
)
db.init_app(app)
migrate = Migrate(app, db)


# with app.app_context():
#     db.create_all()


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


# @app.get("/hello/")
# def hello_view():
#     name = request.args.get("name", "")
#     name = name.strip()
#     if not name:
#         name = "World"
#     # return {"message": "Hello, World!"}
#     # return jsonify([{"message": "Hello, World!"}])
#     return jsonify(message=f"Hello, {name}!")


@app.route("/hello/")
@app.get("/hello/<name>/")
def hello_path_view(name: str | None = None):
    print(request)
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
