from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Post, Author
from .forms import PostForm, PostModelForm


def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return HttpResponse('<h2>ABOUT US</h2>')


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    # posts = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    print(post)
    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', context=context)


# def add_post(request):
#     """Представление для обработки нового поста через форму."""
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
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
#     return render(request, 'blog_app/add_post.html', context=context)


def add_post(request):
    """Представление для обработки нового поста через форму."""
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
    return render(request, 'blog_app/add_post.html', context=context)


def edit_post(request, post_id):
    """Представление для редактирования поста через форму."""
    post = get_object_or_404(Post, id=post_id)

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
    return render(request, 'blog_app/edit_post.html', context=context)