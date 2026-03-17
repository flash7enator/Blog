from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, Category, Tag, Comment, SubComment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')


@admin.register(SubComment)
class SubCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'created_at')