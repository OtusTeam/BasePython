from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declared_attr


class UserRelationMixin:
    _user_relation_unique = False

    @declared_attr
    def user_id(cls):
        return Column(
            Integer,
            ForeignKey("users.id"),
            unique=cls._user_relation_unique,
            nullable=False,
        )
