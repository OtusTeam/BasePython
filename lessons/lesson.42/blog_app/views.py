from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages


from blog_app.models import Post, Author
from .forms import PostForm, PostModelForm


# def index(request):
#     """Главная страница."""
#     return render(request, 'blog_app/index.html')


class IndexTemplateView(TemplateView):
    template_name = 'blog_app/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Список постов!'
    #     return context

#
# def about(request):
#     """Страница о нас."""
#     return HttpResponse("<h2>Страница о нас.</h2><hr>You're the blog app!")

class AboutTemplateView(TemplateView):
    template_name = 'blog_app/about.html'


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Список постов."""
    # model = Post
    # template_name = "blog_app/post_list.html"
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


class PostDetailView(PostBase, DetailView):
    """Детальный постов."""
    # model = Post
    # template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)
        # return post


class PostCreateView(PostBase, CreateView):
    """Добавление нового поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать пост!'
        return context


class PostUpdateView(PostBase, UpdateView):
    """Редактирование  поста."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить пост!'
        return context


class PostDeleteView(PostBase, DeleteView):
    """Удаление  поста."""
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')


# def post_edit(request, post_id):
#     """Редактирование  поста."""
#     post = get_object_or_404(Post, pk=post_id)
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
#         'title': 'Редактировать пост',
#     }
#     return render(request, 'blog_app/post_form.html', context=context)


# def post_list(request):
#     """Список постов."""
#     posts1 = Post.objects.all()
#     context = {
#         'posts': posts1,
#         'title': 'Список постов!'
#     }
#     return render(request, 'blog_app/post_list.html', context=context)



# def post_detail(request, post_id):
#     """Детальный постов."""
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'post': post,
#         'title': post.title,
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)



# def post_add(request):
#     """Добавление нового поста."""
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
#                 author=Author.objects.first(),
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост',
#     }
#     return render(request, 'blog_app/post_add.html', context=context)

# def post_add(request):
#     """Добавление нового поста."""
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
#         'title': 'Добавить пост',
#     }
#     return render(request, 'blog_app/post_form.html', context=context)