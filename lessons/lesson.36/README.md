mkdir my_project
cd my_project
python -m  venv .venv
source .venv/bin/activate
pip install django
poetry add django

django-admin --version

django-admin startproject config .

python manage.py runserver

python manage.py startapp my_app

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000