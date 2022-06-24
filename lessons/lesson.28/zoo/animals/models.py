from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class Animal(models.Model):
    # class Meta:
    #     ...
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(null=True)
    kind = models.ForeignKey(AnimalKind, on_delete=models.PROTECT, null=True)
    description = models.TextField(blank=True, null=False)
    food = models.ManyToManyField("animals.AnimalFood", related_name="animals")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Animal #{self.pk} {self.name!r}>"


class AnimalDetail(models.Model):
    animal = models.OneToOneField(
        Animal,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="details",
    )
    biography = models.TextField(blank=True)

    # @property
    # def bio_short(self):
    #     return self.biography[:50]

    def __str__(self):
        return self.biography


class AnimalFood(models.Model):
    class Meta:
        verbose_name_plural = "Animal food"

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
