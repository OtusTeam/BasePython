from combojsonapi.event import EventPlugin
from flask_combo_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from flask_combo_jsonapi.data_layers.alchemy import SqlalchemyDataLayer
from flask_combo_jsonapi.exceptions import ObjectNotFound
from sqlalchemy.orm.exc import NoResultFound

from models import Person, Computer
from models.database import db
from schemas import PersonSchema
from views.permissions.person import PersonPermission


class PersonDetailSqlalchemyDataLayer(SqlalchemyDataLayer):

    def before_get_object(self, view_kwargs):
        if not view_kwargs.get("computer_id"):
            return

        try:
            # result = self.session.query(Computer).values("id", "person_id").filter_by(
            computer = self.session.query(Computer).filter_by(
                id=view_kwargs["computer_id"],
            ).one()
        except NoResultFound:
            raise ObjectNotFound(
                "Computer: {} not found".format(view_kwargs["computer_id"]),
                source={"parameter": 'computer_id'},
             )
        else:
            view_kwargs["id"] = computer.person_id


class PersonListEvents(EventPlugin):
    def event_get_info(self):
        return {"message": "Hello Person List events!"}

    def event_refresh_persons(self):
        return {"message": "Persons refreshed!"}


class PersonList(ResourceList):
    schema = PersonSchema
    events = PersonListEvents
    # methods = ["GET"]
    data_layer = {
        "session": db.session,
        "model": Person,
        "permission_get": [PersonPermission],
        # "permission_post": [PersonPermission],
    }


class PersonDetailEvents(EventPlugin):
    def event_update_online_status(self, *args, **kwargs):
        # language=YAML
        """
        ---
        summary: Update person's online status
        tags:
        - Person
        parameters:
        - in: path
          name: id
          required: True
          type: integer
          format: int32
          description: 'person id'
        consumes:
        - application/json
        responses:
          200:
            description: update status
        """
        # some swagger description
        person_id = kwargs["id"]
        # person update status
        return {"status": "updated", "person_id": person_id}

    event_update_online_status.extra = {
        "url_suffix": "update-online",
        "method": "PUT",
    }


class PersonDetail(ResourceDetail):
    schema = PersonSchema
    events = PersonDetailEvents
    # methods = ["GET", "PATCH"]
    # methods = ["GET"]
    data_layer = {
        "class": PersonDetailSqlalchemyDataLayer,
        "session": db.session,
        "model": Person,
        "permission_get": [PersonPermission],
        # "permission_patch": [PersonPermission],
        # "permission_put": [PersonPermission],
        # "permission_delete": [PersonPermission],
    }


class PersonRelationship(ResourceRelationship):
    schema = PersonSchema
    data_layer = {
        'session': db.session,
        'model': Person
    }

