from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Author
from .forms import PostModelForm


class IndexTemplateView(TemplateView):
    template_name = 'blog_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OTUS blog'
        context['description'] = 'Добро пожаловать в OTUS blog'
        return context


# def index(request):
#     return render(request, 'blog_app/index.html')
#

def about(request):
    return render(request, 'blog_app/about.html')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        # post.rating += 1
        post.views = getattr(post, 'views', 0) + 1
        # post.save()
        post.save(update_fields=['views'])
        return super().get(request, *args, **kwargs)


# def post_detail(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, pk=post_id)
#     # comments = post.comments.filter(active=True)
#     comments = Comment.objects.filter(post=post)
#     tags = post.tags.all()
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'comments': comments,
#         'tags': tags,
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        min_rating = self.request.GET.get('rating')

        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)


        return queryset


# def post_list(request):
#     posts = Post.objects.all()
#     context = {'posts': posts, 'title': 'Список всех постов'}
#     return render(request, 'blog_app/post_list.html', context=context)


# def add_post(request):
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
#     context = {'form': form, 'title': 'Добавить пост'}
#     return render(request, 'blog_app/add_post.html', context=context)


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_app/add_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # print(form)
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


# def add_post(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm()
#
#     context = {'form': form, 'title': 'Добавить пост'}
#     return render(request, 'blog_app/add_post.html', context=context)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_app/edit_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # print(form)
        messages.success(self.request, 'Пост успешно обновлен')
        return super().form_valid(form)

#
# def edit_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm(instance=post)
#
#     context = {'form': form, 'title': 'Редактировать пост'}
#     return render(request, 'blog_app/edit_post.html', context=context)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('post_list')


def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'Список всех авторов'}
    return render(request, 'blog_app/author_list.html', context=context)
