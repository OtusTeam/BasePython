from .base import BaseAllowGetAllPermission


class PersonPermission(BaseAllowGetAllPermission):
    ALL_FIELDS = [
        "id",
        "name",
        "birth_date",
        # "email",
        "verbose_name",
        "computers",
    ]
