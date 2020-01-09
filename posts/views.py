# django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# utilities
from datetime import datetime

from posts.forms import PostForm
from posts.models import Post



class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    # Ordenar desde el más reciente
    ordering = ('-created',)
    # Paginar cada 2 elementos
    paginate_by = 2
    # Como va a recibir el html este valor
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name='posts/detail.html'
    queryset=Post.objects.all()
    slug_field='id'
    slug_url_kwarg='post_id'
    context_object_name='post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['user'] = post.user
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

