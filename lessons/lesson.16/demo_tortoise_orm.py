from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

PG_CONN_URI = "postgres://user:password@localhost/project"


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)

    events: fields.ReverseRelation["Event"]

    def __str__(self):
        return self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)
    description = fields.TextField()
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament",
        related_name="events",
    )

    def __str__(self):
        return self.name


async def run():
    await Tortoise.init(db_url=PG_CONN_URI, modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    tournament = Tournament(name="New Tournament")
    await tournament.save()

    event1 = Event(
        name="Another one",
        description="Big description",
        tournament_id=tournament.id,
    )
    await event1.save()
    print("event 1", event1)
    event2 = Event(
        name="Without participants",
        description="Some huge desc",
        tournament=tournament,
    )
    await event2.save()
    print("event 2", event2)
    print("event 2'd", event2.tournament)

    t = await Tournament.first()
    print("Tournament", t)
    await t.fetch_related("events")
    print("Tournament events:", t.events.all())


if __name__ == "__main__":
    run_async(run())
