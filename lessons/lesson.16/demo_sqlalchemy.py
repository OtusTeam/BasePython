import asyncio

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func,
    select,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    joinedload,
    selectinload,
    sessionmaker,
)

SQLALCHEMY_CONN_URI = "postgresql+asyncpg://user:password@localhost/project"

engine = create_async_engine(SQLALCHEMY_CONN_URI, echo=True)

Base = declarative_base()


class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="", server_default="")
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    children = relationship("Child", back_populates="parent")

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, name={self.name!r}, created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="", server_default="")

    parent_id = Column(Integer, ForeignKey(Parent.id), nullable=False)
    parent = relationship("Parent", back_populates="children")

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, name={self.name!r}, parent_id={self.parent_id})"

    def __repr__(self):
        return str(self)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_parents_with_children_opt1():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        session: AsyncSession

        async with session.begin():

            parent = Parent(name="John Smith")
            child_1 = Child(name="Sam")
            child_2 = Child(name="Ann")
            parent.children = [child_1, child_2]

            session.add(parent)

        print(parent)
        print(child_1)
        print(child_2)

    print("done creating (1)")


async def create_parents_with_children_opt2():
    async_session = sessionmaker(engine, class_=AsyncSession)

    async with async_session() as session:
        session: AsyncSession

        async with session.begin():

            parent = Parent(name="John Smith")
            child_1 = Child(name="Sam")
            child_2 = Child(name="Ann")
            parent.children = [child_1, child_2]

            session.add(parent)

        await session.refresh(parent)
        await session.refresh(child_1)
        await session.refresh(child_2)
        print(parent)
        print(child_1)
        print(child_2)

    print("done creating (2)")


async def fetch_parents():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        session: AsyncSession
        stmt = select(Parent).options(selectinload(Parent.children))

        result = await session.execute(stmt)
        print("result parents:", result)

        for parent in result.scalars():
            print(parent)
            print(parent.children)


async def fetch_children():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        session: AsyncSession

        stmt = select(Child).options(joinedload(Child.parent)).order_by(Child.id.desc())
        all_children = await session.execute(stmt)
        print("all_children", all_children)
        result = all_children.scalars()
        print("result children", result)
        last_child: Child = result.first()
        print("last child:", last_child)
        print("and his parent:", last_child.parent)


async def main():
    print("Starting main")
    await create_tables()
    await create_parents_with_children_opt1()
    # await create_parents_with_children_opt2()
    await fetch_parents()
    await fetch_children()


if __name__ == '__main__':
    asyncio.run(main())
