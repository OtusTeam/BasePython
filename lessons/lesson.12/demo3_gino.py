import asyncio
from datetime import date

from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)

    def __str__(self):
        values = [f"{n}={getattr(self, n)}" for n in ("id", "name", "birth_date")]
        return f"{self.__class__.__name__}({', '.join(values)})"

    __repr__ = __str__


async def main():
    await db.set_bind("postgresql://username:password@localhost/demo")
    users = await db.all(User.query)
    print(users)
    john = await User.get(7)
    print("John?", john)
    user = await User.create(name="Sam", birth_date=date(1991, 2, 8))
    print("New:", user)

    johns = await User.query.where(User.name == "John").gino.all()
    print("Johns:", johns)
    users_count = await db.func.count(User.id).gino.scalar()
    print("Total:", users_count)


if __name__ == "__main__":
    asyncio.run(main())
