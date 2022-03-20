from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(null=True)
    kind = models.CharField(max_length=32)
    desc = models.TextField(blank=True)
