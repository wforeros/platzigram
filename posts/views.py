# django
from django.shortcuts import render
from django.http import HttpResponse

# utilities
from datetime import datetime
# Solo para pruebas:
posts = [
    {
        'name': 'Chocolates',
        'user': 'Wilson Forero',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Lactea',
        'user': 'Andrés A',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Auditorio',
        'user': 'Johan W',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]

def list_posts(request):
    ''' List existing post '''
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src={picture}/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))