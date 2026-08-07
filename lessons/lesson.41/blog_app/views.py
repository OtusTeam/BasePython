from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blog_app.models import Post, Author
from .forms import PostForm, PostModelForm


def index(request):
    """Главная страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return HttpResponse("<h2>Страница о нас.</h2><hr>You're the blog app!")


def post_list(request):
    """Список постов."""
    posts1 = Post.objects.all()
    context = {
        'posts': posts1,
        'title': 'Список постов!'
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Детальный постов."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'blog_app/post_detail.html', context=context)


# def post_add(request):
#     """Добавление нового поста."""
#     if request.method == 'POST':
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
#         'title': 'Добавить пост',
#     }
#     return render(request, 'blog_app/post_add.html', context=context)

def post_add(request):
    """Добавление нового поста."""
    if request.method == 'POST':
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
    return render(request, 'blog_app/post_form.html', context=context)



def post_edit(request, post_id):
    """Редактирование  поста."""
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
        'title': 'Редактировать пост',
    }
    return render(request, 'blog_app/post_form.html', context=context)