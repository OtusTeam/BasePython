from django.db import models

# Create your models here.
# 1 - 1, 1 - *, * - *

# Медведь - Маша - Мёд
# Тигр - Николай - Мясо
# Карточка животного (текст)


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f'{self.name}/{self.category}'


class Card(models.Model):
    text = models.TextField()
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
