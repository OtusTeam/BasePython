from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Author
from .forms import PostForm, PostModelForm


def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return HttpResponse('<h2>ABOUT US</h2>')


class PostListView(ListView):
    """Представление для отображения списка постов."""
    model = Post
    # template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Фильтрует список постов по рейтингу."""
        queryset = super().get_queryset()
        min_rating = self.request.GET.get('rating')
        author = self.request.GET.get('author')

        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)

        if author:
            queryset = queryset.filter(author_id=author)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['authors'] = Author.objects.all()
        context['title'] = 'Список постов!!!'
        return context


class PostDetailView(DetailView):
    """Представление для отображения деталей поста."""
    model = Post
    # template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


class PostCreateView(CreateView):
    """Представление для создания поста."""
    model = Post
    template_name = 'blog_app/add_post.html'
    success_url = reverse_lazy('post_list')
    form_class = PostModelForm

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    """Представление для обновления поста."""
    model = Post
    template_name = 'blog_app/edit_post.html'
    success_url = reverse_lazy('post_list')
    form_class = PostModelForm

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно обновлен')
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    """Представление для удаления поста."""
    model = Post
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'

# def post_list(request):
#     posts = Post.objects.all()
#     context = {
#         'title': 'Список постов',
#         'posts': posts
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


# def post_detail(request, post_id):
#     # posts = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, pk=post_id)
#     print(post)
#     context = {
#         'title': post.title,
#         'post': post
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


# def add_post(request):
#     """Представление для обработки нового поста через форму."""
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
#                 author=Author.objects.first()
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост'
#     }
#     return render(request, 'blog_app/add_post.html', context=context)


# def add_post(request):
#     """Представление для обработки нового поста через форму."""
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
#     return render(request, 'blog_app/add_post.html', context=context)

#
# def edit_post(request, post_id):
#     """Представление для редактирования поста через форму."""
#     post = get_object_or_404(Post, id=post_id)
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
#         'title': 'Редактировать пост'
#     }
#     return render(request, 'blog_app/edit_post.html', context=context)