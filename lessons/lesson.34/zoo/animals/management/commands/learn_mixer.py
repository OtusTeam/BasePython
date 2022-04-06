from django.core.management.base import BaseCommand

from mixer.backend.django import mixer


class Command(BaseCommand):

    def handle(self, *args, **options):
        # with transaction.atomic:
        # animal = mixer.blend('animals.Animal',
        #                      kind__name='dog')
        # print(vars(animal))
        # print(animal.kind)
        # animals = mixer.cycle(3).blend('animals.Animal')
        # # __str__, __repr__
        # print(animals)
        # animals = mixer.cycle(3).blend(
        #     'animals.Animal',
        #     name=mixer.sequence(lambda x: f'animal_{x}')
        # )
        # print(animals)
        new_user = mixer.blend('myauth.MyUser',
                               username=mixer.MIX.last_name)
        print(new_user.username, new_user.last_name)
