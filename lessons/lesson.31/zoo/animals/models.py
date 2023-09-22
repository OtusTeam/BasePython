from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(null=True)
    kind = models.ForeignKey(
        AnimalKind,
        on_delete=models.PROTECT,
        related_name="animals",
        # null=True,
        # null=False,
        # on_delete=models.CASCADE,
        # default=
    )
    # parent_male = models.ForeignKey
    # parent_female

    relatives = models.ManyToManyField(
        "animals.Animal",
        # null=True,
        # blank=True,
    )

    def __str__(self):
        return self.name

