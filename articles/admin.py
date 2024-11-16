from django.contrib import admin
from .models import *

# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = [
        "title",
        "body",
        "author",
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)