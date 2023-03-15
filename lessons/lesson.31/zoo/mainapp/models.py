from django.db import models

# Create your models here.
# Животные, надо кормить, разной едой, делятся на категории, медведи, попугаи, ...
# Карточка - описание животного
#


class Food(models.Model):
    name = models.CharField(max_length=32, unique=True)
    # categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Category(models.Model):
    # Медведь, Белый медведь
    name = models.CharField(unique=True, max_length=32)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name



class Animal(models.Model):
    name = models.CharField(max_length=32)
    # 1-1, 1-*, *-*
    # cascade, protect, setnull
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Card(models.Model):
    text = models.TextField(blank=True, null=True)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal.name







