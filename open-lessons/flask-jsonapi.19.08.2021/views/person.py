from flask_combo_jsonapi import ResourceList, ResourceDetail

from models import Person
from models.database import db
from schemas import PersonSchema


class PersonList(ResourceList):
    schema = PersonSchema
    data_layer = {
        "session": db.session,
        "model": Person,
    }


class PersonDetail(ResourceDetail):
    schema = PersonSchema
    data_layer = {
        "session": db.session,
        "model": Person,
    }
