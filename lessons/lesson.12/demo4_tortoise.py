from tortoise import Tortoise, run_async, fields
from tortoise.models import Model


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url="postgres://username:password@localhost/demo",
        modules={'models': ['__main__']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def main():
    await init()

    tournament = Tournament(name='New Tournament')
    await tournament.save()

    # Or by .create()
    await Tournament.create(name='Another Tournament')

    # Now search for a record
    tour = await Tournament.filter(name__contains='Another').first()
    print(tour.id, tour.name)


if __name__ == "__main__":
    # run_async is a helper function to run simple async Tortoise scripts.
    # run_async(init())
    run_async(main())
