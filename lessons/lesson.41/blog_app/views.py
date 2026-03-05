from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Post, Author
from blog_app.forms import PostForm, PostModelForm


def index(request):
    """Главная страница."""
    return render(request, "blog_app/index.html")


def about(request):
    """Главная страница."""
    return HttpResponse("<h2>Cтраница о нас.</h2>")


def post_list(request):
    """Список постов."""
    posts = Post.objects.all()
    context = {
        'title': 'Список постов!',
        'posts': posts,
    }
    return render(request, "blog_app/post_list.html", context=context)


def post_detail(request, post_id):
    """Детайльный пост."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }

    return render(request, "blog_app/post_detail.html", context=context)


# def post_add(request):
#     """Представление для добавления нового поста через форму."""
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
#                 author=Author.objects.first(),
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить поста',
#     }
#     return render(request, "blog_app/post_add.html", context=context)

def post_add(request):
    """Представление для добавления нового поста через форму."""

    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()

    context = {
        'form': form,
        'title': 'Добавить пост',
    }
    return render(request, "blog_app/post_add.html", context=context)


def post_edit(request, post_id):
    """Представление для изменения поста через форму."""
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)

    context = {
        'form': form,
        'title': 'Изменить поста',
    }
    return render(request, "blog_app/post_edit.html", context=context)


def author_list(request):
    """Список авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список Авторов!',
        'authors': authors,
    }
    return render(request, "blog_app/author_list.html", context=context)


def author_detail(request, author_id):
    """Детальный автор."""
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author,
    }

    return render(request, "blog_app/author_detail.html", context=context)