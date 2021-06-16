from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=32)
    kind = models.TextField()
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
