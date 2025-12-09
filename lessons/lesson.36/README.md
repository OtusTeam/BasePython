# Создание виртуального окружения
python -m venv .venv

# Установка Django
poetry add django
pip install django

# Проверяем версию django
django-admin --version


django-admin startproject blog
django-admin startproject config .


python manage.py startapp blog_app

python manage.py migrate