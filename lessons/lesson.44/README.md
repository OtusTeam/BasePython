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

python manage.py shell

# REDIS
sudo apt update
sudo apt install redis

sudo systemctl start redis-server
sudo systemctl enable redis-server


docker run -d --name redis-server -p 6379:6379 redis