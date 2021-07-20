from flask import Flask, request, render_template
from flask_migrate import Migrate, upgrade

from web_app.models import db
from web_app.views.products import products_app

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(products_app)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/hello/")
def hello_name_qs():
    name = request.args.get("name", "World")
    return f"Hello {name}!"


@app.route("/hello/<name>/")
def hello_name_path(name):
    return f"Hello {name}!"


@app.cli.command(help="Create all tables using metadata.create_all")
def create_all_tables():
    print("Hello flask command")
    with app.app_context():
        upgrade()
        # db.metadata.create_all()


if __name__ == '__main__':
    app.run(debug=True)
