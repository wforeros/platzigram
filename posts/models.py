# django
from django.db import models

class User(models.Model):
    """User test model"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    country = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.email

