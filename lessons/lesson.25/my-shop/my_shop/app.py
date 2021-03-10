from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.products import product_app
from models.database import db


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(product_app, url_prefix="/products")


@app.route("/")
def hello_index():
    return render_template("index.html")


@app.route("/demo", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return "Hello, World!"

    # print("data:", request.form)
    # print("name:", request.form.get("name"))
    # print("name list:", request.form.getlist("name"))

    name = request.form.get("name")
    return f"Hello {name}!"


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello(name="World"):
    return f"Hello {name}!!!"

