from datetime import datetime

from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from users.models import MyUser


class Command(BaseCommand):
    help = "Learn mixer"

    def handle(self, *args, **options):
        # animal = mixer.blend(Animal)
        # animal = mixer.blend(Animal, category__name='tiger')
        # animals = mixer.cycle(3).blend(Animal)
        # animals = mixer.cycle(2).blend(
        #     Animal,
        #     category__name=(name for name in ('monkey2', 'elephant2')),
        # )
        # print(animals)

        # user = mixer.blend(MyUser, username=mixer.MIX.email)
        user = mixer.blend(
            MyUser,
            username=mixer.MIX.email,
            # b_year=mixer.RANDOM(2005, 2007, 2009, 2012),
            b_year=mixer.RANDOM(*[year for year in range(1970, 2015)]),
        )
        print(vars(user))
