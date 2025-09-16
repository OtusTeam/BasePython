from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Менеджер для кастомного пользователя."""

    def create_user(self, email, password=None, **extra_fields):
        """Создает обычного пользователя с email и password."""
        if not email:
            raise ValueError("Поле email обязательно для заполнения")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает суперпользователя."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""

    # username = None
    username = models.CharField(
        max_length=100,
        unique=False,
        blank=True,
        null=True,
        verbose_name="Имя пользователя",
    )
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    data_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )
    avatar = models.ImageField(
        blank=True, null=True, upload_to="avatars/", verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
