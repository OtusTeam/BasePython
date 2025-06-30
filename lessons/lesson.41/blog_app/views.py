from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment
from .forms import PostForm, PostModelForm


def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return render(request, 'blog_app/about.html')


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    # comments = post.comments.filter(active=True)
    comments = Comment.objects.filter(post=post)
    tags = post.tags.all()

    context = {
        'post': post,
        'title': post.title,
        'comments': comments,
        'tags': tags,
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'title': 'Список всех постов'}
    return render(request, 'blog_app/post_list.html', context=context)


# def add_post(request):
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
#     context = {'form': form, 'title': 'Добавить пост'}
#     return render(request, 'blog_app/add_post.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()

    context = {'form': form, 'title': 'Добавить пост'}
    return render(request, 'blog_app/add_post.html', context=context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)

    context = {'form': form, 'title': 'Редактировать пост'}
    return render(request, 'blog_app/edit_post.html', context=context)



def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'Список всех авторов'}
    return render(request, 'blog_app/author_list.html', context=context)