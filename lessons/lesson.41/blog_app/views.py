from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author


# Create your views here.
def index(request):
    """Главная страница."""
    context = {
        'title': 'Главная страница !'
    }
    return render(request, 'blog_app/index.html', context=context)


def about(request):
    """Страница о нас."""
    context = {
        'title': 'О нас !'
    }
    return render(request, 'blog_app/about.html', context=context)


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts,
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def post_add(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()

    context = {
        'form': form,
        'title': 'Добавить пост'
    }
    return render(request, 'blog_app/post_add.html', context=context)


# def post_add(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data.get('title'),
#                 content=form.cleaned_data.get('content'),
#                 rating=form.cleaned_data.get('rating'),
#                 author=Author.objects.first()
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост'
#     }
#     return render(request, 'blog_app/post_add.html', context=context)

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)

    context = {
        'form': form,
        'title': 'Редактировать пост'
    }
    return render(request, 'blog_app/post_edit.html', context=context)