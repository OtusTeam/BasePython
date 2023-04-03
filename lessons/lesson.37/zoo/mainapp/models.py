from django.db import models

# Create your models here.
# Животные, надо кормить, разной едой, делятся на категории, медведи, попугаи, ...
# Карточка - описание животного
#


class Food(models.Model):
    name = models.CharField(max_length=32, unique=True)
    # categories = models.ManyToManyField(Category)
    # Date
    # DateTime
    # Timestamp
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # Number (Int)
    # models.IntegerField
    # models.PositiveIntegerField
    # models.SmallIntegerField
    # models.PositiveSmallIntegerField
    # Float
    # models.FloatField
    # models.DecimalField
    # Bool
    # models.BooleanField
    # Blob, clob
    # models.BinaryField
    # models.ImageField
    # models.FileField
    # Enum
    # models.CharField(max_length=32, unique=True, choices=)
    # models.URLField
    # models.EmailField

    def __str__(self):
        return self.name


class Category(models.Model):
    # Медведь, Белый медведь
    name = models.CharField(unique=True, max_length=32)
    is_active = models.BooleanField(default=True)
    max_age = models.PositiveIntegerField(default=50)
    foods = models.ManyToManyField(Food)
    img = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.name

    def count_category_types(self):
        return self.foods.count()

    def some_error(self):
        raise ValueError('some error')


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







