from django.contrib import admin
from .models import Post, Comment, Tag, Author, AuthorProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'rating', 'tag_list')
    ordering = ('rating',)
    list_filter = ('rating', 'author')
    search_fields = ('title', 'content')
    search_help_text = "Введите слово для поиска"

    fields = ('title', 'author', 'content', 'rating', 'tags')
    readonly_fields = ('rating',)
    # exclude = ('rating',)

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Тэги'

    @admin.action(description="Увеличить рейтинг на 3")
    def increase_rating(self, request, queryset):
        for post in queryset:
            post.rating += + 3
            post.save()
    actions = (increase_rating, )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post')
    list_filter = ('author',)
    search_fields = ('text',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('text', 'author')
        }),
        ('Дополнительная информация', {
            'fields': ('post',),
            'classes': ('collapse',)
        })
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)




