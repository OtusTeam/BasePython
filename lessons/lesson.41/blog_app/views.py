from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import PostForm, PostModelForm, PostDeleteForm


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


# def add_post(request):
#     '''form = PostForm()'''
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             rating = form.cleaned_data['rating']
#             author = Author.objects.first()
#             Post.objects.create(title=title, content=content, rating=rating, author=author)
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     context = {
#         'form': form,
#         'title': 'Добавление поста'
#     }
#     return render(request, 'blog_app/add_post.html', context=context)


def add_post(request):
    """ form = PostModelForm() """
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()
    context = {
        'form': form,
        'title': 'Добавление поста'
    }
    return render(request, 'blog_app/add_post.html', context=context)


def edit_post(request, post_id):
    """ form = PostModelForm() """

    post =get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():

            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
    context = {
        'form': form,
        'title': 'Изменение поста'
    }
    return render(request, 'blog_app/edit_post.html', context=context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            post.delete()
            return redirect('post_list')
    else:
        form = PostDeleteForm()
    context = {
        'form': form,
        'post': post,
        'title': f'Удаление поста {post.title}'
    }
    return render(request, 'blog_app/delete_post.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    print(authors)
    context = {'authors': authors}
    return render(request, 'blog_app/author_list.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, 'blog_app/author_detail.html', context=context)


