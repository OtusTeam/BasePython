from django.core.management.base import BaseCommand

from animals.models import AnimalKind, Animal

from mixer.backend.django import mixer, Mixer


class Command(BaseCommand):
    def handle(self, *args, **options):
        # AnimalKind.objects.all().delete()
        # Animal.objects.all().delete()
        #
        # # animal_1 = mixer.blend(Animal)
        # # animal_1 = mixer.blend(Animal, kind__name='lion')
        # # print(vars(animal_1))
        #
        # # lions = mixer.cycle(3).blend(Animal, kind__name='lion')
        # # print([el.kind.name for el in lions])
        #
        # # mixer.blend(AnimalKind)
        # mixer.cycle(2).blend(AnimalKind)
        #
        # new_animals = mixer.cycle(5).blend(
        #     Animal,
        #     # kind__name=(el for el in ['lion', 'monkey', 'horse']),
        #     # kind__name=mixer.RANDOM('lion', 'monkey', 'horse'),
        #     kind=mixer.SELECT,
        #     # name=mixer.sequence(lambda x: f'animal_{x}'),
        # )
        # print([el.kind.name for el in new_animals])
        #
        # animal_kinds = AnimalKind.objects.all()
        # animals = Animal.objects.all()
        # print(f'AnimalKinds: {animal_kinds}')
        # print(f'Animals: {animals}')

        # MyUser
        # new_user = mixer.blend('myauth.MyUser')
        # new_user = mixer.blend('myauth.MyUser',
        #                        username=mixer.MIX.last_name)
        # new_user = mixer.blend('myauth.MyUser',
        #                        username=mixer.MIX.last_name(
        #                            lambda x: x.lower()
        #                        ))

        my_mixer = Mixer(locale='ru_RU')
        new_animal = my_mixer.blend(Animal)
        print(vars(new_animal))

