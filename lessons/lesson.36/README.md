# Создание виртуального окружения
python3 -m venv .venv

в Linux/Mac
source ./.venv/bin/activate
в Windows
./.venv/Scripts/activate.ps1

deactivate

# Установка Django
pip install django
poetry add django

# Проверка установки
django-admin --version

# Создание проекта
django-admin startproject config .

# Запуск проекта
python manage.py runserver

# Создание приложения
python manage.py startapp blog_app

# Применяем миграции
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser