from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category, Tag, Comment, SubComment, Subscriber, Profile, Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    readonly_fields = ('preview',)
    fields = ('preview', 'image', 'is_main')


    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100">', obj.image.url)
        return 'no image'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    inlines = [PhotoInline]
    exclude = ('published_date',)





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


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'user__email', 'phone')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at', 'post', 'id')
