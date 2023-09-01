from flask import Flask, request, render_template
from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(items_app)
app.register_blueprint(products_app)


@app.get("/")
def get_index():
    return render_template("index.html")


@app.get("/hello/")
def handle_hello():
    name = request.args.get("name", "")
    print(request.args)
    print(request.args.get("foo"))
    print(request.args.getlist("foo"))
    print(request.args.getlist("spam"))
    print(request.args.getlist("fizz"))
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello {name}!"}


@app.get("/hello/<name>/")
def handle_hello_name(name: str):
    return {"message": f"Hello {name}!"}
