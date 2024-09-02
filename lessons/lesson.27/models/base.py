from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

import config
from utils.case_converter import camel_case_to_snake_case


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"

    metadata = MetaData(
        naming_convention=config.SQLALCHEMY_NAMING_CONVENTION,
    )
