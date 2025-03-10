from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author


# Create your views here.
def index(request):
    return render(request, 'blog_app/home.html')


def about(request):
    return HttpResponse("About me info")


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog_app/post_detail.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    print(authors)
    context = {'authors': authors}
    return render(request, 'blog_app/author_list.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, 'blog_app/author_detail.html', context=context)
