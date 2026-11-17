from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import PostModelForm, PostDeleteForm
from blog_app.models import Post, Author
from .tasks import send_notifcation_email


def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return render(request, 'blog_app/about.html')


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Представление для отображения списка постов."""
    # model = Post
    # template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()

        author_id = self.request.GET.get('name')
        min_rating = self.request.GET.get('rating')

        if author_id:
            queryset = queryset.filter(author__id=author_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)

        # queryset = queryset.filter(author_id=1)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все посты'
        return context


class PostDetailView(LoginRequiredMixin, PostBase, DetailView):
    """Представлени для отображения деталей поста."""
    # model = Post
    # context_object_name = 'post'
    # template_name = 'blog_app/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        # post.rating += 1
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, PostBase, CreateView):
    """Представление для создания поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        send_notifcation_email.delay(
            subject=f"Новый пост {form.instance.title} создан",
            recipient_email="user@example.com",
            message=f"Новый пост '{form.instance.title}' был создан пользователем"
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пост'
        context['button_name'] = 'Создать'
        return context


class PostUpdateView(LoginRequiredMixin, PostBase, UpdateView):
    """Представление для обновления поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить пост'
        context['button_name'] = 'Изменить'
        return context


class PostDeleteView(LoginRequiredMixin, PostBase, DeleteView):
    """Представление для удаления поста."""
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')
