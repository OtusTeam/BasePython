from http.client import responses

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post, Author
from .forms import PostForm, PostModelForm, PostDeleteForm
from .tasks import send_info_email


# def index(request):
#     """Главная страница."""
#     return render(request, 'blog_app/index.html')


class PostBase():
    model = Post


class IndexTemplateView(TemplateView):
    template_name = 'blog_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наш Блог'
        context['text'] = 'Самый лучший блог'
        return context


def about(request):
    """Страница о нас."""
    return HttpResponse('<h1>About us</h1>')


class PostListView(PostBase, ListView):
    """CBV всех постов."""
    # model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'
    # paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        min_rating = self.request.GET.get('rating')
        author_id = self.request.GET.get('author')

        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        if author_id:
            queryset = queryset.filter(author__id=author_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постов'
        return context


class PostDetailView(LoginRequiredMixin, PostBase, DetailView):
    # model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        """Добавляем сообщение об успешном создании поста."""

        response = super().form_valid(form)

        send_info_email.delay(
            recipient_email='user@mail.ru',
            subject='Новый пост создан',
            message=f'Пост {form.cleaned_data['title']} успешно создан',
            )

        messages.success(self.request, 'Пост успешно создан')
        return response


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        """Добавляем сообщение об успешном обновлении поста."""
        messages.success(self.request, 'Пост успешно обновлен')
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')


# def post_list(request):
#     """Cтраница всех постов."""
#     posts = Post.objects.all()
#     context = {
#         'title': 'Список постов',
#         'posts': posts,
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


# def post_detail(request, post_id):
#     """Cтраница для одного поста."""
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'post': post,
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)



# def post_add(request):
#     """Представление для добавления нового поста. PostModelForm"""
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост'
#     }
#     return render(request, 'blog_app/post_add.html', context=context)


# def post_edit(request, post_id):
#     """Представление для редактирования поста."""
#
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm(instance=post)
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост'
#     }
#     return render(request, 'blog_app/post_edit.html', context=context)


# def post_delete(request, post_id):
#     """Представление для удаления поста."""
#
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirm']:
#             post.delete()
#             # messages.success()
#             return redirect('post_list')
#     else:
#         form = PostDeleteForm()
#
#     context = {
#         'form': form,
#         'post': post,
#         'title': 'Удалить пост'
#     }
#     return render(request, 'blog_app/post_delete.html', context=context)

# def post_add(request):
#     """Представление для добавления нового поста. PostForm"""
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data.get('title'),
#                 content=form.cleaned_data.get('content'),
#                 rating=form.cleaned_data.get('rating'),
#                 author=Author.objects.first(),
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


def author_list(request):
    """Cтраница всех авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors,
    }
    return render(request, 'blog_app/author_list.html', context=context)