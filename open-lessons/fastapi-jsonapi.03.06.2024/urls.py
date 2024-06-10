from typing import ClassVar

from fastapi import (
    APIRouter,
    Depends,
)

from fastapi_jsonapi import RoutersJSONAPI
from fastapi_jsonapi.misc.sqla.generics.base import (
    ListViewBaseGeneric,
    DetailViewBaseGeneric,
)
from fastapi_jsonapi.views.utils import (
    HTTPMethodConfig,
    HTTPMethod,
)
from fastapi_jsonapi.views.view_base import ViewBase
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from db import Connector
from models import (
    User,
    UserBio,
)
from schemas import (
    UserSchema,
    UserUpdateSchema,
    UserBioSchema,
    UserBioUpdateSchema,
)


class SessionDependency(BaseModel):
    session: AsyncSession = Depends(Connector.get_session)

    class Config:
        arbitrary_types_allowed = True


def session_dependency_handler(view: ViewBase, dto: SessionDependency):
    return {
        "session": dto.session,
    }


class DetailView(DetailViewBaseGeneric):
    method_dependencies: ClassVar = {
        HTTPMethod.ALL: HTTPMethodConfig(
            dependencies=SessionDependency,
            prepare_data_layer_kwargs=session_dependency_handler,
        ),
    }


class ListView(ListViewBaseGeneric):
    method_dependencies: ClassVar = {
        HTTPMethod.ALL: HTTPMethodConfig(
            dependencies=SessionDependency,
            prepare_data_layer_kwargs=session_dependency_handler,
        ),
    }


def register_routes(router: APIRouter) -> None:
    default_methods = [
        RoutersJSONAPI.Methods.GET_LIST,
        RoutersJSONAPI.Methods.POST,
        RoutersJSONAPI.Methods.GET,
        RoutersJSONAPI.Methods.PATCH,
        RoutersJSONAPI.Methods.DELETE,
    ]
    RoutersJSONAPI(
        router=router,
        path="/users",
        tags=["User"],
        class_detail=DetailView,
        class_list=ListView,
        model=User,
        schema=UserSchema,
        resource_type="user",
        schema_in_patch=UserUpdateSchema,
        methods=default_methods,
    )

    RoutersJSONAPI(
        router=router,
        path="/user-bio",
        tags=["User", "User Bio"],
        class_detail=DetailView,
        class_list=ListView,
        model=UserBio,
        schema=UserBioSchema,
        resource_type="user_bio",
        schema_in_patch=UserBioUpdateSchema,
        methods=default_methods,
    )
