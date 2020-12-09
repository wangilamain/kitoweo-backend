from django.contrib import admin
from .models import Profile, Post, Catalogue

# Register your models here.
admin.site.register(Catalogue)
admin.site.register(Profile)
admin.site.register(Post)