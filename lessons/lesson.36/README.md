# Создание виртуального окружения
python -m venv .venv

# Установка Django
poetry add django
pip install django

# Проверяем версию django
django-admin --version

# Создать проект django во вложенной директории
django-admin startproject blog

# Создать проект django в текущей директории
django-admin startproject config .

# Создать приложение blog_app
python manage.py startapp blog_app

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
