from django.contrib import admin
from django.db.models import F

from .models import Post, Comment, Author, AuthorProfile, Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'created_at', 'tag_list')
    ordering = ('rating', 'created_at',)
    list_filter = ('author', 'rating')
    search_fields = ('title', 'content')
    search_help_text = 'Поиск по заголовку и содержимому'

    fields = ('title', 'content', 'author',  'tags')
    readonly_fields = ('rating',)
    # exclude = ('rating',)

    @admin.action(description='Увеличить рейтинг на 1')
    def increase_rating(self, request, queryset):
        for post in queryset:
            post.rating += 1
            post.save()
        self.message_user(request, 'Рейтинг увеличен на 1')

    @admin.action(description='Увеличить рейтинг на 2')
    def increase_rating_2(self, request, queryset):
        queryset.update(rating=F('rating') + 2)


    actions = (increase_rating, increase_rating_2)

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    tag_list.short_description = 'Теги'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile']
    search_fields = ['name']
    search_help_text = 'Введите имя автора или его профиль'

    def profile(self, obj):
        return obj.profile if obj.profile else 'Нет профиля'

admin.site.register(Author, AuthorAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    search_help_text = 'Введите название тега'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'post', 'created_at']
    list_filter = ['post', 'author']
    search_fields = ['text', 'author']
    search_help_text = 'Поиск по тексту комментария, имени автора и названию поста'


