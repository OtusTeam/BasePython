import asyncio
from datetime import date

from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, default="")
    birth_date = db.Column(db.Date())

    def __str__(self):
        return f"User(id={self.id}, name={self.name!r}, birth_date={self.birth_date!r}))"


async def main():
    await db.set_bind("postgresql://user:password@localhost/postgres")
    # await db.gino.create_all()

    user = await User.create(name="Robin", birth_date=date(1977, 1, 19))
    print(user)

    bob: User = await User.query.where(User.name == "Bob").gino.one()
    print(bob)
    await bob.update(birth_date=date(1988, 11, 23)).apply()
    print(bob)

    population = await db.func.count(User.id).gino.scalar()
    print("Total users:", population)

    all_users = await User.query.order_by(User.id).gino.all()
    for user in all_users:
        print(user)

    await db.pop_bind().close()


if __name__ == '__main__':
    asyncio.run(main())
