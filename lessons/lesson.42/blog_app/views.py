from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView,
                                  RedirectView, View)
from .models import Post, Author
from .forms import PostForm, PostModelForm, PostDeleteForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'blog_app/home.html')


# def about(request):
#     return HttpResponse("About me info")


class PostListView(ListView):
    """Представление для отображения списка постов"""
    model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset().filter(rating=1)
        # min_rating = self.request.GET.get('rating')
        author_id = self.request.GET.get('author')

        # if min_rating:
        #     queryset = queryset.filter(rating=1)
        # #
        # # if author_id:
        # #     queryset = queryset.filter(author_id=author_id)
        return queryset


class PostDetailView(DetailView):
    """Представление для отображения одного поста"""
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating += 1
        post.save()

        return super().get(request, *args, **kwargs)



# def add_post(request):
#     '''form = PostForm()'''
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             rating = form.cleaned_data['rating']
#             author = Author.objects.first()
#             Post.objects.create(title=title, content=content, rating=rating, author=author)
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     context = {
#         'form': form,
#         'title': 'Добавление поста'
#     }
#     return render(request, 'blog_app/add_post.html', context=context)


# def add_post(request):
#     """ form = PostModelForm() """
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm()
#     context = {
#         'form': form,
#         'title': 'Добавление поста'
#     }
#     return render(request, 'blog_app/add_post.html', context=context)


class PostCreateView(CreateView):
    """Представление для создания нового поста"""
    model = Post
    template_name = 'blog_app/add_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        """ Добавляем сообщение об успешном создании поста """
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)

#
# def edit_post(request, post_id):
#     """ form = PostModelForm() """
#
#     post =get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm(instance=post)
#     context = {
#         'form': form,
#         'title': 'Изменение поста'
#     }
#     return render(request, 'blog_app/edit_post.html', context=context)


class PostUpdateView(UpdateView):
    """Представление для редактирования поста"""
    model = Post
    template_name = 'blog_app/edit_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


# def delete_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirm']:
#             post.delete()
#             return redirect('post_list')
#     else:
#         form = PostDeleteForm()
#     context = {
#         'form': form,
#         'post': post,
#         'title': f'Удаление поста {post.title}'
#     }
#     return render(request, 'blog_app/delete_post.html', context=context)


class PostDeleteView(DeleteView):
    """Представление для удаления поста"""
    model = Post
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('post_list')


def author_list(request):
    authors = Author.objects.all()
    print(authors)
    context = {'authors': authors}
    return render(request, 'blog_app/author_list.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, 'blog_app/author_detail.html', context=context)


class AboutTemplateView(TemplateView):
    template_name = 'blog_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['text'] = 'Это страница о нас'
        return context
