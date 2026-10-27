from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, PostModelForm, PostDeleteForm
from blog_app.models import Post, Author


def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return render(request, 'blog_app/about.html')


def post_list(request):
    all_post = Post.objects.all()
    context = {
        'posts': all_post,
        'title': "Все посты"
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # comments = Comment.objects.filter(post=post)
    comments = post.comments.all()
    tags = post.tags.all()
    context = {
        'post': post,
        'tags': tags,
        'comments': comments
    }
    return render(request, 'blog_app/post_detail.html', context=context)


# def post_add(request):
#     """Представление для добавления нового поста через форму."""
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
#     return render(request, 'blog_app/post_add.html', context=context)


def post_add(request):
    """Представление для добавления нового поста через форму."""
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
    return render(request, 'blog_app/post_form.html', context=context)


def post_edit(request, post_id):
    """Представление для изменения поста через форму."""
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
        'title': 'Изменить пост'
    }
    return render(request, 'blog_app/post_form.html', context=context)


def post_delete(request, post_id):
    """Представление для удаления поста через форму."""
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            post.delete()
            # messages.succes
            return redirect('post_list')
    else:
        form = PostDeleteForm()

    context = {
        'form': form,
        'title': f'Удалить пост {post.title}',
        'post': post
    }
    return render(request, 'blog_app/post_delete.html', context=context)


