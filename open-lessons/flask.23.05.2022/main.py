from flask import Flask, request

from views.products import products_app

app = Flask(__name__)
app.config.update(ENV="development")

app.register_blueprint(
    products_app,
    url_prefix="/products",
)


@app.route("/")
def hello_world():
    # another_func()
    return "<p>Hello, World!!</p>"


def another_func():
    print(request)
    print(request.path)


@app.route("/hello/")
def hello_view():
    # another_func()
    name = request.args.get("name", "World")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello {name}!"}


@app.route("/items/<int:item_id>/")
def get_item(item_id: int):
    return {"item_id": item_id}


@app.route("/items/<string:item_id>/")
def get_item_str(item_id: str):
    return {"item": {"id": item_id.lower()}}


if __name__ == '__main__':
    app.run(debug=True)
