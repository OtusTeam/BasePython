from flask_combo_jsonapi import ResourceList, ResourceDetail


from models import Computer
from models.database import db
from schemas import ComputerSchema


class ComputerList(ResourceList):
    schema = ComputerSchema
    data_layer = {
        "session": db.session,
        "model": Computer,
    }


class ComputerDetail(ResourceDetail):
    schema = ComputerSchema
    data_layer = {
        "session": db.session,
        "model": Computer,
    }
