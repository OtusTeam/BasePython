from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=64)
    # ...animal_set.all()
    # ...animals.all()

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=32)
    kind = models.ForeignKey(
        Kind,
        on_delete=models.CASCADE,
        related_name='animals',
    )  # kind_id
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     pass

    # ....animal.biography

    class Meta:
        verbose_name = 'Zoo animal'
        verbose_name_plural = 'Zoo animals'


class AnimalProfile(models.Model):
    # id = ...
    animal = models.OneToOneField(
        Animal,
        primary_key=True,
        on_delete=models.CASCADE,
    )  # animal_id
    biography = models.TextField()


class Food(models.Model):
    name = models.CharField(max_length=64)
    animal = models.ManyToManyField(Animal)

    def __str__(self):
        return self.name
