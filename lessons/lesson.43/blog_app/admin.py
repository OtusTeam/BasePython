from django.contrib import admin
from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'rating', 'tag_list')
    ordering = ['-rating', 'title']
    list_filter = ('author', 'rating', 'tags')
    search_fields = ('title', 'content')
    search_help_text = 'Введите часть заголовка или поста.'

    # fields = ('title', 'content', 'author', 'rating', 'tags')
    # readonly_fields = ('rating',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'author')
        }),
        ('Дополнительная информация', {
            'fields': ('content',  'rating', 'tags'),
            'classes': ('collapse',)
        }),
    )

    @admin.action(description='Увеличить рейтинг постов на 10')
    def increase_rating(self, request, queryset):
        for post in queryset:
            post.rating += 10
            post.save()
        self.message_user(request, f'{queryset.count()} постов обновлено')

    actions = (increase_rating,)

    def tag_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Тэги'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name', )
    search_help_text = 'Введите имя автора.'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name', )
    search_help_text = 'Введите тэг.'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'author')
    ordering = ('-created_at', )
    list_filter = ('author', )
    search_fields = ('text', )
    search_help_text = 'Введите часть комментария.'


admin.site.register(Comment, CommentAdmin)
admin.site.register(AuthorProfile)


