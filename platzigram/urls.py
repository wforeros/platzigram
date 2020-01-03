"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django
from django.contrib import admin
# Para que se vean las imágenes bien 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Local
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('sort/', local_views.sort_numbers, name='sort'),
    # Aquí vemos otra forma de pasar variables en nuestra url con django
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),
    path('posts/', posts_views.list_posts, name='feed'),
    path('users/login/', users_views.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


