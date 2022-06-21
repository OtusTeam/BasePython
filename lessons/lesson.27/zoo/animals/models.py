from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(null=True)
    kind = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Animal #{self.id} {self.name!r}>"
