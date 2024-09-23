from flask import (
    Flask,
    request,
    render_template,
)
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

import config

from models import db
from views.items import items_app
from views.products import products_app


app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
    SECRET_KEY=config.SECRET_KEY,
)
app.register_blueprint(items_app)
app.register_blueprint(products_app)

db.init_app(app=app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app=app)


@app.get("/", endpoint="index")
def hello_world():
    return render_template("index.html")


@app.get("/hello/")
@app.get("/hello/<name>/")
def hello_name(name=None):
    if name is None:
        name = request.args.get("name", "")

    name = name.strip() or "World"
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
