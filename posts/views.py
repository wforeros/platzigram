# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# utilities
from datetime import datetime

from posts.forms import PostForm
from posts.models import Post
# Solo para pruebas:
posts = [
]

@login_required
def list_posts(request):
    ''' List existing post '''
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {
        'posts': posts
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
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
