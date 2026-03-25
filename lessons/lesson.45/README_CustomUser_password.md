# Работа с паролями и правами в Django

## 1. Хеширование паролей

Django не хранит пароль в открытом виде. Он хранит только хеш и умеет сам проверять пароль через настроенные хешеры. Список алгоритмов задаётся в `PASSWORD_HASHERS`. По умолчанию Django использует безопасные алгоритмы и умеет автоматически пере-хешировать пароль при успешном входе, если текущий алгоритм или его параметры устарели. ([Django Project][1])

Пример настройки:

```python
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
```

Что важно:

* `Argon2` обычно рассматривают как хороший современный вариант, если можно поставить дополнительную зависимость.
* `PBKDF2` — хороший стандартный вариант “из коробки”.
* Менять `salt` вручную обычно не нужно: Django сам генерирует его корректно.
* Полностью писать свой хешер стоит только если есть реальная причина: интеграция со старой системой, миграция пользователей, особые требования безопасности. ([Django Project][2])

---

## 2. Как переопределяется проверка пароля при аутентификации

Стандартная аутентификация идёт через `authenticate()` и backend'ы из `AUTHENTICATION_BACKENDS`. Именно backend решает:

* как найти пользователя;
* как проверить пароль;
* можно ли вообще считать пользователя аутентифицированным. ([Django Project][3])

Если нужно поменять логику входа, обычно делают свой backend:

```python
AUTHENTICATION_BACKENDS = [
    "users.auth_backends.EmailAuthBackend",
]
```

Примерно так:

```python
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get("email") or username
        if not email or not password:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
```

Если задача только в том, чтобы изменить поле входа, например логин по email, чаще всего достаточно своего backend'а. Полностью переписывать механизм проверки пароля обычно не требуется: безопаснее использовать `user.check_password()`. ([Django Project][3])

---

## 3. Как изменить стандартные views смены и сброса пароля

Django уже даёт готовые class-based views:

* `PasswordChangeView`
* `PasswordChangeDoneView`
* `PasswordResetView`
* `PasswordResetDoneView`
* `PasswordResetConfirmView`
* `PasswordResetCompleteView` ([Django Project][1])

Обычно их меняют тремя способами:

### Вариант 1. Просто подключить свои шаблоны

```python
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html"
        ),
        name="password_change",
    ),
]
```

### Вариант 2. Подменить форму

```python
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPasswordChangeForm

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "users/password_change.html"
```

### Вариант 3. Унаследоваться и добавить свою логику

Например: логирование, уведомления, дополнительные проверки, свой success URL.

Для сброса пароля важно, что Django использует токены и стандартный безопасный механизм восстановления доступа. Но его нужно правильно настроить: email, шаблоны, HTTPS, корректный домен, защита от утечки ссылок. ([Django Project][1])

---

## 4. Как настраивать свои password validators

Валидаторы подключаются через `AUTH_PASSWORD_VALIDATORS`. Django уже содержит готовые валидаторы: минимальная длина, похожесть на данные пользователя, слишком простой пароль, пароль из частых паролей. ([Django Project][2])

Пример:

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 10},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
```

Свой валидатор пишется как обычный класс:

```python
from django.core.exceptions import ValidationError


class NoQwertyPasswordValidator:
    def validate(self, password, user=None):
        if "qwerty" in password.lower():
            raise ValidationError("Пароль не должен содержать 'qwerty'.")

    def get_help_text(self):
        return "Пароль не должен содержать 'qwerty'."
```

Подключение:

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "users.validators.NoQwertyPasswordValidator",
    },
]
```

Если пароль задаётся не стандартной формой, а, например, через API или свою форму, проверки можно вызывать вручную через `validate_password()`. Это штатный путь. ([Django Project][2])

---

## 5. Как разделять проверки: форма/view и backend

Здесь лучше разделять ответственность.

### На уровне формы или view

Здесь удобно делать проверки, связанные с UX:

* поля не пустые;
* пароль и подтверждение совпадают;
* понятные сообщения пользователю;
* базовые ограничения длины и формата.

### На уровне backend / модели / серверной логики

Здесь должны быть проверки, которые нельзя обойти:

* вызов `validate_password()`;
* проверка прав на изменение пароля;
* запрет установки слишком слабого пароля;
* обязательные проверки при создании пользователя через API, management command, кастомный сервис и т.д.

Практическое правило простое: всё, что критично для безопасности, должно проверяться на сервере независимо от формы. Формы нужны для удобства, backend — для гарантии. ([Django Project][3])

---

## 6. Какие есть риски у стандартной логики Django

Стандартная логика Django в целом безопасная, но “из коробки” надо помнить о нескольких вещах.

### Слабые пароли

Если оставить только базовые настройки или ослабить валидаторы, пользователи смогут ставить слабые пароли. Валидаторы нужно явно проверить и при необходимости усилить. ([Django Project][2])

### Нет встроенного rate limit на вход

У Django нет полноценного встроенного ограничения попыток входа. Поэтому brute force-защиту обычно добавляют отдельно: через пакет, middleware, reverse proxy, WAF или rate limiting на уровне приложения/инфраструктуры. ([Django Project][3])

### Сброс пароля требует аккуратной настройки

Механизм хороший, но важно:

* использовать HTTPS;
* корректно настроить отправку email;
* не допускать утечки reset-ссылок в логи;
* проверять домен и шаблоны писем. ([Django Project][1])

### Нельзя полагаться только на `is_superuser`

Для обычной бизнес-логики лучше чаще опираться на `has_perm()` и группы, а не везде проверять только суперпользователя. Это делает систему прав более управляемой. ([Django Project][3])

---

## 7. Кастомный пользователь, суперпользователь и “двойная сессия”

Здесь часто бывает путаница.

### Главное

Обычно нет “двойной сессии” кастомного пользователя и суперпользователя одновременно. Есть **одна текущая аутентифицированная сессия**, и в ней один конкретный пользователь. Если этот пользователь имеет `is_superuser=True`, то он остаётся тем же самым пользователем и на основном сайте, и в админке. Django auth и сессии общие для проекта, если используются один и тот же домен, cookie и настройки сессий. ([Django Project][1])

То есть сценарий такой:

* суперпользователь вошёл в админку;
* у него уже есть сессия;
* на основном сайте `request.user` — это тот же пользователь;
* значит, можно показывать ему дополнительные кнопки.

### Как это проверить на сайте

В шаблоне:

```django
{% if request.user.is_authenticated and request.user.is_superuser %}
    <a href="{% url 'special_admin_tools' %}">Доп. кнопки</a>
{% endif %}
```

Или более гибко:

```django
{% if request.user.has_perm("catalog.can_publish") %}
    <a href="{% url 'publish_product' %}">Публиковать</a>
{% endif %}
```

### Что значат основные флаги

* `is_staff` — пользователь может войти в админку.
* `is_superuser` — пользователь имеет все права без обычных проверок permission system. ([Django Project][4])

То есть для доступа в админку важен `is_staff`, а не просто факт существования кастомной модели пользователя. Суперпользователь обычно имеет и `is_staff=True`, и `is_superuser=True`. ([Django Project][5])

### Если пароль был изменён

После смены пароля текущую сессию пользователя лучше не терять. Для этого Django даёт `update_session_auth_hash()`. Это стандартный способ сохранить пользователя залогиненным после смены собственного пароля. ([Django Project][1])

---

## 8. Практический вывод

Для большинства проектов достаточно такой схемы:

1. Оставить стандартную систему Django auth.
2. При необходимости включить `Argon2` или оставить `PBKDF2`.
3. Усилить `AUTH_PASSWORD_VALIDATORS`.
4. Для входа по email сделать свой authentication backend.
5. Для смены и сброса пароля переопределять формы и шаблоны, а не ломать стандартную механику.
6. Добавить ограничение попыток входа отдельно.
7. На основном сайте показывать “админские” кнопки через `request.user.is_staff`, `is_superuser` или `has_perm()`.

Итоговая рекомендация простая: стандартный механизм Django лучше не переписывать без необходимости. Обычно его не заменяют, а аккуратно расширяют в штатных точках: `PASSWORD_HASHERS`, `AUTH_PASSWORD_VALIDATORS`, `AUTHENTICATION_BACKENDS`, свои формы, свои views, свои permission checks. ([Django Project][3])

---

[1]: https://docs.djangoproject.com/en/6.0/topics/auth/default/ "Using the Django authentication system"
[2]: https://docs.djangoproject.com/en/6.0/topics/auth/passwords/ "Password management in Django"
[3]: https://docs.djangoproject.com/en/6.0/topics/auth/customizing/ "Customizing authentication in Django"
[4]: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/ "The Django admin site"
[5]: https://docs.djangoproject.com/en/6.0/ref/contrib/auth/ "django.contrib.auth"
