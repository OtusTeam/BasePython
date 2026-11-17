from django.contrib import admin

from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_list', 'author', 'rating', 'created_at', "tag_list")
    ordering = ('-rating', 'created_at',)
    list_filter = ('rating', 'author',)
    search_fields = ('title', 'content',)
    search_help_text = "Введите часть заголовка или текса"

    # fields = ('title', 'rating', 'author', 'content',  'tags')
    # readonly_fields = ('rating', )

    fieldsets = (
        # (None, {
        ("Главная информация", {
            'fields': ('title', 'rating')
        }),
        ("Дополнительная информация", {
            'fields': ('author', 'content', 'tags'),
            'classes': ('collapse',)
        })
    )

    def title_list(self, obj: Post):
        return obj.title.lower()

    def tag_list(self, obj: Post):
        return ", ".join(tag.name for tag in obj.tags.all())
        # return "111"

    tag_list.short_description = 'Tags'

    @admin.action(description="Увеличить рейтинг поста")
    def add_rating(self, request, queryset):
        for post in queryset:
            post.rating += 1
            post.save()
        self.message_user(request, f"{queryset.count()} постов обновлено")

    actions = (add_rating,)


class AuthorAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    ordering = ('author', 'created_at',)
    list_filter = ('author',)
    search_fields = ('text',)
    search_help_text = "Введите часть  текса"


admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorProfile)
