from django.contrib import admin

from .models import Author, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'created_at', 'rating', 'tag_list')
    ordering = ('author', '-created_at')
    list_filter = ['author', 'rating']
    search_fields = ('title', 'content')
    search_help_text = "Введите часть поста"

    # fields = ('title', 'author', 'rating', 'tags', 'content')
    # readonly_fields = ('rating', )

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'author')
        }),
        ('Дополнительная информация', {
            'fields': ('rating', 'tags', 'content'),
            'classes': ('collapse',)
        }),

    )

    def tag_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())
    tag_list.short_description = 'Тэги'

    @admin.action(description='Увеличить рейтинг на 5')
    def edit_rating(self, request, queryset):
        for post in queryset:
            post.rating += 5
            post.save()

    actions = (edit_rating, )



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    search_help_text = "Введите тэг"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    search_help_text = "Введите автора"


admin.site.register(Author, AuthorAdmin)
