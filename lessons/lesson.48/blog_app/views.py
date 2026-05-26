from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from blog_app.forms import PostModelForm
from blog_app.models import Post


class IndexTemplateView(TemplateView):
    """"Главная страница."""
    template_name = 'blog_app/index.html'


class AboutTemplateView(TemplateView):
    """Страница о нас."""
    template_name = 'blog_app/about.html'


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Представление для Списка постов."""
    # model = Post
    # template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'
    # paginate_by = 5

    def get_queryset(self):
        """Фильтрует список постов."""
        queryset = super().get_queryset()
        author_id = self.request.GET.get('author')
        min_rating = self.request.GET.get('rating')

        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        return queryset


class PostDetailView(PostBase, DetailView):
    """Детальный пост."""
    # model = Post
    # template_name = 'blog_app/post_detail.html'
    # context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        """Переопредление метода get."""
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


class PostCreateView(PostBase, CreateView):
    """Добавление нового поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


class PostUpdateView(PostBase, UpdateView):
    """Редактирование поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно изменен')
        return super().form_valid(form)


class PostDeleteView(PostBase, DeleteView):
    """Удаление поста."""
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['title'] = "Удалить пост"
        return context
