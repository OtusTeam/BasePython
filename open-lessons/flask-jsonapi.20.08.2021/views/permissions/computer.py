from .base import BaseAllowGetAllPermission


class ComputerPermission(BaseAllowGetAllPermission):
    ALL_FIELDS = [
        "id",
        "serial",
        "owner",
    ]
