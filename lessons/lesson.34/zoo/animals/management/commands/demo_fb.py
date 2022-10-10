from django.core.management.base import BaseCommand
import factory
from factory.django import DjangoModelFactory

from animals.models import AnimalKind, Animal, AnimalProfile


class AnimalKindFactory(DjangoModelFactory):
    class Meta:
        model = AnimalKind
        django_get_or_create = ("name",)

    # name = factory.Faker("word", locale="ru_RU")
    name = factory.Faker("word")
    description = factory.Faker("sentence", nb_words=7, variable_nb_words=False)


class AnimalFactory(DjangoModelFactory):
    class Meta:
        model = Animal

    name = factory.Faker("name")
    age = factory.Faker("pyint", min_value=1, max_value=20)
    kind = factory.SubFactory(AnimalKindFactory)
    description = factory.Faker("paragraph")
    archived = False


def gen_bio(profile: AnimalProfile) -> str:
    return (
        f"Animal {profile.animal.name}\n"
        f"Description: {profile.animal.kind.description}"
    )


class AnimalProfileFactory(DjangoModelFactory):
    class Meta:
        model = AnimalProfile

    animal = factory.SubFactory(AnimalFactory)
    origin = factory.Faker("city")
    biography = ""

    class Params:
        stray_cat = factory.Trait(
            # biography="hello",
            # biography=factory.Faker("paragraph"),
            # biography=factory.SelfAttribute("animal.kind.description"),
            # biography=factory.LazyAttribute(lambda p: p.origin)
            # biography=factory.LazyAttribute(lambda p: p.origin + p.animal.kind.name)
            biography=factory.LazyAttribute(gen_bio),
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Hello factory boy")

        # profile: AnimalProfile = AnimalProfileFactory()
        profile: AnimalProfile = AnimalProfileFactory(stray_cat=True)
        print([profile, profile.biography, profile.animal, profile.animal.kind, profile.animal.kind.description])

        # animal_kind: AnimalKind = AnimalKindFactory(description="Some description")
        animal_kind: AnimalKind = AnimalKindFactory()
        print(animal_kind, animal_kind.pk, repr(animal_kind.description))

        animal: Animal = AnimalFactory()
        # animal: Animal = AnimalFactory.create()
        print(animal, animal.pk, animal.kind, animal.kind.pk, animal.kind.description)

        animal_kinds: list[AnimalKind] = AnimalKindFactory.build_batch(3)
        for ak in animal_kinds:
            print(ak.pk, ak.name, ak.description)

        animal_kinds: list[AnimalKind] = AnimalKindFactory.create_batch(2)

        for ak in animal_kinds:
            print(ak.pk, ak.name, ak.description)
