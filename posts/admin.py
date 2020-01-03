from django.contrib import admin

#Local imports
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'created', 'modified')

    search_fields = (
        'title',
        'profile__user__username'
    )


