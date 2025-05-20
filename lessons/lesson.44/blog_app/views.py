from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post, Author
from .forms import PostForm, PostModelForm
from .tasks import send_notification_email

from random import randint
# Create your views here.


def index(request):
    # post = Post(title=f'Post {randint(1, 100)}', content=f'Hello world {randint(1, 100)}', author=f'Admin{randint(1, 100)}')
    # post = Post(title=f'Post {randint(1, 100)}', content=f'Hello world {randint(1, 100)}', author=f'Admin{randint(1, 100)}')
    # post.save()
    # return HttpResponse("""
    # <h1>Hello, world.</h1>
    # <p>You're at the blog index.</p>""")
    return render(request, 'blog_app/index.html')


# def about(request):
#     return HttpResponse("""
#     <h1>О нас.</h1>
#     <p>Блог ОТУС.</p>""")


class AboutView(TemplateView):
    template_name = 'blog_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог О нас'
        context['content'] = 'Добро пожаловать на наш блог'
        return context




# def post_list(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


class PostListView(ListView):
    """Представление для отображения списка постов"""
    model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'


# def post_detail(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, id=post_id)
#     context = {
#         'post': post
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


class PostDetailView(DetailView):
    """Представление для отображения деталей поста"""
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


### PostForm
# def app_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
#                 author=form.cleaned_data['author'],
#             )
#             return redirect('posts')
#     else:
#         form = PostForm()
#
#     context = {'form': form, 'title': 'Добавить пост'}
#     return render(request, 'blog_app/add_post.html', context)


# def add_post(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')
#     else:
#         form = PostModelForm()
#
#     context = {'form': form, 'title': 'Добавить пост'}
#     return render(request, 'blog_app/add_post.html', context)


class PostCreateView(CreateView):
    """Представление для создания нового поста"""
    model = Post
    template_name = 'blog_app/add_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        # response = super().form_valid(form)

        send_notification_email.delay(
            recipient_email='stasik5@bk.ru',
            subject='Новый пост создан',
            message=f'Поста "{form.instance.title}" был успешно создан'
        )


        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


# def edit_post(request, post_id):
#
#     post = get_object_or_404(Post, id=post_id)
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')
#     else:
#         form = PostModelForm(instance=post)
#
#     context = {'form': form, 'title': 'Добавить пост'}
#     return render(request, 'blog_app/edit_post.html', context)


class PostUpdateView(UpdateView):
    """Представление для обновления поста"""
    model = Post
    template_name = 'blog_app/edit_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно обновлен')
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    """Представление для удаления поста"""
    model = Post
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('posts')


def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'blog_app/author_list.html', context=context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog_app/author_posts.html', context=context)