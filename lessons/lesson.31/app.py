from flask import (
    Flask,
    request,
    render_template,
)
from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(items_app)
app.register_blueprint(products_app)


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
