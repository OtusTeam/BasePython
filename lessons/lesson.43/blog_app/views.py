from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib import messages
from blog_app.models import Post, Author
from blog_app.forms import PostForm, PostModelForm, PostDeleteForm



class IndexTemplateView(TemplateView):
    """Главная страница."""
    template_name = "blog_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '-= Главная страница =-'
        return context

# def index(request):
#     """Главная страница."""
#     return render(request, "blog_app/index.html")


def about(request):
    """Главная страница."""
    return HttpResponse("<h2>Cтраница о нас.</h2>")


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Представления для отображения списка постов."""
    # model = Post
    # template_name = "blog_app/post_list.html"
    context_object_name = "posts"


# def post_list(request):
#     """Список постов."""
#     posts = Post.objects.all()
#     context = {
#         'title': 'Список постов!',
#         'posts': posts,
#     }
#     return render(request, "blog_app/post_list.html", context=context)


class PostDetailView(PostBase, DetailView):
    """Представления для отображения одного поста."""
    # model = Post
    # slug_field = 'slug'
    # template_name = "blog_app/post_detail.html"
    # template_name = "blog_app/detail_post.html"
    # context_object_name = "post"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)

# def post_detail(request, post_id):
#     """Детайльный пост."""
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'post': post,
#     }
#
#     return render(request, "blog_app/post_detail.html", context=context)


class PostCreateView(PostBase, CreateView):
    """Представления для создания нового поста."""
    # model = Post
    # template_name = "blog_app/post_form.html"
    template_name = "blog_app/post_add.html"
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)



# def post_add(request):
#     """Представление для добавления нового поста через форму."""
#
#     if request.method == "POST":
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
#     return render(request, "blog_app/post_add.html", context=context)


class PostUpdateView(PostBase, UpdateView):
    """Представления для редактирования поста."""
    # model = Post
    # template_name = "blog_app/post_form.html"
    template_name = "blog_app/post_edit.html"
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

#
# def post_edit(request, post_id):
#     """Представление для изменения поста через форму."""
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == "POST":
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm(instance=post)
#
#     context = {
#         'form': form,
#         'title': 'Изменить поста',
#     }
#     return render(request, "blog_app/post_edit.html", context=context)


class PostDeleteView(PostBase, DeleteView):
    """Представления для удаления поста."""
    # model = Post
    # template_name = "blog_app/post_form.html"
    template_name = "blog_app/post_delete.html"
    # form_class = PostModelForm
    success_url = reverse_lazy('post_list')


# def post_delete(request, post_id):
#     """Представления для удаления поста."""
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == "POST":
#         form = PostDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data.get("confirm"):
#             post.delete()
#             messages.success(request, f"Пост '{post.title}' был успешно удален")
#             return redirect('post_list')
#
#     else:
#         form = PostDeleteForm()
#
#     context = {
#         'form': form,
#         'post': post,
#         'title': f'Удалить пост {post.title}',
#     }
#     return render(request, "blog_app/post_delete.html", context=context)


def author_list(request):
    """Список авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список Авторов!',
        'authors': authors,
    }
    return render(request, "blog_app/author_list.html", context=context)


def author_detail(request, author_id):
    """Детальный автор."""
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author,
    }

    return render(request, "blog_app/author_detail.html", context=context)