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
        route='post-detail/<str:post_id>',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),

    path(
        route='new-post/', 
        view=views.CreatePostView.as_view(), 
        name='create'
    ),
]