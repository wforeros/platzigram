# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

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

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request,
        template_name='posts/new.html',
        context={
            'form': form, 
            'user': request.user,
            'profile': request.user.profile
        }
    )
