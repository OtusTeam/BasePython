from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Comment


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


def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'Список всех авторов'}
    return render(request, 'blog_app/author_list.html', context=context)