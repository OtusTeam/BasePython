from django.contrib import admin
from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'tags_list')
    ordering = ('rating', '-title')
    list_filter = ('rating', 'author',)
    search_fields = ('title', 'content')
    search_help_text = 'Введите часть заголовка иои текста'

    fields = ('title', 'author', 'rating', 'tags')
    readonly_fields = ('rating',)

    @admin.action(description='Увеличить рейтинг на 10')
    def add_rating(self, request, queryset):
        for post in queryset:
            post.rating += 10
            post.save()

    actions = (add_rating, )

    def tags_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    tags_list.short_description = 'Тэги'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Введите автора'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Введите тэг'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'post']
    ordering = ['author']
    search_fields = ['text']
    search_help_text = 'Введите текст'

    fieldsets = (
        (None, {
            'fields': ('author', 'post'),
        }),
        ('Дополнительная информация', {
            'fields': ('text',),
            'classes': ('collapse',),
        })
    )

    @admin.action(description='Исправить текст')
    def edit_comment(self, request, queryset):
        for comment in queryset:
            comment.text = comment.text.title()
            comment.save()

    actions = (edit_comment, )

admin.site.register(Author, AuthorAdmin)