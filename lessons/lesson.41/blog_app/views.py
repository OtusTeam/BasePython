from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import PostForm, PostModelForm, PostDeleteForm


def index(request):
    """Главная страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return HttpResponse('<h1>About us</h1>')


def post_list(request):
    """Cтраница всех постов."""
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts,
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Cтраница для одного поста."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog_app/post_detail.html', context=context)



def post_add(request):
    """Представление для добавления нового поста. PostModelForm"""
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


def post_edit(request, post_id):
    """Представление для редактирования поста."""

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
        'title': 'Добавить пост'
    }
    return render(request, 'blog_app/post_edit.html', context=context)


def post_delete(request, post_id):
    """Представление для удаления поста."""

    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            post.delete()
            # messages.success()
            return redirect('post_list')
    else:
        form = PostDeleteForm()

    context = {
        'form': form,
        'post': post,
        'title': 'Удалить пост'
    }
    return render(request, 'blog_app/post_delete.html', context=context)

# def post_add(request):
#     """Представление для добавления нового поста. PostForm"""
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data.get('title'),
#                 content=form.cleaned_data.get('content'),
#                 rating=form.cleaned_data.get('rating'),
#                 author=Author.objects.first(),
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


def author_list(request):
    """Cтраница всех авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors,
    }
    return render(request, 'blog_app/author_list.html', context=context)