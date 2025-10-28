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
  
# Создать  миграции  
python manage.py makemigrations  
  
# Интерактивная консоль Django  
python manage.py shell  
  
# CRUD опреации  
author = Author.objects.create(name="User")  
  
author = Author(name="User1")  
author.save()  
  
post = Post.objects.create(  
    title="Первая запись",  
    content="Изучаем Django",  
    author=author  # Связываем пост с автором
)
  
all_posts = Post.objects.all()  
filter_posts = Post.objects.filter(title="Django")  
  
post = Post.objects.get(title="Первая запись")  
post.rating = 10  
post.save()  

post.delete()  


# Загрузить данные из json
python manage.py loaddata ./blog_fixture.json

# Выгрузить данные в json
python manage.py dumpdata blog_app.Post --indent 4 > ./blog_data_post.json
  
  
# Установка faker  
poetry add faker  