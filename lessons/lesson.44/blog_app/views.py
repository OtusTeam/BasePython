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


class AboutTemplateView(TemplateView):
    template_name = 'blog_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '-= О нас =-'
        return context


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
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


class PostDetailView(PostBase, DetailView):
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.rating = getattr(post, 'rating', 0) + 1
        post.save(update_fields=['rating'])
        return super().get(request, *args, **kwargs)


class PostCreateView(PostBase, CreateView):
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        response = super().form_valid(form)
        return response


class PostUpdateView(PostBase, UpdateView):
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно отредактирован')
        return super().form_valid(form)


class PostDeleteView(PostBase, DeleteView):
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')