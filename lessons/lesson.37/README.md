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

# Создать миграции
python manage.py makemigrations

# Интерактивная консоль Django
python manage.py shell

>>> post = Post(title='Первый пост', content='Привет, мир!', author='Bob')
>>> post.save()
> 
> >>> all_post = Post.objects.all()
>>> all_post
> 
> >>> first_post = all_post[0]
> >>> first_post.title
> 
> >>> post1 = Post.objects.create(title='Важный пост', content='Завтра новая версия python', author='Admin')
>>> comment1 = Comment.objects.create(text='Отличная новость', author='User123', post=post1)
>>> comment2 = Comment.objects.create(text='Отличная новость2', author='User345', post=post1)
> 
> >>> comment1.post.title
'Важный пост'
>>> post1.comments.all()
<QuerySet [<Comment: Коммент автора User123>, <Comment: Коммент автора User345>]>
> 
> 
> 
> >>> post = Post.objects.create(title='Еще пост', content='Еще контент', author='Админ123')
>>> tag1 = Tag.objects.create(name='Django')
>>> tag2 = Tag.objects.create(name='Python')
>>> post.tags.add(tag1, tag2)
>>> 
> >>> post.tags.all()
<QuerySet [<Tag: Django>, <Tag: Python>]>
>>> tag2.posts.all()
<QuerySet [<Post: Еще пост>, <Post: Еще пост11>]>