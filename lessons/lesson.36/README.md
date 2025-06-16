python3 -m venv .venv
source ./.venv/bin/activate

pip install django
poetry add django

django-admin --version

django-admin startproject blog
django-admin startproject config .

python manage.py runserver

python manage.py startapp post_app


python manage.py migrate

python manage.py createsuperuser