from flask import Flask
from flask_combo_jsonapi import Api
from combojsonapi.spec import ApiSpecPlugin

from models.database import db
from views import PersonList, PersonDetail, ComputerList, ComputerDetail

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
db.init_app(app)


api_spec_plugin = ApiSpecPlugin(
    app=app,
    tags={
        "Person": "Persons API",
        "Computer": "Computers API",
    },
)

api = Api(
    app,
    plugins=[
        api_spec_plugin,
    ],
)

api.route(PersonList, "person_list", "/persons", tag="Person")
api.route(PersonDetail, "person_detail", "/persons/<int:id>", tag="Person")
api.route(ComputerList, "computer_list", "/computers", tag="Computer")
api.route(ComputerDetail, "computer_detail", "/computers/<int:id>", tag="Computer")


@app.route("/")
def hello():
    db.create_all()  # use for only for dev
    return {"message": "Hello world!"}


if __name__ == "__main__":
    app.run()
