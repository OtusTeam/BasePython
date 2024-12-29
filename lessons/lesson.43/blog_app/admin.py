from django.contrib import admin
from .models import Post, Author, Comment, Tag, AuthorProfile
from django_celery_results.models import TaskResult

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'content', 'author', 'rating', 'tag_list')
    ordering = ['-author', 'rating' ]
    list_filter = ('rating', 'author')
    search_fields = ('title', 'content')
    search_help_text = 'Введите слово для поиска в заголовке или контенте'

    fields = ('title', 'tags', 'content', 'author', 'rating', "created_date")
    readonly_fields = ('created_date', 'rating')

    @admin.action(description='Увеличить рейтинг постов на 10')
    def increase_rating(self, request, queryset):
        for post in queryset:
            post.rating += 10
            post.save()
        self.message_user(request, f'реинг у {queryset.count()} постов обновлен')

    actions = [increase_rating]

    def tag_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Тэги'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_bio')
    ordering = ['-name',  ]
    search_fields = ('name', )
    search_help_text = 'Введите слово для поиска в именах'

    def profile_bio(self, obj):
        return obj.profile.bio if obj.profile else "Пофиль отсутствует"

admin.site.register(Author, AuthorAdmin)

