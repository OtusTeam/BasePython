from flask import Flask, request, render_template

from views.products.views import products_app

app = Flask(__name__)
app.register_blueprint(products_app)


@app.route("/", endpoint="index")
def root():
    words = ["foo", "bar", "spam", "eggs"]
    return render_template("index.html", words=words)


@app.get("/hello/")
def hello_view():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    ids = request.args.getlist("id")
    return {"message": f"Hello {name}!", "ids": ids}


@app.get("/hello/<name>/")
def hello_path_view(name):
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
