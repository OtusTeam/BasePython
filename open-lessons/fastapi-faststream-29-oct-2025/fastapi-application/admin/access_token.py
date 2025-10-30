import secrets
from typing import Any

from sqladmin import ModelView
from starlette.requests import Request

from admin.converter import ModelConverter
from core.models import AccessToken


class AccessTokenAdmin(ModelView, model=AccessToken):
    column_list = [
        AccessToken.token,
        AccessToken.created_at,
        AccessToken.user,
    ]
    form_converter = ModelConverter
    column_default_sort = [
        (AccessToken.created_at, False),
    ]
    form_include_pk = True
    can_edit = False
    form_excluded_columns = [
        AccessToken.user_id,
        AccessToken.created_at,
    ]
    form_create_rules = [
        "user",
        # "token",
    ]

    def insert_model(
        self,
        request: Request,
        data: dict,
    ) -> Any:
        if "token" not in data:
            data.update(token=secrets.token_urlsafe())
        return super().insert_model(
            request=request,
            data=data,
        )
