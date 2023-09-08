from flask import Flask, request, render_template
from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(items_app)
app.register_blueprint(products_app)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


@app.get("/hello/")
def handle_hello():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello {name}!"}


@app.get("/hello/<name>/")
def handle_hello_name(name: str):
    return {"message": f"Hello {name}!"}
