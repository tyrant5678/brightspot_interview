from django.contrib import admin

# Register your models here.
from .models import Comment, Article

admin.site.register(Comment)
admin.site.register(Article)