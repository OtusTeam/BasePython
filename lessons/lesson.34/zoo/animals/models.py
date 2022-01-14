from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=128,
                            db_index=True,
                            unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'вид животного'
        verbose_name_plural = 'виды животных'
        ordering = ['name']


# animal_kind_1.animal_set.filter()


class Animal(models.Model):
    name = models.CharField(max_length=64)
    kind = models.ForeignKey(AnimalKind,
                             on_delete=models.CASCADE,
                             null=True)
    # alt_animal = models.ForeignKey('Animal',
    #                                on_delete=models.CASCADE,
    #                                null=True)
    age = models.PositiveSmallIntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} <{self.kind}>'
        # return f'{self.name} <{self.kind_id}>'
        # return f'{self.name}'

    def my_food(self):
        food = self.animalfood_set.all()
        return ', '.join(map(str, food))

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     pass

    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = 'животные'
        ordering = ['pk']


class AnimalDetail(models.Model):
    animal = models.OneToOneField('animals.Animal',
                                  primary_key=True,
                                  on_delete=models.CASCADE)
    biography = models.TextField()

    def __str__(self):
        return self.biography


class AnimalFood(models.Model):
    name = models.CharField(max_length=64, unique=True)
    animal = models.ManyToManyField(Animal)

    def __str__(self):
        return self.name
