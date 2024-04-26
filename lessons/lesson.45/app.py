from flask import Flask, request

from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(
    items_app,
    # url_prefix="/items",
)
app.register_blueprint(
    products_app,
)


@app.get("/")
def index():
    return "Hello, World!"


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
