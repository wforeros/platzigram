"""
Posts urls
"""
# Django
from django.urls import path
from posts import views

urlpatterns = [
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),

    path(
        route='post/detail/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),

    path(
        route='new-post/', 
        view=views.create_post, 
        name='create'
    ),
]