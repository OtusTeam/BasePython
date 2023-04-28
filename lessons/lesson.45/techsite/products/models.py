from typing import TYPE_CHECKING

from django.db import models


class Device(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32, unique=True)


class Card(models.Model):
    extra_info = models.CharField(max_length=200)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=32, unique=True, blank=True, null=True)
    device_name = models.CharField(max_length=32, unique=True, blank=True, null=True)

    if TYPE_CHECKING:
        objects: models.Manager
