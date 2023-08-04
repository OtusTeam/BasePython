from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)


class Base:
    # __tablename__ = "Cherry"
    # __tablename__ = "cherrys"
    # __tablename__ = "cherries"

    @declared_attr
    def __tablename__(cls):
        # prefix = config.TABLES_PREFIX
        # return f"{prefix}{cls.__name__.lower()}s"
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    # @declared_attr
    # def user_id(self):
    #     return Column(ForeignKey("user_account.id"))
    #
    # @declared_attr
    # def user(self):
    #     return relationship("User")
    #
    # @declared_attr
    # def __mapper_args__(cls):
    #     if cls.__name__ == 'Employee':
    #         return {
    #             "polymorphic_on": cls.type,
    #             "polymorphic_identity": "Employee"
    #         }
    #     else:
    #         return {"polymorphic_identity": cls.__name__}


Base = declarative_base(cls=Base)
