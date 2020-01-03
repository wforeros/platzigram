# django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# utilities
from datetime import datetime
# Solo para pruebas:
posts = [
    {
        'title': 'Chocolates',
        'user': {
            'name': 'Wilson Forero',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'Andrés A',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'title': 'Auditorio',
        'user': {
            'name': 'Johan W',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1076'
    }
]

@login_required
def list_posts(request):
    ''' List existing post '''
    return render(request, 'posts/feed.html', {
        'posts': posts
    })

