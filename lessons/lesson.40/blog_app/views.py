from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


from blog_app.models import Post


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