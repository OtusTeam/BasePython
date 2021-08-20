from flask import Flask
from flask_combo_jsonapi import Api
from combojsonapi.event import EventPlugin
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.permission import PermissionPlugin

from models.database import db
from views import PersonList, PersonDetail, ComputerList, ComputerDetail, PersonRelationship

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


event_plugin = EventPlugin(trailing_slash=False)

permission_plugin = PermissionPlugin(strict=False)

api = Api(
    app,
    plugins=[
        event_plugin,
        api_spec_plugin,
        # permission_plugin,
    ],
)

api.route(
    PersonList, "person_list", "/persons", tag="Person")
api.route(
    PersonDetail,
    "person_detail",
    "/persons/<int:id>",
    # "/computers/<int:computer_id>/owner",
    tag="Person",
)
api.route(
    PersonRelationship,
    "person_computers",
    "/persons/<int:id>/relationships/computers",
)

api.route(
    ComputerList, "computer_list", "/computers", tag="Computer")
api.route(
    ComputerDetail, "computer_detail", "/computers/<int:id>", tag="Computer")


@app.route("/")
def hello():
    db.create_all()  # use for only for dev
    return {"message": "Hello world!"}


if __name__ == "__main__":
    app.run()
