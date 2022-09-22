from typing import TYPE_CHECKING

from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    kind = models.ForeignKey(AnimalKind, on_delete=models.PROTECT, related_name="animal")
    description = models.TextField(blank=True, null=False)
    food = models.ManyToManyField("animals.AnimalFood", related_name="animals")

    if TYPE_CHECKING:
        objects: models.Manager

    def __str__(self):
        return self.name


class AnimalProfile(models.Model):
    animal = models.OneToOneField(
        Animal,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    origin = models.CharField(max_length=64)
    biography = models.TextField()

    def __str__(self):
        return f"Animal #{self.animal.pk} from {self.origin}"


class AnimalFood(models.Model):
    class Meta:
        verbose_name_plural = "Animal food"

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name
