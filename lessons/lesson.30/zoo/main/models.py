from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=32)
    kind = models.TextField()
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
