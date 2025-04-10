from typing import Optional

from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import Mapped, Session
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from models import engine


class Base(DeclarativeBase):
    pass


class Association(Base):
    __tablename__ = "association_table"

    left_id: Mapped[int] = mapped_column(ForeignKey("left_table.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(
        ForeignKey("right_table.id"), primary_key=True
    )
    extra_data: Mapped[Optional[str]]

    # association between Assocation -> Child
    child: Mapped["Child"] = relationship(back_populates="parent_associations")

    # association between Assocation -> Parent
    parent: Mapped["Parent"] = relationship(back_populates="child_associations")


class Parent(Base):
    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    # many-to-many relationship to Child, bypassing the `Association` class
    children: Mapped[list["Child"]] = relationship(
        secondary="association_table", back_populates="parents"
    )

    # association between Parent -> Association -> Child
    child_associations: Mapped[list["Association"]] = relationship(
        back_populates="parent"
    )


class Child(Base):
    __tablename__ = "right_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    # many-to-many relationship to Parent, bypassing the `Association` class
    parents: Mapped[list["Parent"]] = relationship(
        secondary="association_table", back_populates="children"
    )

    # association between Child -> Association -> Parent
    parent_associations: Mapped[list["Association"]] = relationship(
        back_populates="child"
    )


engine = create_engine(
    url="sqlite:///:memory:",
    connect_args={"check_same_thread": False},
)


def main():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        p1 = Parent()
        c1 = Child()
        c2 = Child()
        p1.children.append(c1)

        p1.child_associations.append(Association(child=c2))

        session.add(p1)
        session.add(c1)
        session.add(c2)
        session.commit()

        print(session.scalars(select(Parent)).all())
        print(session.scalars(select(Child)).all())


if __name__ == "__main__":
    main()
