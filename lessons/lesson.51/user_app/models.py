from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Менеджер кастомного пользователя."""

    def create_user(self, email, password=None, **extra_fields):
        """Создает и сохраняет пользователя с заданным email и паролем."""
        if not email:
            raise ValueError("Поле email должно быть установлено")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и сохраняет суперпользователя с заданным email и паролем."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Суперпользователь должен иметь is_superuser=True")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Кастомный пользователь."""

    username = models.CharField(
        max_length=150,
        unique=False,
        blank=True,
        null=True,
        verbose_name="Имя пользователя",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Адрес электронной почты",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """Как пользователь будет отображаться в админке."""
        return self.email
