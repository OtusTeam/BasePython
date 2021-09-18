from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=64)
    kind = models.TextField()
    age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'
