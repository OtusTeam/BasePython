from django.core.management import BaseCommand
from django.db.models import F

from mixer.backend.django import mixer

from products.models import Device, Card


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("hello")
        # self.stdout.write("create of get device and card")
        # mixer.cycle(8).blend(Device)
        # mixer.cycle(5).blend(Card, device=mixer.SELECT)
        # self.stdout.write("created some data")

        cards = Card.objects.annotate(
            device_type=F("device__type"),
            device_name=F("device__name"),
        ).all()
        # .prefetch_related("device")
        for card in cards:
            print("--")
            print(card.device.name, card.device_name)
            print(card.device.type, card.device_type)
