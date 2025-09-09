Установить Django  
poetry add django  
pip install django  

django-admin --version  

django-admin startproject config .  

python manage.py runserver  

python manage.py startapp blog_app


python manage.py loaddata ./fixtures/blog_app.json
python manage.py dumpdata blog_app.Post > ./fixtures/post_fixtures.json
  
poetry add faker  
  
## Установка тестовых модулей в группу test   
poetry add --group test pytest pytest-mock pytest-django  

## Запуск тестов в реальной базе
pytest --reuse-db

## Запуск redis в docker
docker run -d --name redis-server -p 6379:6379 redis

https://redis.io/download

## Проверка redis
redis-cli ping

# Установка celery и redis в проект
poetry add celery[redis]
poetry add django-celery-results
poetry add django-celery-beat


celery -A config beat --loglevel=info
celery -A config worker --loglevel=info