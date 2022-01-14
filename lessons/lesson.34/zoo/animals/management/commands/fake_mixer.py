from random import randint

from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from animals.models import Animal
from zauth.models import ZooUser


def step_1():
    # new_animal = mixer.blend('animals.Animal')
    # new_animal = mixer.blend(Animal)
    # print(vars(new_animal))
    new_animals = mixer.cycle(5).blend(Animal)
    print(new_animals)


def step_2():
    # new_animal = mixer.blend('animals.Animal',
    #                          kind__name='bee')
    new_animal = mixer.blend('animals.Animal',
                             age=7)
    print(vars(new_animal))
    # print(new_animal.__dict__)


def step_3():
    new_animals = mixer.cycle(3).blend(
        Animal,
        # name=(name for name in ('Alex', 'Bob', 'George')),
        # name=mixer.sequence(lambda x: f'monkey_{x}'),
        # kind=mixer.SELECT,
        # age=mixer.RANDOM,
        age=mixer.sequence(lambda x: randint(1, 9)),
    )
    print([el.age for el in new_animals])


def step_4():
    new_users = mixer.cycle(3).blend(
        ZooUser,
        username=mixer.MIX.last_name,
    )
    print(*map(vars, new_users))


class Command(BaseCommand):

    def handle(self, *args, **options):
        # step_1()
        # step_2()
        # step_3()
        step_4()
