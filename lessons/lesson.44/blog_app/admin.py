from django.contrib import admin
from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'tag_list')
    ordering = ('rating', 'title' )
    list_filter = ('rating', 'author')
    search_fields = ('title', 'content')
    search_help_text = 'Введите часть заголовка или контента для поиска.'

    # fields = ('title', 'content', 'tags', 'author', 'rating')
    # readonly_fields = ('rating', )

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'tags')
        }),
        ('Дополнительная информация', {
            'fields': ('author', 'rating'),
            'classes': ('collapse',)
        }),
    )
    def tag_list(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])

    tag_list.short_description = 'Тэги'

    @admin.action(description="Увеличить рейтинг на 5")
    def edit_rating(self, request, queryset):
        for post in queryset:
            post.rating += 5
            post.save()

    actions = (edit_rating, )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text',]
    ordering = ['text',]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]
    ordering = ['name',]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    ordering = ['name',]


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['bio',]
    ordering = ['bio',]


admin.site.register(Author, AuthorAdmin)