from django.core.management.base import BaseCommand
from mixer.backend.django import mixer


class Command(BaseCommand):
    def handle(self, *args, **options):
        # animal = mixer.blend('main.Animal')
        # print(animal, type(animal))
        # print(vars(animal))
        # print(vars(animal.kind), type(animal.kind))

        # getattr(globals(), 'Command')

        # animals = mixer.cycle(1).blend('main.Animal', kind__name='lion')
        # animals = mixer.cycle(1).blend('main.Animal')
        # for el in animals:
        #     print(el, el.kind)

        # user = mixer.blend('myauth.MyUser', username=mixer.MIX.email)
        user = mixer.blend('myauth.MyUser')
        print(vars(user))
