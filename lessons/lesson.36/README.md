# Создание виртуального окружения
python -m venv .venv
source ./.venv/bin/activate
.\.venv\Scripts\activate.ps1
deactivate

# Poetry
poetry init

# Установка Django
poetry add django
pip install django

# Проверяем версию django
django-admin --version

# Создание проекта django во вложенной директории
django-admin startproject blog

# Создание проекта django в текущей директории config
django-admin startproject config .

# Запустить проект
python manage.py runserver

# Создание приложения blog_app
python manage.py startapp blog_app

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser