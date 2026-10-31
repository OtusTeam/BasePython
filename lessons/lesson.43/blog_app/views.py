from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostModelForm, PostDeleteForm
from blog_app.models import Post, Author


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


# def post_list(request):
#     all_post = Post.objects.all()
#     context = {
#         'posts': all_post,
#         'title': "Все посты"
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


class PostDetailView(PostBase, DetailView):
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


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     comments = post.comments.all()
#     tags = post.tags.all()
#     context = {
#         'post': post,
#         'tags': tags,
#         'comments': comments
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


class PostCreateView(PostBase, CreateView):
    """Представление для создания поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # pass
        # message.success
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пост'
        context['button_name'] = 'Создать'
        return context


# def post_add(request):
#     """Представление для добавления нового поста через форму."""
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
#     return render(request, 'blog_app/post_form.html', context=context)


class PostUpdateView(PostBase, UpdateView):
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


# def post_edit(request, post_id):
#     """Представление для изменения поста через форму."""
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
#         'title': 'Изменить пост',
#         'button_name': 'Изменить'
#     }
#     return render(request, 'blog_app/post_form.html', context=context)


class PostDeleteView(PostBase, DeleteView):
    """Представление для удаления поста."""
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')


# def post_delete(request, post_id):
#     """Представление для удаления поста через форму."""
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirm']:
#             post.delete()
#             # messages.succes
#             return redirect('post_list')
#     else:
#         form = PostDeleteForm()
#
#     context = {
#         'form': form,
#         'title': f'Удалить пост {post.title}',
#         'post': post,
#         'button_name': 'Удалить'
#     }
#     return render(request, 'blog_app/post_delete.html', context=context)


