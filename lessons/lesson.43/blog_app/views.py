from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author


class IndexTemplateView(TemplateView):
    template_name = 'blog_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '-= Главная страница =-'
        return context


# def index(request):
#     """Главная страница."""
#     context = {
#         'title': 'Главная страница !'
#     }
#     return render(request, 'blog_app/index.html', context=context)


class AboutTemplateView(TemplateView):
    template_name = 'blog_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '-= О нас =-'
        return context
#
# def about(request):
#     """Страница о нас."""
#     context = {
#         'title': 'О нас !'
#     }
#     return render(request, 'blog_app/about.html', context=context)


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    # model = Post
    # template_name = 'blog_app/post_list.html'
    # context_object_name = 'post_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        # return queryset.filter(is_active=True)
        author_id = self.request.GET.get('author')
        min_rating = self.request.GET.get('rating')
        if author_id:
            queryset = queryset.filter(author__id=author_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '-= Список постов =-'
        return context


# def post_list(request):
#     posts = Post.objects.all()
#     context = {
#         'title': 'Список постов',
#         'posts': posts,
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


class PostDetailView(PostBase, DetailView):
    # model = Post
    # template_name = 'blog_app/post_detail.html'
    # context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'title': post.title,
#         'post': post,
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


class PostCreateView(PostBase, CreateView):
    # model = Post
    # template_name = blog_app/post_form.html'
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


# def post_add(request):
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


class PostUpdateView(PostBase, UpdateView):
    # model = Post
    # template_name = blog_app/post_form.html'
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно отредактирован')
        return super().form_valid(form)

#
# def post_edit(request, post_id):
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
#         'title': 'Редактировать пост'
#     }
#     return render(request, 'blog_app/post_edit.html', context=context)


class PostDeleteView(PostBase, DeleteView):
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')