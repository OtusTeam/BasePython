from django.db import models


class Family(models.Model):
    # Медведь, Тигр
    # ID
    # Текстовое поле ограниченной длины
    name = models.CharField(max_length=16, unique=True)
    # Стока любой длины
    # text = models.TextField()
    # Целове число
    # age = models.IntegerField()
    # age = models.PositiveIntegerField()
    # age = models.SmallIntegerField()
    # age = models.PositiveSmallIntegerField()
    # Дата
    # models.DateTimeField
    # models.DateField
    # models.TimeField
    # Логический
    # models.BooleanField
    # Список массив
    # Дробное число
    # models.FloatField
    # Decimal
    # models.DecimalField
    # Blob - Байты
    # models.BinaryField
    # Email
    # models.EmailField
    # Картинка
    # models.ImageField
    # models.FileField
    # Url
    # models.URLField
    # Хэш


class Kind(models.Model):
    # Бурый, Амурский
    name = models.CharField(max_length=16, unique=True)
    # Связь
    # 1 - 1 (редкая)
    # 1 - * (самая распростаненная)
    # * - * (самая сложная)
    # тут 1 ко *
    #
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    # family = models.ForeignKey(Family, on_delete=models.PROTECT)
    # family = models.ForeignKey(Family, on_delete=models.SET_NULL)


# На уровне объектов
# бурый.family
# медведь.много видов
# На уровне базы данных
# 1, бурый, 1
# 2, белый, 1


class Animal(models.Model):
    # Борис
    name = models.CharField(max_length=16)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# борис.kind.family

class Card(models.Model):
    # Текс карты
    text = models.TextField(blank=True)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)


class Food(models.Model):
    # Еда
    # вид животного
    name = models.CharField(max_length=16)
    kinds = models.ManyToManyField(Kind)
