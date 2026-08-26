from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from blog_app.models import Post, Author
from .forms import PostForm, PostModelForm
from .tasks import send_mail_task


class IndexTemplateView(TemplateView):
    template_name = 'blog_app/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'blog_app/about.html'


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Список постов."""
    context_object_name = 'posts'

    def get_queryset(self):
        """Фильтруем список постов."""
        queryset = super().get_queryset()
        author_id = self.request.GET.get('author')
        min_rating = self.request.GET.get('rating')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постов!'
        return context


class PostDetailView(LoginRequiredMixin, PostBase, DetailView):
    """Детальный постов."""
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)
        # return post


class PostCreateView(LoginRequiredMixin, PostBase, CreateView):
    """Добавление нового поста."""
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        send_mail_task.delay(
            rec_email='user@gmail.com',
            subject="Новый пост создан",
            message=f'Пост "{form.instance.title}" был создан'

        )
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать пост!'
        return context


class PostUpdateView(LoginRequiredMixin, PostBase, UpdateView):
    """Редактирование  поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить пост!'
        return context


class PostDeleteView(LoginRequiredMixin, PostBase, DeleteView):
    """Удаление  поста."""
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')

