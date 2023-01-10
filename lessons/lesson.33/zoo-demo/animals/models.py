from django.db import models

# Кормить, карточка, виды животных

# Бурый Медведь, Белый медведь
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    code = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.name

    def exception_method(self):
        raise NotImplementedError()

class Animal(models.Model):
    name = models.CharField(max_length=64)
    # CASCADE, PROTECT, NULL
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # kind = models.CharField('kind', max_length=64)
    age = models.IntegerField(verbose_name='age', default=1)
    desc = models.TextField(verbose_name='description', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # return f'{self.name} ({self.category.name})'
        return f'{self.name}'

    # class Meta:
    #     verbose_name = 'animal'
    #     verbose_name_plural = 'animals'
    #     ordering = ['pk']

class Card(models.Model):
    text = models.TextField(blank=True)
    animal = models.OneToOneField(Animal, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=5, blank=True)



class Food(models.Model):
    name = models.CharField(max_length=128, unique=True)
    animals = models.ManyToManyField(Animal)
