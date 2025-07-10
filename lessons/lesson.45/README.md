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


>>> author = Author.objects.create(name='Bob')
>>> author = Author(name='Ann')
>>> author.save()
>>> author1 = Author.objects.create(name='John')
>>> author2 = Author.objects.create(name='Kat')
>>> post = Post.objects.create(title="Post 1", content="content 1", author=author)
>>> post2 = Post.objects.create(title="Post 2", content="content 2", author=author1)
>>> post3 = Post.objects.create(title="Post 3", content="content 3", author=author2)
>>> tag1 = Tag.objects.create(name='Django')
>>> tag2 = Tag.objects.create(name='Python')
>>> tag3 = Tag.objects.create(name='FastAPI')

>>> post3.tags.add(tag2)
>>> comment1 = Comment.objects.create(text='Отличный пост', author=author, post=post)
>>> comment2 = Comment.objects.create(text='Отличный пост 22', author=author2, post=post2)
>>> author4 = Author.objects.get(name='Ann')
>>> author4
<Author: Ann>
>>> author4.posts.all()
<QuerySet [<Post: Post 1>]>
>>> Tag.objects.get(name='Django').posts.all()
<QuerySet [<Post: Post 1>]>
>>> Tag.objects.get(name='FastAPI').posts.all()
<QuerySet [<Post: Post 1>, <Post: Post 2>]>
>>> my_post = Post.objects.filter(title='Post 1')
>>> my_post
<QuerySet [<Post: Post 1>]>
>>> my_post = Post.objects.filter(title='Post')
>>> my_post
<QuerySet []>
> 


## Тестирование  
   
poetry add --group test pytest pytest-mock pytest-django   


pytest blog_app/tests/test_views.py::test_index_view -vv
pytest blog_app/tests/test_views.py -vv
pytest

  
sudo apt update  
sudo apt install redis   
sudo systemctl start redis-server  
sudo systemctl enable redis-server  
  
docker run -d --name redis-server -p 6379:6379 redis  
  
poetry add celery[redis]  
poetry add django-celery-results  
  

