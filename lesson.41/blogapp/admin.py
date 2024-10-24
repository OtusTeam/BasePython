from django.contrib import admin
from .models import Post, Author


# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'viwes_count')
    list_filter = ('is_published',)
    search_fields = ('title',)
    actions = ('make_published',)

    @admin.action(description='Опубликовать выбранные посты')
    def make_published(self, request, queryset):
        queryset.update(is_published=True)

admin.site.register(Author)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):