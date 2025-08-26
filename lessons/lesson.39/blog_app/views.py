from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Post


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
