from django.contrib import admin
from .models import ArticlePost,ArticleColumn

# Register your models here.
admin.site.register(ArticleColumn)
admin.site.register(ArticlePost)
