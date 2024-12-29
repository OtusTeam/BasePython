from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Author
from .forms import PostForm, PostModelForm

# Create your views here.
def index(request):
    return render(request, 'blog_app/home.html')


def contacts(request):
    return HttpResponse("Hello, contacts!!")


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
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
        context['authors'] = Author.objects.all()  # Список авторов для формы
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating += 100
        post.save()
        return super().get(request, *args, **kwargs)


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_app/add_post_model.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан!')
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_app/edit_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    """ Представление для удаления поста """
    model = Post
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('post_list')


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            rating = form.cleaned_data['rating']
            author = Author.objects.first()
            post = Post(title=title, content=content, rating=rating, author=author)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'title': 'Добавление поста',
        'form': form
    }
    return render(request, 'blog_app/add_post.html', context=context)


# def post_list(request):
#     posts = Post.objects.all()
#     context = {
#         'title': 'Список постов',
#         'posts': posts
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


# def post_detail(request, post_id):
#     # post = Post.objects.get(pk=post_id)
#     post =  get_object_or_404(Post, pk=post_id)
#
#     context = {
#         'title': post.title,
#         'post': post
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)



# def add_post_model(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # title = form.cleaned_data['title']
#             # content = form.cleaned_data['content']
#             # rating = form.cleaned_data['rating']
#             # author = Author.objects.first()
#             #
#             # post = Post(title=title, content=content, rating=rating, author=author)
#             # post.save()
#             return redirect('post_list')
#         else:
#             print(form.errors)
#     else:
#         form = PostModelForm()
#     context = {
#         'title': 'Добавление поста',
#         'form': form
#     }
#     return render(request, 'blog_app/add_post_model.html', context=context)


# def edit_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             # title = form.cleaned_data['title']
#             # content = form.cleaned_data['content']
#             # rating = form.cleaned_data['rating']
#             # # author = Author.objects.first()
#
#             # post = Post(title=title, content=content, rating=rating, author=author)
#             # post.save()
#             return redirect('post_list')
#         else:
#             print(form.errors)
#     else:
#         form = PostModelForm(instance=post)
#     context = {
#         'title': 'Редактирование поста',
#         'form': form
#     }
#     return render(request, 'blog_app/edit_post.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors
    }
    return render(request, 'blog_app/author_list.html', context=context)