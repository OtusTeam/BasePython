from flask import Flask
from flask import request
from flask import render_template

from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(items_app, url_prefix="/items")
app.register_blueprint(products_app)

app.config.update(
    SECRET_KEY="42ba97397b44e2296d2a4eb1e03e432d978124",
)


@app.get("/", endpoint="index")
def hello_root():
    return render_template("index.html")


@app.get("/loading/")
def loading_page():
    return render_template("loading.html")


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
