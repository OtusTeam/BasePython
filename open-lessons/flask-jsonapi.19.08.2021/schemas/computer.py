from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

from combojsonapi.utils import Relationship


class ComputerSchema(Schema):
    class Meta:
        type_ = "computer"
        self_view = "computer_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "computer_list"

    id = fields.Integer(as_string=True, dump_only=True)
    serial = fields.String(required=True)
    owner = Relationship(
        type_="person",
        attribute="person",
        schema="PersonSchema",
        nested="PersonSchema",
        related_view="person_detail",
        related_view_kwargs={"id": "<id>"},
        self_view="computer_person",
        self_view_kwargs={"id": "<id>"},
    )
