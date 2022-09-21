from typing import TYPE_CHECKING

from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    kind = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    if TYPE_CHECKING:
        objects: models.Manager

    # def price_with_discount(self):
    # @property
    # def desc_short(self) -> str:
    #     self.description: str
    #     if len(self.description) < 40:
    #         return self.description
    #     return self.description[:38] + "..."

    def __str__(self):
        return self.name
