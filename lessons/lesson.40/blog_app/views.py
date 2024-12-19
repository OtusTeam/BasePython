from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import PostForm, PostModelForm

# Create your views here.
def index(request):
    return render(request, 'blog_app/home.html')


def contacts(request):
    return HttpResponse("Hello, contacts!!")


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post =  get_object_or_404(Post, pk=post_id)

    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            rating = form.cleaned_data['rating']
            author = Author.objects.first()
            post = Post(title=title, content=content, rating=rating, author=author)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'title': 'Добавление поста',
        'form': form
    }
    return render(request, 'blog_app/add_post.html', context=context)


def add_post_model(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            # form.save()
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            rating = form.cleaned_data['rating']
            author = Author.objects.first()

            post = Post(title=title, content=content, rating=rating, author=author)
            post.save()
            return redirect('post_list')
        else:
            print(form.errors)
    else:
        form = PostModelForm()
    context = {
        'title': 'Добавление поста',
        'form': form
    }
    return render(request, 'blog_app/add_post_model.html', context=context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # rating = form.cleaned_data['rating']
            # # author = Author.objects.first()

            # post = Post(title=title, content=content, rating=rating, author=author)
            # post.save()
            return redirect('post_list')
        else:
            print(form.errors)
    else:
        form = PostModelForm(instance=post)
    context = {
        'title': 'Редактирование поста',
        'form': form
    }
    return render(request, 'blog_app/edit_post.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors
    }
    return render(request, 'blog_app/author_list.html', context=context)