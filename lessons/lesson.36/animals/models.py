from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    class Meta:
        verbose_name_plural = "Food"

    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


# class MedicalInfo(models.Model):
#     pass


class Animal(models.Model):
    name = models.CharField(max_length=64)
    # med_card = models.OneToOneField(MedicalInfo, on_delete=models.CASCADE)
    # 1 - 1, 1 - *, * - *
    # cascade, protect, setnull
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="animals",
    )
    meals = models.ManyToManyField(
        Food,
        related_name="animals",
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'

# CRUD Create Read Update Delete (5 views)