
from django.forms import ModelForm
from posts.models import Post

class PostForm(ModelForm):

    class Meta:
        """Form sttings"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
