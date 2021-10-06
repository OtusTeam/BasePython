from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(verbose_name='about')

    def __str__(self):
        return f'{self.name}'


class Animal(models.Model):
    name = models.CharField(max_length=64)
    kind = models.ForeignKey(
        AnimalKind,
        on_delete=models.CASCADE,
        related_name='animals',
    )
    age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.name} ({self.kind})'
        # return f'{self.name} ({self.kind_id})'


class AnimalProfile(models.Model):
    animal = models.OneToOneField(Animal,
                                  on_delete=models.CASCADE,
                                  primary_key=True)
    desc = models.TextField(verbose_name='about')

    def __str__(self):
        return f'{self.animal}'


# class Scientist(models.Model):
#     speciality = models.ForeignKey(
#         AnimalKind,
#         on_delete=models.CASCADE,
#         related_name='learning_animals',
#     )


class Food(models.Model):
    name = models.CharField(max_length=16)
    kinds = models.ManyToManyField(AnimalKind)
