from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
from combojsonapi.utils import Relationship


class PersonSchema(Schema):
    class Meta:
        type_ = "person"
        self_view_many = "person_list"
        self_view = "person_detail"
        self_view_kwargs = {"id": "<id>"}

    id = fields.Integer(as_string=True)
    name = fields.String()
    birth_date = fields.Date()
    computers = Relationship(
        type_="computer",
        schema="ComputerSchema",
        nested="ComputerSchema",
        many=True,
        related_view="computer_list",
        # related_view_kwargs={"id": "<id>"},
        self_view="person_computers",
        self_view_kwargs={"id": "<id>"},
    )
