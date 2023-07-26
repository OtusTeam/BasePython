from flask import Flask
from flask import request

from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(items_app, url_prefix="/items")
app.register_blueprint(products_app)


@app.get("/")
def hello_root():
    return "Hello World!"


def hello_qs():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return f"Hello {name}!"


@app.get("/hello/")
@app.get("/hello/<name>/")
def hello_path(name: str | None = None):
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run(debug=True)
